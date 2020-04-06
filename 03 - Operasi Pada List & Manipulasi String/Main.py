# len : menghitung panjang atau banyak elemen dari list (Sring menghitung jumlah karakternya)
l = [1,2,3,4,4,4,5,6,7]
s = set(l)
x = 'Hello World'

print(l)
print(len(l))

print(s)
print(len(s))

print(x)
print(len(x))

# Penggabungan dan Replikasi

# Pada list juga memungkinkan adanya penggabungan (+) dan replikasi(*)
[1,2,3] + ['A','B','C']

['X','Y','Z'] * 3

spam = [1,2,3]
spam = spam + ['A','B','C']
print(spam)

# Fungsi pengali juga dapat Anda manfaatkan untuk inisialisasi List.
arr = [0]*10
print(len(arr))
print(arr)

# Range : memberikan deret bilangan dengan pola tertentu.
# Range dengan 1 parameter n: membuat deret bilangan yang dimulai dari 0, sebanyak n bilangan.

for i in range(9):
    print(i)

# Range dengan 2 parameter (n,p) (inklusif)
for i in range(3,9):
    print(i)

# Range dengan 3 parameter (n,p,q)
for i in range (1,9,2):
    print(i)

# In dan not in : untuk mengetahui sebuah nilai atau objek ada dalam list
'fiki' in ['hello','hi','fiki','alamsyah']

spam = ['hello','hi','fiki','alamsyah']
'cat' in spam

'fiki' not in spam

'cat' not in spam

# Memberikan nilai (assignment) untuk lebih dari 1 variabel sekaligus
cat = ['fat','orange','loud']
size = cat[0]
color = [1]
disposition = cat[2]

cat = ['fat','orange','loud'] # from list
size, color, disposition = cat

cat = ('fat','orange','loud') # from tuple
size, color, disposition = cat

a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
print(b)

# Sort : untuk mengurutkan data pada list
x = [2,3,1,6,7,3.14,-1]
print(x.sort())

y = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(y.sort())

# Memasukan keyword reverse
y.sort(reverse=True)
print(y)

# Manipulasi string

# String literals
st = "That is Alice's cat"

st = 'That is Alice\'s cat'

print("Hello there!\nHow are you ?\nI'm doing fine")

multi_line = """Hello there1!
How are you ?
i'm doing fine
"""
print(multi_line)

# Raw string
print(r'That is carol\'s cat')