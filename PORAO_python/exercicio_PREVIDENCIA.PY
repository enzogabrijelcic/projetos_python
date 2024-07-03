#REFORMA DA PREVIDENCIA
#tempo mínimo contribuição : 25 anos
#id minima homem : 65
#id minima mulher : 62
# 40 anos de contribuição para 100% do beneficio

print("calculo reforma da previdência.")
sexo = input("qual seu sexo? [M] para masculino, [F] para feminino. ")
id_inicio_contribuicao = int(input("qual idade iniciou a contribuir com a previdência? "))
id_minima_homem = 65
id_minima_mulher = 62
id_beneficio_projetada_homem = 65 - id_inicio_contribuicao
id_beneficio_projetada_mulher = 62 - id_inicio_contribuicao

tempo_de_contribuicao_h = id_beneficio_projetada_homem + 40
tempo_de_contribuicao_m = id_beneficio_projetada_mulher + 40
if sexo == "m":
    print("Você terá direito a aposentadoria integral com 65 anos")
if sexo == "m" and id_beneficio_projetada_homem >= 25 and id_beneficio_projetada_homem <= 29:
    print ("com o tempo de contribuição de", id_beneficio_projetada_homem, "anos, voce terá direito a 70 por cento do beneficio" )
elif sexo == "m" and id_beneficio_projetada_homem >= 30 and id_beneficio_projetada_homem <= 34:
    print ("com o tempo de contribuição de", id_beneficio_projetada_homem, "anos,voce terá direito a 77.5 por cento do beneficio")
elif sexo == "m" and id_beneficio_projetada_homem >= 35 and id_beneficio_projetada_homem <= 39:
    print ("com o tempo de contribuição de", id_beneficio_projetada_homem, "anos, voce terá direito a 87.5 por cento do beneficio")
elif sexo == "m" and id_beneficio_projetada_homem >=40:
     print ("com o tempo de contribuição de", id_beneficio_projetada_homem, "anos, voce terá direito a 100 por cento do beneficio")
     
if sexo == "f":
    print("Você terá direito a aposentadoria integral com 62 anos")
if sexo == "f" and id_beneficio_projetada_mulher >= 25 and id_beneficio_projetada_mulher <= 29:
    print ("com o tempo de contribuição de", id_beneficio_projetada_mulher, "anos, voce terá direito a 70 por cento do beneficio" )
elif sexo == "f" and id_beneficio_projetada_mulher >= 30 and id_beneficio_projetada_mulher <= 34:
    print ("com o tempo de contribuição de", id_beneficio_projetada_mulher, "anos, voce terá direito a 77.5 por cento do beneficio")
elif sexo == "f" and id_beneficio_projetada_mulher >= 35 and id_beneficio_projetada_mulher <= 39:
    print ("com o tempo de contribuição de", id_beneficio_projetada_mulher, "anos, voce terá direito a 87.5 por cento do beneficio")
elif sexo == "f" and id_beneficio_projetada_mulher >=40:
     print ("com o tempo de contribuição de", id_beneficio_projetada_mulher, "anos, voce terá direito a 100 por cento do beneficio")
    
#nao acabei ainda