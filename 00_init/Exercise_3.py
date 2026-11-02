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

if __name__ == "__main__":
    studente1 = Studente("Mario", "Rossi", 15, "Roma")
    studente2 = Studente("Luca", "Bianchi", 17, "Milano")
    studente3 = Studente("Giulia", "Verdi", 16, "Napoli")

    scuola = Scuola("Liceo Scientifico")

    print(scuola.aggiungi_studente(studente1))
    print(scuola.aggiungi_studente(studente2))
    print(scuola.aggiungi_studente(studente3))

    print(scuola.ricerca_per_cognome("Bianchi"))
    print(scuola.ricerca_per_cognome("Neri"))

    print(scuola.ricerca_per_età(16))
    print(scuola.ricerca_per_età(18))

    print(f"Numero di studenti nella scuola: {scuola.get_numero_studenti()}")