# import
# fungsinya untuk mngambil progam dari file extrenal

# 1. untuk enyambung progam dari external dan menjalankannya
import progam_print

# 2.import dengan data
import databejo
# variabel bejo ada di namespace nama folder
# print(bejo) ----> jika langsung gini tidak akan bisa
print(databejo.bejo) # --> harus seperti ini bila ingin mengambil variabelnya


# 3. import dengan fungsi
import mtk
print(mtk.tambah(2,3))