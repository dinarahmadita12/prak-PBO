class Film:
    def __init__(self, judul, tahun, jenis_film):
        self.judul = judul
        self.tahun = tahun
        self.jenis_film = jenis_film

    def __del__(self):
        print(f"Informasi film '{self.judul}' telah dihapus.")

    def data_film(self):
        print(f"Judul: {self.judul}")
        print(f"Tahun Rilis: {self.tahun}")
        print(f"Jenis Film: {self.jenis_film}\n")


def format_output(func):
    def wrapper(self):
        func(self)
    return wrapper

film1 = Film("Hafalan Sholat Delisa", 2011, "Religi")
film2 = Film("Ketika Cinta Bertasbih", 2009, "Romantis")

@format_output
def dekorator_film(film):
    film.data_film()

dekorator_film(film1)
print()
dekorator_film(film2)

del film1
del film2
