# copy dict

nama = {
    'jo' : "bejo",
    'sd' : "sudrun",
    'sl' : "slamet",
    'pj' : "paijo"
}
teman2 = nama.copy()
print(nama)
print(teman2)
print()

teman2['jo'] = "seijo"
print(nama)
print(teman2)
print("\n\n")

# pop dict
data_sudrun = teman2.pop('sd') # mengambil data berdaarkan key
# dampaknya datanya sudah tidak ada di dict
print(f"data sududrun = {data_sudrun}") 
print(teman2)

# popitem
data_jo = teman2.popitem() # akan mengambil data terakhir
print(f"data jo = {data_jo}\n")
print(teman2)