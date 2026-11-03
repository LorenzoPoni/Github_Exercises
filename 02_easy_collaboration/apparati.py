APPARATI = {
	"NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
	"COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
	"SEN-03": {"nome": "Sensore assetto", "bus": "BUS-A", "stato": "OFFLINE"},
}

class apparato:
    def __init__(self):
        self.apparati = APPARATI

    def aggiungi_apparato(self, codice, nome, bus, stato):
        if codice in self.apparati:
            raise ValueError("L'apparato con questo codice esiste già")
        self.apparati[codice] = {"nome": nome, "bus": bus, "stato": stato}

    def aggiorna_stato(self, codice, stato):
        if codice not in self.apparati:
            raise ValueError("L'apparato con questo codice non esiste")
        if stato not in ["OK", "ATTENZIONE", "OFFLINE"]:
            raise ValueError("Stato non valido. Deve essere 'OK', 'ATTENZIONE' o 'OFFLINE'")
        self.apparati[codice]["stato"] = stato
