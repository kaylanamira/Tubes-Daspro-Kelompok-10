#Berisi fungsi-fungsi custom 
import random

def adaUsername(uname,arr):
    #mendeteksi apakah uname ada pada array
    i = 0
    ada = False
    while i<360 and ada == False:
        if arr[i] == uname:
            ada = True
        i += 3
    return ada

def length(arr):
    #menghitung panjang suatu array
    string_of_arr = str(arr)
    count = 0
    for i in range(len(string_of_arr)):
        if string_of_arr[i] == "'":
            count += 1
    panjang = count//2
    return panjang

def get_index(element,arr):
    #menentukan index suatu elemen array
    for i in range(length(arr)):
        if arr[i] == element:
            index = i
    return index


def hitungJin(role,data_user):
    #menghitung jumlah jin dengan role tertentu pada array data_user
    count = 0
    for i in range(360):
        if data_user[i] == role :
            count += 1
    return count

def ubahCSV(data,panjang_data):
    arr3 = [None for i in range(panjang_data)]
    tempStr = ""
    i = 0
    for k in range(len(data)):
        if data[k] == ";" or data[k] == "\n":
            arr3[i] = tempStr
            tempStr = ""
            i += 1
        else:
            tempStr += data[k]
    return arr3

# konversi array ke string
# user part
def strUser(user):
    tempStr = ""
    
    for i in range(360):
        if user[i] != None and i != 359:
            if i%3 == 2:
                tempStr += user[i]
                tempStr += "\n"
            else:
                tempStr += user[i]
                tempStr += ";"
                 
    return tempStr

# candi part
def strCandi(candi):
    tempStr = ""
    for i in range(505):
        if candi[i] != None and i != 505:
            if i%5 == 4:
                tempStr += candi[i]
                tempStr += "\n"
            else:
                tempStr += candi[i]
                tempStr += ";"
    
    return tempStr
    
# bahan part
def strBahan(bahan):
    tempStr = ""
    for i in range(15):
        if bahan[i] != None and i != 14:
            if i%3 == 2:
                tempStr += bahan[i]
                tempStr += "\n"
            else:
                tempStr += bahan[i]
                tempStr += ";"
    
    return tempStr

def isAdaCandi(num,candi):
    for i in range(5,505,5):
        if candi[i] == num:
            return True
    return False
    
def assignPenghancuran(num,candi):
    for i in range(5,505,5):
        if candi[i] == num:
            candi[i]   = None
            candi[i+1] = None
            candi[i+2] = None
            candi[i+3] = None
            candi[i+4] = None
            
    # mengembalikan hasil candi
    return candi


# fungsi hitung total pasir yang dipakai
def banyakPasir(candi):
    jumlahPasir = 0
    for i in range(7,505,5):
        if candi[i] == None:
            jumlahPasir += 0
        else:
            jumlahPasir += int(candi[i])
    return jumlahPasir

# fungsi hitung total batu yang dipakai
def banyakBatu(candi):
    jumlahBatu = 0
    for i in range(8,505,5):
        if candi[i] == None:
            jumlahBatu += 0
        else:
            jumlahBatu += int(candi[i])
    return jumlahBatu

# fungsi hitung total air yang dipakai
def banyakAir(candi):
    jumlahAir = 0
    for i in range(9,505,5):
        if candi[i] == None:
            jumlahAir += 0
        else:
            jumlahAir += int(candi[i])
    return jumlahAir

# fungsi cari harga candi
def rpHargaCandi(pasir,batu,air):
    hasil = 10000*int(pasir) + 15000*int(batu) + 7500*int(air)
    return str(hasil)

# fungsi harga candi ter(mahal/murah)
def hargaCandiTer(candi):
    if banyakCandi(candi) == 0:
        idMahal = "-"
        idMurah = "-"
    else:
        hargaArr = [None for i in range(100)]
        mahal = 0; murah = 9999999999999999
        
        panjang = 0
        for i in range(5,505,5):
            if candi[i] == None:
                panjang += 0
            else:
                hargaArr[panjang] = rpHargaCandi(candi[i+2],candi[i+3],candi[i+4])
                panjang += 1
        
        for i in range(panjang):
            if int(hargaArr[i]) <= murah:
                murah = int(hargaArr[i])
            if int(hargaArr[i]) >= mahal:
                mahal = int(hargaArr[i])
        
        for i in range(5,505,5):
            if candi[i] != None:
                harga = rpHargaCandi(candi[i+2],candi[i+3],candi[i+4])
                if mahal == int(harga):
                    idMahal = (f"{str((i-5)//5)} (Rp {mahal})")
                if murah == int(harga):
                    idMurah = (f"{str((i-5)//5)} (Rp {murah})")
    
    return (idMahal,idMurah)


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


