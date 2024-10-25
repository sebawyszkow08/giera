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


        print(f"{self.imie} odpoczywa, ma teraz {self.hp} hp")

    def walka(self,przeciwnik):
        walka = True
        while walka:
            print(f" hp gracza :{self.hp}")
            print(f" hp {przeciwnik.imie} :{przeciwnik.hp}")

            akcja = input("atak czy ucieczka?")
            if akcja == "atak":
                self.atakuj(przeciwnik)
                if przeciwnik.hp <= 0:
                    print(f"{self.imie} zabija {przeciwnik.nazwa}")
                    return True
                przeciwnik.atakuj(self)
            

            elif akcja == "ucieczka":
                print(f"{self.gracz} uciekl z pola bitwy :( ")

                przeciwnik.atakuj(self)
                
                walka = False

            else:
                print("-_- wpisz poprawna komende")
    
            if self.hp <= 0:
                print(f"{self.imie} umiera")
                return False



gracz1 = gracz()
gra = True

while gra:
    akcja = input("jaka akcja wariacie? zwiedzaj lub odpocznij")

    if akcja == "zwiedzaj":
        if random.randint(0,1) == 0:
            print("jaskina")
        else:
            przeciwnik1 = przeciwnik(gracz1)
            print(f"{gracz1.imie} natrafil na przeciwnika {przeciwnik1.imie}")
            gra = gracz1.walka(przeciwnik1)
    elif akcja == "odpoczynek":
        gracz1.odpoczynek()


    else:
        print("nieznana akcja")

        

















