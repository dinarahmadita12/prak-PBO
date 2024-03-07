class Mahasiswa:
    def __init__(self, NIM, Nama, Angkatan, isMahasiswa=True):
        self.__NIM = NIM
        self.__Nama = Nama
        self.Angkatan = Angkatan
        self.isMahasiswa = isMahasiswa

    @property
    def NIM(self):
        return self.__NIM

    @NIM.setter
    def NIM(self, NIM_terbaru):
        self.__NIM = NIM_terbaru

    @property
    def Nama(self):
        return self.__Nama

    @Nama.setter
    def Nama(self, Nama_terbaru):
        self.__Nama = Nama_terbaru

    def data_mahasiswa(self):
        return f"NIM: {self.NIM}\nNama: {self.Nama}\nAngkatan: {self.Angkatan}\nMahasiswa: {'Aktif' if self.isMahasiswa else 'Tidak Aktif'}\n"

    def angkatan_cek(self, tahun_saat_ini):
        return f"Mahasiswa Angkatan {self.Angkatan} {'telah' if tahun_saat_ini >= self.Angkatan else 'belum'} lulus."

    def ganti_status(self, status_terbaru):
        self.isMahasiswa = status_terbaru
        return f"Status mahasiswa {self.Nama} {'diaktifkan' if status_terbaru else 'dinonaktifkan'}.\n"


mahasiswa1 = Mahasiswa("122140184", "Dina", 2023)
print(mahasiswa1.data_mahasiswa())

mahasiswa1.Nama = "Dina Rahma Dita"
print(mahasiswa1.data_mahasiswa())

print(mahasiswa1.angkatan_cek(2022))
print(mahasiswa1.ganti_status(False))

mahasiswa2 = Mahasiswa("122140185", "Anya", 2022)
print(mahasiswa2.data_mahasiswa())
