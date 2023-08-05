'''
1. Lambda adalah sebuah anonymous fungsi yang di bisa gunakan untuk 1 argumen sehinga lebih simple

contoh:
f = lambda x : x + 2

cara memanggilnya:
print(f(10)) # 10 sendiri adalah variabel untuk argumen yang di gunakan pada fungsi lambda
'''

# tampa lambda
def f_kuadrat(x):
    print(x**2)
    
f_kuadrat(2)

# menggunakan lambda
kuadrat = lambda x:x**2

print(kuadrat(3))

# menggunakan 2 argumen
hasil = lambda x,y : x**y
print(hasil(5,2)) # 5 sebagai x dan 2 sebagai y