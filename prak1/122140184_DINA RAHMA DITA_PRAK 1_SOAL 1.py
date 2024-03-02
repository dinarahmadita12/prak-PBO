batas_bawah = int(input("Batas bawah: "))
batas_atas = int(input("Batas atas: "))

def bil_ganjil(batas_bawah, batas_atas):
    if batas_bawah < 0 or batas_atas < 0:
        print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah Nol")
        return bil_ganjil

    total_bil_ganjil = 0
    for angka in range(batas_bawah, batas_atas):
        if angka % 2 != 0:
            total_bil_ganjil += angka
            print(angka)
    print(f"total : {total_bil_ganjil}")
bil_ganjil(batas_bawah, batas_atas)
