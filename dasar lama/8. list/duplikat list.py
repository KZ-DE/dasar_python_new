# teknik duplikat list

a = ["sudrun", "santi", "bejo"]
print(f"a = {a}")

b = a # menduplikat namun nilai addres listny sama berakibatkan jika salah satu berupah isi nya yang duplikat juga berubah
print(f"b = {b}")

a[1] = "asep"
print(b)

print("awal progam\n")
c =a.copy() # sedangkan ini tidak
print(f"data a ={a}")
print(f"data b ={b}")
print(f"data c ={c}\n\n")
c[1] = "paijo"
print(f"data a ={a}")
print(f"data b ={b}")
print(f"data c ={c}\n\n")

