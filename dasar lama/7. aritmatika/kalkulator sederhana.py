# kalkulator sederhana

a= float(input("masukan angka : "))
operator= input("pilih operator (+,/,-,x)")
b= float(input("masukan angka : "))

if operator== "+":
    hasil = a + b
    print(hasil)
elif operator== "-":
    hasil = a - b
    print(hasil)
elif operator== "/":
    hasil = a / b
    print(hasil)
elif operator== "x":
    hasil = a * b
    print(hasil)
else :
    print("maaf masukan yang benar.")