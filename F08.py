# F08 - Batch Kumpul/Bangun
# ket: username : Bondowoso (akses)
from custom_function import *

def batchKumpul(user,bahan):
    # hitung jumlah jin dengan tipe tertentu
    countJinPengumpul = hitungJin("jin_pengumpul",user)
    
    # kondisi batchKumpul
    if countJinPengumpul == 0: # jumlah jin pengumpul berjumlah 0
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.\n")
    else:                # jumlah jin pengumpul berjumlah tidak 0
        bahan = jinBatchKumpul(countJinPengumpul,bahan)
    
    # mengembalikan array bahan    
    return bahan

def batchBangun(user,bahan,candi):
    # hitung jumlah jin dengan tipe tertentu (role jin_pembangun)
    countJinPembangun = hitungJin("jin_pembangun",user)
    
    # kondisi batchBangun
    if countJinPembangun == 0: # jumlah jin pembangun berjumlah 0
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.\n")
    else:                      # jumlah jin pembangun berjumlah tidak 0
        if countJinPembangun + banyakCandi(candi) >= 0:
            tempTuple = jinBatchBangun(countJinPembangun,bahan,candi,user)
            bahan = tempTuple[0]; candi = tempTuple[1]
    
    # mengembalikan array bahan
    return (bahan,candi)

def batchBukanBandung():
    print("batch hanya dapat diakses oleh Bandung Bondowoso")
        