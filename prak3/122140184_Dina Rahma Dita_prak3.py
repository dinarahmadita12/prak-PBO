class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga

        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((self.__nama, self.__stok, self.__harga))

    @classmethod
    def lihat_barang(cls):
        print("Jumlah barang dagangan pada toko:", cls.jumlah_barang, "buah")
        for i, barang in enumerate(cls.list_barang, start=1):
            print(f"{i}. {barang[0]} seharga Rp {barang[2]} (stok: {barang[1]})")
        print() 

    def __del__(self):
        for barang in Dagangan.list_barang:
            if barang[0] == self.__nama:
                print(f"{self.__nama} dihapus dari toko!")
                Dagangan.jumlah_barang -= 1
                Dagangan.list_barang.remove(barang)
                break

Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()

del Dagangan1
Dagangan.lihat_barang()
