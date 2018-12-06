from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException
from django.contrib.auth.models import User

@given(u'there are no users')
def impl(context):
    users = User.objects.all()
    if not users:
        #there are no users
        assert True
    else:
        #there are users
        assert False

@when(u'a user is created')
def user_create(context):
    user = User.objects.create_user(username='registeredUser', password="Password")
    user.save()

@then(u'there is 1 user')
def impl(context):
    users = User.objects.all()
    if users:
        #there are users
        assert True
    else:
        #there are no users
        assert False


@given(u'a user visits the site "{location}"')
def impl(context, location):
    user_create(context) 
    url = context.base_url + location 
    context.browser.get(url)

@when(u'I log in as "{user}"')
def impl(context, user):  
    username_field = context.browser.find_element_by_name('username')
    password_field = context.browser.find_element_by_name('password')
    username_field.send_keys(user)
    password_field.send_keys('Password')
    submit_button = context.browser.find_element_by_xpath('//input[@type="submit"]')
    submit_button.click()

@then(u'I should see the "{auth_class}"')
def imple(context, auth_class): 
    assert context.browser.find_element_by_class_name(auth_class)