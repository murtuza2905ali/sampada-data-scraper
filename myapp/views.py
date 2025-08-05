from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PIL import Image
import pytesseract
import time
import base64
import pandas as pd
from io import BytesIO
import traceback
import os

@csrf_exempt
def trigger_scrape(request):
    message = ""
    if request.method == "POST":
        username   = request.POST.get("userName")
        password   = request.POST.get("password")
        district   = request.POST.get("district")
        deed_type  = request.POST.get("deed_type")

        if not all([username, password, district, deed_type]):
            return render(request, "trigger_scrape.html", {
                "message": "Please fill all required fields."
            })

        # ─── Chrome / Chromedriver Configuration ───────────────────────────────
        chrome_options = Options()
        chrome_options.headless = True
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        # Allow override via ENV; fallback to common Linux paths in Docker
        chrome_bin = os.getenv("CHROME_BINARY", "/usr/bin/google-chrome-stable")
        driver_bin = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
        chrome_options.binary_location = chrome_bin

        driver = None
        try:
            driver = webdriver.Chrome(
                executable_path=driver_bin,
                options=chrome_options
            )

            driver.get("https://sampada.mpigr.gov.in/#/clogin")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "username"))
            )

            # ─── Language Switch (if present) ───────────────────────────────────
            try:
                lang_switch = driver.find_element(By.XPATH, "//a[contains(text(), 'English')]")
                lang_switch.click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "username"))
                )
            except Exception:
                pass

            # ─── LOGIN LOOP with CAPTCHA OCR ────────────────────────────────────
            success = False
            for attempt in range(1, 21):
                try:
                    print(f"🔁 Attempt {attempt}")
                    # Refresh CAPTCHA if possible
                    try:
                        refresh_btn = driver.find_element(
                            By.XPATH, "//img[contains(@src, 'refresh_image')]"
                        )
                        driver.execute_script("arguments[0].click();", refresh_btn)
                        time.sleep(1)
                    except Exception:
                        pass

                    # Enter credentials
                    driver.find_element(By.ID, "username").clear()
                    driver.find_element(By.ID, "username").send_keys(username)
                    driver.find_element(By.ID, "password").clear()
                    driver.find_element(By.ID, "password").send_keys(password)

                    # Extract and OCR the CAPTCHA
                    raw_src = driver.find_element(
                        By.XPATH, "//img[contains(@src, 'data:image')]"
                    ).get_attribute("src")
                    img_data = base64.b64decode(raw_src.split(",")[1])
                    img = Image.open(BytesIO(img_data))

                    # Use system tesseract
                    captcha_text = pytesseract.image_to_string(
                        img,
                        config='--psm 8 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
                    ).strip().replace(" ", "")
                    print(" CAPTCHA Text:", captcha_text)

                    # Fill and submit
                    cap_input = driver.find_element(By.ID, "captchaStr")
                    driver.execute_script("arguments[0].value = '';", cap_input)
                    cap_input.send_keys(captcha_text)
                    driver.find_element(
                        By.XPATH, "//button[.//span[text()='Login']]"
                    ).click()

                    # Wait for login to complete
                    WebDriverWait(driver, 180).until_not(
                        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Please Wait')]"))
                    )
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Search/Certified Copy')]"))
                    )

                    print("✅ Login successful!")
                    success = True
                    break

                except Exception as e:
                    print(" Error in attempt:", e)
                    traceback.print_exc()
                    time.sleep(2)

            if not success:
                message = "Login failed after multiple attempts."
                return render(request, "trigger_scrape.html", {"message": message})

            # ─── NAVIGATE to Search/Certified Copy ─────────────────────────────
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Search/Certified Copy')]"))
            ).click()

            # Select “Other” doc type
            other_radio = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "P2000_SEARCH_DOC_TYPE_1"))
            )
            driver.execute_script("arguments[0].click();", other_radio)
            time.sleep(1)

            # Select District & Financial Year
            driver.find_element(By.ID, "P2000_DISTRICT").click()
            driver.find_element(By.XPATH, f"//option[contains(text(), '{district}')]").click()
            time.sleep(1)
            driver.find_element(By.ID, "CurrentFinancialYear1").click()
            time.sleep(1)

            # Enter Deed Type
            deed_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@aria-autocomplete='list']"))
            )
            deed_input.clear()
            deed_input.send_keys(deed_type)
            time.sleep(2)
            conveyance_option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='Conveyance']"))
            )
            driver.execute_script("arguments[0].click();", conveyance_option)
            time.sleep(0.5)

            # ─── SEARCH LOOP with Second CAPTCHA & Results ────────────────────
            all_data = []
            while True:
                try:
                    # Solve second CAPTCHA
                    cap_input2 = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, "captchaStr"))
                    )
                    cap_img_elem = driver.find_element(
                        By.XPATH, "//img[contains(@src,'data:image/png;base64')]"
                    )
                    img2 = Image.open(BytesIO(
                        base64.b64decode(cap_img_elem.get_attribute("src").split(",")[1])
                    ))
                    txt2 = pytesseract.image_to_string(
                        img2,
                        config='--psm 8 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
                    ).strip().replace(" ", "")
                    print(" CAPTCHA Text:", txt2)

                    if len(txt2) < 4:
                        # Refresh if too short
                        try:
                            driver.find_element(
                                By.XPATH, "//img[contains(@src, 'refresh_image.png')]"
                            ).click()
                        except Exception:
                            pass
                        time.sleep(2)
                        continue

                    # Submit the search
                    driver.execute_script("""
                        arguments[0].value = arguments[1];
                        arguments[0].dispatchEvent(new Event('input',{ bubbles:true }));
                    """, cap_input2, txt2)
                    driver.find_element(
                        By.XPATH, "//button[contains(., 'Search')]"
                    ).click()
                    print(" Search button clicked.")
                    time.sleep(5)

                    # Handle alerts
                    try:
                        alert = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "swal2-html-container"))
                        )
                        text = alert.text.strip()
                        driver.find_element(By.CLASS_NAME, "swal2-confirm").click()
                        if "Captcha mismatched" in text:
                            print(" CAPTCHA mismatched, retry.")
                            time.sleep(2)
                            continue
                        if "No Data Found" in text:
                            print(" No Data Found, ending.")
                            break
                    except Exception:
                        pass

                    # Wait for paginator, set 100 per page
                    WebDriverWait(driver, 40).until(
                        EC.presence_of_element_located((By.XPATH, "//mat-paginator"))
                    )
                    dropdown = driver.find_element(
                        By.XPATH,
                        "//mat-paginator//mat-select//div[contains(@class,'mat-select-arrow-wrapper')]"
                    )
                    driver.execute_script("arguments[0].click();", dropdown)
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//mat-option//span[text()='100']"))
                    ).click()
                    time.sleep(2)

                    # Collect rows
                    rows = driver.find_elements(
                        By.XPATH, "//table/tbody/tr/td[2]//span[contains(@class,'link')]"
                    )
                    print(f"🔍 Found {len(rows)} document rows")
                    for idx, row in enumerate(rows):
                        try:
                            driver.execute_script("arguments[0].scrollIntoView();", row)
                            time.sleep(1)
                            row.click()
                            WebDriverWait(driver, 10).until(
                                EC.visibility_of_element_located((By.XPATH, "//legend[contains(text(),'Registration Details')]"))
                            )

                            # Extract details (add more fields here if desired)
                            data = {
                                "Registration No": driver.find_element(
                                    By.XPATH, "(//fieldset)[1]//td[1]"
                                ).text,
                                "Registration Date": driver.find_element(
                                    By.XPATH, "(//fieldset)[1]//td[2]"
                                ).text,
                                "Deed Type": driver.find_element(
                                    By.XPATH, "(//fieldset)[1]//td[3]"
                                ).text,
                            }
                            all_data.append(data)

                            # Close modal
                            driver.find_element(
                                By.XPATH, "//ngb-modal-window//button[contains(@class,'close')]"
                            ).click()
                            time.sleep(0.5)
                        except Exception as e:
                            print(f" Error processing row {idx+1}:", e)
                            continue

                    break  # remove this if you want to paginate further

                except Exception as e:
                    print(" General Error in search loop:", e)
                    break

            # ─── SAVE RESULTS ────────────────────────────────────────────────────
            df = pd.DataFrame(all_data)
            out_file = "/tmp/Sampada_Data_by_Murtuza_Ali.xlsx"
            df.to_excel(out_file, index=False)
            message = f"Scraping completed: {len(all_data)} records saved to {out_file}"

        except Exception as e:
            traceback.print_exc()
            message = f"Error during scraping: {e}"

        finally:
            if driver:
                driver.quit()

    return render(request, "trigger_scrape.html", {
        "message": message or "Scraping process completed."
    })
