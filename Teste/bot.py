# Community Version: This license is intended for educational and tool evaluation purposes.

import pandas as pd
from jornadaRPA.webScrap import Webscrap
from botcity.web.browsers.chrome import default_options
from webdriver_manager.chrome import ChromeDriverManager
from botcity.web import *
from datetime import datetime

class Bot:
    def bot(self):
        # Sequence: Sequencia_teste

        #  Activity Instance WebBot
        # Displayname: Abre_Chrome
        webBot = WebBot()

        # Open Browser Activity
        # Displayname: Pagina_Zabbix
        webDriverPath = ChromeDriverManager().install()
        webBot = WebBot()
        webBot.driver_path = webDriverPath
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
        banco_usuario = Webscrap().webscrap(inBot=webBot, inXPATH="/html/body/div/div[2]/table", inLines=0,inNext='', inGetLink=False)

        banco_usuario = banco_usuario.to_dict(orient='records')

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

        # Scroll Element Activity
        # Displayname: Scroll_Page
        webBot.scroll_down(clicks=10)

        # Click Activity
        # Displayname: Clica_botao
        botao_glpi.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()