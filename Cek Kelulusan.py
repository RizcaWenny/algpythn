"""
RIZCA WENNY/20083000005/2A
11-06-2021
PROGRAM PERHITUNGAN NILAI TOTAL TRANSAKSI PEMBELIAN PRINTER
"""
#cek kelulusan, jika nilai > 60 maka status lulus
print ("==========================")
print (" CEK KELULUSAN ")
print ("==========================")
#setiap value yang diinputkan, secara default bertipe data STRING
n = input(">> Masukkan Nilai = ")
#cek nilai
if n>60:
    sts = "LULUS"
else:
    sts="ULANG"

print(sts)
