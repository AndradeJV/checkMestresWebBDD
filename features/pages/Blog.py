import time

from selenium.webdriver.common.keys import Keys
from features.helpers.buttons.Blog.ClicksButtons import ClickButtons


class Blog:
  def pesquisar_posts(context, post):
    pesquisa = context.browser.find_element_by_css_selector('input[type=text]').send_keys(post)
    ClickButtons.clickButton_pesquisar_post(context)

  def validar_posts_existente(context):
    if context.browser.find_element_by_css_selector('article:nth-child(1)'):
      return 'Sucess'

    else:
      return 'Não encontrado'

  def validar_posts_nao_existe(context):
    time.sleep(2)

    if context.browser.find_element_by_css_selector('aside > div > nav:nth-child(2)'):
      return 'Sucess'

    else:
      return 'Não encontrado'