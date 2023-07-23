print(f"nilai pada fungsi.py = '{__name__}'")
def tambah(a:int,b:int)->int:
    return a+b

# fungsi utama
if __name__ == "__main__":
    x = 5
    y = 2
    hasli = tambah(x,y)
    print(hasli)
else:
    print("Maaf tidak di eksekusi")