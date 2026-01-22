# Community Version: This license is intended for educational and tool evaluation purposes.

import pandas as pd
from jornadaRPA.webScrap import Webscrap
from botcity.web.browsers.chrome import default_options
from botcity.web import *
from datetime import datetime

class Bot:
    def bot(self):
        # Sequence: Sequencia_bot_impressora

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
        banco_email = Webscrap().webscrap(inBot=webBot, inXPATH="/html/body/div/div[2]/table", inLines=0,inNext='', inGetLink=False)

        banco_email = banco_email.to_dict(orient='records')

        #  Navigate to Activity
        # Displayname: Navegar_para
        webBot.navigate_to("http://10.2.17.66/front/user.form.php")

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

        # Find Element Activity
        # Displayname: Encontra_campo
        nome_usuario = webBot.find_element(selector="name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # ForEach Activity
        # Displayname: Laco_repeticao
        for item_email in banco_impressoras_zabbix:
            # Sequence: Corpo

            # DisplayName: Formulario_acao_elementos_web

            # Sequence: Lista_acoes

            # Find Element Activity
            # Displayname: Encontrar_nome
            nome_usuario = webBot.find_element(selector="name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_nome
            nome_usuario.send_keys(item_email["NOME"])

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Scroll Element Activity
            # Displayname: Descer_pagina
            webBot.scroll_down(clicks=20)

            # Find Element Activity
            # Displayname: Find_Element
            email = webBot.find_element(selector="_useremails[-1]", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_ip
            email.send_keys(item_email["EMAIL"])

            # Find Element Activity
            # Displayname: Encontrar_nome
            envia_nome = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Adicionar_impressora
            envia_nome.click()

            # Wait Activity
            # Displayname: Espera_15_segundos
            webBot.wait(15000)

            # Find Element Activity
            # Displayname: Elemento_menu
            menu_porta_rede = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/ul/li[11]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            menu_porta_rede.click()

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_impressora
            adicionar_ip = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            adicionar_ip.click()

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_ip
            end_ip = webBot.find_element(selector="NetworkName__ipaddresses[-1]", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Scroll Element Activity
            # Displayname: Descer_pagina
            webBot.scroll_down(clicks=20)

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Elementos_botao
            envia_ip = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            envia_ip.click()

            # Wait Activity
            # Displayname: Espera_15_segundos
            webBot.wait(15000)

            #  Navigate to Activity
            # Displayname: retornar_pagina
            webBot.navigate_to("http://10.2.17.66/front/user.form.php")

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)



        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()