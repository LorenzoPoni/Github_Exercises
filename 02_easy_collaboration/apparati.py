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
        return f"L'apparato {nome} con codice {codice} è stato aggiunto con successo."

    def aggiorna_stato(self, codice, stato):
        if codice not in self.apparati:
            raise ValueError("L'apparato con questo codice non esiste")
        stato = stato.upper()
        if stato not in ["OK", "ATTENZIONE", "OFFLINE"]:
            raise ValueError("Stato non valido. Deve essere 'OK', 'ATTENZIONE' o 'OFFLINE'")
        self.apparati[codice]["stato"] = stato
        return f"Lo stato dell'apparato {codice} è stato aggiornato a {stato}."

if __name__ == "__main__":
    apparato1 = apparato()
    print(apparato1.aggiungi_apparato("NAV-04", "Ricevitore GPS", "BUS-C", "OK"))
    print(apparato1.aggiorna_stato("COM-02", "OK"))
    print(apparato1.aggiorna_stato("SEN-03", "attenzione"))

