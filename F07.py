# F07 - Jin Pengumpul
from custom_function import *
import random

def jinKumpul(bahan):
    # mensummon random bahan-bahan
    nPasir = random.randint(0,5)
    nBatu  = random.randint(0,5)
    nAir   = random.randint(0,5)
    
    # mencreate nama bahan bila array masih belum ada
    if isAdaElmt(bahan) == False:
        bahan = createElmt(bahan)
    
    # assign ke array bahan
    print(f"Jin menemukan {nPasir} pasir, {nBatu} batu, dan {nAir} air.\n")
    bahan = assignBahan(bahan,nPasir,nBatu,nAir)
    
    # mengembalikan array bahan
    return bahan
