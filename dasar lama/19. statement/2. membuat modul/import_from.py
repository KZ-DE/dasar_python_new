# di dalam modul biasahnya membuat tool fungsi
from matematika import tambah,kali # mengambil method satu persatu
# untuk menggunakanya setiap method harus di improt dulu melalu from
'''
bisa menggunakan template di atas atau seperti ini:
from matematika import tambah
from matematika import kali
'''
# juga bisa mengimport semuanya dengan cara:
from matematika import *


'''
jika tidak menggunakan from maka penulisannya seperti ini
print(matematika.tambah(3,4))
'''
# berubah seprti ini:
print(tambah(2,3)) # tidak perlu ada (matematika.)
# hanya menggunakan methodnya saja
print(kali(5,5))
print(kurang(10,5))
print(bagi(10,5))