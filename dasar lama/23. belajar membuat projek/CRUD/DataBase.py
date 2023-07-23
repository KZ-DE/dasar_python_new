'''
untuk membuat data base yang berupa .txt maka harus membuat data fremnya(tempalte) agar bisa di urutkan berapa banyak yang terisi dari database nya
'''

from. import operasi
from. import read

### membuat template database
TEMPLATE = {
    'pk':"XXXXXX",
    'date_add':"yyyy-mm-dd",
    'judul':""*225,
    'penulis':""*225,
    'tahun':"yyyy"
}

### cek data base ada atau tidak
def console():
    try:
        with open("/belajar bahasa progam/belajar_python/dasar/23. belajar membuat projek/Database/Data.csv", "r") as file:
            # file.read()
            print("database di temukan")
    except:
        print("database tidak di temukan , silahkan membuat dataase baru")
        operasi.memebuat_data_pertama()

# def console_read ():
#     try:
#         with open ("/belajar bahasa progam/belajar_python/dasar/23. belajar membuat projek/Database/Data.csv", "r") as file:
#             file.readline()
#     except:
#         print("mboh wesss")