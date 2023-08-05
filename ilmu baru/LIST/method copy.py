'''
penggunaan copy di list di gunakan untuk mennambah list baru dengan isi yang sama
method copy ini tidak mempunyai parameter
contoh :
'''
# mempunyai data pertama
data_a = [1, 2, 3]
print(f"data A = {data_a} \n")

# lalu kita membuat copy dari data pertama
data_b = data_a.copy()
print(f"data B = {data_b} \n")


# melihat addres yang di gunakan oleh data tersebut
print(f"addres data A = {id(data_a)} \n")
print(f"addres data B = {id(data_b)} \n")

'''
pada kedua data tersebut, addres yang di gunakan sudah berbeda
'''

# melihat addres pada index dari data tersebut
print(f"addres index 0 data A = {data_a[0]} \n")
print(f"addres index 0 data B = {data_b[0]} \n")

print(f"addres index 1 data A = {data_a[1]} \n")
print(f"addres index 1 data B = {data_b[1]} \n")

'''
walaupun addres data tersebut sudah berbeda, namun addres index dari isi dari data tersebut masih sama
'''
# coba kita ganti isi dari data list tersebut
data_a[0] = 8
data_b[0] = 9

# kita lihat isi dari masing masing data tersebut beserta addres yang di gunakan
print(f"isi data A baru = {data_a} \n")
print(f"isi data B baru = {data_b} \n")

print(f"addres index 0 data A baru = {id(data_a[0])} \n")
print(f"addres index 0 data A baru = {id(data_b[0])} \n")

'''
setelah data dari index di rubah pada setiap data, addres dari index yang di ganti telah berubah
sehingga jika kita rubah data index A tidak akan mengubah data index B karena tidak saling terkait.

penggunaan method copy untuk data LISt membuat copy-an data baru yang tidak saling terkait oleh addres satu sama lain,
inilah kelebihan method copy dari pada menduplikat data list yang ada.
'''
