from behave import given, when, then
from appium import webdriver
import os
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given(u'the App loaded on devices')
def step_impl(context):
    time.sleep(2)
    context.home_element = WebDriverWait(context.appdriver, 5).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Home')))
    context.home_element.click()
    time.sleep(1)

    context.story_element = WebDriverWait(context.appdriver, 5).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'All About')))
    context.story_element.click()
    time.sleep(1)


@when(u'tap around the App {icon}')
def step_impl(context, icon):
    time.sleep(1)
    if icon == 'My Story':
        context.favorites_icon = context.appdriver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Story')
        context.favorites_icon.click()
        time.sleep(1)
    elif icon == 'Favorites':
        context.favorites_icon = context.appdriver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Favorites')
        context.favorites_icon.click()
        time.sleep(1)
    elif icon == 'Fun Facts':
        fun_facts_element = context.appdriver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Fun Facts')
        fun_facts_element.click()
        time.sleep(1)


@then(u'display specific Tab {dispinfo}')
def step_impl(context, dispinfo):
    if dispinfo == 'My Story Title':
        try:
            context.My_Story_Title = context.appdriver.find_element(AppiumBy.ACCESSIBILITY_ID, 'My Story')
            context.Is_My_Story_Title_Found = True
        except Exception:
            context.Is_My_Story_Title_Found = False
        assert context.Is_My_Story_Title_Found == True
    elif dispinfo == 'Favorites Title':
        try:
            context.My_favorites_title = context.appdriver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Hobbies')
            context.Is_My_Favorites_Title_Found = True
        except Exception:
            context.Is_My_Favorites_Title_Found = False
        assert context.Is_My_Favorites_Title_Found == True
    elif dispinfo == 'Fun Facts Title':
        try:
            context.My_fun_facts_title = context.appdriver.find_element(AppiumBy.IOS_CLASS_CHAIN,
                                                     '**/XCUIElementTypeStaticText[`label == "Fun Facts"`]')
            context.Is_My_Fun_Facts_Title_Found = True
            fun_fact_link = context.appdriver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show Random Fact')
            fun_fact_link.click()
            time.sleep(1)
            fun_fact_link.click()
            time.sleep(1)
        except Exception:
            context.Is_My_Fun_Facts_Title_Found = False
        assert context.Is_My_Fun_Facts_Title_Found == True

