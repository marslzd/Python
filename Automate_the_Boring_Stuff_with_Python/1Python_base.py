"""
该文件为“Python编程快速上手——让繁琐工作自动化”
第一部分python基础
"""
# 加法
print(2 + 2)
# 指数
print(2 ** 3)
# 取余
print(22 % 8)
# 整除
print(22 // 8)
# 除法
print(22 / 8)
# 乘法
print(3 * 5)
# 减法
print(5 - 2)
# 优先级
print(2 + 3 * 6)
print((2+3) * 6)
print(2 ** 8)
print("数学优先级")
print((5-1) * ((7+1) / (3-1)))

# 字符串
print('Alice' + 'Bob')
# 复制
print('Alice' * 5)

# 变量名赋值
spam = 40
print("spam_value:", spam)

eggs = 2
print(eggs)
print(spam + eggs)

# the first program
# This program says hello and asks for my name
print("Hello world!")
print("What is your name ?") # ask for their name
Myname = input()
print("Nice to meet you, " + Myname)
print("The length of your name is :")
print(len(Myname))
print("What's your age?")   # ask for their age
Myage = input()
print("You will be " + str(int(Myage) + 1) + " in a year")

# len() 传递一个字符串，返回长度
a = str(29)
print(type(a))

print(float(10.0))

print(42 == '42')

# 习题1.8
bacon = 20
bacon + 1
print(bacon)  # 20

print('spam'+'spamspam')
print('spam' * 3)