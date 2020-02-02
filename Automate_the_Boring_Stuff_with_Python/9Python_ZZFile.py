# 组织文件
# shutil模块
# 复制文件和文件夹
import shutil
import os

# copy file
# os.chdir('/home/linux/Desktop')
# shutil.copy('/home/linux/Desktop/hello.txt', '/home/linux/Documents/')
# copy directory
# shutil.copytree('/home/linux/Desktop/hello', '/home/linux/Desktop/hello_backup')

# 文件和文件夹的移动与改名
# shutil.move(source, destination)

# 永久删除文件和文件夹
# os.unlink(path)
for filename in os.listdir('/home/linux/Desktop/hello'):
    print(filename)
    if filename.endswith('.rxt'):
        print(filename)
        os.unlink(filename)

# 用send2trash模块安全地删除
import send2trash

# creat file
# baconfile = open('/home/linux/Desktop/bacont.txt', 'a')
# baconfile.write('Bacon is not a vegetable. ')
# baconfile.close()

# send2trash.send2trash('/home/linux/Desktop/bacont.txt')

# 遍历目录数os.walk()
import os

for folderName, subfolders, filenames in os.walk('/home/linux/Desktop/Hello/'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    
    print('')

# 用zipfile模块压缩文件
# 创建和添加到zip文件
# import zipfile
# os.chdir('/home/linux/Desktop/Hello/')
# newzip = zipfile.ZipFile('/home/linux/Desktop/Hello/new.zip', 'w')
# newzip.write('hello.txt', compress_type=zipfile.ZIP_DEFLATED)
# newzip.close()

# 读取zip文件
# import zipfile 
# import os

# os.chdir('/home/linux/Desktop/Hello/')
# exampleZip = zipfile.ZipFile('/home/linux/Desktop/Hello/new.zip')
# print(exampleZip.namelist())

# SpamInfo = exampleZip.getinfo('hello.txt')
# print(SpamInfo.file_size)
# print(SpamInfo.compress_size)

# exampleZip.close()

# 解压缩zip文件
import zipfile 
import os

os.chdir('/home/linux/Desktop/Hello/')
exampleZip = zipfile.ZipFile('new.zip')
exampleZip.extractall('/home/linux/Desktop/Hello/addwork/')  # extract some folder
exampleZip.close()



