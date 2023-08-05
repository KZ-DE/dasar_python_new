''' 
penggunaan emurated pada data list di gunakan untuk menampilkan isi data tersebut beserta indexnya.
jadi kita akan tahu urutan isi pada data tersebut.

contoh:
'''
nama_mahasiswa = ['dudung', 'mamang', 'bejo']

for a, b in enumerate(nama_mahasiswa):
    print(f'index = {a}, isi data = {b} \n')
