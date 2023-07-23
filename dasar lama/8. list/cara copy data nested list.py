# copy data nested list

data0 = [1,2]
data1 = [3,4]

data_nested = [data0, data1]
print(f"data nested = {data_nested}")
data_copy = data_nested.copy()
print(f"data copy ={data_copy}\n\n")

# addres utama
print(f"adres data nested = {hex(id(data_nested))}")
print(f"adres data copy = {hex(id(data_copy))}\n\n")
# sudah beda

# addres baris pertama
print(f"adres data nested = {hex(id(data_nested[0]))}")
print(f"adres data copy = {hex(id(data_copy[0]))}\n\n")
# namu addres tiap list awal masih sama




### cara mengambil data di dalam nested list

# cara penulisan
# data = data_nested[urutan dalam nested list][urutan dalam list awal]
data = data_nested[0][0]
print(f"data di ambil = {data}")


### cara mengkopy data nested list namu menggunakan libary dulu
from copy import deepcopy
data_deepcopy =deepcopy(data_nested)
# addres utama
print(f"adres data nested = {hex(id(data_nested))}")
print(f"adres data copy = {hex(id(data_copy))}")
print(f"adres data deepcopy = {hex(id(data_deepcopy))}\n\n")
# sudah beda

# addres baris pertama
print(f"adres data di dalam list nested = {hex(id(data_nested[0]))}")
print(f"adres data di dalam list copy = {hex(id(data_copy[0]))}")
print(f"adres data di dalam list deepcopy = {hex(id(data_deepcopy[0]))}\n\n")
# addres tiap list awal sudah beda