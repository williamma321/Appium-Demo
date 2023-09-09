import os
from behave import fixture, use_fixture
from dotenv import load_dotenv
from appium import webdriver

load_dotenv()
get_app_path = os.getenv("APP_PATH")
get_device_platform_v = os.getenv("DEVPLTFM")
get_device_device_name = os.getenv("DEVNAME")
get_device_automation_name = os.getenv("DEVAUTOMNAME")
get_device_platformName = os.getenv("DEVPNAME")
get_web_driver_local_url = os.getenv("LCLURL")

caps = {
    "appium:platformVersion": get_device_platform_v,
    "appium:deviceName": get_device_device_name,
    "appium:automationName": get_device_automation_name,
    "appium:platformName": get_device_platformName,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "appium:app": get_app_path
    }

driver = webdriver.Remote(get_web_driver_local_url, caps)


@fixture
def before_all(context):
    context.appdriver = driver


@fixture
def after_all(context):
    context.appdriver.quit()