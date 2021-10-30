from appium import webdriver
import unittest

#------ XPATHS----------#

xpath_btn_login = '//android.widget.Button[@content-desc="Btn6"]'
xpath_campo_email = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]'
xpath_campo_passw = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]'
xpath_btn_loginaccount = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button'
xpath_enter_campo_text = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText'
xpath_enter_boton_submit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button'
xpat_label_login = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]'

titulo_admin = "Enter Admin"

class Boton_Login_fail:

    def __init__(self, driver):
        self.driver = driver

    def conexion(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)


    def btn_login(self):
        self.driver.find_element_by_xpath(xpath_btn_login).click()

    def login(self):
        self.driver.find_element_by_xpath(xpath_btn_loginaccount).click()

    def text_admin(self):
        self.driver.find_element_by_xpath(xpath_enter_campo_text).click()
        self.driver.find_element_by_xpath(xpath_enter_campo_text).send_keys("Admin")

    def btn_submt_login(self):
        self.driver.find_element_by_xpath(xpath_enter_boton_submit).click()

    def resultado(self):
        value = titulo_admin
        resultado = self.driver.find_element_by_xpath(xpat_label_login).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(value, resultado)




driver = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "generic_x86_arm",
        "automationName": "UiAutomator1",
        "appPackage": "com.code2lead.kwad",
        "appActivity": ".MainActivity t67"
    }



