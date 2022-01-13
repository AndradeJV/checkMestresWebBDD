class Configs:
  def init(context):
    context.browser.get('https://mestresdaweb.com.br/')
    context.browser.maximize_window()

  def pag_principal(context):
    context.browser.get('https://mestresdaweb.com.br/')