class ClickButtons:
  def clickButton_pesquisar_post(context):
    context.browser.find_element_by_css_selector('form > i').click()