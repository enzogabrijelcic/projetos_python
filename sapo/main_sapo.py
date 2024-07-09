from sapo import Sapo

def le_sapo():
    with open ('projetos_python\sapo\sapo.txt', 'r')as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('Sapo: '):
                atributos = line .strip().split('Sapo:')[1]
                nome = atributos.split(':')[1].split(',')[0]
                idade = atributos.split(':')[2].split(',')[0]
                cor_olho = atributos.split(':')[3]
                sapo1 = Sapo(nome,idade,cor_olho)
                return sapo1
sapo = le_sapo()

print (sapo)