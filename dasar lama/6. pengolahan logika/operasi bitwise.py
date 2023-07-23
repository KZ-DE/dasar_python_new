# operasi assignment (bitwise) atau operasi biner

a = 9
b = 5

# bitwise OR(|)
c = a | b
print('\n =====OR=====')
print('nilai : ', a, 'binary : ',format(a,'08b'))
print('nilai : ', b, 'binary : ',format(b,'08b'))
print('------------(|)')
print('nilai: ',c,' binary: ',format(c,'08b'))

# bitwise AND(&)
c = a & b
print('\n =====AND=====')
print('nilai : ', a, 'binary : ',format(a,'08b'))
print('nilai : ', b, 'binary : ',format(b,'08b'))
print('------------(&)')
print('nilai : ',c,' binary : ',format(c,'08b'))

# bitwise XOR(&)
c = a ^ b
print('\n =====XOR=====')
print('nilai : ', a, 'binary : ',format(a,'08b'))
print('nilai : ', b, 'binary : ',format(b,'08b'))
print('------------(^)')
print('nilai : ',c,' binary : ',format(c,'08b'))

# bitwise NOT(~)
c = ~a
print('\n =====NOT=====')
print('nilai : ', a, 'binary : ',format(a,'08b'))
print('------------(^)')
print('nilai : ',c,' binary : ',format(c,'08b'))



# shifting

# shift righ (>>)
c = a >> 2
print('\n =====>>=====')
print('nilai : ', a, 'binary : ',format(a,'08b'))
print('------------(>>)')
print('nilai : ',c,' binary : ',format(c,'08b'))

# shift left (<<)
c = a << 2
print('\n =====>>=====')
print('nilai : ', a, 'binary : ',format(a,'08b'))
print('------------(<<)')
print('nilai : ',c,' binary : ',format(c,'08b'))