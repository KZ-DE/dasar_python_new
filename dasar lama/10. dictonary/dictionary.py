# list --> array, untuk mengakses datanya menggunakan index

data_list = ["bejo", 11, True]
print(f"data list ke 2 = {data_list[1]}")

# dictionary (dict) --> associative array, untuk mengakses datanya menggunakan identifier (key)
#### cara penulisan sebagai berikut :
        # data_dict = {
        #     'key' : 'value1',
        #     'key' : 'value2'
        # }


# contoh
data_dict = {
    '1a'   : "bejo",
    '0b'   : 20,
    'dl'   : data_list,
    'bool' : True,
}
print(data_dict['1a'])