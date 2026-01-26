from scrap import Scrap
from processador_ia import IA
from crud import Crud

app_scrapping = Scrap()
scrapping_response = app_scrapping.Scraping()

app_ia = IA()
ia_response = app_ia.processar_com_ia(scrapping_response)
dics_dates = app_ia.limpar_resposta_ia(ia_response)


app_crud = Crud()
crud_response = app_crud.add_history(Product="Cellphone", Price=dics_dates["Preco"])
print(crud_response)


