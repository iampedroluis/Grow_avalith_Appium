from appium import webdriver

#------ XPATHS----------#

xpath_btn_zoom = '//android.widget.Button[@content-desc="Btn5"]'


class Boton_Zoom:

    def __init__(self, driver):
        self.driver = driver

    def conexion(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

    def btn_zoom(self):
        self.driver.find_element_by_xpath(xpath_btn_zoom).click()


driver = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "generic_x86_arm",
        "automationName": "UiAutomator1",
        "appPackage": "com.code2lead.kwad",
        "appActivity": ".MainActivity t67"
    }


