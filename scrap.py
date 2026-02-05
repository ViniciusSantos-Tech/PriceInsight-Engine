import requests
from bs4 import BeautifulSoup
from ai_processor import IA
import time
app = IA()


class Scrap():
    def __init__(self):
        self.url = "https://www.magazineluiza.com.br/placa-de-video-rtx-5090-aorus-master-ice-32g-gigabyte-nvidia-geforce-32gb-gddr7-512bits-rgb-dlss-ray-tracing-9vn5090ami-00-g10/p/cb0969d93f/in/pcvd/?seller_id=kabum"
        self.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
     }
    def scraping_item1(self):
        try:
            time.sleep(5)
            r = requests.get(self.url, headers=self.headers, timeout=10)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                for trash in soup(["script", "style", "nav", "footer", "header"]):
                    trash.decompose()

                clean_text = soup.get_text(separator=' ', strip=True)
                return True, clean_text
            else:
                return False, r.status_code
        except: 
            return "unknown error"
        
class Scrap2():
    def __init__(self):
        self.url = "https://www.magazineluiza.com.br/placa-de-video-msi-geforce-rtx-4090-gaming-trio-24gb-gddr6x/p/eb2a9d83kf/in/pcvd/?seller_id=bestgames&srsltid=AfmBOooFkzDdGdlgxzVPMoZ53dYq-Gq4PQ_NBqlEd9bGkH5zvptQ-xeNRFw"
        self.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
     }
    def scraping_item2(self):
        try:
            time.sleep(5)
            r = requests.get(self.url, headers=self.headers, timeout=10)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                for trash in soup(["script", "style", "nav", "footer", "header"]):
                    trash.decompose()

                clean_text = soup.get_text(separator=' ', strip=True)
                return True, clean_text
            else:
                return False, r.status_code
        except: 
            return "unknown error"
