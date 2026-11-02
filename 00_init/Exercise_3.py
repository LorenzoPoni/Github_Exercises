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