# F11 - Hancurkan Candi

def isAdaCandi(num,candi):
    for i in range(5,505,5):
        if candi[i] == num:
            return True
    return False
    
def assignPenghancuran(num,candi):
    for i in range(5,505,5):
        if candi[i] == num:
            candi[i]   = None
            candi[i+1] = None
            candi[i+2] = None
            candi[i+3] = None
            candi[i+4] = None
            
    # mengembalikan hasil candi
    return candi

def hancurkanNotLogin():
    print("hancurkancandi hanya dapat diakses oleh akun Roro Jonggrang.\n")
    
def hancurkan(candi):
    # input inisiasi
    idCandi = input("Masukkan ID Candi: ")
    
    # cek adanya idCandi tersebut di candi.csv
    if isAdaCandi(idCandi,candi):
        cekYakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {idCandi} (Y/N)? ")
        if cekYakin == "Y":
            candi = assignPenghancuran(idCandi,candi)
            
            # print out kalau tujuan fungsi sudah tercapai
            print("\nCandi telah berhasil dihancurkan.")
            return candi
        
        elif cekYakin == "N":
            return candi
        
    else:
        print("\ntidak ada candi dengan ID tersebut.\n")
        return candi