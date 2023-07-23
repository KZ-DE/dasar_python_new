# *args pada fungsi


# cara memasukan data di dalam fungsi dengan lebih simpel
def fungsi (*args): # args typenya tuppel dan bisa di looping
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama}, tinggi {tinggi}, berat {berat}")
fungsi("bejo", 120, 40)

# bagus di gunakan bila isi dari argumen banyak lebih dari 4
# dan juga bisa di ganti dengan nama lain
# contoh
def tambah (*data):
    output = 0
    for angka in data:
        output += angka
    return output
# efeknya adalah input di dalam kurung bisa berapapun
hasil = tambah(1,2,3,4,5,6,7,8,9)
print(hasil)
        
        