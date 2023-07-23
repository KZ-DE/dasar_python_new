# 1. mode write --> akan membuat file baru jika tidak ada, lalu akan menulis di baris itu aja (ketimpa dengan yang baru)
# kode write adalah "w"
with open("d:/belajar bahasa progam/belajar_python/dasar/21. read external file/data2.txt","w", encoding="utf-8") as file:
    file.write("bejo")
    

with open("d:/belajar bahasa progam/belajar_python/dasar/21. read external file/data2.txt","w", encoding="utf-8") as file:
    file.write("makmur\n")

    
# 2. mode append --> menambahakan tulisan baru di samping tulisan lama, agar berada di bawah tulisan lama maka mengunakan format \n untuk membuat line baru
# kode append adalaha "a"
with open("d:/belajar bahasa progam/belajar_python/dasar/21. read external file/data2.txt","a", encoding="utf-8") as file:
    file.write("bejo")
    file.write("\ntambah lagi dong dengan append")
    
# agar tidak menghapus histtori tulisa sudah ada di dalam file teks maka mulai dari awal jangan menggunaka mode "w"
# begitu pun untuk seterusnya

# 3. mode r+ --> bisa read dan write namun tidak bisa membau file baru jika belum ada file teks
with open("d:/belajar bahasa progam/belajar_python/dasar/21. read external file/data3.txt","r+", encoding="utf-8") as ft:
    ft.write("menambah dengan r+ ")
    ft.write("\nmenambah dengan r+ lagi ")
    print(ft.read())
    # tulisan lama akan di reset atau ketimpa dengan baru sesuai dengan panjang data atau kalimat

# untuk membacanya harus mengakses ulang dengan whit baru terlebih dahulu
with open("d:/belajar bahasa progam/belajar_python/dasar/21. read external file/data3.txt","r+", encoding="utf-8") as ft:
    print(ft.read())

with open("d:/belajar bahasa progam/belajar_python/dasar/21. read external file/data3.txt","r+", encoding="utf-8") as ft:
    ft.write("12345678")