import json


class Home:
  def validar_whatsapp(context, whatsapp):
    with open('features/fixtures/Contatos/Contatos.json') as contato:
      dados_contato = json.load(contato)

    contato_whatsapp = dados_contato.get('whatsApp')

    whatsapp = context.browser.find_element_by_css_selector("span > small:nth-child(1)").text

    if whatsapp == contato_whatsapp:
      print(f'Contato{contato_whatsapp} validado com sucesso')

    else:
      return


  def validar_telefone(context, telefone):
    with open('features/fixtures/Contatos/Contatos.json') as contato:
      dados_contato = json.load(contato)

    contato_telefone = dados_contato.get('telefone')

    telefone = context.browser.find_element_by_css_selector("span > small:nth-child(2)").text

    if telefone == contato_telefone:
      print(f'Contato{contato_telefone} validado com sucesso')

    else:
      return