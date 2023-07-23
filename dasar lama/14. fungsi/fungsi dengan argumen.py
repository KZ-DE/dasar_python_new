# fungsi denganargumen (input)

# '''penulisan'''

# def nama_fungsi (argumen):
    # isi fungsi

def hello (nama):  # membuat fungsi dengan vaiable nama sebagai input
   print(f"selamat pagi {nama}")
   
hello("bejo") # bisa di isi selain string

# contoh
def tambah(a,b):
    hasil = a+b
    print(f"{a} + {b} = {hasil}")

tambah(2,10)

# dengan list
namalist=["bejo", "sudrun", "asep"]
def say(nama):
    data_nama =nama.copy() # digunakan agar nilai list yang asli tidak akan berubah bila ada perubahan yang di lakukan di dalam dev terhadap isi list
    data_nama[0] = "kz"
    for name in data_nama:
        print(name)

say(namalist)
print(*namalist)