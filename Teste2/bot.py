# Community Version: This license is intended for educational and tool evaluation purposes.

from botcity.web.browsers.chrome import default_options
from botcity.web import *
from datetime import datetime

class Bot:
    def bot(self):
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
        webBot.browse("http://10.2.17.66/front/ruleproblem.form.php?id=103")

        # Find Element Activity
        # Displayname: Find_Element
        botao = webBot.find_element(selector="/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        botao.click()

        # DisplayName: Element_Library

        # Sequence: Element list

        # Find Element Activity
        # Displayname: Find_Element
        login = webBot.find_element(selector="submit", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Find_Element
        usuario = webBot.find_element(selector="login_name", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Find Element Activity
        # Displayname: Find_Element
        senha = webBot.find_element(selector="login_password", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Type_Into
        usuario.send_keys("ricardo")

        # Type Into Activity
        # Displayname: Type_Into
        senha.send_keys("0805")

        # Click Activity
        # Displayname: Click
        login.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Find_Element
        var_1 = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/ul/li[2]/a/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        var_1.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Find_Element
        var_2 = webBot.find_element(selector="add_criterion", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        var_2.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Find_Element
        var_3 = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div[2]/div/div/form/div/div/div/div/div/div/div/div/span/div/div/span/span/span/span/span", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        var_3.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Find_Element
        var_4 = webBot.find_element(selector="/html/body/span/span/span/input", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Type_Into
        var_4.send_keys("Descricao")

        # Wait Activity
        # Displayname: Wait
        webBot.wait(5000)

        # Find Element Activity
        # Displayname: Find_Element
        var_5 = webBot.find_element(selector=".select2-results__option--highlighted", by=By.CSS_SELECTOR, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        var_5.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: outrodrop
        var_6 = webBot.find_element(selector="/html/body/div[2]/div[2]/div/main/div/div/div[2]/div[2]/div/div[2]/div/div/form/div/div/div/div/div/div/div/div/span/div/span/span/span/span/span[2]", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        var_6.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Find_Element
        var_7 = webBot.find_element(selector="/html/body/span/span/span/input", by=By.XPATH, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Type_Into
        var_7.send_keys("contem")

        # Wait Activity
        # Displayname: Wait
        webBot.wait(5000)

        # Find Element Activity
        # Displayname: Find_Element
        var_5 = webBot.find_element(selector=".select2-results__option--highlighted", by=By.CSS_SELECTOR, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        var_5.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(3000)

        # Find Element Activity
        # Displayname: Find_Element
        var_8 = webBot.find_element(selector="pattern", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Type Into Activity
        # Displayname: Type_Into
        var_8.send_keys("10.3.3.0")

        # Wait Activity
        # Displayname: Wait
        webBot.wait(5000)

        # Find Element Activity
        # Displayname: Find_Element
        var_9 = webBot.find_element(selector="add", by=By.NAME, waiting_time=1000, ensure_visible=False, ensure_clickable=False)

        # Click Activity
        # Displayname: Click
        var_9.click()

        # Wait Activity
        # Displayname: Wait
        webBot.wait(15000)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()