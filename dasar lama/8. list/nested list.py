# nested list (list dalam list)
data0 = [1,2]
data1 = [3,4]

data = [1,2,3,4,1,3,1]
print(f"data list biasah = {data}")

data_nested = [data0, data1, "bejo", 1]
print(f"data nested = {data_nested}")
data_nested[0] = "tets"
print(f"data nested baru {data_nested}")


# contoh penggunaan

peserta1 = ["bejo", 12, "laki-laki"]
peserta2 = ["asep", 7, "laki-laki"]
peserta3 = ["dedeh", 10, "wanita"]
nama_peserta = [peserta1, peserta2, peserta3]
print(f"daftar peserta : \n{nama_peserta}\n\n")

for peserta in nama_peserta:
    print(f"nama  \t: {peserta[0]}")
    print(f"umur  \t: {peserta[1]}")
    print(f"gender \t: {peserta[2]}\n")
    

## kelemahan nested list

list_copy = nama_peserta.copy()
print(f"list copy = {list_copy}\n")
peserta1[0]= "jawir"
print(f"nama pererta = {nama_peserta}")
print(f"list copy = {list_copy}")
# list pertama dan copy ikut berubah