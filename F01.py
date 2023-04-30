# F01 - login

def login(user):
    name = input("Username : ")
    pwrd = input("Password : ")
    print()
    
    cond = 0
    ind = 2
    
    for i in range(0,360,3):
        if name == user[i]:
            cond = 1
            if pwrd == user[i+1]:
                cond = 2
                ind = i+1
                
    if ind == 2:
        role = 0
    else:
        if user[ind+1] == "bandung_bondowoso":
            role = 1
        elif user[ind+1] == "roro_jonggrang":
            role = 2
        elif user[ind+1] == "jin_pengumpul":
            role = 3
        elif user[ind+1] == "jin_pembangun":
            role = 4
    
    if cond == 0:
        print("Username tidak terdaftar!\n") 
        return (False,role,None)
    elif cond == 1:
        print("Password salah!\n")
        return (False,role,None)
    elif cond == 2:
        print(f"Selamat datang, {name}!")
        print('Masukkan command "help" untuk daftar command yang dapat kamu panggil\n')
        return (True,role,name)

def loginLagi(username):
    print("Login gagal!")
    print(f'Anda telah login dengan username {username}, silahkan lakukan "logout" sebelum melakukan login kembali.\n')