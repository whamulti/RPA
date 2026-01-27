# Community Version: This license is intended for educational and tool evaluation purposes.

from jornadaRPA.webScrap import Webscrap
from botcity.web.browsers.chrome import default_options
from botcity.web import *
from datetime import datetime

class Bot:
    def bot(self):
        # Sequence: Sequencia_glpi_regra_problema

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
        # Displayname: Usuario_zabbix
        usuario_zabbix = webBot.find_element(selector="name", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Senha_zabbix
        senha_zabbix = webBot.find_element(selector="password", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Conectar_se_zabbix
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
        banco_regra = Webscrap().webscrap(inBot=webBot, inXPATH="/html/body/div/main/form/table", inLines=0,inNext='', inGetLink=False)

        # Sequence: Lista_acoes

        # Assign Activity
        # Displayname: Assign
        banco_regra = banco_regra.assign(Interface2=banco_regra['Interface'].str.split(':').str[0])

        # Assign Activity
        # Displayname: Assign_Values
        lista_ips = banco_regra['Interface2'].tolist()

        # Assign Activity
        # Displayname: Assign_Values
        banco_regra = banco_regra.assign(Localizacao=banco_regra['Nome'].str.split(' - ').str[1])

        # Assign Activity
        # Displayname: Assign_Values
        lista_localizacoes = banco_regra['Localizacao'].tolist()

        # Assign Activity
        # Displayname: Converte_dados
        banco_regra = banco_regra.to_dict(orient='records')

        #  Navigate to Activity
        # Displayname: Navegar_para
        webBot.navigate_to("http://10.2.17.26/front/ruleproblem.form.php")

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
        nome_regra = webBot.find_element(selector="name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # ForEach Activity
        # Displayname: Laco_repeticao
        for item_regra in banco_regra:
            # Sequence: Corpo

            # DisplayName: Formulario_acao_elementos_web

            # Sequence: Lista_acoes

            # Find Element Activity
            # Displayname: Encontrar_nome
            nome_regra = webBot.find_element(selector="name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_nome
            nome_regra.send_keys(item_regra["Nome"])

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Encontrar_nome
            add_regra = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Adicionar_impressora
            add_regra.click()

            # Wait Activity
            # Displayname: Espera_15_PRIMEIRO_CRITERIO
            webBot.wait(15000)

            # Find Element Activity
            # Displayname: Elemento_menu
            criterio = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/ul/li[2]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            criterio.click()

            # Wait Activity
            # Displayname: Espera_3_segundos
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
            condicao.send_keys(item_regra["Interface2"])

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
            # Displayname: ESPERA_1_ULTIMO_CRITERIO
            webBot.wait(1000)

            # Wait Activity
            # Displayname: Espera_2_PRIMEIRO_ACOES
            webBot.wait(2000)

            # Find Element Activity
            # Displayname: Elemento_menu
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
            nome_acoes.send_keys("Elementos associados")

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
            # Displayname: Find_Element
            elemento = webBot.find_element(selector="value", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Type Into Activity
            # Displayname: Dados_de_ip
            elemento.send_keys(item_regra["Interface2"])

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Elementos_botao
            envia_regra = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Clica_botao
            envia_regra.click()

            # Wait Activity
            # Displayname: ESPERA_1_ULTIMO_ACOES
            webBot.wait(3000)

            #  Navigate to Activity
            # Displayname: retornar_pagina
            webBot.navigate_to("http://10.2.17.26/front/ruleproblem.form.php")

            # Wait Activity
            # Displayname: Espera_3_segundos
            webBot.wait(3000)



        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()