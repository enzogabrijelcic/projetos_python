
livros = [{"titulo": "livroA", "autor": "autorA", "ano_lancamento": 2000,"favorito": 0},
          {"titulo": "livroB", "autor": "autorB", "ano_lancamento": 2001,"favorito": 0},
          {"titulo": "livroC", "autor": "autorC", "ano_lancamento": 2002,"favorito": 0},
          {"titulo": "livroD", "autor": "autorD", "ano_lancamento": 2003,"favorito": 0}]

fav = livros[2]
fav["favorito"]=1
livros[2] = fav

print (fav)


for fav in livros:
    if fav["titulo"] == "livroC":
        fav["favorito"] = 1