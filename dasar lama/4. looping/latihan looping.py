# gambar segitiga dengan looping
import time

sisi = 0
a = int(input("masukan angka = "))

### 1.menggunakan while
# while True :
#     sisi += 1
#     print(sisi*"*")
#     if sisi == a:
#         break
# print("")
    
# ### 2.menggunakan for
# jumblah = 1
# for i in range(a):
#     print("*"*jumblah)
#     jumblah += 1
# print("")

### 3. hanya angka gajil saja menggunakan while
# jumblah = 0
# while True:
#     jumblah +=1
#     if jumblah%2==1:
#         print("*"*jumblah)
#     if jumblah > a:
#         break

### 4. hanya ganjil saja menggunakan for
# jumblah=0
# for i in range(a):
#     jumblah +=1
#     if jumblah%2==1:
#         print("*"*jumblah)


### 5. segitiga sama kaki for
# jumblah =0
# for i in range(a):
#     jumblah +=1
#     a -=1
#     print(" "*a+" *"*jumblah)
    
    
### 6. belah ketupat menggunakan for
jarak =int(a/2)
jumblah = 0
hasil = a-1
for x in range(a):
    jumblah += 1
    if jumblah % 2 == 1:
        time.sleep(0.5) #fungsinya seperti delay dalam c++
        print(" "*jarak+"*"*jumblah)
        jarak -= 1
for i in range(a):
    hasil -= 1
    if jarak == 0:
        jarak +=2
    if hasil % 2 == 1:
       time.sleep(0.5) 
       print(" "*jarak+"*"*hasil)
       jarak += 1

        
### 7. segitiga terbalik      
# jumblah = a
# for i in range(a):
#     jumblah -= 1
#     if jumblah % 2 == 1:
#        print(" "*jarak+"*"*jumblah)
#        jarak += 1
#     print(f"jumblah {jumblah}")
#     print(f"jarak {jarak}")
       

print("akhir progam")