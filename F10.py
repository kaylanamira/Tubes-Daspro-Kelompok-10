# F10 - Ambil Laporan Candi
# ket: username : Bondowoso (akses)
from custom_function import *

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
    