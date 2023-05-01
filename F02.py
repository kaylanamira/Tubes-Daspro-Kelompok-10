# F02 - Logout
def logout(): #Kondisi ketika user ingin logout pada keadaan sudah login
    print("Anda berhasil logout")
    return False

def not_logout(): #Kondisi ketika user ingin logout pada keadaan belum login   
    print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout\n")