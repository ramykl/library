from behave import when, then

@when(u'I use django\'s test client to visit "{url}"')
def use_django_client(context, url):
   context.response = context.test.client.get(url, follow=True)
   #last_url, status_code = context.response.redirect_chain[-1]
   #print(last_url)
   


@then(u'it should return a successful response')
def it_should_be_successful(context):
    #print(context.response.status_code)
    assert context.response.status_code == 200