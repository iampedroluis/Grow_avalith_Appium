
from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction

from pages_objects.boton_esv_po import PrimerBoton


driver = {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "generic_x86_arm",
  "automationName": "UiAutomator1",
  "appPackage": "com.code2lead.kwad",
  "appActivity": ".MainActivity t67"
}

#ABRIR LA APPLICACION
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

#<------ PRIMER BOTON (ENTER SOME VALUE) ----->
#HACE CLICK EN EL PRIMER BOTON






#<------ SEGUNDO BOTON (CONTACT US FORM)------>

#CLICK EN EL SEGUNDO BOTON
driver.find_element_by_xpath("//android.widget.Button[@content-desc='Btn2']").click()
#CLICK EN CASILLA "ENTER NAME"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]").click()
#ESCONDE EL TECLADO
driver.hide_keyboard()
#ESCROBE EN LA CASILLA "ENTER NAME"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]").send_keys("Pedro")
#CLICK EN LA CASILLA "ENTER EMAIL"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[2]").click()
#ESCONDE TECLADO
driver.hide_keyboard()
#ESCRIBE EN LA CASILLA "ENTER EMAIL"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[2]").send_keys("test.pedro@testappium.com")
#CLICK EN "ENTER ADDRES"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[3]").click()
#ESCONDE TECLADO
driver.hide_keyboard()
#ESCRIBE EN CASILLA "ENTER ADDRES"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[3]").send_keys("Calle test 122, appium")
#CLICK EN "MOBILE NO"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[4]").click()
#ESCONDE TECLADO
driver.hide_keyboard()
#ESCRIBE "MOBILE NO"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[4]").send_keys("11-555-55555")
#BOTON SUBMIT
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button").click()
#ATRAS
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()


#<----- TERCER BOTON (SCROLLView)------->

#CLICK EN TERCER BOTON
driver.find_element_by_xpath().click()
driver.implicitly_wait(3)
#CLICK "BUTTON1"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[1]").click()
#CIERRA "NO" Pop-up
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[1]").click()
#CLICK "BUTTON2"
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]").click()
#CIERRA "NO" Pop-up
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[1]").click()

""" 
#COORDENADAS DEL SCROLL

  #TouchAction(driver)   .press(x=542, y=1954)   .move_to(x=566, y=912)   .release()   .perform()
"""

#SCROLL ABAJO


#CLICK "BUTTON5"
driver.find_element_by_xpath().click()
#CIERRA "YESS" Pop-up
driver.find_element_by_xpath().click()

#<------ BOTON 4 (TAB ACTIVITY) ----->

#CLICK BOTON 4
driver.find_element_by_xpath().click()
""" COORDENADAS SCROLL SPORT
  TouchAction(driver)   .press(x=1000, y=1286)   .move_to(x=80, y=1328)   .release()   .perform()
    
"""
#SCROLL SPORT
touch.press(x=1000, y=1286).move_to(x=80, y=1328).release().perform()

"""COORDENADAS SCROLL MOVIE
  TouchAction(driver)   .press(x=951, y=1185)   .move_to(x=87, y=1227)   .release()   .perform()
"""
#SCROLL MOVIE
touch.press(x=951, y=1185).move_to(x=87, y=1227).release().perform()

#CLICK SPORT
driver.find_element_by_xpath().click()
#CLICK HOME
driver.find_element_by_xpath(').click()
#CLICK  MOVIE
driver.find_element_by_xpath().click()
#ATRAS
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()

#<------BOTON 5 (zoom) ---->
#CLICK
driver.find_element_by_xpath().click()

#<----BOTON 6 (LOGIN) ---->
#CLICK BOTON 6
driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn6"]').click()
#CLICK CAMPO EMAIL
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]').click()
#ESCRIBIR CAMPO EMAIL
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[1]').send_keys("admin@gmail.com")
#CLICK PASSW
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]').click()
#ESCRIBIR PASSW
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText[2]').send_keys("admin123")
#CLICK BOTON LOGIN
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button').click()

