'''
set di gunakan untuk menghapus data yang ganda di dalam list serta akan mengurutkan data tersebut dari terkecil hingga tebesar
'''

def x(arr):
    a = b = set(arr)
    return a if arr.count(a) == 1 else b

print(x([1,2,3,2,12,2,1,1,2,3,4,4,1,2,3]))