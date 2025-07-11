from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import base64
from io import BytesIO
import pandas as pd

import time

# ✅ Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Connect to existing Chrome session
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)

def solve_only_captcha_and_search():
   ############################
    



   #####################################



    # try:
    #     # Wait for and click the pagination dropdown
    #     dropdown = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((
    #             By.XPATH,
    #             "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset[2]/div/div[2]/div/div[2]/div[2]/mat-paginator/div/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[2]"
    #         ))
    #     )
    #     driver.execute_script("arguments[0].click();", dropdown)
    #     print("🔽 Dropdown clicked.")

    #     # Wait for and click the '100' option
    #     option_100 = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((
    #             By.XPATH,
    #             "/html/body/div[3]/div[2]/div/div/div/mat-option[4]/span"
    #         ))
    #     )
    #     driver.execute_script("arguments[0].click();", option_100)
    #     print("✅ Selected '100' from dropdown.")

    # except Exception as e:
    #     print("❌ Error during dropdown selection:", str(e))










##############################################################




    # try:
    #     while True:
    #         try:
    #             # 🔹 Wait for CAPTCHA input & image
    #             captcha_input = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.NAME, "captchaStr"))
    #             )
    #             captcha_img_elem = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.XPATH, "//img[contains(@src,'data:image/png;base64')]"))
    #             )
    #             captcha_src = captcha_img_elem.get_attribute("src")
    #             captcha_base64 = captcha_src.split(",")[1]
    #             captcha_image = Image.open(BytesIO(base64.b64decode(captcha_base64)))

    #             # 🔹 OCR for CAPTCHA
    #             captcha_text = pytesseract.image_to_string(
    #                 captcha_image,
    #                 config='--psm 8 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #             ).strip().replace(" ", "").replace("\n", "")
    #             print("🔍 CAPTCHA Text:", captcha_text)

    #             # ✅ Refresh CAPTCHA if too short
    #             if len(captcha_text) < 4:
    #                 print("⚠️ CAPTCHA too short, refreshing...")
    #                 driver.find_element(By.XPATH, "//img[contains(@src, 'refresh_image.png')]").click()
    #                 time.sleep(2)
    #                 continue

    #             # 🔹 Fill CAPTCHA input
    #             driver.execute_script("""
    #                 const input = arguments[0];
    #                 input.focus();
    #                 input.value = arguments[1];
    #                 input.dispatchEvent(new Event('input', { bubbles: true }));
    #             """, captcha_input, captcha_text)

    #             # 🔹 Click Search Button using JS
    #             search_button_xpath = "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset/div[4]/div[2]/div/button[1]"
    #             search_button = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.XPATH, search_button_xpath))
    #             )
    #             driver.execute_script("arguments[0].click();", search_button)
    #             print("✅ Search button clicked.")
    #             #⏳ Wait for alert to show
    #             # ⏳ Wait for alert to show
    #             time.sleep(20)

    #             # ✅ Smart Alert Handler (Captcha mismatch / No Data Found)
    #             try:
    #                 alert_ok_btn = WebDriverWait(driver, 5).until(
    #                     EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[6]/button[1]"))
    #                 )
    #                 alert_msg_elem = driver.find_element(By.XPATH, "/html/body/div/div/div[5]")
    #                 alert_msg_text = alert_msg_elem.text.strip()
    #                 print("⚠️ Alert Detected:", alert_msg_text)

    #                 if "Captcha mismatched" in alert_msg_text:
    #                     print("❌ CAPTCHA mismatched popup.")
    #                     try:
    #                         alert_ok_btn.click()
    #                         print("☑️ OK clicked.")
    #                     except:
    #                         print("⚠️ OK failed, clicking on CAPTCHA input.")
    #                         captcha_input.click()
    #                     time.sleep(3)
    #                     driver.find_element(By.XPATH, "//img[contains(@src, 'refresh_image.png')]").click()
    #                     time.sleep(2)
    #                     continue

    #                 elif "No Data Found" in alert_msg_text:
    #                     print("ℹ️ No Data Found.")
    #                     try:
    #                         alert_ok_btn.click()
    #                         print("☑️ OK clicked.")
    #                     except:
    #                         print("⚠️ OK failed, clicking on CAPTCHA input.")
    #                         captcha_input.click()
    #                     time.sleep(3)
    #                     return  # ✅ End if valid captcha but no record

    #             except Exception as e:
    #                 print("❌ Alert handler error:", str(e))

    #             # ⏳ Wait max 60s for results (mat-paginator to appear)
    #             print("⏳ Waiting for results...")
    #             WebDriverWait(driver, 60).until(
    #                 EC.presence_of_element_located((By.XPATH, "//mat-paginator"))
    #             )
    #             print("📄 Results loaded!")

    #             # 🔽 Select '100' from dropdown using JS
    #             try:
    #                 dropdown_xpath = "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset[2]/div/div[2]/div/div[2]/div[2]/mat-paginator/div/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[2]"
    #                 dropdown = WebDriverWait(driver, 10).until(
    #                     EC.presence_of_element_located((By.XPATH, dropdown_xpath))
    #                 )
    #                 driver.execute_script("arguments[0].click();", dropdown)
    #                 print("🔽 Dropdown clicked.")

    #                 option_xpath = "/html/body/div[3]/div[2]/div/div/div/mat-option[4]/span"
    #                 option_100 = WebDriverWait(driver, 10).until(
    #                     EC.presence_of_element_located((By.XPATH, option_xpath))
    #                 )
    #                 driver.execute_script("arguments[0].click();", option_100)
    #                 print("✅ Selected '100' from dropdown.")
    #             except Exception as dropdown_error:
    #                 print("❌ Error during dropdown selection:", str(dropdown_error))

    #             break  # ✅ Success – exit loop

    #         except Exception as result_error:
    #             print("⚠️ Results not loaded, checking for error alert...")

    #             try:
    #                 ok_btn_xpath = "/html/body/div[4]/div/div[6]/button[1]"
    #                 ok_btn = WebDriverWait(driver, 5).until(
    #                     EC.presence_of_element_loc((By.XPATH, ok_btn_xpath))
    #                 )
    #                 driver.execute_script("arguments[0].click();", ok_btn)
    #                 print("☑️ Captcha error OK clicked. Retrying...")
    #             except Exception as inner_e:
    #                 print("❌ No error alert found either:", str(inner_e))
    #             # Loop will retry
    # except Exception as final_e:
    #     print("❌ Fatal error occurred:", str(final_e))




