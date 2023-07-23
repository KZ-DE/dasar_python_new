## tutorial membaca file external

# macam macam mode
'''
mode="r" --> membaca yang ada di dalam file
cara membacanya --> print(namaFile.read())
untuk mengecek bisa di baca atau tidak --> print(namaFile.readable)

mode="w" --> menulis yang ada di dalam file
cara membacanya --> print(namaFile.write())
untuk mengecek bisa di tulis atau tidak --> print(namaFile.writable)
'''

print(3*"=", " membaca file txt ", 3*'=', "\n")

### mendeklarasikan file tersebut untuk mengakses file (read)

file = open("d:/belajar bahasa progam/belajar_python/dasar/21. read external file/data.txt",mode="r")

## untuk melihat apakah file tersebut bisa di baca atau tidak
# jika file tersebut belum di deklarasi untuk bisa di akses maka tidak akan bisa di baca
print(f"status file = {file.readable()}")

### untuk membaca isi teks

# untuk membaca semua isi
# print(file.read())

# untuk membaca baris per baris
# print(file.readline(), end="") # baca baris pertama
# print(file.readline(), end="") # baca baris kedua
# end="" --> berguna untuk menghilankan \n yang ada di isi file teks tersebut

# untuk membaca semua baris sebagai list
print(file.readlines())



### mendeklarasikan file tersebut untuk mengakses file (read)

# file = open("d:/belajar bahasa progam/belajar_python/dasar/21. read external file/data.txt",mode="w")
''' jika di aktifkan isi dari file akan di reset menjadi kosong karena mau di tulis'''


## untuk melihat apakah file tersebut bisa di tulis atau tidak

# print(f"status file = {file.writable()}")

### untuk membaca isi teks

# print(file.write()) 



### setelah file di open untuk mengakses maka harus di tutup juga

# untuk mengecek apakah file sudah di tutup atau belum
print(f"apakah file sudah di tutup = {file.closed}")

# untuk menutupnya dengan cara
file.close()

# kita cek kembali
print(f"apakah file sudah di tutup = {file.closed}")


### membuka file di python dengan with
print("\n",3*"=", " membaca file txt dengan with ", 3*'=', "\n")

with open("d:/belajar bahasa progam/belajar_python/dasar/21. read external file/data.txt", mode="r") as file:
    isi = file.readline()
    print(isi,end="")


''' keuntungan dengan menggunakan metode ini adalah kita tidak perlu menutup isi file karena akan menutup otomati ketika kita keluar dari progam with (progam selesai di eksekusi) '''

