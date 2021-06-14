# -*- coding: utf-8 -*-
"""

@author: hp
"""

jwb = "y"

while jwb=="y":
    print("------------------")
    print("CEK KELULUSAN")
    print("------------------")
    n = input("Masukkan Nilai = ")
    if int(n)>60:
        status = "Lulus"
    else:
        status="Ulang"
    print (status)
    jwb = input(">> Mau mengulangi ? y/t = ")
    if jwb=="t":
        break