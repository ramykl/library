"""
behave environment module for testing moh_qualitycontrol
"""
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.contrib.auth.models import User


def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.base_url = 'http://127.0.0.1:5984/_utils'
        context.browser = webdriver.Chrome()
        context.browser.implicitly_wait(20)

def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()

def django_ready(context):
    context.django = True