###################




    # try:
    #     while True:
    #         try:
    #             # 🔹 Wait for CAPTCHA input & image
    #             captcha_input = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.NAME, "captchaStr"))
    #             )
    #             captcha_img_elem = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.XPATH, "//img[contains(@src,'data:image/png;base64')]"))
    #             )
    #             captcha_src = captcha_img_elem.get_attribute("src")
    #             captcha_base64 = captcha_src.split(",")[1]
    #             captcha_image = Image.open(BytesIO(base64.b64decode(captcha_base64)))

    #             # 🔹 OCR for CAPTCHA
    #             captcha_text = pytesseract.image_to_string(
    #                 captcha_image,
    #                 config='--psm 8 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #             ).strip().replace(" ", "").replace("\n", "")
    #             print("🔍 CAPTCHA Text:", captcha_text)
                
    #             if len(captcha_text) < 4:
    #                 print("⚠️ CAPTCHA too short, refreshing...")
    #                 try:
    #                     refresh_img = WebDriverWait(driver, 5).until(
    #                         EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset/div[4]/div[1]/div/div[2]/img"))
    #                     )
    #                     driver.execute_script("arguments[0].click();", refresh_img)
    #                     print("🔄 CAPTCHA refreshed via JS.")
    #                     time.sleep(5)
    #                 except Exception as e:
    #                     print("❌ CAPTCHA refresh failed:", str(e))
    #                 continue  # Retry loop

    #             # 🔹 Fill CAPTCHA input
    #             driver.execute_script("""
    #                 const input = arguments[0];
    #                 input.focus();
    #                 input.value = arguments[1];
    #                 input.dispatchEvent(new Event('input', { bubbles: true }));
    #             """, captcha_input, captcha_text)

    #             # 🔹 Click Search Button
    #             search_button = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset/div[4]/div[2]/div/button[1]"))
    #             )
    #             driver.execute_script("arguments[0].click();", search_button)
    #             print("✅ Search button clicked.")

    #             # ⏳ Wait a bit for alert if any
    #             time.sleep(3)

    #             # ✅ Smart Alert Handler
    #             try:
    #                 alert_ok_btn = WebDriverWait(driver, 5).until(
    #                     EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[6]/button[1]"))
    #                 )
    #                 alert_msg_elem = driver.find_element(By.XPATH, "/html/body/div/div/div[5]")
    #                 alert_msg_text = alert_msg_elem.text.strip()
    #                 print("⚠️ Alert Detected:", alert_msg_text)

    #                 if "Captcha mismatched" in alert_msg_text:
    #                     print("❌ CAPTCHA mismatched popup.")
    #                     try:
    #                         alert_ok_btn.click()
    #                         print("☑️ OK clicked.")
    #                     except:
    #                         captcha_input.click()
    #                     time.sleep(3)
    #                     driver.find_element(By.XPATH, "//img[contains(@src, 'refresh_image.png')]").click()
    #                     time.sleep(2)
    #                     continue

    #                 elif "No Data Found" in alert_msg_text:
    #                     print("ℹ️ No Data Found.")
    #                     try:
    #                         alert_ok_btn.click()
    #                         print("☑️ OK clicked.")
    #                     except:
    #                         captcha_input.click()
    #                     time.sleep(3)
    #                     return

    #             except:
    #                 print("✅ No alert found, continuing...")

    #             # ✅ If no popup, check spinner gone
    #             try:
    #                 WebDriverWait(driver, 5).until(
    #                     EC.invisibility_of_element_located((By.XPATH, "//div[contains(text(), 'Please Wait')]"))
    #                 )
    #                 print("✅ CAPTCHA accepted, request successful.")
    #             except:
    #                 print("⏳ Spinner didn't disappear. Retrying...")
    #                 time.sleep(5)
    #                 driver.find_element(By.XPATH, "//img[contains(@src, 'refresh_image.png')]").click()
    #                 continue

    #             # ⏳ Wait for results
    #             print("⏳ Waiting for results...")
    #             WebDriverWait(driver, 60).until(
    #                 EC.presence_of_element_located((By.XPATH, "//mat-paginator"))
    #             )
    #             print("📄 Results loaded!")

    #             # 🔽 Set dropdown to 100
    #             try:
    #                 dropdown_xpath = "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset[2]/div/div[2]/div/div[2]/div[2]/mat-paginator/div/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[2]"
    #                 option_xpath = "/html/body/div[3]/div[2]/div/div/div/mat-option[4]/span"

    #                 dropdown = WebDriverWait(driver, 10).until(
    #                     EC.presence_of_element_located((By.XPATH, dropdown_xpath))
    #                 )
    #                 driver.execute_script("arguments[0].click();", dropdown)
    #                 print("🔽 Dropdown clicked.")

    #                 option_100 = WebDriverWait(driver, 10).until(
    #                     EC.presence_of_element_located((By.XPATH, option_xpath))
    #                 )
    #                 driver.execute_script("arguments[0].click();", option_100)
    #                 print("✅ Selected '100' from dropdown.")

    #             except Exception as dropdown_error:
    #                 print("❌ Error during dropdown selection:", str(dropdown_error))

    #             break  # ✅ Success

    #         except Exception as e:
    #             print("⚠️ CAPTCHA solve error:", str(e))
    #             time.sleep(5)
    #             try:
    #                 driver.find_element(By.XPATH, "//img[contains(@src, 'refresh_image.png')]").click()
    #             except:
    #                 pass
    #             continue

    # except Exception as final_e:
    #     print("❌ Fatal error occurred:", str(final_e))






