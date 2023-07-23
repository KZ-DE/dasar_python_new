 # manipulasi list

# index 0(-3)   1(-2)  2(-1)
data =["bejo",10,"mancing"]

# mengambil data dari list
nama = (f"nama = {data[0]}")
print(nama)
kelas = (f"kelas = {data [-2]}")
print(kelas)
hobi = (f"hobi = {data [-1]}")
print(hobi)

# melihat jumblah data dalam list
panjang_data = len(data)
print((f"panjang data = {panjang_data}"))



### manipulasi list

# menambahkan item pada list sesuai posisi
# cara penulisa ---> data.insert(posisi, item)
data.insert(1,12)
print(f"data sesudah di tambah = \n{data}")

# menambahkan item pada list di posisi akhir
data.append("SDN2")
print(f"data yang baru = \n{data}")

# menambahkan list dengan list
data_baru = ["bogor", 2002]
data.extend(data_baru)
print(f"data terbaru = {data}")

# merubah data
data[0] = "sudrun"
print(data)

# menghapus data
data.remove("sudrun") #tidak bisa menggunakan index
print(data)

# menghapus data paling belakang
data.pop()
print(data)

# menampilkan data terakhir
data_akhir = data.pop()
print(data_akhir)