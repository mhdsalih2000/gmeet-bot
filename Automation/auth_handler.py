from selenium import webdriver
import pickle
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Runs in headless mode (new method)
options.add_argument("--disable-gpu")   # Disable GPU acceleration
options.add_argument("--no-sandbox")    # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Prevent crashes in Docker/Linux

driver = webdriver.Chrome(options=options)
driver.get("https://accounts.google.com/signin")

input("Log in manually, then press Enter to save cookies...")

pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
print("✅ Cookies saved successfully!")

driver.quit()
