# --- LIST ---
# kumpulan data (angka, string, dam boolean)

data = [1,"apa",True]
print(data)

## cara alternatif membuat list
dataRage = range(0,10,2) # rage (start, stop, step)
print(dataRage)
dataList = list(dataRage)
print(dataList)


## membuat list dengan for loop
dataLisFor = [i for i in range(0,10)]
print(dataLisFor)



## membuat list dengan for loop dengan di kuadratkan
dataLisFor = [i**2 for i in range(0,10)]
# i** msdnya nilai i akan di pangkatkan 2
print(dataLisFor)


## membuat list menggunakan for loop dan if
dataListForIf = [i for i in range(0,10) if i != 5]
# artinya : membuat variabel i bernilai 0 sampai 10 (jika) tidak menggunakan angka 5
print(dataListForIf)

# list genap
datagenap = [i for i in range(0,10) if i%2==0]
print(datagenap)

# list ganjil
dataganjil = [i for i in range(0,10) if i%2==1]
print(dataganjil)