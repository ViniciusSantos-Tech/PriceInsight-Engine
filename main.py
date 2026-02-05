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
app_ai = IA()
msg,response, ai_response = app_ai.analyze_with_ai(scrapping_response)
ai_sucess, ai_log, dics_dates = app_ai.format_response(ai_response)
if msg == False:
    print(response)
print(ai_response)

if not ai_sucess:
    print(ai_log)
    exit()

print("Phase three----------------")
app_crud = Crud()
msg, crud_response = app_crud.add_history(Product="VideoCard", Price=dics_dates["Price"])
if crud_response == False:
    print(crud_response)
print(crud_response)




