import string
import random

def random_string(panjang:int)->str:
    '''membuat fungsi agar bisa di gunakan meng random nilai pk'''
    hasil_pk = "".join(random.choice(string.ascii_letters)for i in range(panjang))
    
    return hasil_pk