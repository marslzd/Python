# 习题9.8.1 选择性拷贝
import os
import re
import shutil

# find 扩展名 的方法 正则表达，字符串endswith
# PDFRegex = re.compile(r'.*.pdf')
# print(PDFRegex.search('ll1.pdf'))
# a = 'llll.pdf'
# print(a.endswith('.pdf'))

Filepath = '/home/linux/Desktop/Test'
NewFolderPath = '/home/linux/Desktop/Test_C'
findsuffix = '.pdf'

def CopyFileToNewFolder(source, destination, findsuffix):
    '''
    该函数用于查找特定扩展名文件，并copy到新文件夹
    Bug：未考虑相同文件名称
    '''
    # if destination folder doesn't exist, make destination directory
    if os.path.exists(destination) == False:
        os.makedirs(destination)
    
    # 遍历目录树and Copy file to NewPath
    for foldername, subfolders, filenames in os.walk(source):
        print(foldername)
        # for subfolder in subfolders:
        #     print(foldername + subfolder)
        for filename in filenames:
            print(foldername + '/' +filename)
            if filename.endswith(findsuffix):
                # Bug the same file name
                print("Copying File ...")
                # Copy to New folder
                shutil.copy(foldername+'/'+filename, destination)   
                
    
CopyFileToNewFolder(Filepath, NewFolderPath, findsuffix)