from typing import List, Optional

# Class Brano

class Brano:
    def __init__ (self, titolo, autore, durata):
        self.titolo = titolo
        self.autore = autore
        self.durata = durata

    # Getters
    
    @property
    def titolo(self) -> str:
        return self._titolo

    @property
    def autore(self) -> str:
        return self._autore

    @property
    def durata(self) -> int:
        return self._durata

    # Setters

    @titolo.setter
    def titolo(self, titolo: str) -> None:
        self._titolo = titolo

    @autore.setter
    def autore(self, autore: str) -> None:
        self._autore = autore

    @durata.setter
    def durata(self, durata: int) -> None:
        self._durata = durata

    # Method to check if the song is short (less than 2 minutes)

    def short_song(self) -> bool:
        if self.durata < 120:
            return True
        else:
            return False

    # Method to return all song's information

    def __str__(self) -> str:
        return f"{self.titolo} - {self.autore} - ({self.durata} secondi)"

class CD:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.lista_brani = []

    # Methods to add and remove songs from the CD
    def aggiungi_brano(self, brano: Brano) -> str:
        if brano in self.lista_brani:
            return f"Brano {brano.titolo} già presente nel CD"
        else:
            self.lista_brani.append(brano)
            return f"Brano {brano.titolo} aggiunto"

    def rimuovi_brano(self, brano: Brano) -> str:
        if brano in self.lista_brani:
            self.lista_brani.remove(brano)
            return f"Brano {brano.titolo} rimosso"
        else:
            return f"Brano {brano.titolo} non trovato"

    def get_lista_brani(self) -> list:
        for brano in self.lista_brani:
            print(brano.__str__())

    # Method to calculate the total duration of the CD

    def durata_complessiva(self) -> int:
        durata_totale = 0
        for brano in self.lista_brani:
            durata_totale += brano.durata

        return durata_totale

    # Method to return all CD's information

    def __str__(self) -> str:
        return f"{self.titolo} - {self.autore} - ({len(self.lista_brani)} brani)"

if __name__ == "__main__":

    brano1 = Brano("Beggin'", "Maneskin", 180)
    brano2 = Brano("L'Altra Dimensione", "Måneskin", 200)
    brano3 = Brano("ZITTI E BUONI", "Måneskin", 210)

    print(brano1.short_song())
    print(brano1.__str__())

    cd1 = CD("Chosen", "Måneskin")
    print(cd1.__str__())

    cd1.aggiungi_brano(brano1)
    cd1.aggiungi_brano(brano2)
    cd1.aggiungi_brano(brano3)

    print(cd1.durata_complessiva())

    print(cd1.get_lista_brani())

    cd1.rimuovi_brano(brano1)
    cd1.rimuovi_brano(brano2)
    cd1.rimuovi_brano(brano3)

    print(cd1.get_lista_brani())

