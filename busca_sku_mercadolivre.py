from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configura o Selenium para se conectar ao Chrome aberto no modo de depuração na porta 9222
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "localhost:9222"  # Porta de depuração remota definida anteriormente

# Conecta ao Chrome já aberto
driver = webdriver.Chrome(options=chrome_options)

# Lista de SKU atualizada
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


# Verifique se a página desejada já está aberta
print("Conectado à página existente.")

# Função para buscar cada SKU e verificar se houve resultados
for sku in sku_list:
    try:
        # Encontra o campo de pesquisa pelo ID e insere o SKU
        search_box = driver.find_element(By.ID, ":R2akacq5p6:")
        search_box.send_keys(Keys.CONTROL, 'a')  # Seleciona todo o texto com "CTRL + A"
        search_box.send_keys(Keys.DELETE)  # Apaga o conteúdo selecionado com DELETE
        search_box.send_keys(sku)  # Insere o SKU
        search_box.send_keys(Keys.ENTER)  # Pressiona Enter para buscar

        # Espera para que a página de resultados carregue
        time.sleep(3)  # Ajuste o tempo de acordo com a velocidade da internet e o tempo de resposta do site

        # Verifica o estado da checkbox para ver se o anúncio foi encontrado
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

    # Pequena pausa entre buscas
    time.sleep(1)

# A janela do navegador permanecerá aberta após a execução
