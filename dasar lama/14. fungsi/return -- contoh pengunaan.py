### penggunaan retrun

# cara 1
def luas_persegi_panjang(panjang, lebar):                           
    hasil = panjang * lebar
    return hasil

luas = luas_persegi_panjang(2, 4)
print(luas)


# cara 2
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

print("Luas Perseg Panjang",luas_persegi_panjang(2, 2))