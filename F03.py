from custom_function import *

def boleh_summon(data_user):
    jumlah_jin = hitungJin("jin_pengumpul",data_user) + hitungJin("jin_pembangun",data_user)
    if (jumlah_jin < 100):
        return True
    else:
        return False

def summonjin(data_user):
    status_summon = boleh_summon(data_user)
    berhenti_summon = False
    if status_summon:
        print("Jenis jin yang dapat dipanggil: ")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi")
        print()
        
        while (status_summon):
            jenis = int(input("Masukkan nomor jenis jin yang ingin dipanggil : "))
            print()
            if (jenis != 1) and (jenis != 2):
                print("Tidak ada jenis jin bernomor \""+ str(jenis) + "\" !")
                print()

            else:
                if jenis == 1:
                    role = "jin_pengumpul"
                    print("Memilih jin \"Pengumpul\".")
                elif jenis == 2:
                    role = "jin_pembangun"
                    print("Memilih jin \"Pembangun\".")
                print()

                uname_jin = input("Masukkan username jin: ")
                while adaUsername(uname_jin,data_user):
                    print()
                    print("Username \""+ uname_jin +"\" sudah diambil!")
                    print()
                    uname_jin = input("Masukkan username jin: ")   

                password_jin = input("Masukkan password jin: ")  
                print() 
                while len(password_jin)<5 or len(password_jin)>25:
                    print("Password panjangnya harus 5-25 karakter!")
                    print()
                    password_jin = input("Masukkan password jin: ")  
                
                #Update data_useray data_user
                for i in range(0,360,3):
                    if data_user[i] == None:
                        data_user[i] = uname_jin
                        data_user[i+1] = password_jin
                        data_user[i+2] = role
                        break
                #UI
                print()
                print("Mengumpulkan sesajen...")
                print("Menyerahkan sesajen...")
                print("Membacakan mantra...")
                print()
                print(f"Jin {uname_jin} berhasil dipanggil!")

                pilihan = input("Apakah ingin summon lagi? (Y/N)")
                if pilihan == "N" or pilihan == "n" :
                    berhenti_summon = True
                    status_summon = False
                else:
                    status_summon = boleh_summon(data_user)
        else:
            if (not(status_summon) and not(berhenti_summon)):
                print("Jumlah Jin telah maksimal!. Bandung tidak dapat men-summon lebih dari itu.")
            else: #berhenti_summon == True
                print("Summon jin selesai!")
    else:
        print("Jumlah Jin telah maksimal!. Bandung tidak dapat men-summon lebih dari itu.")

    return data_user
