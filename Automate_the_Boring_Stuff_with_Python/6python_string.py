# 字符串操作
## 双引号
spam = "That is Alices's cat. "
print(spam)

# 转义字符
# \'   单引号
# \"   双引号
# \n   换行
# \t   制表符
# \\   倒斜杠
spam = 'I\'m a boy. '
print(spam)

# 原始字符串
print(r'That is Garol\'s cat.')

# 三重引号
print("""Dear Alice:

Eve's cat has been arrestedfor catnapping, cat burglary, and extortion/.

Sincerely,
Bob
""")

print("使用换行号")
print('Dear Alice: \n Eve\'s cat has been arrestedfor catnapping, \
cat burglary, and extortion/.\n\nSincerely,\nBob')

# 多行注释
"""This is a test Python program/
Written by Mars 

This program was designed for python3 in Linux.
"""

def spam():
    print("hello")

# 字符串下标和切片
spam = 'Hello World!'
print(spam[0])
print(spam[-1])
print(spam[0:5])

# 字符串的in和not in 
print('hello' in 'hello world')
print('Hello' not in spam)
print('cats' not in 'cats and dogs')

# 字符串转换
spam = "Hello World!"
print(spam.upper())   # 大写
print(spam.lower())   # 小写

print('How are you?')
# feeling = input()
feeling = 'great'
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good! ')


spam = 'Hello World!'
print(spam.islower())
print(spam.isupper())
print('abc'.islower())
print('12345'.islower())

print('Hello'.upper())
print('Hello'.upper().isupper())
print('HELLO'.lower().islower())

# isX
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isalnum())
print('123'.isdecimal())
print(' '.isspace())
print('This Is Title Case.'.istitle())
print('This Is not Title.'.istitle())

#validateInput
while True:
    print('Enter you age : ')
    # age = input()
    age = '5'
    if age.isdecimal():
        break
    print('Please enter a number for you age.')

while True:
    print('Select a new password (letters or numbers only) : ')
    # password = input()
    password = '3ee'
    if password.isalnum():
        break
    print("Password can only have letters and numbers")

# startwith() endswith()
print('Hello world'.startswith('Hello'))
print('Hello world'.endswith('world'))

print(','.join(['cats', 'dogs', 'bats']))
print(' '.join(['My','name','is','Simon.']))

print('My name is Simon'.split())
print('MyABCnameABCisABCSimo'.split('ABC'))
print(('Dear Alice: \n Eve\'s cat has been arrestedfor catnapping, \
cat burglary, and extortion/.\n\nSincerely,\nBob').split('\n'))

# rjust() ljust() center()
print('hello'.rjust(10))
print('hello'.rjust(20))
print('hello world'.rjust(20))
print('hello'.ljust(20))
print('hello'.rjust(10, '*'))
print('hello'.rjust(20, '-'))
print('hello'.center(20))
print('hello'.center(10, '='))

# picnicTable
def printPicnic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# strip() rstrip() lstrip() 删除空白字符
spam = ' Hello World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

# pyperclip模块copy paste string
# 我是在linux下作的报错，
# 官方https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error
# 指出会报错，在Mac和Windows下不存在

# import pyperclip   # 需要pip3 install pyperclip

# pyperclip.copy('Hello world')
# pyperclip.paste()
