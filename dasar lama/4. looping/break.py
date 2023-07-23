# break --> akan melewatkan apa saja di bawahnya

# angka = 0
# print(f"angka sekarangan sebelum mulai = {angka}")
# while angka <5:
#     angka +=1
#     print(f"angka sekarangan = {angka}")
#     if angka == 3:
#         print("ini ke 3")
#         break
#     print("adalah angka")
# print("akhir progam")


# contoh 2
no = int(input("masukan angka = "))
angka2 = 0
while angka2 < 10:
    angka2 +=1
    print(angka2)
    if angka2 == no:
        print("cukup")
        break
    print("ini lanjutan")
print("ini akhir progam")