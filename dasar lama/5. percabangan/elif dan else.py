# if dan else

# cara penulisan
# if kondisi(boolean): aksi

# persamaan: a == b
# Npertidaksamaan: a != b
# kurang dari: a < b
# kurangdari samadengan: a <= b
# lebih dari: a > b
# lebih dari samadengan: a >= b

nama = input("Silahkan Masukan Nama Anda :")
print(f"hallo {nama}")

# if inline
if nama == "taufik": print(f'hallo tuan bos')
else: print(f'maaf anda "{nama}" bukan admin\nsilahkan logout\n')
    
# if indentation
# akan melakukan aksi selama codingan kita keluar ke kanan dari lurus if
# contohnya seperti berikut
if nama != 'taufik' :
    print('Daftarkan diri anda dahulu')
    print('lalu login kembali')
else :
    print("belajar python")
print('terimaksi')