######################$####################










################ test 1 = its a alert button click ###########

    # try:
    #     # Wait for alert message and OK button
    #     alert_msg_elem = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'swal2-html-container')]"))
    #     )
    #     alert_text = alert_msg_elem.text.strip()

    #     alert_ok_btn = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'swal2-confirm')]"))
    #     )

    #     print("⚠️ Alert Detected:", alert_text)

    #     if "Captcha mismatched" in alert_text:
    #         print("❌ CAPTCHA mismatched! Retrying...")
    #         driver.execute_script("arguments[0].click();", alert_ok_btn)
    #         time.sleep(2)

    #         # Refresh captcha via JS
    #         try:
    #             refresh_img = WebDriverWait(driver, 5).until(
    #                 EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset/div[4]/div[1]/div/div[2]/img"))
    #             )
    #             driver.execute_script("arguments[0].click();", refresh_img)
    #             print("🔄 CAPTCHA refreshed via JS.")
    #         except Exception as e:
    #             print("❌ CAPTCHA refresh image not found:", str(e))
    #         time.sleep(2)

    #         # Recursively retry
    #         solve_only_captcha_and_search()

    #     elif "No Data Found" in alert_text:
    #         print("ℹ️ No Data Found.")
    #         driver.execute_script("arguments[0].click();", alert_ok_btn)
    #         time.sleep(2)
    #         return  # Stop further action

    #     else:
    #         print("⚠️ Unknown alert:", alert_text)
    #         driver.execute_script("arguments[0].click();", alert_ok_btn)

    # except Exception as e:
    #     print("❌ No alert found or error during handling:", str(e))



