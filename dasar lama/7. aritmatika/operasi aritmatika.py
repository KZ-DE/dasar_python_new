# operasi aritmatika

from tkinter import Y


a = 4
b = 3

# operasi pertambahan +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

#  operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus (sisa dari pembagian) %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floar division(pembulatan hasil pembagian) //
hasil = a // b
print(a,'//',b,'=',hasil)


#  prioritas operasi
# ()
# perkalian dan pembagian
# pertambahan dan pengurangan

# contoh
x=3
y=5
z=9

hasil= x / y + z * x // y ** x % z - y
print(hasil)