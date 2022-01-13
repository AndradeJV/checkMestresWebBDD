import json

from behave import given, when, then
from features.config.init_test import Configs as cf
from features.helpers.links.ClickLinks import Links
from features.pages.Blog import Blog


@given(u'que eu esteja na página do blog')
def step_impl(context):
  cf.init(context)
  Links.clickLink_blog(context)

@when(u'eu buscar por um post existente')
def step_impl(context):
  with open('features/fixtures/Posts/Posts.json') as posts:
    dados_posts = json.load(posts)
  
  Blog.pesquisar_posts(context, dados_posts['postExistente'])


@then(u'eu devo ver o post sendo exibido em sua área')
def step_impl(context):
  Blog.validar_posts_existente(context)


@when(u'eu buscar por um post não existente')
def step_impl(context):
  with open('features/fixtures/Posts/Posts.json') as posts:
    dados_posts = json.load(posts)

  Blog.pesquisar_posts(context, dados_posts['postNaoExistente'])


@then(u'eu não devo ver a área de post sendo exibida')
def step_impl(context):
  Blog.validar_posts_nao_existe(context)