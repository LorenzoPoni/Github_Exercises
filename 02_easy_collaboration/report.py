class report:
    def __init__(self, apparati):
        self.lista_apparati = apparati

    def filtra_per_stato(self, stato):
        if stato not in ["OK", "ATTENZIONE", "OFFLINE"]:
            raise ValueError("Stato non valido. Deve essere 'OK', 'ATTENZIONE' o 'OFFLINE'")
        for codice, apparato in self.lista_apparati.items():
            if apparato["stato"] == stato:
                return f"{codice}: {apparato['nome']} - {apparato['bus']} - {apparato['stato']}"
            
    def filtra_per_bus(self, bus):
            if bus not in ["BUS-A", "BUS-B"]:
                raise ValueError("Bus non valido. Deve essere 'BUS-A' o 'BUS-B'")
            for codice, apparato in self.lista_apparati.items():
                if apparato["bus"] == bus:
                    return f"{codice}: {apparato['nome']} - {apparato['bus']} - {apparato['stato']}"