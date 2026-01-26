# Community Version: This license is intended for educational and tool evaluation purposes.

import pandas as pd
from jornadaRPA.webScrap import Webscrap
from botcity.web.browsers.chrome import default_options
from botcity.web import *
from datetime import datetime

class Bot:
    def bot(self):
        # Sequence: Sequencia_glpi_regra_chamado

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
        webBot.browse("file:///C:/Users/ricardo/Downloads/usuarios_biotipo.html")

        # Maximize window Activity
        # Displayname: Maximize_Window
        webBot.maximize_window()

        # Extract DataTable Activity
        # Displayname: Extrair_dados_tabela
        banco_regra = Webscrap().webscrap(inBot=webBot, inXPATH="/html/body/div/div[2]/table", inLines=0,inNext='', inGetLink=False)

        banco_regra = banco_regra.to_dict(orient='records')

        #  Navigate to Activity
        # Displayname: Navegar_para
        webBot.navigate_to("http://10.2.17.66/front/ruleticket.form.php")

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
        # Displayname: elementos_impressora_primeiro
        regra = webBot.find_element(selector="name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # ForEach Activity
        # Displayname: Laco_repeticao_criterio
        for item_regra in banco_regra:
            # Sequence: Corpo

            # DisplayName: Formulario_acao_elementos_web

            # Sequence: Lista_acoes

            # Find Element Activity
            # Displayname: elementos_impressora_primeiro
            regra = webBot.find_element(selector="name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Type_Into
            regra.send_keys(item_regra["NOME"])

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_impressora_primeiro
            nova_regra = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            nova_regra.click()

            # Wait Activity
            # Displayname: 15_segundos
            webBot.wait(15000)

            # Find Element Activity
            # Displayname: elementos_impressora_primeiro
            criterio = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/ul/li[2]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            criterio.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_impressora_primeiro
            add_criterio = webBot.find_element(selector="add_criterion", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            add_criterio.click()

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_ip_inicio_criterio
            drop_criterio = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div[2]/div/div/form/div/div/div/div/div/div/div/div/span/div/div/span/span/span/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            drop_criterio.click()

            # Wait Activity
            # Displayname: Espera_drop
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            nome_criterio = webBot.find_element(selector="/html/body/span/span/span/input", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Type_Into
            nome_criterio.send_keys("Descricao")

            # Wait Activity
            # Displayname: espera_nome
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            select_criterio = webBot.find_element(selector=".select2-results__option--highlighted", by=By.CSS_SELECTOR, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            select_criterio.click()

            # Wait Activity
            # Displayname: espera_final_criterio
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_ip_inicio_condicao
            drop_condicao = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div[2]/div/div/form/div/div/div/div/div/div/div/div/span/div/span/span/span/span/span/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            drop_condicao.click()

            # Wait Activity
            # Displayname: Espera_drop
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            nome_condicao = webBot.find_element(selector="/html/body/span/span/span/input", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Type_Into
            nome_condicao.send_keys("contem")

            # Wait Activity
            # Displayname: espera_nome
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            select_condicao = webBot.find_element(selector=".select2-results__option--highlighted", by=By.CSS_SELECTOR, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            select_condicao.click()

            # Wait Activity
            # Displayname: espera_final_condicao
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            condicao = webBot.find_element(selector="pattern", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_ip
            condicao.send_keys(item_regra["NOME"])

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Elementos_botao
            envia_condicao = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            envia_condicao.click()

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_impressora_primeiro
            acoes = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/ul/li[3]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            acoes.click()

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_impressora_primeiro
            add_acoes = webBot.find_element(selector="add_action", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            add_acoes.click()

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_ip_inicio_criterio
            drop_acoes = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div[3]/div[2]/div/form/div/div/div/div/div/div/div/div/span/div/span/span/span/span/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            drop_acoes.click()

            # Wait Activity
            # Displayname: Espera_drop
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            nome_acoes = webBot.find_element(selector="/html/body/span/span/span/input", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Type_Into
            nome_acoes.send_keys("Requerente")

            # Wait Activity
            # Displayname: espera_nome
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            select_acoes = webBot.find_element(selector=".select2-results__option--highlighted", by=By.CSS_SELECTOR, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            select_acoes.click()

            # Wait Activity
            # Displayname: espera_final_criterio
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_ip_inicio_criterio
            drop_adiciona = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div[3]/div[2]/div/form/div/div/div/div/div/div/div/div/span/div/span[2]/span/span/span/span/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            drop_adiciona.click()

            # Wait Activity
            # Displayname: Espera_drop
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            nome_adicionar = webBot.find_element(selector="/html/body/span/span/span/input", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Type_Into
            nome_adicionar.send_keys("Adicionar")

            # Wait Activity
            # Displayname: espera_nome
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            select_acoes = webBot.find_element(selector=".select2-results__option--highlighted", by=By.CSS_SELECTOR, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            select_acoes.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: elementos_ip_inicio_criterio
            drop_requerente = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div[3]/div[2]/div/form/div/div/div/div/div/div/div/div/span/div/span[2]/span[2]/div/span/span/span/span/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            drop_requerente.click()

            # Wait Activity
            # Displayname: espera_final_criterio
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            elemento = webBot.find_element(selector="/html/body/span/span/span/input", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_ip
            elemento.send_keys(item_regra["NOME"])

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(5000)

            # Find Element Activity
            # Displayname: Find_Element
            select_acoes1 = webBot.find_element(selector="li.select2-results__option:nth-child(2)", by=By.CSS_SELECTOR, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            select_acoes1.click()

            # Find Element Activity
            # Displayname: Elementos_botao
            envia_regra = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            envia_regra.click()

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Elemento_menu
            acoes = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/ul/li[3]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            acoes.click()

            #  Navigate to Activity
            # Displayname: Navigate_To
            webBot.navigate_to("http://10.2.17.66/front/ruleticket.form.php")



        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()