############ captha too short problem ######
    # while True:
    #     try:
    #         # Wait for CAPTCHA input & image
    #         captcha_input = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.NAME, "captchaStr"))
    #         )
    #         captcha_img_elem = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, "//img[contains(@src,'data:image/png;base64')]"))
    #         )
    #         captcha_src = captcha_img_elem.get_attribute("src")
    #         captcha_base64 = captcha_src.split(",")[1]
    #         captcha_image = Image.open(BytesIO(base64.b64decode(captcha_base64)))

    #         # OCR for CAPTCHA
    #         captcha_text = pytesseract.image_to_string(
    #             captcha_image,
    #             config='--psm 8 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #         ).strip().replace(" ", "").replace("\n", "")
    #         print("🔍 CAPTCHA Text:", captcha_text)

    #         # Retry if too short
    #         if len(captcha_text) < 4:
    #             print("⚠️ CAPTCHA too short, refreshing...")
    #             try:
    #                 refresh_img = WebDriverWait(driver, 5).until(
    #                     EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'refresh_image.png')]"))
    #                 )
    #                 driver.execute_script("arguments[0].click();", refresh_img)
    #                 print("🔄 CAPTCHA refreshed.")
    #             except Exception as e:
    #                 print("❌ Failed to refresh CAPTCHA:", str(e))
    #             time.sleep(2)
    #             continue

    #         # Fill CAPTCHA via JS
    #         driver.execute_script("""
    #             const input = arguments[0];
    #             input.focus();
    #             input.value = arguments[1];
    #             input.dispatchEvent(new Event('input', { bubbles: true }));
    #         """, captcha_input, captcha_text)

    #         # Click Search Button via JS
    #         search_button = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset/div[4]/div[2]/div/button[1]"))
    #         )
    #         driver.execute_script("arguments[0].click();", search_button)
    #         print("✅ Search button clicked.")

    #         # Wait for possible alert
    #         time.sleep(2)

    #         # Check if alert appears
    #         try:
    #             alert_msg_elem = WebDriverWait(driver, 5).until(
    #                 EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'swal2-html-container')]"))
    #             )
    #             alert_text = alert_msg_elem.text.strip()

    #             alert_ok_btn = WebDriverWait(driver, 5).until(
    #                 EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'swal2-confirm')]"))
    #             )

    #             print("⚠️ Alert Detected:", alert_text)

    #             if "Captcha mismatched" in alert_text:
    #                 print("❌ CAPTCHA mismatched! Retrying...")
    #                 driver.execute_script("arguments[0].click();", alert_ok_btn)
    #                 time.sleep(2)

    #                 # Refresh image
    #                 refresh_img = WebDriverWait(driver, 5).until(
    #                     EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'refresh_image.png')]"))
    #                 )
    #                 driver.execute_script("arguments[0].click();", refresh_img)
    #                 time.sleep(2)
    #                 continue  # retry loop

    #             elif "No Data Found" in alert_text:
    #                 print("ℹ️ No Data Found.")
    #                 driver.execute_script("arguments[0].click();", alert_ok_btn)
    #                 time.sleep(2)
    #                 return  # exit gracefully

    #             else:
    #                 print("⚠️ Unknown alert:", alert_text)
    #                 driver.execute_script("arguments[0].click();", alert_ok_btn)

    #         except Exception as alert_e:
    #             print("✅ No alert, continuing...")

    #         # Done if no alert
    #         break

    #     except Exception as e:
    #         print("❌ Error occurred:", str(e))
    #         try:
    #             refresh_img = driver.find_element(By.XPATH, "//img[contains(@src, 'refresh_image.png')]")
    #             driver.execute_script("arguments[0].click();", refresh_img)
    #             print("🔁 Retry after error.")
    #             time.sleep(2)
    #         except:
    #             pass
    #         continue












