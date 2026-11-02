class Libro:
    def __init__(self, autore, titolo, anno, editore, numero_pagine):
        self.autore = autore
        self.titolo = titolo
        self.anno = anno
        self.editore = editore
        self.numero_pagine = numero_pagine

    def reading_time(self) -> int:
        return 2*self.numero_pagine

    def __str__(self) -> str:
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Editore: {self.editore}, Numero Pagine: {self.numero_pagine}"