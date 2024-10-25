import random



class postac:
    def __init__(self):
        self.imie = ""
        self.hp = 1
        self.maxhp = 10

    def atakuj(self,przeciwnik):
        print(f"{self.imie} atakuje!")
        atak = random.randint(0,3)
        if atak == 0:
            print(f"{przeciwnik.nazwa} unika ataku")

        else:
            print(f"{self.imie} trafił, zadał {atak} obrażeń")
            przeciwnik.hp -= atak




class przeciwnik(postac):
    def __init__(self,gracz):
        super().__init__()
        nazwy = ["goblin","ryboczłowiek","bezdomny"]
        self.nazwa = random.choice(nazwy)
        self.hp = random.randint(1,(gracz.hp // 2))
        

    
class gracz(postac):
    def __init__(self):
        super().__init__()
        self.hp = 10
        self.maxhp = 10


    #def pobracnazwe(self):
        self.imie = input("podaj swoje imie")

    def odpoczynek(self):
        if self.hp < self.maxhp:
            self.hp +=1


        


    







