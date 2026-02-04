from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


def inspecionar_pagina_reboot():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    
    caminho_chromedriver = r"C:\Users\ricardo\Documents\GitHub\RPA\WebDrivers\CHROME\chromedriver.exe"
    servico = Service(caminho_chromedriver)
    
    driver = webdriver.Chrome(service=servico, options=chrome_options)
    
    try:
        print("Acessando o roteador...")
        driver.get("http://10.2.17.30")
        
        wait = WebDriverWait(driver, 10)
        
        print("Fazendo login...")
        campo_usuario = wait.until(EC.presence_of_element_located((By.ID, "userName")))
        campo_usuario.send_keys("admin")
        
        campo_senha = driver.find_element(By.ID, "pcPassword")
        campo_senha.send_keys("Admin1")
        
        botao_login = driver.find_element(By.ID, "loginBtn")
        botao_login.click()
        
        time.sleep(3)
        
        print("Trocando para o frame do menu...")
        driver.switch_to.frame("bottomLeftFrame")
        
        print("Clicando em System Tools...")
        system_tools = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "System Tools")))
        system_tools.click()
        
        time.sleep(1)
        
        print("Clicando em - Reboot...")
        reboot_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "- Reboot")))
        reboot_link.click()
        
        time.sleep(2)
        
        print("Voltando ao contexto principal...")
        driver.switch_to.default_content()
        
        print("Trocando para o frame do conteúdo (mainFrame)...")
        driver.switch_to.frame("mainFrame")
        
        print("\n=== HTML DA PÁGINA DE REBOOT ===")
        print(driver.page_source)
        
        print("\n=== PROCURANDO BOTÕES ===")
        botoes = driver.find_elements(By.TAG_NAME, "button")
        for botao in botoes:
            print(f"Botão encontrado: ID='{botao.get_attribute('id')}' - Texto='{botao.text}'")
        
        inputs = driver.find_elements(By.TAG_NAME, "input")
        for inp in inputs:
            if inp.get_attribute('type') in ['button', 'submit']:
                print(f"Input encontrado: ID='{inp.get_attribute('id')}' - Type='{inp.get_attribute('type')}' - Value='{inp.get_attribute('value')}'")
        
        print("\n\nO navegador vai ficar aberto por 30 segundos.")
        time.sleep(30)
        
    except Exception as e:
        print(f"Erro: {e}")
        import traceback
        traceback.print_exc()
        time.sleep(10)
    
    finally:
        driver.quit()
        print("Navegador fechado.")


if __name__ == "__main__":
    inspecionar_pagina_reboot()