from appium import webdriver

#-------- XPPATS -----------
xpath_btn_cuf = "//android.widget.Button[@content-desc='Btn2']"
xpath_campo_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]"
xpath_campo_email = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[2]"
xpath_campo_addres = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[3]"
xpath_campo_mobile = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[4]"
xpath_btn_submt = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button"
xpat_btn_atras = "//android.widget.ImageButton[@content-desc='Navigate up']"




class Boton_CUF:

    def __init__(self, driver):
        self.driver = driver

    def conexion(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

    def btoncuf(self):
        self.driver.find_element_by_xpath(xpath_btn_cuf).click()

    def int_botn_cuf(self):
        self.driver.find_element_by_xpath(xpath_campo_name).click()
        self.driver.find_element_by_xpath(xpath_campo_name).send_keys("TEST NAME")
        self.driver.find_element_by_xpath(xpath_campo_email).click()
        self.driver.find_element_by_xpath(xpath_campo_email).send_keys("emailtest@testmail.com")
        self.driver.find_element_by_xpath(xpath_campo_addres).click()
        self.driver.find_element_by_xpath(xpath_campo_addres).send_keys("calletest qa")
        self.driver.find_element_by_xpath(xpath_campo_mobile).click()
        self.driver.find_element_by_xpath(xpath_campo_mobile).send_keys("111555666")
        self.driver.hide_keyboard()

    def click_submit(self):
        self.driver.find_element_by_xpath(xpath_btn_submt).click()

    def back_btn(self):
        self.driver.find_element_by_xpath(xpat_btn_atras).click()





driver = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "generic_x86_arm",
        "automationName": "UiAutomator1",
        "appPackage": "com.code2lead.kwad",
        "appActivity": ".MainActivity t67"
    }



