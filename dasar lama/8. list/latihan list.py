# latihan list

## progam data buku
list_buku = []
while True:
    print("\nmasukan data buku")
    judul = input("masukan judul buku\t: ")
    penulis =input("masuan penulis buku\t: ")
    print()

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru) # memindahkan list buku_baru ke list nested list_buku
    
    # print("no. | judul| | penulis|")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    x = input("\nmau lanjut mengisi? (y) / (t)\t: ")
    if x =="t":
        break