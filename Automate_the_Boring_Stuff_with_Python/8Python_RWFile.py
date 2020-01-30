# 读写文件

# 文件与路径
# 工作目录
import os
print(os.path.join('usr', 'bin', 'python'))
# Linux usr/bin/python   Windows usr\\bin\\python

# 文件名list
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/home/linux/Desktop', filename))

# print working directory
print(os.getcwd())
# os.chdir('/home/linux/Desktop')  # 更改路径
# print(os.getcwd())

# os.makedirs()创建新文件夹
# os.makedirs('/home/linux/Desktop/Test_11')

# os.path() 
# os.path.abspath()     # 返回绝对路径
# os.path.isabs()       # 判断绝对路径
# os.path.relpath()     # 返回相对路径
print(os.path.abspath('.'))
print(os.path.abspath('./sometest'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('/home/linux/Desktop', '/home/linux/'))
print(os.path.relpath('/home/linux/Desktop', '/home/linux/Documents'))

# 处理绝对路径和相对路径
Filepath = '/home/linux/Documents/Python_test/Automate_the_Boring_Stuff_with_Python/temp.py'
print(os.path.basename(Filepath))
print(os.path.dirname(Filepath))

print(os.path.split(Filepath))
print(Filepath.split(os.path.sep))

# 查看文件大小和文件夹内容
print(os.path.getsize('/home/linux/Desktop/hello/hello.py'))
print(os.listdir('/home/linux/Desktop/hello/'))

totalsize = 0
for filename in os.listdir('/home/linux/Desktop/hello/'):
    totalsize = totalsize + os.path.getsize(os.path.join('/home/linux/Desktop/hello/', filename))

print(totalsize)

# 检查路径有效性
print(os.path.exists('/home/linux/Desktop/hello/'))
print(os.path.exists('/home/linux/Desktop/test/'))
print(os.path.isdir('/home/linux/Desktop/hello/'))
print(os.path.isfile('/home/linux/Desktop/hello/'))
print(os.path.isfile('/home/linux/Desktop/hello/hello.py'))

# 文件读写过程
# # open()函数
hellofile = open('/home/linux/Desktop/hello.txt', 'r') # read
hellocontent = hellofile.read()
print(hellocontent)

sonnetfile = open('/home/linux/Desktop/sonnet.txt')
print(sonnetfile.readlines())

hellofile = open('/home/linux/Desktop/hello.txt', 'w')  # write 覆盖之前的内容
hellocontent = hellofile.write('Hello world by python\n')
print(hellocontent)
hellofile.close()

hellofile = open('/home/linux/Desktop/hello.txt', 'a') # add 添加
hellofile.write('it is okay\n')
hellofile.close()
hellofile = open('/home/linux/Desktop/hello.txt', 'r') # read
hellocontent = hellofile.read()
print(hellocontent)

# shelve模块
import shelve

shelfFile = shelve.open('/home/linux/Desktop/hello/mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('/home/linux/Desktop/hello/mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('/home/linux/Desktop/hello/mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

# pprint.pformat()函数保存变量
import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name':'Pooka', 'desc':'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

import myCats        # 导入myCats文件
print(myCats.cats)
print(myCats.cats[0]['name'])