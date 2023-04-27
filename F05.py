from custom_function import *

def ubahjin(arr):
    uname_jin = input("Masukkan username jin : ")

    while not(adaUsername(uname_jin,arr)):
        print("Tidak ada jin dengan username tersebut.")
        uname_jin = input("Masukkan username jin : ")
    else:
        idx_jin = get_index(uname_jin,arr)
        role = arr[idx_jin + 2]
        if role == "jin_pengumpul":
            cek = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            role = "jin_pembangun"
        else:
            cek = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
            role = "jin_pengumpul"

        if cek == "Y":
            arr[idx_jin + 2] = role
            print("Jin telah berhasil diubah.")
        else:
            print("Jin tidak jadi diubah.")

    return arr