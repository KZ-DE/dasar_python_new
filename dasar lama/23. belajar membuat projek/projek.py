# membuat agar progam berjalan di os manapun
'''
membuat agar progam yang di buat berjalan di progam utama dan juga agar bisa berjalan di os apapun
'''  

import os
import CRUD as crud



if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
            case "posix": os.system("clear") # untuk linux dan mac os
            case "nt":os.system("cls") # untuk windows
                
    print(10*"=","DATABASE","="*10)
    print(f"{'masukan input sesuai angka':^30}\n")
    
    # check database itu ada atau tidak
    crud.console()
        
    ### membuat menu
    run = True
    while run:
        match sistem_operasi:
            case "posix": os.system("clear") # untuk linux dan mac os
            case "nt":os.system("cls") # untuk windows
                
        print(10*"=","DATABASE","="*10)
        print(f"{'masukan input sesuai angka':^30}\n")
        print("1. Read Data")
        print("2. Add Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        user = input("Masuka Opsi : ")
        print(f"\n{'='*30}\n")
        
        match user:
            case "1" | "read":
                # crud.read_data()
                # crud.read_data()
                print("apa")
            case "2" | "add":
                print("Add Data")
            case "3" | "update":
                print("Update Data")
            case "4" | "delete":
                print("Delete Data")
            case _: print("maaf masukan dengan benar")
        print(f"\n{'='*30}\n")
        if input("\nKeluar Progam (y/n)? : ") == "y":
            break
    print("\n")
    print(10*"=","TERIMAKASIH","="*10)