'''
Fungsi metode .join() pada Python adalah metode yang digunakan untuk menggabungkan elemen-elemen dalam sebuah iterable menjadi sebuah
string. Metode ini membutuhkan satu argumen, yaitu iterable, yang berisi elemen-elemen yang ingin digabungkan menjadi string.
bisa untuk memanipulasi string
'''

# contoh
words = ['Hello', 'World', 'Python', 'Programming']
separator = ' '

# Menggabungkan elemen dalam daftar menjadi satu string dengan spasi sebagai pemisah
result = separator.join(words)
print(result)  # Output: Hello World Python Programming

numbers = ['1', '2', '3', '4', '5']

# Menggabungkan elemen dalam daftar menjadi satu string tanpa pemisah
result = ''.join(numbers)
print(result)  # Output: 12345

# contoh 2
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

print(fake_bin("45385593107843568"))