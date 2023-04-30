# F07 - Jin Pengumpul
import random

def isAdaElmt(bahan):
    for i in range(0,15,3):
        if "pasir" == bahan[i]:
            return True
    return False

def createElmt(bahan):
    bahan[3] = "pasir" ; bahan[4]  = "bahan pemadat" ; bahan[5]  = "0"
    bahan[6] = "batu"  ; bahan[7]  = "bahan pondasi" ; bahan[8]  = "0"
    bahan[9] = "air"   ; bahan[10] = "bahan perekat" ; bahan[11] = "0"
    return bahan    

# Pertanyaan apakah deskripsi tidak usah diadakan, karena tidak berpengaruh di implementasi program
# Pertanyaan apakah boleh memproses variabel inputan random dikonvert menjadi str dengan dinamic variabel langsung 
def assignBahan(bahan,n1,n2,n3):
    # loop
    for i in range(0,15,3):
        if "pasir" == bahan[i]:
            temp = int(bahan[i+2]) + n1
            bahan[i+2] = str(temp)
        elif "batu" == bahan[i]:
            temp = int(bahan[i+2]) + n2
            bahan[i+2] = str(temp)
        elif "air" == bahan[i]:
            temp = int(bahan[i+2]) + n3
            bahan[i+2] = str(temp)
    
    return bahan

def jinBatchKumpul(banyak,bahan):
    # UI awal
    print(f"Mengerahkan {banyak} jin untuk mengumpulkan bahan.")    
    # inisialisasi banyak bahan
    nPasir = 0; nBatu = 0; nAir = 0
    
    # looping sebanyak banyak jin
    for i in range(banyak):
        nPasir += random.randint(0,5)
        nBatu  += random.randint(0,5)
        nAir   += random.randint(0,5)
    
    # mencreate nama bahan bila array masih belum ada
    if isAdaElmt(bahan) == False:
        bahan = createElmt(bahan)
    
    # assign ke array bahan
    print(f"Jin menemukan total {nPasir} pasir, {nBatu} batu, dan {nAir} air.\n")
    bahan = assignBahan(bahan,nPasir,nBatu,nAir)
    
    # mengembalikan array bahan
    return bahan

def jinKumpul(bahan):
    nPasir = random.randint(0,5)
    nBatu  = random.randint(0,5)
    nAir   = random.randint(0,5)
    
    # mencreate nama bahan bila array masih belum ada
    if isAdaElmt(bahan) == False:
        bahan = createElmt(bahan)
    
    # assign ke array bahan
    print(f"Jin menemukan {nPasir} pasir, {nBatu} batu, dan {nAir} air.\n")
    bahan = assignBahan(bahan,nPasir,nBatu,nAir)
    
    # mengembalikan array bahan
    return bahan
