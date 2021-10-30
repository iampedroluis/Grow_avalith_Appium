from appium import webdriver
import unittest

#--------XPATHS----------#
xpath_btn_esv = "//android.widget.Button[@content-desc='Btn1']"
xpath_campo_text_esv = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText"
xpat_btn_sbmt = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button"
xpat_btn_atras = "//android.widget.ImageButton[@content-desc='Navigate up']"
xpat_resultado = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TextView[2]'
#-------- TYPES --------#
valor = "Valor de Prueba"

class Boton_ESV:

    def __init__(self, driver):
        self.driver = driver

    def conexion(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

    def boton_esv(self):
        self.driver.find_element_by_xpath(xpath_btn_esv).click()

    def int_boton_esv(self):
        self.driver.find_element_by_xpath(xpath_campo_text_esv).click()
        self.driver.implicitly_wait(5)
        self.driver.hide_keyboard()
        self.driver.find_element_by_xpath(xpath_campo_text_esv).send_keys(valor)
        self.driver.hide_keyboard()

    def click_sbmt(self):
        self.driver.find_element_by_xpath(xpat_btn_sbmt).click()

    def resultado(self):
        value = valor
        resultado = self.driver.find_element_by_xpath(xpat_resultado).text
        assercion = unittest.TestCase('__init__')
        assercion.assertEqual(value, resultado)


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





