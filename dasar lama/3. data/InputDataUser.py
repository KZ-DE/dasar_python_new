#Mengambil data dari user

#Data yang di masukann pasting string
Data = input("masukan Data: ")
print("Data = ",Data,"type = ", type(Data))

# Jika kita ingin mengambil int, maka
DataInt = int(input("masukan nilai: "))
print("data =", DataInt, "type = ", type(DataInt))

# namun lebih baik menggunakan float untuk mengambil int
angka = float(input("masukan nilai: "))
print("data =", angka, "type = ", type(angka))

# untuk type data boolean kita casting/ubah dulu nilai input ke int terus ke boolean
biner = bool(int(input("masukan nilai: ")))
print("data =", biner, "type = ", type(biner))
