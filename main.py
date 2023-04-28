# Program Cinta Bondo ke Roro
# Adalah program yang merupakan sarana Bondo dan Roro berseteru di cinta mereka
# Waktu pengejaan : 11/04/2023 - 02/05/2023 
# Tubes K07-10

# import file openCSV
from csvConverter import *
# open csv
# membuka file csv
csvCandi           = open("26-04-2023/candi.csv", 'r')
csvUser            = open("26-04-2023/user.csv", 'r')
csvBahan_bangunan  = open("26-04-2023/bahan_bangunan.csv", 'r')
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
while isRun:
    #kondisi user belum login
    userInput = input(">>> ")

    #Fungsi-fungsi ketika user belum login    
    if userInput == ("login"):      
        isLogin  = (login(arrayOfUser))[0]
        role     = (login(arrayOfUser))[1]
        UserName = (login(arrayOfUser))[2]
    elif userInput == ("logout"):   
        not_logout()
    elif userInput == ("save"):     
        save(arrayOfUser,arrayOfCandi,arrayOfBahan)
    elif userInput == ("help"):     
        loginHelp()
    elif userInput == ("exit"):     
        isRun = exitNotLogin()

    # fungsi-fungsi ketika user sudah melakukan login
    while isLogin:
        userInput = input(">>> ")
        
        # login sebagai role bandung_bondowoso
        if role == 1:
            
            if userInput    == ("login"):
                loginLagi(UserName)
            elif userInput == ("logout"):
                isLogin      = logout()
            elif userInput == ("summonjin"):
                arrayOfUser  = summonjin(arrayOfUser)
            elif userInput == ("hapusjin"):
                arrayOfUser  = (hapusjin(arrayOfUser,arrayOfCandi))[0]
                arrayOfCandi = (hapusjin(arrayOfUser,arrayOfCandi))[1]
            elif userInput == ("ubahjin"):
                arrayOfUser  = ubahjin(arrayOfUser)
            elif userInput == ("batchkumpul"):
                arrayOfBahan = batchKumpul(arrayOfUser,arrayOfBahan)
            elif userInput == ("batchbangun"):
                arrayOfBahan = (batchBangun(arrayOfUser,arrayOfBahan,arrayOfCandi))[0]
                arrayOfCandi = (batchBangun(arrayOfUser,arrayOfBahan,arrayOfCandi))[1]
            elif userInput == ("laporanjin"):
                laporanJinDgnAkses()
            # elif userInput == ("laporancandi"):
            # elif userInput == ("hancurkancandi")
            # elif userInput == ("ayamberkokok")
            # fungsinya
            elif userInput == ("save"):
                save(arrayOfUser,arrayOfCandi,arrayOfBahan)
            elif userInput == ("help"):
                bondowosoHelp()
            elif userInput == ("exit"):
                isLogin = (exitLogin())[0]
                isRun   = (exitLogin())[1]
                        
        # login sebagai role roro_jonggrang
        if role == 2:
            
            if userInput    == ("login"):
                loginLagi(UserName)
            elif userInput == ("logout"):
                isLogin      = logout()
            # elif userInput == ("summonjin"):
            # elif userInput == ("hapusjin"):
            # elif userInput == ("ubahjin"):
            # elif userInput == ("batchkumpul"):
            # elif userInput == ("batchbangun"):
            # elif userInput == ("laporanjin"):
                laporanJinNoAkses()
            # elif userInput == ("laporancandi"):
            # elif userInput == ("hancurkancandi")
            # elif userInput == ("ayamberkokok")
            # fungsinya
            elif userInput == ("save"):
                save(arrayOfUser,arrayOfCandi,arrayOfBahan)
            elif userInput == ("help"):
                roroHelp()
            elif userInput == ("exit"):
                isLogin = (exitLogin())[0]
                isRun   = (exitLogin())[1]
                    
        # login sebagai role jin_pengumpul
        if role == 3:
            
            if userInput    == ("login"):
                loginLagi(UserName)
            elif userInput == ("logout"):
                isLogin      = logout()
            elif userInput == ("kumpul"):
                arrayOfBahan = jinKumpul(arrayOfBahan)
            # elif userInput == ("summonjin"):
            # elif userInput == ("hapusjin"):
            # elif userInput == ("ubahjin"):
            # elif userInput == ("batchkumpul"):
            # elif userInput == ("batchbangun"):
            elif userInput == ("laporanjin"):
                laporanJinNoAkses()
            # elif userInput == ("laporancandi"):
            # elif userInput == ("hancurkancandi")
            # elif userInput == ("ayamberkokok")
            elif userInput == ("save"):
                save(arrayOfUser,arrayOfCandi,arrayOfBahan)
            elif userInput == ("help"):
                jinpengumpulHelp()
            elif userInput == ("exit"):
                isLogin = (exitLogin())[0]
                isRun   = (exitLogin())[1]
                    
        # login sebagai role jin_pembangun
        if role == 4:
            
            if userInput    == ("login"):
                loginLagi(UserName)
            elif userInput == ("logout"):
                isLogin      = logout()
            elif userInput == ("bangun"):
                arrayOfBahan = (jinBangun(arrayOfBahan,arrayOfCandi,arrayOfUser))[0]
                arrayOfBahan = (jinBangun(arrayOfBahan,arrayOfCandi,arrayOfUser))[1]
            # elif userInput == ("summonjin"):
            # elif userInput == ("hapusjin"):
            # elif userInput == ("ubahjin"):
            # elif userInput == ("batchkumpul"):
            # elif userInput == ("batchbangun"):
            elif userInput == ("laporanjin"):
                laporanJinNoAkses()
            # elif userInput == ("laporancandi"):
            # elif userInput == ("hancurkancandi")
            # elif userInput == ("ayamberkokok")
            # fungsinya
            elif userInput == ("save"):
                save(arrayOfUser,arrayOfCandi,arrayOfBahan)
            elif userInput == ("help"):
                jinpembangunHelp()
            elif userInput == ("exit"):
                isLogin = (exitLogin())[0]
                isRun   = (exitLogin())[1]
            