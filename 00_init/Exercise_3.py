class Studente:
    def __init__(self, nome, cognome, età, città_di_residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.città_di_residenza = città_di_residenza

    def classificazione(self) -> str:
        if self.età < 16:
            return "Studente del Biennio"
        else:
            return "Studente del Triennio"

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Cognome: {self.cognome}, Età: {self.età}, Città di Residenza: {self.città_di_residenza}"

class Scuola:
    def __init__(self, nome):
        self.nome = nome
        self.lista_studenti = []

    def aggiungi_studente(self, studente: Studente) -> str:
        if studente in self.lista_studenti:
            return f"Studente {studente.nome} {studente.cognome} già presente"
        else:
            self.lista_studenti.append(studente)
            return f"Studente {studente.nome} {studente.cognome} aggiunto alla scuola"

    def ricerca_per_cognome(self, cognome: str) -> str:
        for studente in self.lista_studenti:
            if studente.cognome == cognome:
                return f"Studente presente"

        return f"Studente non trovato"

    def ricerca_per_età(self, età: int) -> str:
        for studente in self.lista_studenti:
            if studente.età == età:
                return f"Studente presente"

        return f"Studente non trovato"

    def get_numero_studenti(self) -> int:
        return len(self.lista_studenti)
    