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


@given('el usuario esta en la aplicacion')
def abrir_app(context):
    Boton_ESV.conexion(context)
    time.sleep(3)


@when('el usuario hace click en el boton enter some value')
def click_primer_boton(context):
    Boton_ESV.boton_esv(context)
    time.sleep(2)


@when('escribe el primer valor')
def escribe_valor(context):
    Boton_ESV.int_boton_esv(context)


@when('le da click en submit')
def click_envi(context):
    Boton_ESV.click_sbmt(context)


@then('se muestra el primer valor')
def primervalor(context):
    time.sleep(5)
    Boton_ESV.resultado(context)
    Boton_ESV.back_btn(context)
# ------------------------------------#


#------------TC2-----------------#

@given('estando el usuario en la aplicacion')
def app_demo(context):
    Boton_CUF.conexion(context)
    time.sleep(3)


@when('el usuario hace click en el boton contact us from')
def step_impl(context):
    Boton_CUF.btoncuf(context)
    time.sleep(2)


@when(u'completa los datos solicitados')
def step_impl(context):
    Boton_CUF.int_botn_cuf(context)
    time.sleep(2)


@when(u'hace click en submit')
def step_impl(context):
    Boton_CUF.click_submit(context)
    time.sleep(2)


@then(u'se visualizan los datos cargados')
def step_impl(context):
    time.sleep(2)

#--------- TEST CASE 3 -------

@given('el usuario esta en la app')
def step_impl(context):
    BotonScrolview.conexion(context)
    time.sleep(2)


@when(u'hace click en el boton Scrollview')
def step_impl(context):
    BotonScrolview.btn_sv(context)
    time.sleep(2)


@when(u'Hace scroll hacia abajo')
def step_impl(context):
    BotonScrolview.scroll(context)


@when(u'hace click en la opcion 15')
def step_impl(context):
    BotonScrolview.btn_15(context)


@when(u'hace click en yes')
def step_impl(context):
    BotonScrolview.btn_yes(context)


@then(u'se muestra la ventana de home')
def step_impl(context):
    time.sleep(2)

#------- TEST CASE 4 --- ------

@given(u'el usuario ingreso en la app')
def step_impl(context):
    Boton_ta.conexion(context)
    time.sleep(3)

@when(u'hace click en el boton Tab Activity')
def step_impl(context):
    Boton_ta.btn_ta(context)


@when(u'hace scroll en forma horizontal')
def step_impl(context):
    Boton_ta.scroll(context)
    time.sleep(2)
    Boton_ta.scroll(context)


@when(u'hace click en las diferentes casillas')
def step_impl(context):
     Boton_ta.btn_home(context)
     Boton_ta.btn_movie(context)


@then(u'puede navegar por las diferentes secciones')
def step_impl(context):
    Boton_ta.btn_sport(context)

#----- TEST CASE 5 -------

@given(u'ingreso en app')
def step_impl(context):
    Boton_Zoom.conexion(context)
    time.sleep(2)

@when(u'hace click en el boton zoom')
def step_impl(context):
   Boton_Zoom.btn_zoom(context)

@then(u'Se visualiza el logo haciendo zoom')
def step_impl(context):
    time.sleep(5)


#--------------- test case 6 -------#

@given(u'estando en la aplicacion')
def step_impl(context):
    Boton_Login.conexion(context)



@when(u'hace click en el boton login')
def step_impl(context):
    Boton_Login.btn_login(context)


@when(u'completa los datos de email y passw')
def step_impl(context):
    Boton_Login.emailpassw(context)



@when(u'hace click en login')
def step_impl(context):
    Boton_Login.login(context)


@when(u'escribe admin en el campo requerido')
def step_impl(context):
   Boton_Login.text_admin(context)


@when(u'hace click en el boton de submit')
def step_impl(context):
    Boton_Login.btn_submt_login(context)


@then(u'se ve la palabra Admin en la pantalla')
def step_impl(context):
    time.sleep(2)


#------- TEST CASE 7 --------#

@given(u'aplicacion mobile demo')
def step_impl(context):
    Boton_Crash.conexion(context)
    time.sleep(2)

@when(u'el usuario hace scroll hacia la parte inferion')
def step_impl(context):
    Boton_Crash.scroll(context)
    time.sleep(2)
@when(u'hace click en el boton crash')
def step_impl(context):
    Boton_Crash.btn_crash(context)

@then(u'sale de la aplicacion')
def step_impl(context):
    time.sleep(3)

#------ TEST FAIL ------#
@given(u'usuario un app mobile')
def step_impl(context):
    Boton_Login.conexion(context)



@when(u'el usuario hace click en login boton')
def step_impl(context):
    Boton_Login.btn_login(context)


@when(u'no coloca las credenciales')
def step_impl(context):
    time.sleep(2)



@when(u'hace click en login sin credenciales')
def step_impl(context):
    Boton_Login.login(context)

@then(u'le deja iniciar sesion')
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