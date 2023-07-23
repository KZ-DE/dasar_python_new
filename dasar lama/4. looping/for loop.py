# for loop

# tampa loop
angka = 1
angka = angka + 1
angka = angka + 1
print(f"nilai angka dengan metode tanpa loop --> {angka}\n")

# dengan loop
for i in range(3):
    angka + 1    
print(f"nilai angka dengan metode loop --> {angka}\n")
# bisa di lihat hasilnya sama

# bisa dengan menggunakan variabel
pengali = 3
for i in range(pengali):
    angka + 1
print(f"nilai angka dengan metode loop menggunakan variabel --> {angka}\n")

# mengunakan rage
angka_range = range(1,4)
for i in angka_range:
    angka + 1
print(f"nilai angka dengan metode loop menggunakan range --> {angka}\n")
# angka 4 di angggkap batas 4(atau bisa di bilang <4)

# menggunakan string
data_string = "belajar python"
for i in data_string:
    print(f"loop dengan string --> {i}")
# akan mengeluarka kalimat per huruf(satu per satu)
