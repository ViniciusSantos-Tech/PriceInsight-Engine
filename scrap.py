from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Scrap():

    def __init__(self):  
        self.driver = None
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--headless=new")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.url = "https://www.mercadolivre.com.br/smartphone-motorola-moto-g06-128gb-12gb-4gb-ram-8gb-ram-boost-e-camera-50mp-com-ai-bateria-de-5200-mah-tela-69-azul-marinho/p/MLB58353028#polycard_client=search-desktop&search_layout=grid&position=1&type=product&tracking_id=7889f463-4084-46f1-8a63-1b8a7fb0429b&wid=MLB4228627923&sid=search"
    def Scraping(self):
        self.driver = webdriver.Chrome(options=self.options)
        try:
            self.driver.get(self.url)
            wait = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "header")))

            price_fraction = self.driver.find_element(By.XPATH, '//*[@id="price"]/div/div[1]/div[1]/span[1]/span/span[2]').text

            return f"Preço do produto: {price_fraction}, status: 'Sucesso"
        except NoSuchElementException:
            return "Error!, elemento nao encontrado, status: 'Falha"
        finally:
            self.driver.quit()
        





