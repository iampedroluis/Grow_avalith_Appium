from appium import webdriver
driver= {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "generic_x86_arm",
  "automationName": "UiAutomator1",
  "appPackage": "com.code2lead.kwad",
  "appActivity": ".MainActivity t67"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)