################# test 3 now checking after search click ############ SUCEESSFULL


    # while True:
    #     try:
    #         # 🔹 Wait for CAPTCHA input & image
    #         captcha_input = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.NAME, "captchaStr"))
    #         )
    #         captcha_img_elem = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, "//img[contains(@src,'data:image/png;base64')]"))
    #         )
    #         captcha_src = captcha_img_elem.get_attribute("src")
    #         captcha_base64 = captcha_src.split(",")[1]
    #         captcha_image = Image.open(BytesIO(base64.b64decode(captcha_base64)))

    #         # 🔹 OCR for CAPTCHA
    #         captcha_text = pytesseract.image_to_string(
    #             captcha_image,
    #             config='--psm 8 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #         ).strip().replace(" ", "").replace("\n", "")
    #         print("🔍 CAPTCHA Text:", captcha_text)

    #         if len(captcha_text) < 4:
    #             print("⚠️ CAPTCHA too short, refreshing...")
    #             try:
    #                 refresh_img = WebDriverWait(driver, 5).until(
    #                     EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'refresh_image.png')]"))
    #                 )
    #                 driver.execute_script("arguments[0].click();", refresh_img)
    #             except Exception as e:
    #                 print("❌ Failed to refresh CAPTCHA:", str(e))
    #             time.sleep(2)
    #             continue

    #         # 🔹 Fill CAPTCHA input
    #         driver.execute_script("""
    #             const input = arguments[0];
    #             input.focus();
    #             input.value = arguments[1];
    #             input.dispatchEvent(new Event('input', { bubbles: true }));
    #         """, captcha_input, captcha_text)

    #         # 🔹 Click Search Button
    #         search_button = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset/div[4]/div[2]/div/button[1]"))
    #         )
    #         driver.execute_script("arguments[0].click();", search_button)
    #         print("✅ Search button clicked.")
    #         time.sleep(2)

    #         # 🔽 Alert Handling
    #         try:
    #             alert_msg_elem = WebDriverWait(driver, 5).until(
    #                 EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'swal2-html-container')]"))
    #             )
    #             alert_text = alert_msg_elem.text.strip()

    #             alert_ok_btn = WebDriverWait(driver, 5).until(
    #                 EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'swal2-confirm')]"))
    #             )

    #             print("⚠️ Alert Detected:", alert_text)

    #             if "Captcha mismatched" in alert_text:
    #                 print("❌ CAPTCHA mismatched! Retrying...")
    #                 driver.execute_script("arguments[0].click();", alert_ok_btn)
    #                 time.sleep(2)

    #                 # Refresh image
    #                 refresh_img = WebDriverWait(driver, 5).until(
    #                     EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'refresh_image.png')]"))
    #                 )
    #                 driver.execute_script("arguments[0].click();", refresh_img)
    #                 time.sleep(2)
    #                 continue  # retry loop

    #             elif "No Data Found" in alert_text:
    #                 print("ℹ️ No Data Found.")
    #                 driver.execute_script("arguments[0].click();", alert_ok_btn)
    #                 time.sleep(2)
    #                 return  # Stop loop

    #             else:
    #                 print("⚠️ Unknown alert:", alert_text)
    #                 driver.execute_script("arguments[0].click();", alert_ok_btn)
    #                 time.sleep(2)
    #                 continue

    #         except Exception:
    #             print("✅ No alert detected.")

    #         # 🕐 Wait for paginator to confirm success
    #         try:
    #             WebDriverWait(driver, 15).until(
    #                 EC.presence_of_element_located((By.XPATH, "//mat-paginator"))
    #             )
    #             print("📄 Results loaded successfully.")
    #             break  # ✅ All done — exit loop

    #         except Exception:
    #             print("⚠️ No paginator found, retrying...")
    #             try:
    #                 refresh_img = driver.find_element(By.XPATH, "//img[contains(@src, 'refresh_image.png')]")
    #                 driver.execute_script("arguments[0].click();", refresh_img)
    #             except:
    #                 pass
    #             time.sleep(2)
    #             continue

    #     except Exception as e:
    #         print("❌ General Error:", str(e))
    #         time.sleep(2)
    #         continue


