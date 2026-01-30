from scrap import Scrap
from ai_processor import IA
from crud import Crud

print("Phase one----------------")
app_scrapping = Scrap()
scrapping_response = app_scrapping.Scraping()
if "Error" in scrapping_response:
    print(f"Fail: {scrapping_response}")
    exit()
else:
    print("Sucess!")

print("Phase two----------------")
app_ia = IA()
ia_response = app_ia.analyze_with_ai(scrapping_response)
dics_dates = app_ia.format_response(ia_response)



print("Phase three----------------")
app_crud = Crud()
crud_response = app_crud.add_history(Product="VideoCard", Price=dics_dates["Price"])




