# F12 - Ayam Berkokok
from custom_function import *

def berkokok(candi):
    # menghitung banyak candi & UI awal
    jumlahCandi = banyakCandi(candi)
    print("Kukuruyuk.. Kukuruyuk..\n")
    print("Jumlah Candi:",jumlahCandi)

    # kondisi berdasar jumlah candi
    if 0 <= jumlahCandi and jumlahCandi < 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!\n")
        print("*Bandung Bondowoso angry noise")
        print("Roro Jonggrang dikutuk menjadi candi.")
        
        # kondisi logout
        varLogin = False; varRun = False
    
    elif jumlahCandi == 100:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        # kondisi exit
        varLogin = False; varRun = False
    
    # mengembalikan kondisi variabel login dan run
    return (varLogin,varRun)

def berkokokNotLogin():
    print("ayamberkokok hanya dapat diakses oleh akun Roro Jonggrang.\n")
    