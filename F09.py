# F09 - Ambil Laporan Jin
# ket: username : Bondowoso (akses)
from custom_function import *

# fungsi laporan jin 
def laporanJinNoAkses():
    print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.\n")
    
def laporanJinDgnAkses(user,bahan,candi):
    # ambil data yang diperlukan
    countJinPengumpul = hitungJin("jin_pengumpul",user)
    countJinPembangun = hitungJin("jin_pembangun",user)
    jinYang = jinTer(candi)
    Bahan   = ambilDataBahan(bahan)
    
    # memasukkan data ke prosedur output
    print()
    print("> Total jin:", countJinPembangun + countJinPengumpul)
    print("> Total jin Pengumpul:", countJinPengumpul)
    print("> Total jin Pembangun:", countJinPembangun)
    print("> Jin Terajin:", jinYang[0])
    print("> Jin Termalas:", jinYang[1])
    print("> Jumlah Pasir:", Bahan[0] ,"unit")
    print("> Jumlah Air:", Bahan[2] ,"unit")
    print("> Jumlah Batu:", Bahan[1] ,"unit\n")
