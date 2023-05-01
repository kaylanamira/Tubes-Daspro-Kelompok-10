# F11 - Hancurkan Candi
from custom_function import *

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