# F08 - Batch Kumpul/Bangun
# ket: username : Bondowoso (akses)
from F06 import *
from F07 import *

def countTipeJin(user):
    # inisiasi penghitung
    countPengumpul = 0
    countPembangun = 0
    
    # looping penghitung
    for i in range(5,360,3):
        if user[i] == "jin_pengumpul":
            countPengumpul += 1
        if user[i] == "jin_pembangun":
            countPembangun += 1

    return (countPengumpul,countPembangun)
    
def batchKumpul(user,bahan):
    # hitung jumlah jin dengan tipe tertentu
    countJin = countTipeJin(user)
    
    # kondisi batchKumpul
    if countJin[0] == 0: # jumlah jin pengumpul berjumlah 0
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.\n")
    else:                # jumlah jin pengumpul berjumlah tidak 0
        bahan = jinBatchKumpul(countJin[0],bahan)
    
    # mengembalikan array bahan    
    return bahan

def batchBangun(user,bahan,candi):
    # hitung jumlah jin dengan tipe tertentu (role jin_pembangun)
    countJinPembangun = (countTipeJin(user))[1]
    
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
        