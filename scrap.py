from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Scrap():
    def __init__(self):  
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--headless=new")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.url = "https://www.amazon.com.br/ZOTAC-Gaming-GeForce-Extreme-Infinity/dp/B0F135FPK3/ref=sr_1_2?dib=eyJ2IjoiMSJ9.moQMh3L63lwyuFpixU-NuoXgJM8vxeIz9TrBkWsOrf3zaZd_HmSocJ8w7pEqfoXiqtE3ecDCVtJ8XONsSSHC7NQj4uZzdQeqfIM6jnZiVCQzL3GMPC8HJlVaJ3OP67g-F3EWPmqsZUS0MOyppKkb9Kb1Gro9bBqKtNITR_avjvXquHHf1D_tjsSLe1ASwaYEFUP8p-F9JkttlEdLP_2bOHf9nSFhRFZ_F0oMKuEgyvNquLocp_PznCpDvUAWg6qmXtEGDi98XMOg3lmUoHWh09MLzOwLx4kGuYc6Lwe_pKw.68qg9e6K0Ic9SscAaZEQxiDhYVfkjlWseal7uoUCS4g&dib_tag=se&keywords=rtx+5090&qid=1769525196&sr=8-2&ufe=app_do%3Aamzn1.fos.a492fd4a-f54d-4e8d-8c31-35e0a04ce61e"

    def Scraping(self):
        driver = webdriver.Chrome(options=self.options)
        try:
            driver.get(self.url)

            wait = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
            )
            price_container = driver.find_element(By.CLASS_NAME, "a-price-whole").text
            
            return f"Data: {price_container}, status: 'Sucess'"
            
        except Exception as e:

            body_error = driver.find_element(By.TAG_NAME, "body").text[:500]
            return f"Element failure. Content: {body_error}"
        finally:
            driver.quit()
