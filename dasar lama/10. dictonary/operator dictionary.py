# operator dictionary

data_dict = {
    '01'    : "bejo",
    '02'    : "slamet",
    '03'    : 123,
}

# cara mengetahui panjang dict
LENDICT = len(data_dict)
print(f"panjang dict = {LENDICT}")

# mengecek key tersebut ada atau tidak di dalam dictonary
cek_key = '01' in data_dict
print(f"apakah ada : {cek_key}")
cekkey = 'aa' in data_dict
print(f"apakah ada : {cekkey}\n")

# mengakses value (read) dengan get
print(data_dict['01'])
print(data_dict.get('01'))
print(data_dict.get('aa')) # jika key salah/tidak ada di dalam dict maka akan muncul tulisan none
print(data_dict.get('aa',"key tidak di temukan")) # sama saja tapi merubah none menjadi apa yang kita inginkan

# mengupdate data (tidak disarankan)
data_dict['01'] = "bejo kuat"
print(data_dict)

# menamnbah data (tidak di sarankan)
data_dict['007'] = "KZ"
print(data_dict)
print()

# menambahkan data dan meng update data dengan .update (disarankan)
data_dict.update({'01':"asep"}) #jika keynya yang sudah ada di dalam dict maka akan mengupdate valuenya
print(data_dict)
data_dict.update({'020':"belajar python"}) # jika key yang di masukan tidak ada di dalam dict maka akan menambah key baru dan value baru
print(data_dict)

# menghapus data dict
del data_dict['020']
print(data_dict)