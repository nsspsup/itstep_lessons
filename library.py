

class Kniha():
    def __init__(self,nazov,autor, isbn,rok,dostupna = True):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.rok = rok
        self.dostupna = dostupna

    def vypozicat(self):
        if self.dostupna == True:
            self.dostupna = False
            return  True
        else:
            return False

    def vratit(self):
        self.dostupna = True

    def __str__(self):
        return (f"{self.nazov}, {self.autor}, {self.isbn}, {self.rok}, {self.dostupna}")

class Kniznica():
    def __init__(self):
        self.knihy = []

    def pridat(self,kniha):
        self.knihy.append(kniha)

    def vyhladat(self,nazov):
        for kniha in self.knihy:
            if nazov.lower() == kniha.nazov.lower():
                return (f"{kniha.nazov} je v kniznici, dostupnost: {kniha.dostupna}")
            else:
                return(f"{kniha.nazov} sa nenachadza v kniznici")

    def vyhladat_text(self,text):
        for kniha in self.knihy:
            if (text.lower() in str(kniha.nazov.lower()) or
                text.lower() in str(kniha.autor.lower()) or
                text.lower() in str(kniha.isbn) or
                text.lower() in str(kniha.rok)):
                print (kniha.nazov,kniha.autor,kniha.isbn,kniha.rok)



    def vypozicat(self,isbn):
        for kniha in self.knihy:
            if kniha.isbn == isbn and kniha.dostupna == True:
                return kniha.vypozicat()
            else:
                return False

    def vratit(self,isbn):
        for kniha in self.knihy:
            if kniha.isbn == isbn:
                return kniha.vratit()
            else:
                return False

    def vsetky(self):
        for kniha in self.knihy:
            print(kniha)


kniznica = Kniznica()
k1 = Kniha("Harry Potter", "J.K. Rowling", 123456, 1997)
k2 = Kniha("Pán Prsteňov", "J.R.R. Tolkien", 654321, 1954)
k3 = Kniha("Prelet nad kukučím hniezdom","Ken Kesey",752691,1962)

kniznica.pridat(k1)
kniznica.pridat(k2)

print(k1)
print(k2)
print(kniznica.vyhladat("Harry Potter"))
kniznica.vypozicat(123456)
print(kniznica.vyhladat("Harry Potter"))
kniznica.pridat(k3)
print(8*"=")
kniznica.vsetky()
print(8*"=")
kniznica.vyhladat_text("19")

