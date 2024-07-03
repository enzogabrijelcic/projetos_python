class Shark:
    def nadar(self):
        print ("o tubarao está nadando.")
    def nadar_costa(self):
        print ("o tubarao nao consegue nadar para tras.")
    def esqueleto(self):
        print("o esqueleto do tubarao é feito de cartilagem.")

class Clowfish():
    def nadar(self):
        print("o peixe-palhaço está nadando.")
    def nadar_costa(self):
        print("o peixe-palhaço nada para tras.")
    def esqueleto(self):
        print("o esqueleto do peixe-palhaço é feito de osso.")

def poliformismo_peixe(peixe):
    peixe.nadar()
    peixe.nadar_costa()
    peixe.esqueleto()

shark = Shark()
clowfish = Clowfish()

poliformismo_peixe(shark)
poliformismo_peixe(clowfish)
