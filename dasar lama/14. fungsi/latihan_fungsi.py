# latihan fungsi
import os
os.system("cls")

'''
CARA BIASA
while True :
    # membuat header progam
    print(f"{'PROGAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG' :^40}")
    print("-"*40)

    # mengambil input user
    LEBAR = int(input(f'masukan nilai lebar :')) 
    PANJANG = int(input(f'masukan nilai panjang : '))

    # progam menghitung luas dan kelilinng
    LUAS = LEBAR * PANJANG
    KELILING = 2 * (PANJANG + LEBAR)

    # tampilkan hasil
    print(f"hasil dari luas persegi ={LUAS}")
    print(f"hasil dari keliling persegi ={KELILING}")
'''


# cara jika mengggunakan fungsi
def header():
    print(f"{'PROGAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG' :^40}")
    print("-"*40)
    print("pilih 1 untuk menghitung luas")
    print("pilih 2 untuk menghitung keliling")
    print("pilih 3 untuk menghitung luas dan keliling")

def input_user():
    ''' fungsi input user '''
    lebar = int(input(f'masukan nilai lebar :')) 
    panjang = int(input(f'masukan nilai panjang : '))
    
    return lebar, panjang

def hitung_luas():
    ''' luas dan keliling '''
    LUAS = lebar * panjang
    return LUAS

def hitung_keliling():
    KELILING = 2 * (lebar * panjang)
    return KELILING

def display(pesan,hasil):
    print(f"hasil perhitungan {pesan} = {hasil}")

    
    
# membuat progam utama
while True:
    header()
    pilihan = input("masukan piliha anda (1/2/3) : ")
    if pilihan =="1":
        lebar,panjang = input_user()
        LUAS = hitung_luas()
        display("luas",LUAS)
    elif pilihan == "2":
        lebar,panjang = input_user()
        KELILING = hitung_keliling()
        display("keliling",KELILING)
    elif pilihan == "3":
        lebar,panjang = input_user()
        LUAS = hitung_luas()
        KELILING = hitung_keliling()
        display("luas",LUAS)
        display("keliling",KELILING)
    else:
        print("masukan yang benar ngentod!!")
        pass
    lanjut = input('apakah mau lanjut menghitung ? (y/n) : ')
    if lanjut == 'n':
        break
    
print("progam selesai")
    