# manipulasi string

nama_depan = 'Mongkay '
nam_tengah = 'D '
nama_akhir = 'Lutfy '
nama_lengkap = nama_depan + nam_tengah + nama_akhir
print(nama_lengkap)

# menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)


# operator untuk srtring

# 1. mengecek apakah huruf tertentu ada dalam string tersebut
D = 'D'
status = D in nama_lengkap
print(str(status))

D = 'D'
status = D not in nama_lengkap
print(str(status))

# 2. pengulangan string
print("wk"*10)
print(15*"wk")

# 3. indexing
print(nama_lengkap[5])
# urutan index ke 5 adalah huruf "a" karena index di mulai dari angka 0
print(nama_lengkap[-3])
print(nama_lengkap[0:7])

print(nama_lengkap[0:10:2])
# arti angka 2 tersebut adalah menloncati 2 huruf

# 4. item palig kecil
print(min(nama_lengkap))

# 5. item paling besar
print(max(nama_lengkap))

ascii = ord('y')
print(ascii)
ascii = ord('M')
print(ascii)

# 6. operasi dalam bentuk metod
print("\noperasi dalam method \n")

# 1 count
data = "alon alon asal kelakon"
jumblah = data.count("n")
print(str(jumblah))

# 2 upper
salam = "bro!"
salam = salam.upper()
print(salam)

# 3 lower
test = "aKu AkaN SukSeSSSssss"
print(test.lower())

# 4 isx
salam = 'apa'
a = salam.islower()
print(str(a))
b = salam.isupper()
print(str(b))

# isalpha() --> untuk mengecek apakah semua huruf
h1 = 'apakah 3431 itu haram?'
cekh1 = h1.isalpha()
print(h1 + ' ' + str(cekh1))

# isalnum() --> untuk megecek huruf dan angka
angka = "ahasf23442?"
cekangka = angka.isalnum()
print(angka + ' = ' + str(cekangka))

# isdecimal() --> untuk megecek angka aja
nomor = '088298392hjds'
ceknomor = nomor.isdecimal()
print(nomor + ' = ' + str(ceknomor))

# isspace() --> untuk megecek spasi, tab, newline /n
isi = 'apakah salam'
cekisi = isi.isspace()
print(isi + ' = ' + str(cekisi))

# istitle() --> untuk mengecek semua kata di mulai dengan berhurf besar
judul = 'It Is Okay'
cekjudul = judul.istitle()
print(judul + ' = ' + str(cekjudul))

# membuat panjang string
print(f"{'Hallo':10} {'apa kabar':20} bro")
