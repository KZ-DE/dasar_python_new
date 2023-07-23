# **kwargs args

def fungsi(nama,tinggi,berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",183,79)

def fungsi(**kwargs): # type data kwargs adalah dict
    '''fungsi kwargs'''
    nama = kwargs["nama"] # di dalam kurung siku adalah key dari dict
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup",tinggi=183,berat=79)


# studi kasus

def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output +=angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        output = print("tidak ada operasi")

    return output

hasil = math(1,2,3,4,option="tambah")
#            args     kwags
print(f"hasil jumlah {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"hasil kali {hasil}")

hasil = math(1,2,4,2,3, option = "bagi")
print(hasil)