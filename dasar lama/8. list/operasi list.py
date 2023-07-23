# operasi list
BaseException

data_angka = [1,4,6,3,7,9,4,7,0,4,7,3,0,3,4,6,3,5,2,7,9,2,3,4,5,7,3,6,3]
print(f"banyak data = {data_angka}\n")

# mengetahui jumlah idex dalam list
lenght = len(data_angka)
print(f"{lenght}\n")

# menghitung banyaknya item dalam list
data4 = data_angka.count(4)
data9 = data_angka.count(9)
print(f"banyaknya angka 4 = {data4}\n")
print(f"banyaknya angka 9 = {data9}\n")

# mengetahu posisi data(index)
data = ["sudrun","bejo","slamet","ahri"]
print(f"data nama = {data}\n")
index_bejo = data.index("bejo")
print(f"index bejo = {index_bejo}\n")

# mengurutkan data
print(f"data angka = {data_angka}")
data_angka.sort()
print(f"data angka terurut = {data_angka}\n") # di urutukan terhadap angka terkecil terlebih dahulu
print(data)
data.sort()
print(f"data terurut = {data}\n") # akan menampilkan sesuai aljabar huruf depannya

# membalik urutan data list
data_angka.reverse()
print(f"data terurut terbesar = \n{data_angka}")