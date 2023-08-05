'''
Fungsi sum() pada Python digunakan untuk menghitung jumlah dari semua elemen dalam sebuah iterable, seperti daftar (list), tupel (tuple),
atau set. Fungsi ini mengambil satu argumen, yaitu iterable, yang merupakan kumpulan elemen yang ingin dijumlahkan.
'''
# contoh
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Output: 15 (1 + 2 + 3 + 4 + 5)

'''
bisa juga untuk mengecek apakah bilangan tersebut memenuhi kiteria atau tidak
'''
# contoh 2


def x(a, b, c):
    # angakan mengecek apakah dalam list tersebut hanya terdapat 2 bilangan yang lebih dari 0
    return sum([a > 0, b > 0, c > 0]) == 2


print(x(1, 2, 3))

#  contoh 3


def a(a, b):
    return sum([a > b]) == True


print(a(3, 2))

# contoh 3


def aa(class_points, your_points):
    # akan menghitung apakah your point lebih besar dari pada seluruh jumlah point yang sudah di bagi panjang jumlah point yang ada
    return your_points > sum(class_points) / len(class_points)


print(aa([20, 2, 32, 34, 56, 36, 75, 3, 56, 12], 30))
