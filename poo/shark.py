class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5

new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)

class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#como instanciar o shark?
new_shark = Shark("Dentusso", 20)
print(new_shark.name)
print(new_shark.age)

class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 0
    
    def __init__(self, name_p, age_p):
        self.name = name_p
        self.age = age_p
        
    def set_followers(self, followers_p):
        self.followers = followers_p
        print ("esse usuario tem" + str(self.followers) + "seguidores")
        #metodo que modifica o nome do tubarao
    def set_name(self, name_p):
        self.name = name_p
        #metodo que apaga todas as informações do tubarao
    def clean_all(self):
        self.animal = ""
        self.location = ""
        self.followers = 0
        self.age = 0
        self.name = ""
        print("tudo foi limpo")
          
new_shark = Shark("Joshi", 20)
print(new_shark.followers)
new_shark.set_followers(5)
print(new_shark.followers)

new_shark.set_name("Jose")
print(new_shark.name)

new_shark.clean_all()
print(new_shark.age)        