from . import DataBase
from .Utility import random_string
import csv

import time


def memebuat_data_pertama():
    
    with open("/belajar bahasa progam/belajar_python/dasar/23. belajar membuat projek/Database/Data.csv","w", encoding="utf-8") as file:
        penulis = input("Penulis : ")
        judul = input("Judul : ")
        tahun = input("Tahun terbit : ")
        # data_str = f"{penulis},{judul},{tahun}"
        # file.write(data_str)

        # memakai tempalte sebagai urutan untuk menulis data
        
        data = DataBase.TEMPLATE.copy()
        
        data['pk'] = random_string(6)
        data['date_add'] = time.strftime("%Y-%m-%d-%H-%M-%S",time.gmtime())
        data['penulis'] = penulis + DataBase.TEMPLATE["penulis"][len(penulis):]
        data['judul'] = judul + DataBase.TEMPLATE["judul"][len(judul):]
        data['tahun'] = tahun
        
        # mendeklarasikan data ke template
        # data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}"
        # print(data_str)
        data_header = ["penulis" , "judul" , "tahun terbit"]
        data_list =[penulis , judul , tahun]
        try:
            with open("/belajar bahasa progam/belajar_python/dasar/23. belajar membuat projek/Database/Data.csv",'w',newline='',encoding='utf-8') as file:
                wdata = csv.writer(file) 
                wdata.writerow(data_header)
                wdata.writerow(data_list)
        except:
            print("gagalllll")
            