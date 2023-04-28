# F16 - exit
from F14 import * # import command untuk menjalankan save
    
def exitNotLogin():
    isInputSalah = True
    while isInputSalah:
        # UI tampilan command
        varExit = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        
        # kondisi cek apakah save terlebih dahulu 
        if varExit == "y" or varExit == "n" or varExit == "Y" or varExit == "N":
            isInputSalah = False
            return False
        else:
            isInputSalah = True

def exitLogin():
    isInputSalah = True
    while isInputSalah:
        # UI tampilan command
        varExit = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        
        # kondisi cek apakah save terlebih dahulu 
        if varExit == "y" or varExit == "n" or varExit == "Y" or varExit == "N":
            isInputSalah = False
            return False,False
        else:
            isInputSalah = True