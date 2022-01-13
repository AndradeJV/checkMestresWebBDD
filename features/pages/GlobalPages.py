from features.helpers.links.Links import Links


class GlobalPages:
  def varrer_endpoints_header(context):
    Links.clickLink_mestres(context)
    Links.clickLink_metodologia(context)
    Links.clickLink_servicos(context)
    Links.clickLink_portfolio(context)
    Links.clickLink_blog(context)
    Links.clickLink_vamos_conversar(context)
