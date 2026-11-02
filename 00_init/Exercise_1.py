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

    # Method to calculate the total duration of the CD

    def durata_complessiva(self) -> int:
        durata_totale = 0
        for brano in self.lista_brani:
            durata_totale += brano.durata

        return durata_totale

    # Method to return all CD's information

    def __str__(self) -> str:
        return f"{self.titolo} - {self.autore} - ({len(self.lista_brani)} brani)"