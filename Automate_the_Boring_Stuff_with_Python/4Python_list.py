print([1, 2, 3])
print(['cat', 'bat', 'rat', 'elephant'])

spam = ['cat', 'bat', 'rat', 'elephant']
# Index of list
print(spam)
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print(spam[-1])
print(spam[-2])

samp = [['cat', 'bat', 'rat', 'elephant'], [10, 20, 30, 40]]
print(type(samp))
print(samp[0][1])
print(samp[1][3])

# slice
print(spam[1:3])
print(spam[0: -1])
print(spam[:2])
print(spam[:])

print(len(spam))
print(len(samp))
print(samp[1])

# 修改值
spam[1] = 'aardvark'
spam[-1] = 123456
print(spam)

a = [1, 2, 3]
b = ['A', 'B', 'C']
print(a * 3)
print(a+b)

# delete element
c = a + b
del c[1]
print(c)

# Multi-Variable
# 这是一种非常不好的编程方式
catName1 = 'Zophine'
catName2 = 'Pooka'
catName3 = 'Simon'
catName4 = 'Lady Macbeth'
catName5 = 'Fat-tail'
catName6 = 'Miss Cleo'

# print('Enter the name of cat 1 :')
# catName1 = input()
# print('Enter the name of cat 2 :')
# catName2 = input()
# print('Enter the name of cat 3 :')
# catName3 = input()
# print('Enter the name of cat 4 :')
# catName4 = input()
# print('Enter the name of cat 5 :')
# catName5 = input()
# print('Enter the name of cat 6 :')
# catName6 = input()
# print('The cat names are : ')
# print(catName1 + '' + catName2 + '' + catName3 + '' + \
# catName4 + '' + catName5 + '' + catName6 + '')

catNames = []
while True:
    print("Enter the name of cat " + str(len(catNames) + 1) + \
    " (or enter nothing to stop. ) : ")
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation

print('The cat names are : ')
for name in catNames:
    print('' + name)

for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index' +str(i) + ' in supplies is: ' + supplies[i])

# in and not in for string 
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print("Enter a pet name : ")
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else :
    print(name + ' is my pet.')

# 多重赋值
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

size, color, disposition = cat

# 增强赋值语句
# sapm += 1     <=>     spam = spam + 1
# sapm -= 1     <=>     spam = spam - 1
# sapm *= 1     <=>     spam = spam * 1
# sapm /= 1     <=>     spam = spam / 1
# sapm %= 1     <=>     spam = spam % 1

spam = 42
spam = spam + 1
print(spam)

samp = 42
samp += 1
print(samp)

spam = 'Hello'
spam += ' World!'

print(spam)

bacon = ['zophie']
bacon *= 3
print(bacon)

# 方法
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'))

# append() 和 insert() 在list中添加值
spam = ['cat', 'dog', 'bat']
spam.append('mouse')
print(spam)

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)

# remove() 和 del 删除list中的值
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[1]
print(spam)

spam = ['cat', 'bat', 'rat', 'elephant', 'cat', 'cat', 'bat']
spam.remove('bat')
print(spam)

# Sort() 排序
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'bat', 'elephants']
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'bat', 'elephants']
spam.sort(reverse=True)  # 逆序排列
print(spam)

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

spam = ['A', 'a', 'Z', 'z']
spam.sort(key=str.lower)
print(spam)

# Magic8Ball
import random

messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hzy try again',
    'Ask again later',
    'Concentraite and ask again',
    'My reply is so good',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

# String and Tuple
name = 'Zophie'
print(name[0])
print(name[0:4])
print('Zo' in name)
for i in name:
    print('* * * ' + i + ' * * *')

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)

eggs = [1, 2, 3]
eggs = [4, 5, 6]
print(eggs)

eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)

# Tuple
eggs = ('hello', 42, 0.5)
print(type(eggs))
print(len(eggs))
print(eggs[0])
print(eggs[1:3])

# 元组不能更改
print(type(('hello', )))
print(type(('hello')))

# tuple() <=to=> list()
a = tuple(['cat', 'dog', 5])
print(a)
print(type(a))

b = list(('cat', 'dog', 5))
print(b)
print(type(b))

# 引用
# Scalar
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

# List is not same as scalar
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print("spam : ", spam)
print("cheese : ", cheese)

# 传递引用
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# copy模块中 copy() 和 deepcopy()
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)    # ['A', 'B', 'C', 'D']
print(cheese)  # ['A', 42, 'C', 'D']

bacon = [['A', ['hello'], 'B'],['a', 'b']]
bacon_cp = copy.copy(bacon)
print(copy.deepcopy(bacon))
print(bacon_cp)

# 习题4.10.1 逗号代码
spam = ['apples', 'bananas', 'tofu', 'cats']

def List_process(spam):
    """
    将list处理成字符串
    """
    for i in range(len(spam)):
        if i == (len(spam) - 1):
            print('and ' + spam[i])
            break
        print(spam[i] + ', ' , end='')

spam = ['A', 'B', 'C', 'D']
List_process(spam)

# 习题4.10.2 字符图网格

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print(len(grid))
for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print('\n', end='')