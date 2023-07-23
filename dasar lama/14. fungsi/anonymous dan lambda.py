# lambda fungsi

# fungsi biaah
def fkuadrat(angka):
    return angka**2
print(f"hasil fungsi biasa = {fkuadrat(2)}")

# fungsi lambda
'''
cara penulisan 
output = lamda argument : isi

contoh :
'''
kuadrat = lambda angka:angka**2
print(f"hasil dengan lambda = {kuadrat(2 )}") 
# fungsinya membuat fungsi yang hanya berisi 1 baris menjadi lebih simpel

# contoh lainnya

# filter angka di bawah 5
list_angka = [1,2,3,4,5,6,7,8,9]
list_kurangdari5 =list(filter(lambda x:x<=5,list_angka))
# artinya buat list dari fiter x yang bernilai kurang dari sama dengan 5 dari list yang adaa di variabel list angka
print(list_kurangdari5)

# filter angka genap
list_genap = list(filter(lambda x:(x%2==0),list_angka))
print(list_genap)

# filtr angka ganjil
list_ganjil = list(filter(lambda x : (x%2==1),list_angka))
print(list_ganjil)

# filter kelipatan 3
list3 = list(filter(lambda x : (x%3==0), list_angka))
print(list3)




# anonymous fungsi
''''
contoh penulisan
def fungsi(argumen):
    return lambda argumen2 : argumen2 --|isi sesuai kebutihan|-- argumen1
'''
# contoh fungsi biasah
def pangkat (angka,n):
    hasil = angka**n
    return hasil
a=pangkat(5,2)
print(a)

# contoh dengan fingsi anonymous
def pangkat (n):
    return lambda angka : angka**n
pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")# artinya pangkat 2 dari 5
pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(2)(6)}") # artinya pangkat 2 dari angka 6