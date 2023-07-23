# kegunaan __main__
'''
jika di bahasa lain contohnya c++ fungsinya adalah progam utama
contohnya seperti berikut :
# 1. c++ :
    int main(){
        
    }
    
# 2. java
    Clas main(){
        
        static void main(){
            
        }
    }
    
    
sedangkan __main__ adalah top level code evironment (name adalah main jika di python)
'''
## __name__ pada file progam utama
print(f"nilai pada main.py = '{__name__}'")
# akan berubah main jika di jalankan di dalam file utama

## __name__ pada file progam eksternal
import fungsi
# akan berubah menjadi nama file dari progam tersebut

## contoh penggunaan

# deklarasi
def tambah(a:int,b:int)->int:
    return a+b

# fungsi utama
if __name__ == "__main__":
    x = 5
    y = 5
    hasli = tambah(x,y)
    print(hasli)
else:
    print("Maaf tidak di eksekusi main")
    

# artinya jika __name__ berubah menjadi __main__ maka progam akan berjalana
# jika tidak maka tidak akan di eksekusi


## isi dari package biasahnya file
# 1. __init__.py
# 2. __main__.py
# 3. nama modul.py

## import package
import package
