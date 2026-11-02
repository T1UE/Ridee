import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
# options.page_load_strategy = 'eager' 

# 2. Disable heavy browser features
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

# Headless mode
options.add_argument("--headless=new")

# Performance optimizations
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")


def check(username, password):
    r = requests.get(f"https://www.instagram.com/{username}")
    r_str = str(r.text)

    soup = BeautifulSoup(r_str, "html.parser")
    html_length = len(soup.text)
    if html_length > 100:
        pass
    else:
        return 99
    #password checking
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com/accounts/login")

    usr = driver.find_element(By.NAME, "email")
    usr.send_keys(f"{username}")
    passs = driver.find_element(By.NAME, "pass")
    passs.send_keys(f"{password}")
    # time.sleep(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    WebDriverWait(driver, 30).until(
        lambda driver: driver.execute_script(
            "return document.readyState"
        ) == "complete"
    )
    time.sleep(10)
    try:
        usr = driver.find_element(By.NAME, "email")
        return 99
    except:
        return 100
    
