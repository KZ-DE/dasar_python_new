'''
set di gunakan untuk menghapus data yang ganda di dalam list serta akan mengurutkan data tersebut dari terkecil hingga tebesar
'''


def x(arr):
    a = b = set(arr)
    return a if arr.count(a) == 1 else b


print(x([1, 2, 3, 2, 12, 2, 1, 1, 2, 3, 4, 4, 1, 2, 3]))

# contoh tampa funsi
no = [1, 2, 3, 1, 2, 3, 1, 3, 4, 1, 2, 3, 4, 1, 2, 4, 3, 5, 1, 3, 1,
      2, 3, 4, 1, 2, 4, 21, 3, 4, 5, 2, 4, 30, 10, 3, 12, 42, 12, 31, 1]
print(f"\ndata acak = {no} \n")

hasil = set(no)
print(f'data terurut = {hasil} \n')

# dengan tipe data string
nama = ['dudung', 'mamang', 'bejo', 'ucup', 'bejo', 'apel', "dudung", "apel"]
print(f"nama tidak terurut = {nama} \n")
nama_urut = set(nama)
print(f'nama urut = {nama_urut}')