def isAdaElmt(bahan):
    # cek di array bahan
    for i in range(0,15,3):
        if "pasir" == bahan[i]:
            return True
    return False

def createElmt(bahan):
    # mengisi array bahan dalam keadaan default
    bahan[3] = "pasir" ; bahan[4]  = "bahan pemadat" ; bahan[5]  = "0"
    bahan[6] = "batu"  ; bahan[7]  = "bahan pondasi" ; bahan[8]  = "0"
    bahan[9] = "air"   ; bahan[10] = "bahan perekat" ; bahan[11] = "0"
    return bahan    

def assignBahan(bahan,n1,n2,n3):
    # loop
    for i in range(0,15,3):
        if "pasir" == bahan[i]:
            temp = int(bahan[i+2]) + n1
            bahan[i+2] = str(temp) # diganti ke elemen pengganti
        elif "batu" == bahan[i]:
            temp = int(bahan[i+2]) + n2
            bahan[i+2] = str(temp) # diganti ke elemen pengganti
        elif "air" == bahan[i]:
            temp = int(bahan[i+2]) + n3
            bahan[i+2] = str(temp) # diganti ke elemen pengganti
    
    return bahan

def jinBatchKumpul(banyak,bahan):
    # UI awal
    print(f"Mengerahkan {banyak} jin untuk mengumpulkan bahan.")    
    # inisialisasi banyak bahan
    nPasir = 0; nBatu = 0; nAir = 0
    
    # looping sebanyak banyak jin
    for i in range(banyak):
        # mencummon random bahan-bahan
        nPasir += random.randint(0,5)
        nBatu  += random.randint(0,5)
        nAir   += random.randint(0,5)
    
    # mencreate nama bahan bila array masih belum ada
    if isAdaElmt(bahan) == False:
        bahan = createElmt(bahan)
    
    # assign ke array bahan
    print(f"Jin menemukan total {nPasir} pasir, {nBatu} batu, dan {nAir} air.\n")
    bahan = assignBahan(bahan,nPasir,nBatu,nAir)
    
    # mengembalikan array bahan
    return bahan

def banyakCandi(candi):
    count = 0
    for i in range(5,505,5):
        if candi[i] == None:
            count += 0
        else:
            count += 1
    return count

