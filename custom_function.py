
def adaUsername(uname,arr):
    #cek apakah uname terdaftar
    #uname nantinya berupa input
    i = 0
    ada = False
    while i<360 and ada == False:
        if arr[i] == uname:
            ada = True
        i += 3
    return ada

#UBAH LEN(ARR) DI SINI!
def get_index(element,arr):
    for i in range(len(arr)):
        if arr[i] == element:
            index = i
    return index

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

def hitungJin(role,data_user):
    count = 0
    for i in range(360):
        if data_user[i] == role :
            count += 1
    return count

#HANYA UTK TEST DI PROGRAM INI
#ASLINYA DILETAKKAN DI MAIN.PY