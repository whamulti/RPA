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
        # Displayname: Abre Chrome
        webBot = WebBot()

        # Open Browser Activity
        # Displayname: OpenBrowser
        webDriverPath = ChromeDriverManager().install()
        webBot = WebBot()
        webBot.driver_path = webDriverPath
        webBot.browser = Browser.CHROME
        webBot.headless = False
        webBotDef_options = default_options()
        webBotDef_options.add_argument("--page-load-strategy=Normal")
        webBot.options = webBotDef_options
        webBot.browse("https://www.google.com.br")

        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()