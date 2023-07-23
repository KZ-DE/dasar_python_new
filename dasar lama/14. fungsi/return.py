# fungsi dengan return

# template
# def nama_fungsi (argumen):
    # isi fungsi
    # return output

y = 3**2
print(y)

def kuadrat(x):
    z = x**2
    return z
# artinya adalah retru merupakan hasil dari progam di atas
# di sini retrunnya z ya itu "berapa nila z bila bilangan (x) bernialai imputan (contohnya 3)"
# setelah itu tampilkan retrunnya / hasilnya

a = kuadrat(3)
print(f"contoh ke 2 : {a}\n")
# kuadrat(10)
print(kuadrat(5))

# fungsi tambah
def fungsi_tambah (a,b):
    return a+b
print(fungsi_tambah(2,3))

# bisa juga di tambahkan dengan lainnya
s = 3 + fungsi_tambah(1,2)
print(s)

# bisa juga menggunakan return banyak
def mtk (q,w):
    tambah = q + w
    kurang = q - w
    kali = q * w
    bagi = q / w
    return tambah,kurang,kali,bagi
k,l,m,n = mtk(2,2)
print(f"hasil = {k}")
print(f"hasil = {l}")
print(f"hasil = {m}")
print(f"hasil = {n}")