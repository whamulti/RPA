from botcity.web.browsers.chrome import default_options
from webdriver_manager.chrome import ChromeDriverManager
from botcity.web import *
from datetime import datetime
from jornadaRPA.webScrap import Webscrap
import pandas as pd

class Bot:
    def bot(self):
        # Sequence: Sequencia_teste

        #  Activity Instance WebBot
        # Displayname: Abre Chrome
        webBot = WebBot()

        # Open Browser Activity
        # Displayname: Pagina Zabbix
        webDriverPath = ChromeDriverManager().install()
        webBot.driver_path = webDriverPath
        webBot.browser = Browser.CHROME
        webBot.headless = False
        webBotDef_options = default_options()
        webBotDef_options.add_argument("--page-load-strategy=Normal")
        webBot.options = webBotDef_options
        webBot.browse("http://10.2.17.7/zabbix/zabbix.php?action=item.list&context=host&filter_groupids%5B%5D=22&filter_hostids%5B%5D=10927&filter_hostids%5B%5D=10928&filter_hostids%5B%5D=10929&filter_hostids%5B%5D=10930&filter_hostids%5B%5D=10931&filter_hostids%5B%5D=10932&filter_hostids%5B%5D=10933&filter_hostids%5B%5D=10934&filter_hostids%5B%5D=10935&filter_hostids%5B%5D=10986&filter_hostids%5B%5D=10937&filter_hostids%5B%5D=10938&filter_hostids%5B%5D=10939&filter_hostids%5B%5D=10940&filter_hostids%5B%5D=10941&filter_hostids%5B%5D=10942&filter_hostids%5B%5D=10943&filter_hostids%5B%5D=10944&filter_hostids%5B%5D=10945&filter_hostids%5B%5D=10946&filter_hostids%5B%5D=10947&filter_hostids%5B%5D=10948&filter_hostids%5B%5D=10949&filter_hostids%5B%5D=10950&filter_hostids%5B%5D=10951&filter_hostids%5B%5D=10952&filter_hostids%5B%5D=10953&filter_hostids%5B%5D=10954&filter_hostids%5B%5D=10955&filter_hostids%5B%5D=10956&filter_hostids%5B%5D=10957&filter_hostids%5B%5D=10958&filter_hostids%5B%5D=10959&filter_hostids%5B%5D=10960&filter_hostids%5B%5D=10961&filter_hostids%5B%5D=10962&filter_hostids%5B%5D=10963&filter_hostids%5B%5D=10964&filter_hostids%5B%5D=10965&filter_hostids%5B%5D=10966&filter_hostids%5B%5D=10967&filter_hostids%5B%5D=10968&filter_hostids%5B%5D=10969&filter_hostids%5B%5D=10970&filter_hostids%5B%5D=10987&filter_hostids%5B%5D=10972&filter_hostids%5B%5D=10973&filter_hostids%5B%5D=10974&filter_hostids%5B%5D=10975&filter_hostids%5B%5D=10976&filter_hostids%5B%5D=10977&filter_hostids%5B%5D=10985&filter_hostids%5B%5D=10978&filter_hostids%5B%5D=10979&filter_hostids%5B%5D=10980&filter_hostids%5B%5D=10981&filter_hostids%5B%5D=10982&filter_name=ICMP+ping&filter_key=icmpping&filter_type=-1&filter_value_type=-1&filter_history=&filter_trends=&filter_delay=&filter_evaltype=0&filter_tags%5B0%5D%5Btag%5D=target&filter_tags%5B0%5D%5Boperator%5D=0&filter_tags%5B0%5D%5Bvalue%5D=snmp&filter_state=-1&filter_status=-1&filter_with_triggers=-1&filter_inherited=-1&filter_discovered=-1&filter_set=1")

        # Maximize window Activity
        # Displayname: Maximiza Navegador
        webBot.maximize_window()

        # Find Element Activity
        # Displayname: Encontra o botão
        botao_login = webBot.find_element(selector="login", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Clica no botão
        botao_login.click()

        # DisplayName: Element_Library

        # Sequence: Element list

        # Find Element Activity
        # Displayname: Encontra campo usuario
        idusuario = webBot.find_element(selector="name", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Encontra campo senha
        idsenha = webBot.find_element(selector="password", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Encontra botão login
        idconecta = webBot.find_element(selector="enter", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Campo usuário
        idusuario.send_keys("admin")

        # Type Into Activity
        # Displayname: Campo senha
        idsenha.send_keys("biotipo2023")

        # Click Activity
        # Displayname: Botão Conectar-se
        idconecta.click()

        # Wait Activity
        # Displayname: Espera
        webBot.wait(3000)

        # Extract DataTable Activity
        # Displayname: Extração de tabela
        tabela_zabbix = Webscrap().webscrap(inBot=webBot, inXPATH="/html/body/div/main/form/table", inLines=0,inNext='', inGetLink=False)

        tabela_zabbix = tabela_zabbix.to_dict(orient='records')

        # ForEach Activity
        # Displayname: ForEach
        for item_zabbix in tabela_zabbix:
            # Find Element Activity
            # Displayname: Elemento percorre host
            host = webBot.find_element(selector=item_zabbix["Host"], by=By.LINK_TEXT, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click no host
            host.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Find Element Activity
            # Displayname: Find_Element
            link = webBot.find_element(selector="/html/body/div/main/form/table/tbody/tr/td[4]/a[2]", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Click Activity
            # Displayname: Click
            link.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # DisplayName: Element_Library

            # Sequence: Element list

            # Find Element Activity
            # Displayname: Find_Element
            drop = webBot.find_element(selector="/html/body/div/div[2]/div[2]/form/div/div/div/div[29]/z-select/button", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Find Element Activity
            # Displayname: Find_Element
            interface = webBot.find_element(selector="/html/body/div/div[2]/div[2]/form/div/div/div/div[29]/z-select/ul/li[3]/ul/li", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Find Element Activity
            # Displayname: Find_Element
            atualizar = webBot.find_element(selector="/html/body/div/div[2]/div[3]/button", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Click Activity
            # Displayname: Click
            drop.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Click Activity
            # Displayname: Click
            interface.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            # Click Activity
            # Displayname: Click
            atualizar.click()

            # Wait Activity
            # Displayname: Wait
            webBot.wait(3000)

            #  Navigate to Activity
            # Displayname: Navigate_To
            webBot.navigate_to("http://10.2.17.7/zabbix/zabbix.php?action=item.list&context=host&filter_groupids%5B%5D=22&filter_hostids%5B%5D=10927&filter_hostids%5B%5D=10928&filter_hostids%5B%5D=10929&filter_hostids%5B%5D=10930&filter_hostids%5B%5D=10931&filter_hostids%5B%5D=10932&filter_hostids%5B%5D=10933&filter_hostids%5B%5D=10934&filter_hostids%5B%5D=10935&filter_hostids%5B%5D=10986&filter_hostids%5B%5D=10937&filter_hostids%5B%5D=10938&filter_hostids%5B%5D=10939&filter_hostids%5B%5D=10940&filter_hostids%5B%5D=10941&filter_hostids%5B%5D=10942&filter_hostids%5B%5D=10943&filter_hostids%5B%5D=10944&filter_hostids%5B%5D=10945&filter_hostids%5B%5D=10946&filter_hostids%5B%5D=10947&filter_hostids%5B%5D=10948&filter_hostids%5B%5D=10949&filter_hostids%5B%5D=10950&filter_hostids%5B%5D=10951&filter_hostids%5B%5D=10952&filter_hostids%5B%5D=10953&filter_hostids%5B%5D=10954&filter_hostids%5B%5D=10955&filter_hostids%5B%5D=10956&filter_hostids%5B%5D=10957&filter_hostids%5B%5D=10958&filter_hostids%5B%5D=10959&filter_hostids%5B%5D=10960&filter_hostids%5B%5D=10961&filter_hostids%5B%5D=10962&filter_hostids%5B%5D=10963&filter_hostids%5B%5D=10964&filter_hostids%5B%5D=10965&filter_hostids%5B%5D=10966&filter_hostids%5B%5D=10967&filter_hostids%5B%5D=10968&filter_hostids%5B%5D=10969&filter_hostids%5B%5D=10970&filter_hostids%5B%5D=10987&filter_hostids%5B%5D=10972&filter_hostids%5B%5D=10973&filter_hostids%5B%5D=10974&filter_hostids%5B%5D=10975&filter_hostids%5B%5D=10976&filter_hostids%5B%5D=10977&filter_hostids%5B%5D=10985&filter_hostids%5B%5D=10978&filter_hostids%5B%5D=10979&filter_hostids%5B%5D=10980&filter_hostids%5B%5D=10981&filter_hostids%5B%5D=10982&filter_name=ICMP+ping&filter_key=icmpping&filter_type=-1&filter_value_type=-1&filter_history=&filter_trends=&filter_delay=&filter_evaltype=0&filter_tags%5B0%5D%5Btag%5D=target&filter_tags%5B0%5D%5Boperator%5D=0&filter_tags%5B0%5D%5Bvalue%5D=snmp&filter_state=-1&filter_status=-1&filter_with_triggers=-1&filter_inherited=-1&filter_discovered=-1&filter_set=1")

        # Wait Activity
        # Displayname: Espera
        webBot.wait(3000)

        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()