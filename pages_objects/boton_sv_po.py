from appium import webdriver


#---------- XPATHS -------------

xpath_btn_sv = '//android.widget.Button[@content-desc="Btn3"]'
xpath_btn_15 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[9]'
xpath_btn_yes = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]"


class BotonScrolview:

    def __init__(self, driver):
        self.driver = driver

    def conexion(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

    def btn_sv(self):
        self.driver.find_element_by_xpath(xpath_btn_sv).click()

    def scroll(self):
        self.driver.swipe(150, 400, 150, 200, 1000)

    def btn_15(self):
        self.driver.find_element_by_xpath(xpath_btn_15).click()

    def btn_yes(self):
        self.driver.find_element_by_xpath(xpath_btn_yes).click()


driver = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "generic_x86_arm",
        "automationName": "UiAutomator1",
        "appPackage": "com.code2lead.kwad",
        "appActivity": ".MainActivity t67"
    }

