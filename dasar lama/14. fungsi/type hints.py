''' type hinst fungsi '''
# untuk memberi tahu bahwa apa input dari fungsi dan juga outputnya

# bentuk standar fungsi
""""
def fungsi(parameter):
    print(parameter)
    
fungsi(1)
fungsi("bejo")
fungsi(True)

def kuadrat(parameter2):
    hasil = (parameter2**2)
    print(hasil)

kuadrat(2)
kuadrat("bejo") # akan eror
kuadrat(True) # akan eror
"""

# penggunaan type hinst
'''
cara penulisan:

def fungsi (parameter:type):

'''
# contoh
import os
import string


def fungsi (parameter:int)-> int:
    output= 10**parameter
    return output

hasil = fungsi(2)
print(hasil)

def display (argument:string):
    print(argument)
    
display("hallo")