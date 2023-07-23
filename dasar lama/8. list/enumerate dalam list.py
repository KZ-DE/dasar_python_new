### cara looping dalam list

data = ["asep",1,5,7,3, "bejo"]

# 1. mengunakann for
for dataList in data:
    print(f"data = {dataList}")
print()

# 2. menggunakan while
panjang = len(data)
i = 0
while i < panjang:
    print(f"data = {data[i]}")
    i += 1
print()
    
# 3. menggunaka standar list comprehension
[print(f"data = {x}")for x in data]
print()

# 4. enumerate (bisa menggambil index serta isi data nya)
for a,b in enumerate (data):
    print(f"index = {a}, data = {b}")