####################### 100 click dropdown ################## SUCCESSFULL

    # while True:
    #         try:
    #             # 🔹 Wait for CAPTCHA input & image
    #             captcha_input = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.NAME, "captchaStr"))
    #             )
    #             captcha_img_elem = WebDriverWait(driver, 10).until(
    #                 EC.presence_of_element_located((By.XPATH, "//img[contains(@src,'data:image/png;base64')]"))
    #             )
    #             captcha_src = captcha_img_elem.get_attribute("src")
    #             captcha_base64 = captcha_src.split(",")[1]
    #             captcha_image = Image.open(BytesIO(base64.b64decode(captcha_base64)))

    #             # 🔹 OCR for CAPTCHA
    #             captcha_text = pytesseract.image_to_string(
    #                 captcha_image,
    #                 config='--psm 8 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    #             ).strip().replace(" ", "").replace("\n", "")
    #             print("🔍 CAPTCHA Text:", captcha_text)

    #             if len(captcha_text) < 4:
    #                 print("⚠️ CAPTCHA too short, refreshing...")
    #                 try:
    #                     refresh_img = WebDriverWait(driver, 5).until(
    #                         EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'refresh_image.png')]"))
    #                     )
    #                     driver.execute_script("arguments[0].click();", refresh_img)
    #                 except Exception as e:
    #                     print("❌ Failed to refresh CAPTCHA:", str(e))
    #                 time.sleep(2)
    #                 continue

    #             # 🔹 Fill CAPTCHA input
    #             driver.execute_script("""
    #                 const input = arguments[0];
    #                 input.focus();
    #                 input.value = arguments[1];
    #                 input.dispatchEvent(new Event('input', { bubbles: true }));
    #             """, captcha_input, captcha_text)

    #             # 🔹 Click Search Button
    #             search_button = WebDriverWait(driver, 10).until(
    #                 EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset/div[4]/div[2]/div/button[1]"))
    #             )
    #             driver.execute_script("arguments[0].click();", search_button)
    #             print("✅ Search button clicked.")
    #             time.sleep(2)

    #             # 🔽 Alert Handling
    #             try:
    #                 alert_msg_elem = WebDriverWait(driver, 5).until(
    #                     EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'swal2-html-container')]"))
    #                 )
    #                 alert_text = alert_msg_elem.text.strip()

    #                 alert_ok_btn = WebDriverWait(driver, 5).until(
    #                     EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'swal2-confirm')]"))
    #                 )

    #                 print("⚠️ Alert Detected:", alert_text)

    #                 if "Captcha mismatched" in alert_text:
    #                     print("❌ CAPTCHA mismatched! Retrying...")
    #                     driver.execute_script("arguments[0].click();", alert_ok_btn)
    #                     time.sleep(2)

    #                     # Refresh image
    #                     refresh_img = WebDriverWait(driver, 5).until(
    #                         EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'refresh_image.png')]"))
    #                     )
    #                     driver.execute_script("arguments[0].click();", refresh_img)
    #                     time.sleep(2)
    #                     continue  # retry loop

    #                 elif "No Data Found" in alert_text:
    #                     print("ℹ️ No Data Found.")
    #                     driver.execute_script("arguments[0].click();", alert_ok_btn)
    #                     time.sleep(2)
    #                     return  # Stop loop

    #                 else:
    #                     print("⚠️ Unknown alert:", alert_text)
    #                     driver.execute_script("arguments[0].click();", alert_ok_btn)
    #                     time.sleep(2)
    #                     continue

    #             except Exception:
    #                 print("✅ No alert detected.")

    #             # 🕐 Wait for paginator to confirm success
    #             try:
    #                 WebDriverWait(driver, 15).until(
    #                     EC.presence_of_element_located((By.XPATH, "//mat-paginator"))
    #                 )
    #                 print("📄 Results loaded successfully.")
    #                  # ✅ All done — exit loop
    #                 try:
    #                     dropdown_xpath = "/html/body/app-root/div/app-layout/div/div/div/div/app-search-document/div[3]/div[2]/div[2]/div/fieldset[2]/div/div[2]/div/div[2]/div[2]/mat-paginator/div/div/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[2]"
    #                     option_100_xpath = "/html/body/div[3]/div[2]/div/div/div/mat-option[4]/span"

    #                     dropdown = WebDriverWait(driver, 10).until(
    #                         EC.presence_of_element_located((By.XPATH, dropdown_xpath))
    #                     )
    #                     driver.execute_script("arguments[0].click();", dropdown)
    #                     print("🔽 Dropdown clicked.")

    #                     option_100 = WebDriverWait(driver, 10).until(
    #                         EC.presence_of_element_located((By.XPATH, option_100_xpath))
    #                     )
    #                     driver.execute_script("arguments[0].click();", option_100)
    #                     print("✅ Selected '100' from dropdown.")
                        
    #                 except Exception as e:
    #                     print("❌ Error during dropdown selection:", str(e))

    #                 break  # ✅ Exit after setting dropdown

    #             except Exception:
    #                 print("⚠️ No paginator found, retrying...")
    #                 try:
    #                     refresh_img = driver.find_element(By.XPATH, "//img[contains(@src, 'refresh_image.png')]")
    #                     driver.execute_script("arguments[0].click();", refresh_img)
    #                 except:
    #                     pass
    #                 time.sleep(2)
    #                 continue

    #         except Exception as e:
    #             print("❌ General Error:", str(e))
    #             time.sleep(2)
    #             continue




