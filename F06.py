# F06 - Jin Pembangun
import random
from custom_function import *

def jinBangun(bahan,candi,user):
    # mengambil angka random
    nPasir = random.randint(1,5)
    nBatu  = random.randint(1,5)
    nAir   = random.randint(1,5)
    
    # mencreate nama bahan bila array masih belum ada
    if isAdaElmt(bahan) == False:
        bahan = createElmt(bahan)

    # mengecek kemungkinan dapat membagun candi
    if isMungkinBangun(bahan,nPasir,nBatu,nAir): # cek apakah jumlah bahan cukup
        
        # mengecek apakah mungkin membangun candi
        if banyakCandi(candi) < 100:
            candi = assignCandi(candi,user,nPasir,nBatu,nAir)
            bahan = ambilBahan(bahan,nPasir,nBatu,nAir)
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100-banyakCandi(candi)}.\n")
        else:
            bahan = ambilBahan(bahan,nPasir,nBatu,nAir)
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: 0.\n")
        
    else: # jumlah bahan bangunan tidak cukup
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!\n")
   
    return (bahan,candi)
