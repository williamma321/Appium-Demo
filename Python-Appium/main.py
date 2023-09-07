from appium import webdriver
import os
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



caps = {}
caps["appium:platformVersion"] = "16.4"
caps["appium:deviceName"] = "iPhone 14 Pro"
caps["appium:automationName"] = "XCUITest"
caps["appium:platformName"] = "iOS"
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
caps["appium:app"] = ("/Users/irenema/Library/Developer/Xcode/DerivedData/About_Me-gqyfljzusgrenmackngeiqigjpjg/Build"
                      "/Products/Debug-iphonesimulator/About Me.app")
driver = webdriver.Remote("http://127.0.0.1:4723", caps)
time.sleep(2)
story_element = WebDriverWait(driver, 5).until(
       EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Story')))

story_element.click()
time.sleep(1)
try:
    My_Story_Title = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'My Story')
except Exception:
    print('not found')
time.sleep(1)
favorites_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites')
favorites_element.click()
time.sleep(1)
try:
    My_favorites_title = driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Favorites"`]')
except Exception:
    print('Favorites Title not found')
fun_facts_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Fun Facts')
fun_facts_element.click()
time.sleep(1)
try:
    My_fun_facts_title = driver.find_element(AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeStaticText[`label == "Fun Facts"`]')
except Exception:
    print('Fun Fact title not found')
fun_fact_link = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Show Random Fact')
fun_fact_link.click()
time.sleep(3)
fun_fact_link.click()
time.sleep(3)



driver.quit()
