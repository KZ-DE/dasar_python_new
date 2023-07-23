# width and Multiline

# Data

data_nama = 'sudrun'
data_umur = 17
data_tinggi = 167
data_nomor_sepatu = 44

# data stabdart
print(5*'='+'DATA STRING'+5*'=')
print(f'nama = {data_nama}, umur = {data_umur}, tinngi badana = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}')

# data multiline dengan mengguakan enter(\n)
print('\n'+5*'='+'DATA STRING'+5*'=')
print(f'nama = {data_nama}\numur = {data_umur}\ntinngi badan = {data_tinggi}\nnomor sepatu = {data_nomor_sepatu}')


# data multiline dengan double kutip 3 kali("""))
print('\n'+5*'='+'DATA STRING'+5*'=')
dataString =f"""nama = {data_nama}
umur = {data_umur}
tinngi badan = {data_tinggi}
nomor sepatu = {data_nomor_sepatu}
"""
print(dataString)
# akan menampilkan apa yang kita ketik di dalam tanda kutip tersebut


# untuk mengatur lebarnya
print('\n'+5*'='+'DATA STRING'+5*'=')
dataString = f"""
nama         = {data_nama:>6}
umur         = {data_umur:^7}
tinngi badan = {data_tinggi:<6}
nomor sepatu = {data_nomor_sepatu:>6}
"""
print(dataString)