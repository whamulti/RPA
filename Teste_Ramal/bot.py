# Community Version: This license is intended for educational and tool evaluation purposes.

from jornadaRPA.webScrap import Webscrap
from botcity.web.browsers.chrome import default_options
from botcity.web import *
from datetime import datetime

class Bot:
    def bot(self):
        # Sequence: Sequencia_bot

        #  Activity Instance WebBot
        # Displayname: Abre_Chrome
        webBot = WebBot()

        # Open Browser Activity
        # Displayname: Pagina_Zabbix
        webBot = WebBot()
        webBot.driver_path = "C:\\RPA\\WebDrivers\\CHROME\\chromedriver.exe"
        webBot.browser = Browser.CHROME
        webBot.headless = False
        webBotDef_options = default_options()
        webBotDef_options.add_argument("--page-load-strategy=Normal")
        webBot.options = webBotDef_options
        webBot.browse("http://10.2.17.7/zabbix/zabbix.php?action=host.list&filter_groups%5B%5D=33&filter_host=&filter_dns=&filter_ip=&filter_port=&filter_status=-1&filter_monitored_by=-1&filter_evaltype=0&filter_tags%5B0%5D%5Btag%5D=&filter_tags%5B0%5D%5Boperator%5D=0&filter_tags%5B0%5D%5Bvalue%5D=&filter_set=1")

        # Maximize window Activity
        # Displayname: Maximiza_Window
        webBot.maximize_window()

        # Find Element Activity
        # Displayname: Localiza_botao
        voce = webBot.find_element(selector="/html/body/div/main/output/div[2]/button", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Clicar_botao
        voce.click()

        # DisplayName: Elemetos_Login_Zabbix

        # Sequence: Elementos_Login_Zabbix

        # Find Element Activity
        # Displayname: Usuario
        usuario_zabbix = webBot.find_element(selector="name", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Senha
        senha_zabbix = webBot.find_element(selector="password", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Conectar_se
        botao_zabbix = webBot.find_element(selector="enter", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Usuario_zabbix
        usuario_zabbix.send_keys("admin")

        # Type Into Activity
        # Displayname: Senha_zabbix
        senha_zabbix.send_keys("biotipo2023")

        # Click Activity
        # Displayname: Botao_zabbix
        botao_zabbix.click()

        # Extract DataTable Activity
        # Displayname: Extrair_dados_tabela
        banco_impressoras_zabbix = Webscrap().webscrap(inBot=webBot, inXPATH="/html/body/div/main/form/table", inLines=0,inNext='', inGetLink=False)

        # Sequence: Assign List

        # Assign Activity
        # Displayname: Assign
        banco_impressoras_zabbix = banco_impressoras_zabbix.assign(Interface2=banco_impressoras_zabbix['Interface'].str.split(':').str[0])

        # Assign Activity
        # Displayname: Assign_Values
        lista_ips = banco_impressoras_zabbix['Interface2'].tolist()

        # Assign Activity
        # Displayname: Assign_Values
        banco_impressoras_zabbix = banco_impressoras_zabbix.to_dict(orient='records')

        #  Navigate to Activity
        # Displayname: Navegar_para
        webBot.navigate_to("http://10.2.17.66/front/phone.form.php?id=-1&withtemplate=2")

        # Find Element Activity
        # Displayname: Localiza_botao
        Error = webBot.find_element(selector="/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Clica_botao
        Error.click()

        # DisplayName: Elemetos_Login_Glpi

        # Sequence: Element list

        # Find Element Activity
        # Displayname: Find_Element
        usuario_glpi = webBot.find_element(selector="login_name", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Find_Element
        senha_glpi = webBot.find_element(selector="login_password", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Find_Element
        botao_glpi = webBot.find_element(selector="/html/body/div/div/div/div[2]/div[2]/form/div/div/div[6]/button", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Usuario_glpi
        usuario_glpi.send_keys("ricardo")

        # Type Into Activity
        # Displayname: Senha_glpi
        senha_glpi.send_keys("0805")

        # Click Activity
        # Displayname: Botão
        botao_glpi.click()

        # Find Element Activity
        # Displayname: Encontra_campo
        nome_impressora = webBot.find_element(selector="name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # ForEach Activity
        # Displayname: Laco_repeticao
        for item_impressora in banco_impressoras_zabbix:
            # Sequence: Corpo

            # DisplayName: Formulario_acao_elementos_web

            # Sequence: Lista_acoes

            # Find Element Activity
            # Displayname: Encontrar_nome
            nome_impressora = webBot.find_element(selector="name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_banco
            nome_impressora.send_keys(item_impressora["Nome"])

            # Wait Activity
            # Displayname: Wait
            webBot.wait(5000)

            # Scroll Element Activity
            # Displayname: Descer_pagina
            webBot.scroll_down(clicks=15)

            # Wait Activity
            # Displayname: Wait
            webBot.wait(5000)

            # Find Element Activity
            # Displayname: Encontrar_nome
            envia_impressora = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Adicionar_impressora
            envia_impressora.click()

            # Wait Activity
            # Displayname: Espera_pop_up
            webBot.wait(15000)

            # Find Element Activity
            # Displayname: Find_Element
            menu_porta_impressora = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/ul/li[9]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            menu_porta_impressora.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(5000)

            # Find Element Activity
            # Displayname: Find_Element
            adicionar_ip = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            adicionar_ip.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(5000)

            # Find Element Activity
            # Displayname: Find_Element
            end_ip = webBot.find_element(selector="NetworkName__ipaddresses[-1]", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Type Into end_ip field
            end_ip.send_keys(item_impressora["Interface2"])

            # Wait Activity
            # Displayname: Wait
            webBot.wait(5000)

            # Find Element Activity
            # Displayname: Find_Element
            envia_ip = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            envia_ip.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(15000)

            #  Navigate to Activity
            # Displayname: Navigate_To
            webBot.navigate_to("http://10.2.17.66/front/phone.form.php?id=-1&withtemplate=2")

            # Wait Activity
            # Displayname: Wait
            webBot.wait(5000)



        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()