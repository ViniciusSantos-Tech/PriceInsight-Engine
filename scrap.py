
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
        self.url = "https://www.mercadolivre.com.br/smartphone-motorola-moto-g06-128gb-12gb-4gb-ram-8gb-ram-boost-e-camera-50mp-com-ai-bateria-de-5200-mah-tela-69-azul-marinho/p/MLB58353028"

    def Scraping(self):
        driver = webdriver.Chrome(options=self.options)
        try:
            driver.get(self.url)
            
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ui-pdp-price__second-line"))
            )
            price_data = driver.find_element(By.CLASS_NAME, "ui-pdp-container__row--price").text
            
            return f"Captured data: {price_data}, status: 'Success'"
        except Exception as e:
            page_content = driver.find_element(By.TAG_NAME, "body").text[:500]
            return f"Scraping failed. Page content: {page_content}"
        finally:
            driver.quit()
