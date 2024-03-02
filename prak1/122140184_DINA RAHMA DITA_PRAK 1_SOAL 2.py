class Lingkaran:
    def __init__(self, rasio):
        self.rasio = rasio
    
    def luas(self):
        return self.rasio ** 2 * 3.14
    
    def keliling(self):
        return 2 * 3.14 * self.rasio

rasio = float(input("Masukkan rasio: "))

if rasio < 0:
    print("Jari-jari lingkaran tidak boleh negatif")
else:
    lingkaran = Lingkaran(rasio)
    print("Luas: ", lingkaran.luas())
    print("Keliling: ", lingkaran.keliling())

