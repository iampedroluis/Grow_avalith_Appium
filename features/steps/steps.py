import time
from behave import *
from pages_objects.boton_esv_po import *
from pages_objects.boton_cuf_po import *
from pages_objects.boton_sv_po import *
from pages_objects.boton_ta_po import *
from pages_objects.boton_zoom_po import *
from pages_objects.boton_login_po import *
from pages_objects.boton_crash_po import *
from pages_objects.boton_fail_login_po import *
#--------------TC1----------------------#


@given('the user is in the application')
def abrir_app(context):
    Boton_ESV.conexion(context)
    time.sleep(3)


@when('the user clicks the enter some value button')
def click_primer_boton(context):
    Boton_ESV.boton_esv(context)
    time.sleep(2)


@when('write the first value')
def escribe_valor(context):
    Boton_ESV.int_boton_esv(context)


@when('click submit Button')
def click_envi(context):
    Boton_ESV.click_sbmt(context)


@then('the first value is displayed')
def primervalor(context):
    time.sleep(5)
    Boton_ESV.resultado(context)
    Boton_ESV.back_btn(context)
# ------------------------------------#


#------------TC2-----------------#

@given('being the user in the application')
def app_demo(context):
    Boton_CUF.conexion(context)
    time.sleep(3)


@when('the user clicks on the button contact us from')
def step_impl(context):
    Boton_CUF.btoncuf(context)
    time.sleep(2)


@when('complete the requested data')
def step_impl(context):
    Boton_CUF.int_botn_cuf(context)
    time.sleep(2)


@when('click submit')
def step_impl(context):
    Boton_CUF.click_submit(context)
    time.sleep(2)


@then('the loaded data is displayed')
def step_impl(context):
    time.sleep(2)

#--------- TEST CASE 3 -------

@given('the user is in the app')
def step_impl(context):
    BotonScrolview.conexion(context)
    time.sleep(2)


@when('click on the Scrollview button')
def step_impl(context):
    BotonScrolview.btn_sv(context)
    time.sleep(2)


@when('Scrolls down')
def step_impl(context):
    BotonScrolview.scroll(context)


@when('click on option number 09')
def step_impl(context):
    BotonScrolview.btn_15(context)


@when('click yes')
def step_impl(context):
    BotonScrolview.btn_yes(context)


@then('the home window is displayed')
def step_impl(context):
    time.sleep(2)

#------- TEST CASE 4 --- ------

@given(u'the user entered the app')
def step_impl(context):
    Boton_ta.conexion(context)
    time.sleep(3)

@when(u'click on the Tab Activity button')
def step_impl(context):
    Boton_ta.btn_ta(context)


@when(u'scrolls horizontally')
def step_impl(context):
    Boton_ta.scroll(context)
    time.sleep(2)
    Boton_ta.scroll(context)
    time.sleep(2)
    Boton_ta.scroll(context)


@when(u'click on the different boxes')
def step_impl(context):
     Boton_ta.btn_home(context)
     Boton_ta.btn_movie(context)


@then(u'you can browse the different sections')
def step_impl(context):
    Boton_ta.btn_sport(context)

#----- TEST CASE 5 -------

@given(u'login in app')
def step_impl(context):
    Boton_Zoom.conexion(context)
    time.sleep(2)

@when(u'click on the zoom button')
def step_impl(context):
   Boton_Zoom.btn_zoom(context)

@then(u'The logo is displayed by zooming')
def step_impl(context):
    time.sleep(5)


#--------------- test case 6 -------#

@given(u'being in the application')
def step_impl(context):
    Boton_Login.conexion(context)



@when(u'click on the login button')
def step_impl(context):
    Boton_Login.btn_login(context)


@when(u'complete the email and passw information')
def step_impl(context):
    Boton_Login.emailpassw(context)



@when(u'click on login')
def step_impl(context):
    Boton_Login.login(context)


@when(u'write admin in the required field')
def step_impl(context):
   Boton_Login.text_admin(context)


@when(u'click on the submit button')
def step_impl(context):
    Boton_Login.btn_submt_login(context)


@then(u'you see the word Admin on the screen')
def step_impl(context):
    time.sleep(2)


#------- TEST CASE 7 --------#

@given(u'mobile demo application')
def step_impl(context):
    Boton_Crash.conexion(context)
    time.sleep(2)

@when(u'the user scrolls to the bottom')
def step_impl(context):
    Boton_Crash.scroll(context)
    time.sleep(2)
@when(u'click on the crash button')
def step_impl(context):
    Boton_Crash.btn_crash(context)

@then(u'exit the application')
def step_impl(context):
    time.sleep(3)

#------ TEST FAIL ------#
@given(u'user a mobile app')
def step_impl(context):
    Boton_Login.conexion(context)



@when(u'user clicks login button')
def step_impl(context):
    Boton_Login.btn_login(context)


@when(u'do not put the credentials')
def step_impl(context):
    time.sleep(2)



@when(u'clicks login without credentials')
def step_impl(context):
    Boton_Login.login(context)

@then(u'lets you log in')
def step_impl(context):
    Boton_Login_fail.resultado(context)





"""
───▌─▌─────▐─▐───
──█─█──▄─▄──█─█──
─█▀─▀▀▄▌▄▐▄▀▀─▀█─
▐▌─▄▀▄█████▄▀▄─▐▌
─▀▀─▄▄█████▄▄─▀▀─
──▄▀─▄▀███▀▄─▀▄──
▄█─▄▀──███──▀▄─█▄
█──█───▐▀▌───█──█
█───█───────█───█
▀█──█───────█──█▀
─█───█─────█───█─
──▌──█─────█──▐──
──────▌───▐────── PEDRO-PARKER!⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""