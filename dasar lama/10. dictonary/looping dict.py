# looping dict

nama = {
    'bj' : "bejo",
    'kz' : "king z",
    'sl' : "slamet",
    'sd' : 'sudrun'
}

# looping menggunakan foor
# maka yang keluar hanya keynya
for knama in nama:
    print(knama)
    
# operator untuk mengambil interables
keys = nama.keys() # menampil ka keynya saja
print(keys)

for key in nama.keys(): # akan keluar hanya key nya saja
    print(key)
print()
# sedangkan untuk menampilkan valuenya maka harus menambahka get
for key in nama:
    print(nama.get(key))
print()

# untuk melihat kumpulan value maka menggunakan .value
values = nama.values()
print(values)

# bisa juga menggunaka for 
for value in nama.values():
    print(value)
    
# mengambil data dict menggunakan item
# maka akan menampilkan key berserta valuenya
items = nama.items()
print(items)
print()
# sedangkan berbedaannya dengan cara biasah adalah sebagai berikut
print(f"menggunakan cara biasa = {nama}")

# bisa juga di gabungkan denga for
for i in nama.items():
    print(i)
    
# jika di pisah maka seperti ini
for key,item in nama.items():
    print(f"key = {key}\tvallue = {item}")