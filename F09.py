# F09 - Ambil Laporan Jin
# ket: username : Bondowoso (akses)
from F06 import *
from F07 import *
from F08 import *

def compareStrRajin(str1,str2):
    # pembanding        
    if str1 < str2: return str1
    else:           return str2 # str2 < str1

def compareStrMalas(str1,str2):
    # pembanding
    if str1 > str2: return str1
    else:           return str2 # str2 > str1

def jinTer(candi):
    if banyakCandi(candi) == 0:
        return ("-","-")
    else:
        # inisialisasi nilai
        arrayPemnbuatCandi = [None for i in range(100)]
        arrayCount         = [None for i in range(100)]
        
        # mencari seluruh pembuat yang ada
        indeks = 0
        for i in range(6,505,5):
            countsama = 0
            if candi[i] != None:
                
                # mencari jumlah yang sama pada suatu nama pembuat candi 
                namaJin = candi[i]
                for j in range(i,505,5):
                    if namaJin == candi[j]:
                        countsama += 1
                
                # assign ke arrayPembuat
                arrayPemnbuatCandi[indeks] = namaJin
                arrayCount[indeks] = countsama
                indeks += 1
        
        # mencari nilai terbanyak dan terkecil di arrayCount sambil diambil indeksnya
        large = 0; mini = 100
        for i in range(100):
            if arrayCount[i] != None:
                # largest
                if arrayCount[i] >= large:
                    large = arrayCount[i]
                    indBandingRajin = i
                    
                # smallest
                if arrayCount[i] <= mini:
                    mini = arrayCount[i]
                    indBandingMalas = i
                    
        # dibandingkan nama pembuat jin terajin dan termalas (sudah dengan mekanisme leksikografis str)
        # inisialisasi nilai
        tempStrRajin = arrayPemnbuatCandi[indBandingRajin]
        tempStrMalas = arrayPemnbuatCandi[indBandingMalas]
        # looping
        for i in range(100):
            # rajin
            if arrayCount[i] == large:
                tempStrRajin = compareStrRajin(tempStrRajin,arrayPemnbuatCandi[i])
            # malas
            if arrayCount[i] == mini:
                tempStrMalas = compareStrMalas(tempStrMalas,arrayPemnbuatCandi[i])    
        
        return (tempStrRajin,tempStrMalas)
      
def ambilDataBahan(bahan):
    # cek apakah array None
    if isAdaElmt(bahan) == False:
        bahan = createElmt(bahan)
    
    return (bahan[5],bahan[8],bahan[11])

# fungsi laporan jin 
def laporanJinNoAkses():
    print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.\n")
    
def laporanJinDgnAkses(user,bahan,candi):
    # ambil data yang diperlukan
    jin     = countTipeJin(user)
    jinYang = jinTer(candi)
    Bahan   = ambilDataBahan(bahan)
    
    # memasukkan data ke prosedur output
    print()
    print("> Total jin:", jin[0] + jin[1])
    print("> Total jin Pengumpul:", jin[0])
    print("> Total jin Pembangun:", jin[1])
    print("> Jin Terajin:", jinYang[0])
    print("> Jin Termalas:", jinYang[1])
    print("> Jumlah Pasir:", Bahan[0] ,"unit")
    print("> Jumlah Air:", Bahan[2] ,"unit")
    print("> Jumlah Batu:", Bahan[1] ,"unit\n")
