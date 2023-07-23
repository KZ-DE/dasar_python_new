# kovrensi satuan

#progam temperatur celcius dengan satuan lainnya
print("\n PROGAM KONVERSI temperatur\n")

celcius = float(input('masukan suhu: '))
print("suhu adalah: ",celcius, "celcius")

# reamur
reamur = (4/5)*celcius
print("suhu dalam reamur :",reamur,"reamur")

# fahrenhelt
fahrenhelt = ((9/5)*celcius)+32
print('suhu dalam fahrenhelt:',fahrenhelt,'fahrenhelt')

# kelvin
kelvin = celcius + 273
print('suhu dalam kelvin:',kelvin,"kelvin")