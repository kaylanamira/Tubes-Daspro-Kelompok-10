from custom_function import *
from F04 import *

def ubahjin(data_user):
    #mengubah role jin
    if isAdaJin(data_user):
        uname_jin = input("Masukkan username jin : ")

        while not(adaUsername(uname_jin,data_user)):
            print("\nTidak ada jin dengan username tersebut.\n")
            uname_jin = input("Masukkan username jin : ")
        else:
            idx_jin = get_index(uname_jin,data_user)
            role = data_user[idx_jin + 2]
            if role == "jin_pengumpul":
                cek = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                role = "jin_pembangun"
            else:
                cek = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                role = "jin_pengumpul"

            if cek == "Y":
                data_user[idx_jin + 2] = role
                print("\nJin telah berhasil diubah.\n")
            else:
                print("\nJin tidak jadi diubah.\n")
    else:
        print("Tidak ada jin untuk diubah.")

    return data_user

def ubahNotBandung():
    print("ubahjin hanya dapat dilakukan oleh Bandung Bondowoso.")