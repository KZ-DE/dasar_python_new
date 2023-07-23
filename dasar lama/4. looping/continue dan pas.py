# pass --> berfungsi sebagai dummy, tidak di esekusi

angka = 0
angka2 = 0

# while angka < 5:
#     angka += 1
#     angka2 += 1
#     print(angka)
#     if angka == 3:
#         pass
#         print("test") # tetap di eksekusi karena di bawah pass
#     print("hallo")
# while angka2 > 0:
#     angka2 -= 1
#     print(f"angka = {angka2}")
#     if angka == 2:
#         print("test") # tidak akan di eksekusi karena berada di atas pass
#         pass
#     print("apa")
    
# continue --> melewatkan aksi di bawahnya

# contoh 1
print(f'angka sekarang = {angka}')
while angka <5:
    angka +=1
    print(f"angka sekarang == {angka}")
    if angka ==3:
        print("ini angka ke 3")
    print("ini angka") # tidak akan di skip walaupun kodisi di atas true karena tidak ada kontinue
# contoh 1.2
print(f'angka2 sekarang = {angka2}')
while angka2 <5:
    angka2 +=1
    print(f"angka sekarang == {angka2}")
    if angka2 == 3:
        print(f"ini angka2 ke 3")
        continue
    print("ini angka") # ini akan di skip bila kodidisi di atasnya true dan terdapat continue