from custom_function import *

def ubahjin(data_user):
    uname_jin = input("Masukkan username jin : ")

    if not(adaUsername(uname_jin,data_user)):
        print("Tidak ada jin dengan username tersebut.")
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
            print("Jin telah berhasil diubah.")
        else:
            print("Jin tidak jadi diubah.")

    return data_user