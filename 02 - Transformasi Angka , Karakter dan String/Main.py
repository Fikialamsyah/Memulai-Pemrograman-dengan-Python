# Metode Upper : konversi untuk membuat seluruh karakter dalam string menjadi kapital.
p = 'hello world'
p = p.upper()
print(p)

# Metode Lower : konversi untuk membuat seluruh karakter dalam string menjadi huruf kecil.
p = 'HELLO WORD'
p = p.lower()
print(p)

# Contoh penggunaan lower.
feeling = input("How Are You ? ")
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print("I Hope the rest of your dayis good.")

# Isupper : mengembalikan nilai boolean jika string yang dimaksud memiliki satu karakter dan seluruhnya kapital.
p = 'HELLO'
p = p.isupper()
print(p)

'HELLO'.isupper()
'12345'.isupper()


# Islower : mengembalikan nilai boolean jika string yang dimaksud memiliki satu karakter dan seluruhnya huruf kecil.
p = 'Hello World'
p = p.islower()
print(p)

'abcde12345'.islower()
'12345'.islower()

# isalpha : mengembalikan True jika string berisi hanya huruf dan tidak kosong.
'hello'.isalpha()

'hello123'.isalpha()

# isalnum : mengembalikan True jika string berisi hanya huruf atau angka, dan tidak kosong.
'hello123'.isalnum()

'hello'.isalnum()

# isdecimal : mengembalikan True jika string berisi hanya angka/numerik dan tidak kosong.
'123'.isdecimal()

# isspace : mengembalikan True jika string berisi hanya spasi, tab, newline, atau whitespaces lainnya dan tidak kosong.
'   '.isspace()

# isTitle : mengembalikan True jika string berisi kata yang diawali huruf kapital dan dilanjutkan dengan huruf kecil seterusnya.
'This Is Title Case'.istitle()

'This Is not Title Case'.istitle()

'This Is NOT Title Case Either'.istitle()

# Contoh program
while True:
    print('Enter your age : ')
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number your age")
while True:
    print('Select a new password (letters and number only): ')
    password = input()
    if password.isalnum():
        break
    print('Password can only have letters and numbers')

# startswith :  mengembalikan nilai True berdasarkan nilai awalan
'Hello, World!'.startswith('Hello')

'Hello World!'.startswith('Hello World!')

'abc123'.startswith('abcdef')

# endswith : mengembalikan nilai True berdasarkan akhiran string
'Hello, World!'.endswith('World!')

'Hello World!'.endswith('Hello World!')

'abc123'.endswith('12')

# join : berguna saat Anda memiliki sejumlah string yang perlu digabungkan.
', '.join(['cats','rats','bats'])

' '.join(['My','name','is','Fiki'])

# split :
'My Name Is Fiki'.split()

'abcMyNameIsFiki'.split('abc')

a = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob
'''
a.split('\n')

# rjust: rata kanan.
'Hello'.rjust(10)

'Hello'.rjust(20, '*')

# rjust: rata kanan.
'Hello'.ljust(10)

'Hello'.ljust(20, '-')

# center : rata tengah
'Hello'.center(20)

'Hello'.center(20, '=')

# strip
spam = '     Hello, World!      '
spam.strip()

# rstrip
spam = '     Hello, World!      '
spam.rstrip()

# lstrip
spam = '     Hello, World!      '
spam.lstrip()

# Replace
string = 'Geek for geeks geeks geeks geeks'
print(string.replace('geeks','Geeks'))