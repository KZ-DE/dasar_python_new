'''
Fungsi method .join() pada Python adalah method yang digunakan untuk menggabungkan elemen-elemen dalam sebuah iterable menjadi sebuah
string. Method ini membutuhkan satu argumen, yaitu iterable, yang berisi elemen-elemen yang ingin digabungkan menjadi string.
bisa untuk memanipulasi string

output yang di hasilkan menjadi string tidak lagi berbentuk list

hanya bisa di gunakan untuk list yang berisi string untuk semua datanya atau isinya 
'''

# contoh
words = ['Hello', 'World', 'Python', 'Programming']
print(f'data awal = {words} \n')


# Menggabungkan elemen dalam daftar menjadi satu string dengan spasi sebagai pemisah
spasi = ' '
data_baru = spasi.join(words)
# Output: Hello World Python Programming dan berubah menjadi string tidak lagi dalam bentuk list
print(
    f"data yang telah di beri sepasi dengan menggunakan method join = {data_baru} \n ")

# contoh kedua
no = [1, 2, 3, 4, 5]
pembatas = "-"
hasil_str = str(no)
no_baru = pembatas.join(hasil_str)
print(f'data no baru = {hasil_str} \n ')
print(f'tipe data = {type(hasil_str)}')
