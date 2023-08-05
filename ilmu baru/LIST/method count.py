'''
mencari jumlah yang akan di cari dalam sebuah data list

contoh :
'''


def x(arrayOfSheeps):
    # isi dari parameter merupakan data yang akan di cari jumlahnya.
    return arrayOfSheeps.count(1)


data_angka = [1, 2, 1, 3, 4, 5, 1, 2, 3, 1, 3, 4, 5, 7, 8, 4, 2, 1, 3, 4, 1]

print(f"jumlah isi dari angka 1 dari data list tersebut = {x(data_angka)} \n")

# bisa juga dengan tidak menggunakan fungsi
print(
    f"jumlah isi dari angka 1 dari data list tersebut = {data_angka.count(1)}")

'''
akan menghasilkan angka 6 karena jumlah data dengan angka 1 ada 6 buah.
'''
