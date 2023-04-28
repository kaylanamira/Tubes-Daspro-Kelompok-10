# F14 - Save
import os

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
        if candi[i] != None and i != 359:
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
        if bahan[i] != None and i != 359:
            if i%3 == 2:
                tempStr += bahan[i]
                tempStr += "\n"
            else:
                tempStr += bahan[i]
                tempStr += ";"
    
    return tempStr

def save(user,candi,bahan):
    # inisiasi input awal
    folderName = input("\nMasukkan nama folder: ")
    print("\nSaving...")
    
    if os.path.exists("save") == False:
        os.mkdir("save")
    
    if os.path.exists(os.path.join("save", folderName)) == False:
        os.mkdir(os.path.join("save", folderName))
        # memberitahu user bahwa folder save sudah dibuat
        print(f"\nMembuat folder save/{folderName}...")

    # assign ke file csv
    # user.csv 
    csvUser = os.path.join("save", folderName, "user.csv")
    
    file = open(csvUser, "w")
    file.write(strUser(user)) # karena inputnya array
    file.close()

    # candi.csv
    csvCandi = os.path.join("save", folderName, "candi.csv")
    
    file = open(csvCandi, "w")
    file.write(strCandi(candi))
    file.close()
    
    # bahan_bangunan.csv
    csvBahan = os.path.join("save", folderName, "bahan_bangunan.csv")
    
    file = open(csvBahan, "w")
    file.write(strBahan(bahan))
    file.close()
    
    # notif bila proses telah berhasil
    print(f"Berhasil menyimpan data di folder save/{folderName}!")
    