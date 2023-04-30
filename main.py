# Program Cinta Bondo ke Roro
# Adalah program yang merupakan sarana Bondo dan Roro berseteru di cinta mereka
# Waktu pengejaan : 11/04/2023 - 02/05/2023 
# Tubes K07-10

# import library
import argparse
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

# bagian parser
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("namaFolder", type=str, nargs="?")
    args = parser.parse_args()
    
    if args.namaFolder == None:
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: \x1B[3mpython main.py\x1B[0m <nama_folder>")
        # jika tidak ada maka keluar program
        exit()
    else:
        tempArray = load(args.namaFolder)

# Memasukkan hasil load data ke array
arrayOfBahan = tempArray[0]
arrayOfCandi = tempArray[1]
arrayOfUser  = tempArray[2]

# Algoritma userInput
isRun = True
isLogin = False
while isRun:
    #kondisi user belum login
    userInput = input(">>> ")
    
    #Fungsi-fungsi ketika user belum login    
    if userInput == ("login"):      
        tempVar  = login(arrayOfUser)
        isLogin  = tempVar[0]
        role     = tempVar[1]
        UserName = tempVar[2]
    elif userInput == ("logout"):   
        not_logout()
    elif userInput == ("save"):     
        save(arrayOfUser,arrayOfCandi,arrayOfBahan)
    elif userInput == ("help"):     
        loginHelp()
    elif userInput == ("exit"):     
        isRun = exitNotLogin(arrayOfUser,arrayOfCandi,arrayOfBahan)

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
                tempVar = hapusjin(arrayOfUser,arrayOfCandi)
                arrayOfUser  = tempVar[0]
                arrayOfCandi = tempVar[1]
            elif userInput == ("ubahjin"):
                arrayOfUser  = ubahjin(arrayOfUser)
            elif userInput == ("batchkumpul"):
                arrayOfBahan = batchKumpul(arrayOfUser,arrayOfBahan)
            elif userInput == ("batchbangun"):
                tempVar = batchBangun(arrayOfUser,arrayOfBahan,arrayOfCandi)
                arrayOfBahan = tempVar[0]
                arrayOfCandi = tempVar[1]
            elif userInput == ("laporanjin"):
                laporanJinDgnAkses(arrayOfUser,arrayOfBahan,arrayOfCandi)
            elif userInput == ("laporancandi"):
                laporanCandiDgnAkses(arrayOfCandi)
            elif userInput == ("hancurkancandi"):
                hancurkanNotLogin()
            elif userInput == ("ayamberkokok"):
                berkokokNotLogin()
            elif userInput == ("save"):
                save(arrayOfUser,arrayOfCandi,arrayOfBahan)
            elif userInput == ("help"):
                bondowosoHelp()
            elif userInput == ("exit"):
                tempVar = exitLogin(arrayOfUser,arrayOfCandi,arrayOfBahan)
                isLogin = tempVar[0]
                isRun   = tempVar[1]
                        
        # login sebagai role roro_jonggrang
        if role == 2:
            
            if userInput    == ("login"):
                loginLagi(UserName)
            elif userInput == ("logout"):
                isLogin      = logout()
            elif userInput == ("summonjin"):
                summonNotBandung()
            elif userInput == ("hapusjin"):
                hapusNotBandung()
            elif userInput == ("ubahjin"):
                ubahNotBandung()
            elif userInput == ("batchkumpul"):
                batchBukanBandung()
            elif userInput == ("batchbangun"):
                batchBukanBandung()
            elif userInput == ("laporanjin"):
                laporanJinNoAkses()
            elif userInput == ("laporancandi"):
                laporanCandiNoAkses()
            elif userInput == ("hancurkancandi"):
                hancurkan(arrayOfCandi)
            elif userInput == ("ayamberkokok"):
                berkokok(arrayOfCandi)
            elif userInput == ("save"):
                save(arrayOfUser,arrayOfCandi,arrayOfBahan)
            elif userInput == ("help"):
                roroHelp()
            elif userInput == ("exit"):
                tempVar = exitLogin(arrayOfUser,arrayOfCandi,arrayOfBahan)
                isLogin = tempVar[0]
                isRun   = tempVar[1]
                                    
        # login sebagai role jin_pengumpul
        if role == 3:
            
            if userInput    == ("login"):
                loginLagi(UserName)
            elif userInput == ("logout"):
                isLogin      = logout()
            elif userInput == ("kumpul"):
                arrayOfBahan = jinKumpul(arrayOfBahan)
            elif userInput == ("summonjin"):
                summonNotBandung()
            elif userInput == ("hapusjin"):
                hapusNotBandung()
            elif userInput == ("ubahjin"):
                ubahNotBandung()
            elif userInput == ("batchkumpul"):
                batchBukanBandung()
            elif userInput == ("batchbangun"):
                batchBukanBandung()
            elif userInput == ("laporanjin"):
                laporanJinNoAkses()
            elif userInput == ("laporancandi"):
                laporanCandiNoAkses()
            elif userInput == ("hancurkancandi"):
                hancurkanNotLogin()
            elif userInput == ("ayamberkokok"):
                berkokokNotLogin()
            elif userInput == ("save"):
                save(arrayOfUser,arrayOfCandi,arrayOfBahan)
            elif userInput == ("help"):
                jinpengumpulHelp()
            elif userInput == ("exit"):
                tempVar = exitLogin(arrayOfUser,arrayOfCandi,arrayOfBahan)
                isLogin = tempVar[0]
                isRun   = tempVar[1]
                                    
        # login sebagai role jin_pembangun
        if role == 4:
            
            if userInput    == ("login"):
                loginLagi(UserName)
            elif userInput == ("logout"):
                isLogin      = logout()
            elif userInput == ("bangun"):
                tempVar = jinBangun(arrayOfBahan,arrayOfCandi,arrayOfUser)
                arrayOfBahan = tempVar[0]
                arrayOfBahan = tempVar[1]
            elif userInput == ("summonjin"):
                summonNotBandung()
            elif userInput == ("hapusjin"):
                hapusNotBandung()
            elif userInput == ("ubahjin"):
                ubahNotBandung()
            elif userInput == ("batchkumpul"):
                batchBukanBandung()
            elif userInput == ("batchbangun"):
                batchBukanBandung()
            elif userInput == ("laporanjin"):
                laporanJinNoAkses()
            elif userInput == ("laporancandi"):
                laporanCandiNoAkses()
            elif userInput == ("hancurkancandi"):
                hancurkanNotLogin()
            elif userInput == ("ayamberkokok"):
                berkokokNotLogin()
            elif userInput == ("save"):
                save(arrayOfUser,arrayOfCandi,arrayOfBahan)
            elif userInput == ("help"):
                jinpembangunHelp()
            elif userInput == ("exit"):
                tempVar = exitLogin(arrayOfUser,arrayOfCandi,arrayOfBahan)
                isLogin = tempVar[0]
                isRun   = tempVar[1]
                            