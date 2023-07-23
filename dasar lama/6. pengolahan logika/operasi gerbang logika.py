# operasi logika

# not, or, and, xor

# NOT
print('======NOT======')
a = True
c = not a
print('data a: ',a)
print('data c: ',c)

# OR
print('======OR======')
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)


# OR
print('======AND======')
a = True
b = False
c = a and b
print(a, 'and', b, '=', c)

a = True
b = True
c = a and b
print(a, 'and', b, '=', c)

a = False
b = True
c = a and b
print(a, 'and', b, '=', c)

a = False
b = False
c = a and b
print(a, 'and', b, '=', c)