import os
from csvConverter import *

def load(namaFolder):

    # cek ada tidaknya namaFolder yang diberikan
    if os.path.exists(namaFolder) == False:
        
        if os.path.exists(os.path.join("save", namaFolder)) == False:
            print(f'\nFolder "{namaFolder}" tidak ditemukan.')
            # jika tidak ada keluar dari program
            exit()
        
        else:
            csvFileUser  = os.path.join("save", namaFolder, "user.csv")
            csvFileCandi = os.path.join("save", namaFolder, "candi.csv")
            csvFileBahan = os.path.join("save", namaFolder, "bahan_bangunan.csv")
            
            csvUser  = open(csvFileUser, 'r')
            csvCandi = open(csvFileCandi, 'r')
            csvBahan = open(csvFileBahan, 'r')
            
            tempVar = konvert(csvCandi,csvUser,csvBahan)
            
            # UI ditemukan folder
            print("\nLoading...\n")
            print('Selamat datang di program "Manajerial Candi"')
            print("Silahkan masukkan username Anda\n")
            
            return tempVar
        
    else:
        csvFileUser  = os.path.join(namaFolder, "user.csv")
        csvFileCandi = os.path.join(namaFolder, "candi.csv")
        csvFileBahan = os.path.join(namaFolder, "bahan_bangunan.csv")
        
        csvUser  = open(csvFileUser, 'r')
        csvCandi = open(csvFileCandi, 'r')
        csvBahan = open(csvFileBahan, 'r')
        
        tempVar = konvert(csvCandi,csvUser,csvBahan)
        
        # UI ditemukan folder
        print("Loading...\n")
        print('Selamat datang di program "Manajerial Candi"')
        print("Silahkan masukkan username Anda\n")
        
        return tempVar