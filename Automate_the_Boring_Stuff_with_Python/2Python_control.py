# 2.11习题
spam = 6
if spam == 1 :
    print("Hello")
elif spam == 2 :
    print("howdy")
else:
    print("Greetings! ")


spam = True
print(spam)
# True 和 False 不能做变量名
# 操作符
print(42 == 42)
print(42 == 99)
print(2 != 3)
print(2 != 2)
print('hello' == 'hello')
print('hello' == 'Hello')
print('cat' != 'dog')
print(True == True)
print(42 == 42.0)
print(42 < 100)
print(42 > 100)
eggcount = 42
print(eggcount <= 42)
print(True and True)
print(True and False)
print(False or True)
print(False or False)
print(not True)
print(not not not not True)

print((4<5) and (5<6))
print((4<5) and (9<6))
print((1 == 2) and (2 == 2))

# 代码块
print("Please input name : ")
name = input()
print("Please input password : ")
password = input()
if name == 'Mary':
    print("Hello, Mary")
    if password == "swordfish":
        print("Access granted")
    else:
        print("Wrong Password")

# 
if name == 'Alice':
    print("Hi, Alice")
else:
    print("hello, stranger.")

# 
print("Please input age : ")
age = input()
# print(type(age))
age = int(age)
if name == "Alice":
    print("Hi, Alice")
elif age < 12:
    print("You are not Alice, kiddo")
elif age > 2000:
    print("Unlike you, Alice is not  an undead, immortal vampire.")
elif age >100 :
    print("You are not Alice, grannie. ")

# While 循环语句
sapm = 0
if spam < 5:
    print('Hello world')
    spam = sapm + 1

spam = 0
while spam < 5:
    print("Helloworld")
    spam = spam + 1

# yourName.py
# name = ''
# while name != 'your name':
#     print('Please type your name. ')
#     name = input()
# print("Thank you! ")

# while True:
#     print("Please typer your name: ")
#     name = input()
#     if name == 'your name':
#         break
# print("Thank you! ")

while True:
    print('who are you? ')
    name = input()
    if name != 'Joe':
        continue
    print("Hello, Joe. What is the password? (It is a fish.)")
    password = input()
    if password == 'fish':
        break
print('Access granted')

# for循环
print('My name is ')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')


total = 0
for num in range(101):
    total = total + num
print(total)

for i in range(12, 16):
    print(i)

for i in range(0, 10, 2):
    print(i)

# 倒序
for i in range(5, -1, -1):
    print(i)

# 导入模块
import random
for i in range(5):
    print(random.randint(1, 10))

import random, sys, os, math

while True:
    print("Type eixt to exit. ")
    response = input()
    if response == 'exit':
        sys.exit()
    print("You typed " + response + '.')


