from selenium.webdriver import Firefox, Chrome


# Antes de executar:

def before_all(context):
  browser = context.config.userdata.get('browser')

  browsers = {
    'chrome': Chrome,
    'firefox': Firefox
  }

  context.browser = browsers[browser]()


# Depois de executar:

def after_all(context):
  context.browser.quit()
