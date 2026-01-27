from scrap import Scrap
from ai_processor import IA
from crud import Crud

app_scrapping = Scrap()
scrapping_response = app_scrapping.Scraping()

app_ia = IA()
ia_response = app_ia.analyze_with_ai(scrapping_response)
dics_dates = app_ia.format_response(ia_response)


app_crud = Crud()
crud_response = app_crud.add_history(Product="Cellphone", Price=dics_dates["Price"])
print(crud_response)




