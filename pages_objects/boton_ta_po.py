from appium import webdriver

#------ XPATHS----------#

xpath_btn_ta = "//android.widget.Button[@content-desc='Btn4']"
xpath_btn_sport = "//android.support.v7.app.ActionBar.Tab[@content-desc='Sport']"
xpath_btn_movie = '//android.support.v7.app.ActionBar.Tab[@content-desc="Movie"]'
xpath_btn_home = '//android.support.v7.app.ActionBar.Tab[@content-desc="Home"]'


class Boton_ta:

    def __init__(self, driver):
        self.driver = driver

    def conexion(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

    def btn_ta(self):
        self.driver.find_element_by_xpath(xpath_btn_ta).click()

    def scroll(self):
        self.driver.swipe(877, 1290, 168, 1276, 1000)

    def btn_sport(self):
        self.driver.find_element_by_xpath(xpath_btn_sport).click()

    def btn_movie(self):
        self.driver.find_element_by_xpath(xpath_btn_movie).click()

    def btn_home(self):
        self.driver.find_element_by_xpath(xpath_btn_home).click()




driver = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "generic_x86_arm",
        "automationName": "UiAutomator1",
        "appPackage": "com.code2lead.kwad",
        "appActivity": ".MainActivity t67"
}


