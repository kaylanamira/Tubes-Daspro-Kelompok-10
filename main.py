# Program Cinta Bondo ke Roro
# Adalah program yang merupakan sarana Bondo dan Roro berseteru di cinta mereka
# Waktu pengejaan : 11/04/2023 - 02/05/2023 
# Tubes K07-10

# import file openCSV
from csvConverter import *
# open csv
# membuka file csv
csvCandi           = open("data_csv/candi.csv", 'r')
csvUser            = open("data_csv/user.csv", 'r')
csvBahan_bangunan  = open("data_csv/bahan_bangunan.csv", 'r')
# konvert bacaan csv menjadi array
arrayOfBahan = (konvert(csvCandi,csvUser,csvBahan_bangunan))[0]
arrayOfCandi = (konvert(csvCandi,csvUser,csvBahan_bangunan))[1]
arrayOfUser  = (konvert(csvCandi,csvUser,csvBahan_bangunan))[2]

# import Implementasi Primitif fitur-fitur dari file terpisah
from F01 import * # F01 - Login
from F02 import * # F02 - Logout
from F03 import * # F03 - Summon Jin
from F04 import * # F04 - Hilangkan Jin
from F05 import * # F05 - Ubah Tipe Jin
from F06 import * # F06 - Jin Pembangun
from F07 import * # F07 - Jin Pengumpul
from F08 import * # F08 - Batch Kumpul/Bangun
from F09 import * # F09 - Ambil Laporan Jin
from F10 import * # F10 - Ambil Laporan Candi
from F11 import * # F11 - Hancurkan Candi
from F12 import * # F12 - Ayam Berkokok
from F13 import * # F13 - Load
from F14 import * # F14 - Save
from F15 import * # F15 - Help
from F16 import * # F16 - Exit

# Kamus

# Algoritma
isRun = True
isLogin = False
#while isRun:
#    userInput = input(">>> ")
    
    # kondisi user belum login
    # Fungsi-fungsi ketika user belum login

    # kondisi user sudah login
#    while isLogin:
#        inp = input(">>>> ")
        
        # login sebagai role bandung_bondowoso
        
        
        # login sebagai role roro_jonggrang
            
        
        # login sebagai role jin_pengumpul
            
        
        # login sebagai role jin_pembangun
            