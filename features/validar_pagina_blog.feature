
@exec
Funcionalidade: Validar página blog

  @blog
  Cenário: Validar uma pesquisa válida na página blog
    Dado que eu esteja na página do blog
    Quando eu buscar por um post existente
    Então eu devo ver o post sendo exibido em sua área

  @blog
  Cenário: Validar uma pesquisa inválida na página blog
    Dado que eu esteja na página do blog
    Quando eu buscar por um post não existente
    Então eu não devo ver a área de post sendo exibida