import json

from behave import given, when, then
from features.config.init_test import Configs as cf
from features.pages.Home import Home


@given(u'que eu esteja na página inicial')
def step_impl(context):
  cf.init(context)


@then(u'devo validar os telefones de contato')
def step_impl(context):
  with open('features/fixtures/Contatos/Contatos.json') as contato:
    dados_contato = json.load(contato)

  Home.validar_whatsapp(context, dados_contato['whatsApp'])
  Home.validar_telefone(context, dados_contato['telefone'])