from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "localhost:9222" 

driver = webdriver.Chrome(options=chrome_options)

sku_list = [
    "A100", "A105", "A1200", "A1250", "A140", "A1400", "A145", "A150", "A1500",
    "A155", "A157", "A158", "A160", "A165", "A170", "A175", "A185", "A210", "A220",
    "A240", "A253", "A255", "A260", "A275", "A290", "A295", "A300", "A301", "A305",
    "A310", "A315", "A320", "A440", "A445", "A450", "A480", "A481", "A482", "A490",
    "A500", "A510", "A515", "A520", "A530", "A535", "A540", "A545", "A605", "A610",
    "A620", "A630", "A635", "A640", "A645", "A650", "A655", "A660", "A670", "A690",
    "A730", "A740", "A745", "A750", "A770", "A780", "A820", "A825", "A833", "A835",
    "A840", "A870", "A880", "A940"
]

print("Conectado à página existente.")

for sku in sku_list:
    try:
        search_box = driver.find_element(By.ID, ":R2akacq5p6:")
        search_box.send_keys(Keys.CONTROL, 'a')
        search_box.send_keys(Keys.DELETE)
        search_box.send_keys(sku)
        search_box.send_keys(Keys.ENTER)

        time.sleep(3)

        try:
            checkbox = driver.find_element(By.CLASS_NAME, "andes-checkbox__input")
            if checkbox.get_attribute("disabled"):  # Se a checkbox está desabilitada, não há resultados
                print(f"SKU {sku}: Nenhum anúncio encontrado.")
            else:  # Se a checkbox está habilitada, há resultados
                print(f"SKU {sku}: Anúncio(s) encontrado(s).")
        except Exception as e:
            print(f"SKU {sku}: Erro ao verificar o estado da checkbox. {e}")

    except Exception as e:
        print(f"Erro ao buscar SKU {sku}: {e}")

    time.sleep(1)
