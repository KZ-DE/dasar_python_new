# package adalah sebuah progam yang berisi modul
import pack.mtk ## pack adalah nama folder dari file yang bernama mtk
# bisa juga pakai seperti ini
# 1
from pack import fisika

# 2
from pack.fisika import gaya
# fungsi paycache adalah membuat kerja modul lebih cepat
print(pack.mtk.tambah(2,2,3,4,4,5,5))
print(fisika.gaya(3,3))
print(gaya(5,5))