def assignCandi(candi,user,n1,n2,n3):
    for i in range(5,505,5):
        if candi[i] == None:
            candi[i]   = str(i//5 - 1)
            candi[i+1] = user
            candi[i+2] = str(n1)
            candi[i+3] = str(n2)
            candi[i+4] = str(n3)
            return candi

def ambilBahan(bahan,n1,n2,n3):
    # ambil data bahan bangunan dari bahan.csv
    nPasir = int(bahan[5]) - n1
    nBatu  = int(bahan[8]) - n2
    nAir   = int(bahan[11]) - n3

    # assign ke array bahan    
    bahan[5]  = str(nPasir)
    bahan[8]  = str(nBatu)
    bahan[11] = str(nAir)
    
    # kembalikan array
    return bahan

def isMungkinBangun(bahan,n1,n2,n3):
    nPasir = int(bahan[5])
    nBatu  = int(bahan[8])
    nAir   = int(bahan[11])

    # kondisi agar memungkinkan candi dibangun
    if nPasir < n1 or nBatu < n2 or nAir < n3:
        return False
    else:
        return True

def laporanGagalBangun(bahan,n1,n2,n3):
    nPasir = n1 - int(bahan[5])
    nBatu  = n2 - int(bahan[8])
    nAir   = n3 - int(bahan[11])
    
    if nPasir < 0:  nPasir = 0
    if nBatu  < 0:  nBatu  = 0
    if nAir   < 0:  nAir   = 0
    
    # mengembalikan hasil bahan
    return (nPasir,nBatu,nAir)    
    
def pembangun(banyak,user):
    # inisialisasi array
    jinPembangun  = ["" for i in range(banyak)]
    nPembangun = 0
    
    # assign username jin_pembangun ke dalam array pembangun
    for i in range(5,360,3):
        if user[i] == "jin_pembangun":
            jinPembangun[nPembangun] = user[i-2]
            nPembangun += 1
    
    # mengembalikan array
    return jinPembangun            

def jinBatchBangun(banyak,bahan,candi,user):
    # inisialisasi banyak bahan
    nPasirArr = [0 for i in range(banyak)]
    nBatuArr = [0 for i in range(banyak)]
    nAirArr = [0 for i in range(banyak)]
    nPasir = 0; nBatu = 0; nAir = 0
    Pembangun = pembangun(banyak,user)
    
    # looping sebanyak banyak jin n cek apkh hasil random 0 semua
    for i in range(banyak):
        pasir = random.randint(1,5)  ; nPasir += pasir ; nPasirArr[i] = pasir
        batu  = random.randint(1,5)  ; nBatu  += batu  ; nBatuArr[i]  = batu
        air   = random.randint(1,5)  ; nAir   += air   ; nAirArr[i]   = air
    
    # mencreate nama bahan bila array masih belum ada
    if isAdaElmt(bahan) == False:
        bahan = createElmt(bahan)
    
    # UI awal
    print(f"Mengerahkan {banyak} jin untuk membangun candi dengan total bahan {nPasir} pasir, {nBatu} batu, dan {nAir} air.")
    
    # mengecek kemungkinan dapat membagun candi
    if isMungkinBangun(bahan,nPasir,nBatu,nAir): # cek apakah jumlah bahan cukup
        
        if banyak + banyakCandi(candi) <= 100: # perlu ditanyakan
            for i in range(banyak):
                candi = assignCandi(candi,Pembangun[i],nPasirArr[i],nBatuArr[i],nAirArr[i])
                bahan = ambilBahan(bahan,nPasirArr[i],nBatuArr[i],nAirArr[i])            
            print(f"Jin berhasil membangun total {banyak} candi.\n")

            return (bahan,candi)

        else: # apakah
            for i in range(banyak):
                if i + banyakCandi(candi) <= 100:
                    bahan = ambilBahan(bahan,nPasirArr[i],nBatuArr[i],nAirArr[i])
                    candi = assignCandi(candi,Pembangun[i],nPasirArr[i],nBatuArr[i],nAirArr[i])
                else: # i + banyakCandi(candi) > 100
                    bahan = ambilBahan(bahan,nPasirArr[i],nBatuArr[i],nAirArr[i])
                    
            print(f"Jin berhasil membangun total {banyak} candi.\n")

            return (bahan,candi)
    else:
        laporanBahan = laporanGagalBangun(bahan,nPasir,nBatu,nAir)
        print(f"Bangun gagal. Kurang {laporanBahan[0]} pasir, {laporanBahan[1]} batu, dan {laporanBahan[2]} air.\n")    
        
        return (bahan,candi)

def isAdaJin(data_user):
    #menentukan apakah jin ada pada array data_user
    jumlah_jin = hitungJin("jin_pengumpul",data_user) + hitungJin("jin_pembangun",data_user)
    if (jumlah_jin == 0):
        return False
    else: #jumlah_jin > 0
        return True
    
def boleh_summon(data_user):
    jumlah_jin = hitungJin("jin_pengumpul",data_user) + hitungJin("jin_pembangun",data_user)
    if (jumlah_jin < 100):
        return True
    else:
        return False

# konverter bahan_bangunan.csv menjadi array
def bahan(data): # data adalah sebuah string
    arrBahan = [None for i in range(15)]
    tempStr = ""
    count = 0
    for i in range(len(data)):
        if data[i] == ";" or data[i] == "\n":
            arrBahan[count] = tempStr 
            tempStr = ""     
            count += 1
        else:
            tempStr += data[i]
    
    # print(arrBahan)
    # ['nama','deskripsi','jumlah',None,None, ...]
    return arrBahan

# konverter candi.csv menjadi array
def candi(data): # data adalah sebuah string
    arrCandi = [None for i in range(505)]
    tempStr = ""
    count = 0
    for i in range(len(data)):
        if data[i] == ";" or data[i] == "\n":
            arrCandi[count] = tempStr 
            tempStr = ""     
            count += 1
        else:
            tempStr += data[i]

    # print(arrCandi)
    # ['id','pembuat','pasir','batu','pasir',None,None, ... ]
    return arrCandi

# koverter user.csv menjadi array
def user(data): # data adalah sebuah string
    arrUser = [None for i in range(360)]
    tempStr = ""
    count = 0
    for i in range(len(data)):
        if data[i] == ";" or data[i] == "\n":
            arrUser[count] = tempStr 
            tempStr = ""     
            count += 1
        else:
            tempStr += data[i]
    
    # print(arrUser)
    # ['username','password','role','Bondowoso','cintaroro','bandung_bondowoso', ...]
    return arrUser

def konvert(readCandi,readUser,readBahan):
    # di read
    Candi   = readCandi.read()
    User    = readUser.read()
    Bahan   = readBahan.read()
    
    # di konversi
    arrBahan = bahan(Bahan)
    arrCandi = candi(Candi)
    arrUser  = user(User)
    
    return (arrBahan,arrCandi,arrUser)
