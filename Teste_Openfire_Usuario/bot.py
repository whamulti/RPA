# Community Version: This license is intended for educational and tool evaluation purposes.

import pandas as pd
from jornadaRPA.webScrap import Webscrap
from botcity.web.browsers.chrome import default_options
from botcity.web import *
from datetime import datetime

class Bot:
    def bot(self):
        # Sequence: Sequencia_Teste_Openfire_Usuario

        #  Activity Instance WebBot
        # Displayname: Abre_Chrome
        webBot = WebBot()

        # Open Browser Activity
        # Displayname: Pagina_web
        webBot = WebBot()
        webBot.driver_path = "C:\\Users\\ricardo\\Documents\\GitHub\\RPA\\WebDrivers\\CHROME\\chromedriver.exe"
        webBot.browser = Browser.CHROME
        webBot.headless = False
        webBotDef_options = default_options()
        webBotDef_options.add_argument("--page-load-strategy=Normal")
        webBot.options = webBotDef_options
        webBot.browse("file:///C:/Users/ricardo/Downloads/openfire_users.html")

        # Maximize window Activity
        # Displayname: Maximize_Window
        webBot.maximize_window()

        # Extract DataTable Activity
        # Displayname: Extrair_dados_tabela
        banco_openfire = Webscrap().webscrap(inBot=webBot, inXPATH="/html/body/div/div[2]/table", inLines=0,inNext='', inGetLink=False)

        banco_openfire = banco_openfire.to_dict(orient='records')

        #  Navigate to Activity
        # Displayname: Navegar_para
        webBot.navigate_to("http://10.2.17.48:9090/user-create.jsp")

        # DisplayName: Elemetos_Login_Glpi

        # Sequence: Element list

        # Find Element Activity
        # Displayname: Find_Element
        nameusername = webBot.find_element(selector="username", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Find_Element
        namepassword = webBot.find_element(selector="password", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Find_Element
        idsubmit = webBot.find_element(selector="submit", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Usuario_glpi
        nameusername.send_keys("admin")

        # Type Into Activity
        # Displayname: Senha_glpi
        namepassword.send_keys("Tipo@12345")

        # Click Activity
        # Displayname: Clica_botao
        idsubmit.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Encontra_campo
        nome_user = webBot.find_element(selector="username", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # ForEach Activity
        # Displayname: Laco_repeticao
        for item_usuario in banco_openfire:
            # Sequence: Corpo

            # DisplayName: Formulario_acao_elementos_web

            # Sequence: Lista_acoes

            # Find Element Activity
            # Displayname: Encontrar_nome
            nome_user = webBot.find_element(selector="username", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_nome
            nome_user.send_keys(item_usuario["USERNAME"])

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Encontrar_nome
            nome_name = webBot.find_element(selector="name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_nome
            nome_name.send_keys(item_usuario["NAME"])

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Encontrar_nome
            nome_senha = webBot.find_element(selector="password", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_nome
            nome_senha.send_keys(item_usuario["PASSWORD"])

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Encontrar_nome
            nome_confirma_senha = webBot.find_element(selector="passwordConfirm", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_nome
            nome_confirma_senha.send_keys(item_usuario["PASSWORD"])

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Encontrar_nome
            envia_usuario = webBot.find_element(selector="create", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Adicionar_usuario
            envia_usuario.click()

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            menu_grupo = webBot.find_element(selector="/html/body/div/div[2]/table/tbody/tr/td/div/div/div/ul/li[2]/ul/li[4]/a", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            menu_grupo.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # DisplayName: Element_Library

            # Sequence: Element list

            # Find Element Activity
            # Displayname: Find_Element
            joli = webBot.find_element(selector="/html/body/div/div[2]/table/tbody/tr/td[2]/div/div[2]/table/tbody/tr/td[3]/a/img", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Find Element Activity
            # Displayname: Find_Element
            itapevi = webBot.find_element(selector="/html/body/div/div[2]/table/tbody/tr/td[2]/div/div[2]/table/tbody/tr[2]/td[3]/a/img", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Find Element Activity
            # Displayname: Find_Element
            mendes = webBot.find_element(selector="/html/body/div/div[2]/table/tbody/tr/td[2]/div/div[2]/table/tbody/tr[3]/td[3]/a/img", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Sequence: Conditional Structure

            # If Activity
            # Displayname: If Condition
            if item_usuario["LOCALIZACAO"] == "JOLI":
                # Sequence: Body

                # Click Activity
                # Displayname: Click
                joli.click()


            # ElseIf Activity
            # Displayname: ElseIf
            elif item_usuario["LOCALIZACAO"] == "ITAPEVI":
                # Sequence: Body

                # Click Activity
                # Displayname: Click
                itapevi.click()


            # Else Activity
            # Displayname: Else
            else:
                # Sequence: Body

                # Click Activity
                # Displayname: Click
                mendes.click()


            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            #  Navigate to Activity
            # Displayname: retornar_pagina
            webBot.navigate_to("http://10.2.17.48:9090/user-create.jsp")

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)



        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()