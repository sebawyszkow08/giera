import random



class postac:
    def __init__(self):
        self.imie = ""
        self.hp = 1
        self.maxhp = 1

    def atakuj(self,przeciwnik):
        print(f"{self.imie} atakuje!")
        atak = random.randint(0,3)
        if atak == 0:
            print(f"{przeciwnik.nazwa} unika ataku")










