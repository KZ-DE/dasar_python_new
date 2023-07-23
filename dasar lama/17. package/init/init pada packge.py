# init adalah suatu file yang ada di package


import pack


print(pack.mtk.tambah(2))

print(pack.kali(2,2))
# jika tampa adanya init maka ini akan eror
# sedangkan jika modul sudah di import ke init terlebih dahulu tidak akan eror

# print(pack.fisika.gaya(3,3)) # yang ini akan eror karena tidak melakukan import ke init terlebih dahulu