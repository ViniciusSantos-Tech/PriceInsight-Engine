from scrap import Scrap
from ai_processor import IA
from crud import Crud

print("--- INICIANDO SCRAPING ---")
app_scrapping = Scrap()
scrapping_response = app_scrapping.Scraping()

# LOG 1: O que o Selenium pegou?
print(f"DEBUG: Tamanho do texto capturado: {len(scrapping_response)} caracteres")
print(f"DEBUG: Início do texto capturado: {scrapping_response[:200]}...")

print("--- INICIANDO IA ---")
app_ia = IA()
ia_response = app_ia.analyze_with_ai(scrapping_response)

# LOG 2: O que a IA respondeu?
print(f"DEBUG: Resposta bruta da IA: {ia_response}")

dics_dates = app_ia.format_response(ia_response)
print(f"DEBUG: Dicionário formatado: {dics_dates}")

print("--- SALVANDO NO BANCO ---")
app_crud = Crud()

# Evita salvar se o preço for None ou lixo
if dics_dates.get("Price") and dics_dates["Price"] != "None":
    crud_response = app_crud.add_history(Product="Monitor", Price=dics_dates["Price"])
    print(f"SUCESSO: {crud_response}")
else:
    print("ERRO: Preço não identificado. Nada foi salvo no banco.")
