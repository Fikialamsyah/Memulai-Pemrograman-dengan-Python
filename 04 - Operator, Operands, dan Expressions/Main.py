# Operator dan Expresi (Expressions)

# Operator matematika
print('Tambah'.center(20,'='))
a = 10 + 2
print('10 + 2 = ', a)

print('kurang'.center(20, '='))
a = 10 - 2
print('10 - 2 = ', a)

print('kali'.center(20,'='))
a = 10 * 2
print('10 x 2 = ', a)

print('bagi'.center(20,'='))
a = 10 / 2
print('10 / 2 = ', a)

print('modulo'.center(20,'='))
a = 10 % 3
print('10 / 3 = ', a)

print('-'*20)

# Operator bit
print('<< (left shift)'.center(20,'='))
a = 2 << 2
print(a)

print('>> (right shift)'.center(20,'='))
a = 11 >> 1
print(a)

print('& (bit-wise AND)'.center(20,'='))
a = 11 & 1
print(a)

print('| (bit-wise OR))'.center(20,'='))
a = 5 | 3
print(a)

print('^ (bit-wise XOR)'.center(20,'='))
a = 5 ^ 3
print(a)

print('~ (bit-wise invert)'.center(20,'='))
a = ~11
print(a)

print('-'*20)

# Perbandingan
print('< atau operator.lt (less than)'.center(20,'='))
a = 5 < 3
print(a)

print('> atau operator.gt (greater than)'.center(20,'='))
a = 5 > 3
print(a)

print('<= atau operator.le (less than or equal to))'.center(20,'='))
a = 5 <= 3
print(a)

print('>= atau operator.ge (greater than or equal to)'.center(20,'='))
a = 5 >= 3
print(a)

print('== atau operator.eq (equal to)'.center(20,'='))
a = 5 == 3
print(a)

print('!= atau operator.ne (not equal to)'.center(20,'='))
a = 5 != 3
print(a)

print('-'*20)

# Penggunaan le, lt, gt, ge, eq, ne
from operator import *
a = 1
b = 5.0
print('a = {}'.format(a))
print('b = {}'.format(b))

for fun in (lt, le, eq, ne, ge, gt):
    print('{}(a, b): {}'.format(fun.__name__, fun(a, b)))


# Boolean operator
print('not (boolean NOT)'.center(20, '='))
a = True
print(not a)

print('and (boolean AND)'.center(20, '='))
a = True
print(not a)

print('or (boolean OR)'.center(20, '='))
a = True
b = False
print(a or b)


# Cara singkat menuliskan operasi
a = 2
a = a * 3
# Menjadi :
a = 2
a *= 3




