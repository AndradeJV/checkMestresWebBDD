from behave import given, when, then
import time


@given(u'que eu esteja na página')
def step_impl(context):
  context.browser.get('https://mestresdaweb.com.br/')


@then(u'devo validar os links disponíveis no header')
def step_impl(context):
  context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(1) > a').click()
  context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(2) > a').click()
  context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(3) > a').click()
  context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(4) > a').click()
  context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(5) > a').click()
  context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(6) > a').click()