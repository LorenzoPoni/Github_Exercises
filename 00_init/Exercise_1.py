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
        return self.autore

    @property
    def durata(self) -> int:
        return self.durata

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
        return f"{self.titolo} - {self.autore} ({self.durata} secondi)"