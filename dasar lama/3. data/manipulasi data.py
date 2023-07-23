# mani pulasi string

# 1. menyambung string
a = "mongkey "
b = "D'"
c = "lutfi"
nama_lengkap = a + b + c
print(nama_lengkap)

## format string

# nama
nama = 'sudrun'
format_str = f'hello {nama}'
print(format_str)

# boolean
bool = True
print(f'nilai bolean = {bool}')

# angka
angka = 2089.4
print(f'angka = {angka}')

# bilangan bulat
bb = 7
print(f'angka bilangan bulat = {bb:d}')

# bilangan ribuan
angka = 2000
print(f'angka ribuan = {angka:,}')
jutaan = 20000000
print(f'angka jutaan = {jutaan:,}')

# bilangan desimal
desimal = 2005.54321
print(f'angka desimal = {desimal:.2f}' )
print(f'angka desimal = {desimal:.3f}' )

# menampilkan leding hero
desimal = 2005.54321
print(f'angka desimal = {desimal:10.3f}' )
print(f'angka desimal = {desimal:11.3f}' )
print(f'angka desimal = {desimal:15.3f}' )
print(f'angka desimal = {desimal:010.3f}' )
print(f'angka desimal = {desimal:015.3f}' )
# pengeseran angka yang ada di depan agar total baris berisi angka setelah titik dua (:)


# menampilkan + dan -
angkaMinus = -10
angkaPlus = 10
print(f'minus = {angkaMinus}')
print(f'minus = {angkaPlus:+}')

# memformat persen
persen = 0.045
print(f'persentase = {persen:%}')
print(f'persentase = {persen:.2%}')

# melakukan perasi arimatika didalam placehorder
harga = 10000
jumlah = 5
print(f'harga total = Rp. {harga * jumlah :,}')

# format angka lain(binari, octal, hexadecimal)
angka = 255
print(f'angka dalam binary = {bin(angka)}')
print(f'angka dalam octal = {oct(angka)}')
print(f'angka dalam hexadecimal = {hex(angka)}')