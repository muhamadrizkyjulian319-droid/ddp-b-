def nama_fungsi():
    # isi fungsi
    print("Halo dari fungsi!")  

def sapa(nama):
    print("Halo", nama)
sapa("Jokowi")
sapa("Hilman")

def tambah(a, b):
    return a + b
hasil = tambah(3, 5)
print(hasil)   # 8

def cetak_nama(nama, jumlah):
    for i in range(jumlah):
        print(nama)
cetak_nama("Alya", 3)