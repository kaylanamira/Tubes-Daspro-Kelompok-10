from custom_function import *

def hapusjin(data_user,data_candi):
    uname_jin = input("Masukkan username jin : ")
    while not(adaUsername(uname_jin,data_user)):
        print()
        print("Tidak ada jin dengan username tersebut.")
        print()
        uname_jin = input("Masukkan username jin : ")
    else:
        yakin = input(f"Apakah anda yakin ingin menghapus jin dengan username {uname_jin} (Y/N)?")
        if yakin == "N" or yakin == "n":
            print("Jin tidak jadi dihapus.")
        elif yakin == "Y" or yakin == "y":
            #menghapus jin dari array data_user
            for i in range(0,360,3):
                if data_user[i] == uname_jin:
                    #menghapus semua data pada 3 kolom yg berkaitan dgn identitas jin
                    for j in range(3):
                        data_user[i+j] = None

            #menghapus candi yang dibangun jin dari array data_candi
            for m in range(1,505,5):
                if data_candi[m] == uname_jin:
                    #menghapus semua data pada 5 kolom yg berkaitan dgn identitas jin
                    for n in range(5):
                        data_candi[m+n] = None

            print("Jin telah berhasil dihapus dari alam gaib.")

    return data_user,data_candi
