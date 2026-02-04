from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


def reiniciar_roteador():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    
    caminho_chromedriver = r"C:\Users\ricardo\Documents\GitHub\RPA\WebDrivers\CHROME\chromedriver.exe"
    servico = Service(caminho_chromedriver)
    
    driver = webdriver.Chrome(service=servico, options=chrome_options)
    
    try:
        print("=" * 60)
        print("AUTOMAÇÃO DE REBOOT DO ROTEADOR TP-LINK")
        print("=" * 60)
        
        print("\n[1/7] Acessando o roteador em http://10.2.17.30...")
        driver.get("http://10.2.17.30")
        
        wait = WebDriverWait(driver, 10)
        
        print("[2/7] Preenchendo credenciais de login...")
        campo_usuario = wait.until(EC.presence_of_element_located((By.ID, "userName")))
        campo_usuario.send_keys("admin")
        
        campo_senha = driver.find_element(By.ID, "pcPassword")
        campo_senha.send_keys("Admin1")
        
        print("[3/7] Realizando login...")
        botao_login = driver.find_element(By.ID, "loginBtn")
        botao_login.click()
        
        time.sleep(3)
        
        print("[4/7] Navegando até o menu System Tools...")
        driver.switch_to.frame("bottomLeftFrame")
        
        system_tools = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "System Tools")))
        system_tools.click()
        
        time.sleep(1)
        
        print("[5/7] Acessando a opção Reboot...")
        reboot_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "- Reboot")))
        reboot_link.click()
        
        time.sleep(2)
        
        print("[6/7] Preparando para reiniciar o roteador...")
        driver.switch_to.default_content()
        driver.switch_to.frame("mainFrame")
        
        botao_reboot = wait.until(EC.element_to_be_clickable((By.ID, "reboot")))
        
        print("[7/7] Clicando no botão Reboot...")
        botao_reboot.click()
        
        time.sleep(1)
        
        print("\n" + "=" * 60)
        print("✓ Comando de reboot enviado com sucesso!")
        print("✓ O roteador está reiniciando...")
        print("=" * 60)
        
        try:
            alert = driver.switch_to.alert
            print(f"\nAlerta detectado: {alert.text}")
            alert.accept()
            print("Alerta confirmado.")
        except:
            pass
        
        time.sleep(5)
        
    except Exception as e:
        print("\n" + "=" * 60)
        print("✗ ERRO DURANTE A AUTOMAÇÃO")
        print("=" * 60)
        print(f"Detalhes: {e}")
        import traceback
        traceback.print_exc()
        time.sleep(5)
    
    finally:
        driver.quit()
        print("\nNavegador fechado.")
        print("\nAutomação finalizada!")


if __name__ == "__main__":
    reiniciar_roteador()