# F10 - Ambil Laporan Candi
# ket: username : Bondowoso (akses)
from F06 import *

# fungsi hitung total pasir yang dipakai
def banyakPasir(candi):
    jumlahPasir = 0
    for i in range(7,505,5):
        if candi[i] == None:
            jumlahPasir += 0
        else:
            jumlahPasir += int(candi[i])
    return jumlahPasir

# fungsi hitung total batu yang dipakai
def banyakBatu(candi):
    jumlahBatu = 0
    for i in range(8,505,5):
        if candi[i] == None:
            jumlahBatu += 0
        else:
            jumlahBatu += int(candi[i])
    return jumlahBatu

# fungsi hitung total air yang dipakai
def banyakAir(candi):
    jumlahAir = 0
    for i in range(9,505,5):
        if candi[i] == None:
            jumlahAir += 0
        else:
            jumlahAir += int(candi[i])
    return jumlahAir

# fungsi cari harga candi
def rpHargaCandi(pasir,batu,air):
    hasil = 10000*int(pasir) + 15000*int(batu) + 7500*int(air)
    return str(hasil)

# fungsi harga candi ter(mahal/murah)
def hargaCandiTer(candi):
    if banyakCandi(candi) == 0:
        idMahal = "-"
        idMurah = "-"
    else:
        hargaArr = [None for i in range(100)]
        mahal = 0; murah = 9999999999999999
        
        panjang = 0
        for i in range(5,505,5):
            if candi[i] == None:
                panjang += 0
            else:
                hargaArr[panjang] = rpHargaCandi(candi[i+2],candi[i+3],candi[i+4])
                panjang += 1
        
        for i in range(panjang):
            if int(hargaArr[i]) <= murah:
                murah = int(hargaArr[i])
            if int(hargaArr[i]) >= mahal:
                mahal = int(hargaArr[i])
        
        for i in range(5,505,5):
            if candi[i] != None:
                harga = rpHargaCandi(candi[i+2],candi[i+3],candi[i+4])
                if mahal == int(harga):
                    idMahal = (f"{str((i-5)//5)} (Rp {mahal})")
                if murah == int(harga):
                    idMurah = (f"{str((i-5)//5)} (Rp {murah})")
    
    return (idMahal,idMurah)

# fungsi format ambil laporan candi
def laporanCandiNoAkses():
    print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.\n")

def laporanCandiDgnAkses(candi):
    print()
    print("> Total Candi:", banyakCandi(candi))
    print("> Total Pasir yang digunakan:", banyakPasir(candi))
    print("> Total Batu yang digunakan:", banyakBatu(candi))
    print("> Total Air yang digunakan:", banyakAir(candi))
    print("> ID Candi Termahal:", (hargaCandiTer(candi))[0])
    print("> ID Candi Termurah:", (hargaCandiTer(candi))[1],"\n")
    