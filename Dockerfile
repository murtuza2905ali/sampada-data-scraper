# Base image: lightweight Python 3.13
FROM python:3.13-slim

# System dependencies install karo
RUN apt-get update && apt-get install -y \
    wget unzip gnupg curl fonts-liberation libasound2 libatk-bridge2.0-0 \
    libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 \
    libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 \
    libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 \
    libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 \
    libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Google Chrome install karo
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install \
    && rm google-chrome-stable_current_amd64.deb

# Chromedriver install karo
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}') && \
    DRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE") && \
    wget https://chromedriver.storage.googleapis.com/$DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm chromedriver_linux64.zip

# Display set karo (headless mode ke liye)
ENV DISPLAY=:99

# Work directory set karo
WORKDIR /app
COPY . /app

# Python dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# Django collectstatic ke liye environment variable
ENV PYTHONUNBUFFERED=1

# Gunicorn ke sath Django run karo
CMD ["gunicorn", "sampada_scraper.wsgi:application", "--timeout", "120", "--workers", "2", "--bind", "0.0.0.0:10000"]
