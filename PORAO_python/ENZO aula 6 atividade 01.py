#letra é vogal ou consoante
print ("progama que verifica se letra é vogal ou consoante")
letra_do_usuario = input ("qual letra você quer testar?")

if letra_do_usuario == 'a' or letra_do_usuario == 'e' or letra_do_usuario == 'i' or letra_do_usuario == 'o' or letra_do_usuario == 'u':
    print ("esta letra é uma vogal")
elif letra_do_usuario == 'A' or letra_do_usuario == 'E' or letra_do_usuario == 'I' or letra_do_usuario == 'O' or letra_do_usuario == 'U':
    print ("esta letra é uma vogal")
elif letra_do_usuario == 'ç' or letra_do_usuario == 'Ç':
    print ("letra invalida")
else:
    print ("esta letra é uma consoante")
