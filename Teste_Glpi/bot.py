# Community Version: This license is intended for educational and tool evaluation purposes.

from jornadaRPA.webScrap import Webscrap
from botcity.web.browsers.chrome import default_options
from botcity.web import *
from datetime import datetime

class Bot:
    def bot(self):
        # Sequence: Sequence_teste_glpi

        #  Activity Instance WebBot
        # Displayname: Instance_Webbot
        webBot = WebBot()

        # Open Browser Activity
        # Displayname: OpenBrowser
        webBot = WebBot()
        webBot.driver_path = "C:\\Users\\ricardo\\Documents\\GitHub\\RPA\\WebDrivers\\CHROME\\chromedriver.exe"
        webBot.browser = Browser.CHROME
        webBot.headless = False
        webBotDef_options = default_options()
        webBotDef_options.add_argument("--page-load-strategy=Normal")
        webBot.options = webBotDef_options
        webBot.browse("http://10.2.17.7/zabbix/zabbix.php?action=host.list&filter_groups%5B%5D=29&filter_host=&filter_dns=&filter_ip=&filter_port=&filter_status=-1&filter_monitored_by=-1&filter_evaltype=0&filter_tags%5B0%5D%5Btag%5D=&filter_tags%5B0%5D%5Boperator%5D=0&filter_tags%5B0%5D%5Bvalue%5D=&filter_set=1")

        # Find Element Activity
        # Displayname: Find_Element
        botao = webBot.find_element(selector="/html/body/div/main/output/div[2]/button", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        botao.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # DisplayName: Element_Library

        # Sequence: Element list

        # Find Element Activity
        # Displayname: Find_Element
        namename = webBot.find_element(selector="name", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Find_Element
        namepassword = webBot.find_element(selector="password", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Find_Element
        nameenter = webBot.find_element(selector="enter", by=By.ID, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Type_Into
        namename.send_keys("admin")

        # Type Into Activity
        # Displayname: Type_Into
        namepassword.send_keys("biotipo2023")

        # Click Activity
        # Displayname: Click
        nameenter.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Extract DataTable Activity
        # Displayname: ExtractDataTable
        banco_impressoras_zabbix = Webscrap().webscrap(inBot=webBot, inXPATH="/html/body/div/main/form/table", inLines=0,inNext='', inGetLink=False)

        # Wait Activity
        # Displayname: Wait
        webBot.wait(5000)

        # Sequence: Assign List

        # Assign Activity
        # Displayname: Assign
        banco_impressoras_zabbix = banco_impressoras_zabbix.assign(Interface2=banco_impressoras_zabbix['Interface'].str.split(':').str[0])

        # Assign Activity
        # Displayname: Assign_Values
        lista_ips = banco_impressoras_zabbix['Interface2'].tolist()

        # Assign Activity
        # Displayname: Assign_Values
        banco_impressoras_zabbix = banco_impressoras_zabbix.assign(Localizacao=banco_impressoras_zabbix['Nome'].str.split(' - ').str[1])

        # Assign Activity
        # Displayname: Assign_Values
        lista_localizacoes = banco_impressoras_zabbix['Localizacao'].tolist()

        # Assign Activity
        # Displayname: Assign_Values
        banco_impressoras_zabbix = banco_impressoras_zabbix.to_dict(orient='records')

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Print Activity
        # Displayname: Print
        print(banco_impressoras_zabbix)

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()