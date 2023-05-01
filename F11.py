# F11 - Hancurkan Candi
from custom_function import *

def hancurkanNotLogin():
    print("hancurkancandi hanya dapat diakses oleh akun Roro Jonggrang.\n")
    
def hancurkan(candi):
    # input inisiasi
    idCandi = input("Masukkan ID Candi: ")
    
    # cek adanya idCandi tersebut di candi.csv
    if isAdaCandi(idCandi,candi):
        
        inputBenar = False
        while inputBenar == False:
            cekYakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {idCandi} (Y/N)? ")
            if cekYakin == "Y" or cekYakin == "y" or cekYakin == "N" or cekYakin == "n":
                inputBenar = True            
            
        if cekYakin == "Y" or cekYakin == "y":
            candi = assignPenghancuran(idCandi,candi)
            
            # print out kalau tujuan fungsi sudah tercapai
            print("\nCandi telah berhasil dihancurkan.\n")
            return candi
        
        elif cekYakin == "N" or cekYakin == "n":
            
            print("\nCandi tidak jadi dihancurkan\n")
            return candi
        
    else:
        print("\ntidak ada candi dengan ID tersebut.\n")
        return candi