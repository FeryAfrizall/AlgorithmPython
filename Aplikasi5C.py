# -*- coding: utf-8 -*-
"""

@author: hp
"""

jwb = "y"

while jwb=="y":
    print("------------------")
    print("Cek Nilai Angka")
    print("------------------")
    n = input("Masukkan Nilai = ")
    na = int(n)
    if na>80:
        status = "Baik Sekali"
    elif na>=65:
        status = "Baik"
    elif na>=55:
        status = "Cukup"
    elif na>=40:
        status = "Kurang"
    else:
        status="Kurang Sekali"
    print (status)
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t":
        break