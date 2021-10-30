from appium import webdriver

#------ XPATHS----------#

xpath_btn_crash = '(//android.widget.Button[@content-desc="Btn10"])[4]'

"""
.press(x=545, y=1848)   .move_to(x=561, y=1163) 
"""


class Boton_Crash:

    def __init__(self, driver):
        self.driver = driver

    def conexion(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

    def scroll(self):
        self.driver.swipe(545, 1848, 561, 1000, 200)

    def btn_crash(self):
        self.driver.find_element_by_xpath(xpath_btn_crash).click()




driver = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "generic_x86_arm",
        "automationName": "UiAutomator1",
        "appPackage": "com.code2lead.kwad",
        "appActivity": ".MainActivity t67"
    }

