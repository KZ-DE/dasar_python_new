
'''
Fungsi "generate_numbers()" di atas merupakan sebuah generator function dalam Python.
Generator function adalah fungsi yang menggunakan kata kunci "yield" untuk menghasilkan nilai satu per satu secara bertahap ketika dipanggil.
Dalam fungsi "generate_numbers()", setiap kali fungsi dipanggil, akan menghasilkan nilai dari 0 hingga 9 (10 nilai) secara berurutan. 
Namun, yang menarik adalah, fungsi ini tidak akan menghasilkan semua nilai sekaligus, melainkan menghasilkan satu nilai, k
emudian sementara berhenti dan menyimpan statusnya, dan kemudian dilanjutkan dari nilai berikutnya saat dipanggil kembali.

Contoh penggunaan generator function "generate_numbers()":
'''


def generate_numbers():
    for i in range(1, 2):
        yield i


# Memanggil generator function dan menggunakan for loop untuk mengakses hasilnya
for number in range(5):
    print(number)
