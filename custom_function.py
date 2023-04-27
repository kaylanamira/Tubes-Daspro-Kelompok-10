#Berisi fungsi-fungsi custom 

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