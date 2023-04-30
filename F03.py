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
        print(" (2) Pembangun - Bertugas membangun candi\n")
        
        while (status_summon):
            jenis = int(input("Masukkan nomor jenis jin yang ingin dipanggil : "))
            if (jenis != 1) and (jenis != 2):
                print("\nTidak ada jenis jin bernomor \""+ str(jenis) + "\" !"+"\n")

            else:
                if jenis == 1:
                    role = "jin_pengumpul"
                    print("\nMemilih jin \"Pengumpul\".\n")
                elif jenis == 2:
                    role = "jin_pembangun"
                    print("\nMemilih jin \"Pembangun\".\n")

                uname_jin = input("Masukkan username jin : ")
                while adaUsername(uname_jin,data_user):
                    print("\nUsername \""+ uname_jin +"\" sudah diambil!\n")
                    uname_jin = input("Masukkan username jin: ")   

                password_jin = input("Masukkan password jin : ")  
                while len(password_jin)<5 or len(password_jin)>25:
                    print("\nPassword panjangnya harus 5-25 karakter!\n")
                    password_jin = input("Masukkan password jin: ")  
                
                #Update data_useray data_user
                for i in range(0,360,3):
                    if data_user[i] == None:
                        data_user[i] = uname_jin
                        data_user[i+1] = password_jin
                        data_user[i+2] = role
                        break
                #UI
                print("\nMengumpulkan sesajen...")
                print("Menyerahkan sesajen...")
                print("Membacakan mantra...\n")
                print(f"Jin {uname_jin} berhasil dipanggil!")

                pilihan = input("\nApakah ingin summon lagi? (Y/N)")
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

def summonNotBandung():
    print("summonjin hanya dapat dilakukan oleh Bandung Bondowoso.")