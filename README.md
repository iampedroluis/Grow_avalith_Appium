# Grow_avalith_Appium
## Como ejecutar con exito!!


Programas Requeridos:

Appium v.1.21

Link:
https://github.com/appium/appium-desktop/releases/download/v1.21.0-1/Appium-windows-1.21.0-1.exe

Android Studio

Link:https://developer.android.com/studio

*(Crear un emulador de android version 9)*

--

Al clonar el repositorio abrir la terminal de nuestro editor de texto
y ejecutar el siguiente comando 

***pip install requirements.txt***

Una vez ejecutados todos los programas y que el appium se haya sincronizado con el emulador
de android se pueden correr todos los casos de prueba con el siguiente comando que se ingresa
por la terminal del Editor de texto

***behave features/appium_demo_apk.feature***  
o
       ***behave --tags=@features -k***

o si bien se desea correr algun test en especifico 

***behave --tags=@nombredeltag -k***
este nombre del tag se encuentra en el archivo .feature


para realizar reportes con *Allure*

***behave -f allure_behave.formatter:AllureFormatter -o reports/ features***

los cuales se guardaran en una carpeta con nombre reports, si se quiere ver de forma
mas grafica ejecutar el siguiente comando

***allure serve reports*** 

Espero que te haya funcionado, esto es todo!

##HAPPY TEST!!!