# modul matematika
def tambah(*args:int)->int:
    hasil = 0
    for i in args:
        hasil += i
        
    return hasil

def kali(*args:int)->int:
    hasil = 1
    for i in args:
        hasil *= i
        
    return hasil

def pangkat (n:int)->int:
    hasil = lambda angka : angka**n
    
    return hasil

def kurang (angka1:int=0, angka2 :int=0)->int:
    hasil = angka1 - angka2
    
    return hasil

def bagi (x:int, y:int)->int:
    hasil = x/y
    
    return hasil