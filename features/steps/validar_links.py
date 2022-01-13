from behave import given, when, then
from features.pages.GlobalPages import GlobalPages

@given(u'que eu esteja na página')
def step_impl(context):
  context.browser.get('https://mestresdaweb.com.br/')


@then(u'devo validar requests dos links disponíveis no header')
def step_impl(context):
  GlobalPages.varrer_endpoints_header(context)