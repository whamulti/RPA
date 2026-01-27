# Community Version: This license is intended for educational and tool evaluation purposes.

import pandas as pd
from jornadaRPA.webScrap import Webscrap
from botcity.web.browsers.chrome import default_options
from botcity.web import *
from datetime import datetime

class Bot:
    def bot(self):
        # Sequence: Teste_glpi_formulario

        #  Activity Instance WebBot
        # Displayname: Abre_Chrome
        webBot = WebBot()

        # Open Browser Activity
        # Displayname: Pagina_Zabbix
        webBot = WebBot()
        webBot.driver_path = "C:\\Users\\ricardo\\Documents\\GitHub\\RPA\\WebDrivers\\CHROME\\chromedriver.exe"
        webBot.browser = Browser.CHROME
        webBot.headless = False
        webBotDef_options = default_options()
        webBotDef_options.add_argument("--page-load-strategy=Normal")
        webBot.options = webBotDef_options
        webBot.browse("file:///C:/Users/Ricardo/Downloads/usuarios_biotipo.html")

        # Maximize window Activity
        # Displayname: Maximiza_Window
        webBot.maximize_window()

        # Extract DataTable Activity
        # Displayname: Extrair_dados_tabela
        banco_formulario = Webscrap().webscrap(inBot=webBot, inXPATH="/html/body/div/div[2]/table", inLines=0,inNext='', inGetLink=False)

        banco_formulario = banco_formulario.to_dict(orient='records')

        #  Navigate to Activity
        # Displayname: Navegar_para
        webBot.navigate_to("http://10.2.17.26/front/form/form.form.php?id=17")

        # Find Element Activity
        # Displayname: Localiza_botao
        Error = webBot.find_element(selector="/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Clica_botao
        Error.click()

        # DisplayName: Elemetos_Login_Glpi

        # Sequence: Element list

        # Find Element Activity
        # Displayname: usuario_glpi
        usuario_glpi = webBot.find_element(selector="login_name", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: senha_glpi
        senha_glpi = webBot.find_element(selector="login_password", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: conectar_se_glpi
        botao_glpi = webBot.find_element(selector="/html/body/div/div/div/div[2]/div[2]/form/div/div/div[6]/button", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Usuario_glpi
        usuario_glpi.send_keys("ricardo")

        # Type Into Activity
        # Displayname: Senha_glpi
        senha_glpi.send_keys("0805")

        # Click Activity
        # Displayname: Clica_botao
        botao_glpi.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Find_Element
        opcao = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div/form/div/div/div/div/div/div/div/section/div[3]/section/section/div[2]/div[4]/div/div/span/span/span/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        opcao.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Find_Element
        seleciona = webBot.find_element(selector=".select2-results__option--highlighted", by=By.CSS_SELECTOR, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        seleciona.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Encontra_campo
        nome_usuario = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div/form/div/div/div/div/div/div/div/section/div[3]/section/section/div[2]/div[4]/div[2]/div[2]/input[2]", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # ForEach Activity
        # Displayname: Laco_repeticao
        for item_formulario in banco_formulario:
            # Sequence: Corpo

            # DisplayName: Formulario_acao_elementos_web

            # Sequence: Lista_acoes

            # Find Element Activity
            # Displayname: Encontrar_nome
            nome_usuario = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div/form/div/div/div/div/div/div/div/section/div[3]/section/section/div[2]/div[4]/div[2]/div[2]/input[2]", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_nome
            nome_usuario.send_keys(item_formulario["NOME"])

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)


        # Find Element Activity
        # Displayname: Find_Element
        salva = webBot.find_element(selector="update", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        salva.click()

        # Wait Activity
        # Displayname: 3_segundos
        webBot.wait(3000)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()