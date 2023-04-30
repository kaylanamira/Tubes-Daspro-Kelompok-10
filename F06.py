# F06 - Jin Pembangun
import random
from F07 import *

def banyakCandi(candi):
    count = 0
    for i in range(5,505,5):
        if candi[i] == None:
            count += 0
        else:
            count += 1
    return count

def assignCandi(candi,user,n1,n2,n3):
    for i in range(5,505,5):
        if candi[i] == None:
            candi[i]   = str(i//5 - 1)
            candi[i+1] = user
            candi[i+2] = str(n1)
            candi[i+3] = str(n2)
            candi[i+4] = str(n3)
            return candi

def ambilBahan(bahan,n1,n2,n3):
    # ambil data bahan bangunan dari bahan.csv
    nPasir = int(bahan[5]) - n1
    nBatu  = int(bahan[8]) - n2
    nAir   = int(bahan[11]) - n3

    # assign ke array bahan    
    bahan[5]  = str(nPasir)
    bahan[8]  = str(nBatu)
    bahan[11] = str(nAir)
    
    # kembalikan array
    return bahan

def isMungkinBangun(bahan,n1,n2,n3):
    nPasir = int(bahan[5])
    nBatu  = int(bahan[8])
    nAir   = int(bahan[11])

    # kondisi agar memungkinkan candi dibangun
    if nPasir < n1 or nBatu < n2 or nAir < n3:
        return False
    else:
        return True

def laporanGagalBangun(bahan,n1,n2,n3):
    nPasir = n1 - int(bahan[5])
    nBatu  = n2 - int(bahan[8])
    nAir   = n3 - int(bahan[11])
    
    if nPasir < 0:  nPasir = 0
    if nBatu  < 0:  nBatu  = 0
    if nAir   < 0:  nAir   = 0
    
    # mengembalikan hasil bahan
    return (nPasir,nBatu,nAir)    
    
def pembangun(banyak,user):
    # inisialisasi array
    jinPembangun  = ["" for i in range(banyak)]
    nPembangun = 0
    
    # assign username jin_pembangun ke dalam array pembangun
    for i in range(5,360,3):
        if user[i] == "jin_pembangun":
            jinPembangun[nPembangun] = user[i-2]
            nPembangun += 1
    
    # mengembalikan array
    return jinPembangun            

def jinBatchBangun(banyak,bahan,candi,user):
    # inisialisasi banyak bahan
    nPasirArr = [0 for i in range(banyak)]
    nBatuArr = [0 for i in range(banyak)]
    nAirArr = [0 for i in range(banyak)]
    nPasir = 0; nBatu = 0; nAir = 0
    Pembangun = pembangun(banyak,user)
    
    # looping sebanyak banyak jin n cek apkh hasil random 0 semua
    for i in range(banyak):
        pasir = random.randint(1,5)  ; nPasir += pasir ; nPasirArr[i] = pasir
        batu  = random.randint(1,5)  ; nBatu  += batu  ; nBatuArr[i]  = batu
        air   = random.randint(1,5)  ; nAir   += air   ; nAirArr[i]   = air
    
    # mencreate nama bahan bila array masih belum ada
    if isAdaElmt(bahan) == False:
        bahan = createElmt(bahan)
    
    # UI awal
    print(f"Mengerahkan {banyak} jin untuk membangun candi dengan total bahan {nPasir} pasir, {nBatu} batu, dan {nAir} air.")
    
    # mengecek kemungkinan dapat membagun candi
    if isMungkinBangun(bahan,nPasir,nBatu,nAir): # cek apakah jumlah bahan cukup
        
        if banyak + banyakCandi(candi) <= 100: # perlu ditanyakan
            for i in range(banyak):
                candi = assignCandi(candi,Pembangun[i],nPasirArr[i],nBatuArr[i],nAirArr[i])
                bahan = ambilBahan(bahan,nPasirArr[i],nBatuArr[i],nAirArr[i])            
            print(f"Jin berhasil membangun total {banyak} candi.\n")

            return (bahan,candi)

        else: # apakah
            for i in range(banyak):
                if i + banyakCandi(candi) <= 100:
                    bahan = ambilBahan(bahan,nPasirArr[i],nBatuArr[i],nAirArr[i])
                    candi = assignCandi(candi,Pembangun[i],nPasirArr[i],nBatuArr[i],nAirArr[i])
                else: # i + banyakCandi(candi) > 100
                    bahan = ambilBahan(bahan,nPasirArr[i],nBatuArr[i],nAirArr[i])
                    
            print(f"Jin berhasil membangun total {banyak} candi.\n")

            return (bahan,candi)
    else:
        laporanBahan = laporanGagalBangun(bahan,nPasir,nBatu,nAir)
        print(f"Bangun gagal. Kurang {laporanBahan[0]} pasir, {laporanBahan[1]} batu, dan {laporanBahan[2]} air.\n")    
        
        return (bahan,candi)

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