######################## now clicking on data




# 🔹 Click First Document Link
#     try:
#         first_doc = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'link') and contains(text(),'MP50IGR')]"))
#         )
#         first_doc.click()
#         print("✅ First document link clicked.")
#     except Exception as e:
#         print("❌ Failed to click document link:", str(e))
#         driver.quit()

#     # 🔸 Wait for Popup to Load
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//legend[contains(text(),'Registration Details')]"))
#         )
#         print("✅ Registration Details section loaded.")
#     except Exception as e:
#         print("❌ Registration section not found:", str(e))
#         driver.quit()

#     time.sleep(5)  # optional buffer

#     # 🔸 Extract All Data
#     try:
#         # 🔸 Wait for Party To data row to load
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//legend[contains(text(),'Party To')]/following::table[1]/tbody/tr"))
#         )

#         data = {
#             # 🔹 Registration
#             "Registration No": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[1]/div/table/tbody/tr/td[1]").text,
#             "Registration Date": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[1]/div/table/tbody/tr/td[2]").text,
#             "Deed Type": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[1]/div/table/tbody/tr/td[3]").text,

#             # 🔹 Party From
#             "Party From Name": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[2]/div/div/div[1]/fieldset/div/table/tbody[1]/tr/td[1]").text,
#             "Party From Guardian": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[2]/div/div/div[1]/fieldset/div/table/tbody[1]/tr/td[2]").text,
#             "Party From Type": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[2]/div/div/div[1]/fieldset/div/table/tbody[1]/tr/td[3]").text,

#             # 🔹 Party To (relative XPath safer approach)
#             "Party To Name": driver.find_element(By.XPATH, "//legend[contains(text(),'Party To')]/following::table[1]/tbody/tr/td[1]").text,
#             "Party To Guardian": driver.find_element(By.XPATH, "//legend[contains(text(),'Party To')]/following::table[1]/tbody/tr/td[2]").text,
#             "Party To Type": driver.find_element(By.XPATH, "//legend[contains(text(),'Party To')]/following::table[1]/tbody/tr/td[3]").text,

#             "Districts": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[1]").text,
#             "Tehsil": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[2]").text,
#             "Type Of Area": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[3]").text,
#             "Ward/Village Name": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[4]").text,
#             "Property Type": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[5]").text,
#             "Address": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[6]").text,
#             "Property ID": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[7]").text,
#             "Khasra No": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[8]").text,
#             "House/Flat No./Plot No.": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[9]").text
        
#         }

#         # 💾 Save to Excel
#         df = pd.DataFrame([data])
#         df.to_excel("sampada_data.xlsx", index=False)
#         print("📁 Data saved to 'sampada_data.xlsx'")
#         try:
#             close_button = WebDriverWait(driver, 5).until(
#                 EC.element_to_be_clickable((By.XPATH, "/html/body/ngb-modal-window/div/div/button[2]/span"))
#             )
#             close_button.click()
#             print("✅ Modal closed successfully.")
#         except Exception as e:
#             print("⚠️ Failed to close modal:", str(e))

