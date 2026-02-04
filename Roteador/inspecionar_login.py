from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


def inspecionar_pagina():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    
    caminho_chromedriver = r"C:\Users\ricardo\Documents\GitHub\RPA\WebDrivers\CHROME\chromedriver.exe"
    servico = Service(caminho_chromedriver)
    
    driver = webdriver.Chrome(service=servico, options=chrome_options)
    
    try:
        print("Acessando o roteador...")
        driver.get("http://10.2.17.30")
        
        time.sleep(2)
        
        print("\n=== HTML DA PÁGINA ===")
        print(driver.page_source)
        
        print("\n\nPágina carregada! O navegador vai ficar aberto por 30 segundos.")
        print("Copie o HTML acima e me envie!")
        time.sleep(30)
        
    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        driver.quit()
        print("Navegador fechado.")


if __name__ == "__main__":
    inspecionar_pagina()