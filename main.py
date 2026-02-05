from scrap import Scrap, Scrap2
from ai_processor import IA
from crud import Crud

print("Phase one----------------")
app_scrap1 = Scrap()
app_scrap2 = Scrap2()

status1, response1 = app_scrap1.scraping_item1()
status2, response2 = app_scrap2.scraping_item2()
if not status1 or not status2:
    print("Error in scraping operation!")
    exit()
print("Success!")

print("Phase two----------------")
app_ai = IA()

msg, ai_raw, ai_content = app_ai.analyze_with_ai(response1, response2)
ai_success, ai_log, items_list = app_ai.format_response(ai_content)
print(ai_content)
if not ai_success:
    print(ai_log)
    exit()

print("Phase three----------------")
app_crud = Crud()

for item in items_list:
    product_name = item.get("item")
    price = item.get("Price")

    if price and price != "None":
        success, crud_msg = app_crud.add_history(Product=product_name, Price=price)
        print(f"Item {product_name}: {crud_msg}")
    else:
        print(f"Skipped {product_name}: Price not found.")
