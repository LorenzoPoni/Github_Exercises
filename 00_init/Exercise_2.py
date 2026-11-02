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

class Biblioteca:
    def __init__(self, name):
        self.name = name
        self.lista_libri = []

    def aggiungi_libro(self, libro: Libro) -> str:
        if libro in self.lista_libri:
            return f"Libro {libro.titolo} già presente"
        else:
            self.lista_libri.append(libro)
            return f"Libro {libro.titolo} aggiunto alla biblioteca"

    def ricerca_libro(self, titolo: str) -> str:
        for libro in self.lista_libri:
            if libro.titolo == titolo:
                return f"Libro presente"

        return f"Libro non trovato"

    def get_numero_libri(self) -> int:
        return len(self.lista_libri)

if __name__ == "__main__":
    libro1 = Libro("J.K. Rowling", "Harry Potter e la Pietra Filosofale", 1997, "Bloomsbury", 223)
    libro2 = Libro("J.R.R. Tolkien", "Il Signore degli Anelli", 1954, "Allen & Unwin", 1216)
    libro3 = Libro("George Orwell", "1984", 1949, "Secker & Warburg", 328)

    biblioteca = Biblioteca("Biblioteca Comunale")

    print(biblioteca.aggiungi_libro(libro1))
    print(biblioteca.aggiungi_libro(libro2))
    print(biblioteca.aggiungi_libro(libro3))

    print(biblioteca.ricerca_libro("1984"))
    print(biblioteca.ricerca_libro("Il Grande Gatsby"))

    print(f"Numero di libri nella biblioteca: {biblioteca.get_numero_libri()}")