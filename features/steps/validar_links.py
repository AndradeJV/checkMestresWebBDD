from behave import given, when, then
from features.pages.GlobalPages import GlobalPages
from features.config.init_test import Configs as cf


@given(u'que eu esteja na página')
def step_impl(context):
  cf.init(context)


@then(u'devo validar requests dos links disponíveis no header')
def step_impl(context):
  GlobalPages.varrer_endpoints_header(context)