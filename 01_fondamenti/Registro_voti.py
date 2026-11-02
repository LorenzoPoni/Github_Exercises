class RegistroVoti:
    def __init__(self):
        self.voti = []

    def aggiungi_voto(self, voto):
        if voto < 0 or voto > 10:
            raise ValueError("Il voto deve essere compreso tra 0 e 10")
        self.voti.append(voto)

    def __str__(self):
        return f"Registro Voti: {self.voti}"