class Links:
  def clickLink_mestres(context):
    context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(1) > a').click()

  def clickLink_metodologia(context):
    context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(2) > a').click()

  def clickLink_servicos(context):
    context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(3) > a').click()

  def clickLink_portfolio(context):
    context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(4) > a').click()

  def clickLink_blog(context):
    context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(5) > a').click()

  def clickLink_vamos_conversar(context):
    context.browser.find_element_by_css_selector('#header > nav > ul > li:nth-child(6) > a').click()