#ENTER ADMIN--->
#CLICK "ENTER ADMIN"
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText').click()
# ESCRIBIR "ENTER ADMIN"
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText').send_keys("Admin")
#CLICK BOTON "SUBMIT"
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button').click()
#ATRAS
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()
#ATRAS
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()




#SCROLL
""" SCROLL
TouchAction(driver)   .press(x=381, y=1814)   .move_to(x=357, y=388)   .release()   .perform()
"""
touch.press(x=381, y=1814).move_to(x=357, y=388).release().perform()


#<----- BOTON 7 --->
#CLICK BOTON 7

driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn7"]').click()

#<-----BOTON 8 ---->
#CLICK BOTON "TIME"
driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn8"]').click()

#COLOCAR HORA
driver.find_element_by_xpath('//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="8"]').click()
#COLOCAR MINUTOS
driver.find_element_by_xpath('//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="15"]').click()
#COLOCAR PM
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RadioGroup/android.widget.RadioButton[2]').click()

#ABRIR EL TECLADO
driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Switch to text input mode for the time input."]').click()
#CLICK CAMPO HORA
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText[1]').click()
#ESCRIBIR HORA
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText[1]').clear().send_keys("12")
#CLICK CAMPO MINUTO
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText[2]').click()
#ESCRIBIR EN CAMPO MINUTO
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText[2]').clear().send_keys("45")

#OPCION PM/AM
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.TimePicker/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.Spinner').click()
#OPCION AM
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]').click()
#ATRAS
driver.back()
#ATRAS
driver.back()


#<---- BOTON 9 ---->
#CLICK BOTON 9
driver.find_element_by_xpath('//android.widget.Button[@content-desc="Btn9"]').click()

#CLICK AÑO
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]').click()
#SCROLL AÑO
"""
TouchAction(driver)   .press(x=601, y=846)   .move_to(x=608, y=1533)   .release()   .perform()
"""
touch.press(x=601, y=846).move_to(x=608, y=1533).release().perform()

#SELECCIONA AÑO
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.ListView/android.widget.TextView[5]').click()
#SELECIONA MES
driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Next month"]').click()
driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Next month"]').click()
driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Next month"]').click()
driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Previous month"]').click()
time.sleep(2)
#SELECIONA DIA
driver.find_element_by_xpath('//android.view.View[@content-desc="25 December 1904"]').click()
time.sleep(2)

#ATRAS
driver.back()


#<----- BOTON 10 ----->
#CLICK  BOTN
driver.find_element_by_xpath('(//android.widget.Button[@content-desc="Btn10"])[1]').click()
time.sleep(5)
#SCROLL
"""
TouchAction(driver)   .press(x=122, y=1024)   .move_to(x=846, y=1021)   .release()   .perform()
"""
touch.press(x=122, y=1024).move_to(x=846, y=1021).release().perform()

#CLICK TEXT
driver.hide_keyboard()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText').click()
driver.hide_keyboard()
driver.hide_keyboard()
#ESCRIBE TEXT
driver.hide_keyboard()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText').send_keys("VALOR")
driver.hide_keyboard()
#CLICK SUBMIT
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button').click()
#ATRAS
driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()

#<---- BOTON 11 ------->
driver.find_element_by_xpath('(//android.widget.Button[@content-desc="Btn10"])[2]').click()
driver.back()

#<-----  BOTON 12 ------>
driver.find_element_by_xpath('(//android.widget.Button[@content-desc="Btn10"])[3]').click()
driver.back()

#<---- BOTON 13 ----->
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[10]').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.MultiAutoCompleteTextView').click()
driver.hide_keyboard()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.MultiAutoCompleteTextView').send_keys("here")
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button').click()

#<----- BOTOn 14 ----->
driver.find_element_by_xpath(').click()