from numbers import Number as nb
'''
exception akan terjadi saat progam mengalami eror saat runtime
'''

# contoh sederhana untuk menangkap exception
'''
input_user = int(input("masukan angka : "))
hasil = 0

try:
    hasil = 10/input_user
except:
    print("input tidak boleh 0")
    
print(hasil)
'''

# contoh aplikasi 1
while(True):
    angka = int(input("masukan angka pembagi : "))
    try:
        hasil = 10/angka
        print(hasil)
        done = input("mau ulang lagi (y/n)? : ")
        if done == "n":
            break
    except :
        print("angka pembagi tidak boleh 0 ")

print("akhir progam 1")

# pengaplikasian kedua
'''
progam akan membaca isi dari file data.txt, jika file data.txt belum ada maka progam membuat sendiri
'''
while (True):
    try:
        with open("d:/belajar bahasa progam/belajar_python/dasar/22. exception, try and except/data.txt",'r+') as file:
            print(file.read())
        break
    except:
        print("file tidak di temukan, membuat file baru")
        with open("d:/belajar bahasa progam/belajar_python/dasar/22. exception, try and except/data.txt",'a',encoding="utf-8") as file:
            file.write("")
        break
    
print("akhir progam 2")

# membuat exceptyion sendiri
def tambah (a,b):
    if not isinstance(a,nb) or not isinstance(b,nb):
        raise "input harus angka" # ini akan di tampilkan
    return a+b

print(tambah(2,3))

# menggunakan zerodivisioneror
angka = 0
try:
    hasil = 10/angka
except ZeroDivisionError as eror:
    print(eror)