#     except Exception as e:
#         print("❌ Error extracting data:", str(e))

#     # ✅ Continue with next steps if any
    

# ######## for testing



# 🔹 Test First Document Click (Optional)
    try:
        first_doc = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'link') and contains(text(),'MP50IGR')]"))
        )
        first_doc.click()
        print("✅ First document link clicked.")

        # 🔸 Wait for Popup to Load
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//legend[contains(text(),'Registration Details')]"))
        )
        print("✅ Registration Details section loaded.")

        time.sleep(5)  # optional buffer
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/ngb-modal-window/div/div/button[2]/span"))
        )
        close_button.click()
        print("✅ Closed first modal test.")

    except Exception as e:
        print("❌ Failed first document test:", str(e))

    # 🔁 Loop through all documents and extract data from each popup
    all_data = []

    try:
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr/td[2]/span[contains(@class, 'link')]"))
        )

        print(f"🔍 Found {len(rows)} document rows")

        for index in range(len(rows)):
            try:
                rows = driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]/span[contains(@class, 'link')]")
                driver.execute_script("arguments[0].scrollIntoView(true);", rows[index])
                time.sleep(1)
                rows[index].click()
                print(f"✅ Clicked row {index + 1}")

                # 🔹 Wait for Popup to Load
                try:
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//legend[contains(text(),'Registration Details')]"))
                    )
                    print("✅ Registration Details section loaded.")
                except Exception as e:
                    print("❌ Registration section not found:", str(e))
                    continue

                time.sleep(1)  # Optional buffer

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//legend[contains(text(),'Party To')]/following::table[1]/tbody/tr"))
                )

                data = {
                    "Registration No": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[1]/div/table/tbody/tr/td[1]").text,
                    "Registration Date": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[1]/div/table/tbody/tr/td[2]").text,
                    "Deed Type": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[1]/div/table/tbody/tr/td[3]").text,
                    "Party From Name": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[2]/div/div/div[1]/fieldset/div/table/tbody[1]/tr/td[1]").text,
                    "Party From Guardian": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[2]/div/div/div[1]/fieldset/div/table/tbody[1]/tr/td[2]").text,
                    "Party From Type": driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div/fieldset[2]/div/div/div[1]/fieldset/div/table/tbody[1]/tr/td[3]").text,
                    "Party To Name": driver.find_element(By.XPATH, "//legend[contains(text(),'Party To')]/following::table[1]/tbody/tr/td[1]").text,
                    "Party To Guardian": driver.find_element(By.XPATH, "//legend[contains(text(),'Party To')]/following::table[1]/tbody/tr/td[2]").text,
                    "Party To Type": driver.find_element(By.XPATH, "//legend[contains(text(),'Party To')]/following::table[1]/tbody/tr/td[3]").text,
                    "Districts": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[1]").text,
                    "Tehsil": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[2]").text,
                    "Type Of Area": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[3]").text,
                    "Ward/Village Name": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[4]").text,
                    "Property Type": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[5]").text,
                    "Address": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[6]").text,
                    "Property ID": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[7]").text,
                    "Khasra No": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[8]").text,
                    "House/Flat No./Plot No.": driver.find_element(By.XPATH, "//legend[contains(text(),'Property Details')]/following::table[1]/tbody/tr/td[9]").text
                }

                all_data.append(data)

                try:
                    close_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "/html/body/ngb-modal-window/div/div/button[2]/span"))
                    )
                    close_button.click()
                    print(f"✅ Closed modal for row {index + 1}")
                except Exception as e:
                    print("⚠️ Failed to close modal:", str(e))

                time.sleep(2)

            except Exception as e:
                print(f"❌ Error processing row {index + 1}:", str(e))
                continue

        # Save all data at the end
        df = pd.DataFrame(all_data)
        df.to_excel("sampada_all_data.xlsx", index=False)
        print("📁 All records saved to 'sampada_all_data.xlsx'")

    except Exception as e:
        print("❌ Error during row scraping:", str(e))










solve_only_captcha_and_search()
