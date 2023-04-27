# convert csv

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