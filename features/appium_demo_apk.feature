@feature
Feature: probar demo apk
  "Como usuario quiero probrar la app mobile"
  @testcase1
  Scenario: boton enter some value
    Given el usuario esta en la aplicacion
    When el usuario hace click en el boton enter some value
    And escribe el primer valor
    And le da click en submit
    Then se muestra el primer valor

  @testcase2
    Scenario: boton contact us form
      Given estando el usuario en la aplicacion
      When el usuario hace click en el boton contact us from
      And  completa los datos solicitados
      And hace click en submit
      Then se visualizan los datos cargados

  @testcase3
    Scenario: boton Scrollview
    Given el usuario esta en la app
    When hace click en el boton Scrollview
    And  Hace scroll hacia abajo
    And   hace click en la opcion 15
    And  hace click en yes
    Then se muestra la ventana de home

  @testcase4
    Scenario:  boton TAB ACTIVITY
    Given el usuario ingreso en la app
    When hace click en el boton Tab Activity
    And hace scroll en forma horizontal
    And hace click en las diferentes casillas
    Then puede navegar por las diferentes secciones

  @testcase5
    Scenario: Boton Zoom
    Given ingreso en app
    When hace click en el boton zoom
    Then Se visualiza el logo haciendo zoom

  @testcase6
    Scenario: Boton Login
    Given estando en la aplicacion
    When hace click en el boton login
    And completa los datos de email y passw
    And hace click en login
    And escribe admin en el campo requerido
    And hace click en el boton de submit
    Then se ve la palabra Admin en la pantalla

  @testcase7
    Scenario: boton Crash
    Given aplicacion mobile demo
    When el usuario hace scroll hacia la parte inferion
    And hace click en el boton crash
    Then sale de la aplicacion

  @testcasefail
    Scenario: falla la prueba
    Given usuario un app mobile
    When el usuario hace click en login boton
    And no coloca las credenciales
    And hace click en login sin credenciales
    Then le deja iniciar sesion
