# untuk waktu
from datetime import datetime

data_waktu = datetime.now()
print(data_waktu)
print(f"tahun = {data_waktu.year}")
print(f"tahun = {data_waktu.strftime('%B')}")
print(f"tahun = {data_waktu.strftime('%A')}")

# kumpulan kumpulan data (aray, list, tuppel, dict)
from collections import Counter # untuk menghitung data

data = ["a","b","c","d","e","f","g","h","i","j"]

# cara biasa
hasil = 0
for i in data:
    if i == "a":
        hasil += 1

print(hasil)

# menggunakan modul
print(f"data counter = {Counter(data)}")
print(f"jumblah a = {Counter(data)['a']}")


# imput ouput file
import io

file = io.open("d:/belajar bahasa progam/belajar_python/dasar/libary/hello.txt","r") # nama file (lengkap dengan foldernya), "r" adalah read artinya membaca isi di dalam file
print(file.read()) # untuk menampilkan
