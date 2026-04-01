# Community Version: This license is intended for educational and tool evaluation purposes.

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
        webBot.browse("https://www.vivo.com.br")

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Custom Python Code Activity
        # This activity cannot be used in a community version.

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()