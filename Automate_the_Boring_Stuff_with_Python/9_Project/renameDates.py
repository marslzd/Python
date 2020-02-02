# python3
# renameDates.py - Renames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

# 检查工作目录所有文件名，寻找美国风格的日期
# 如果找到，更换为欧洲风格

import os
import re
import shutil

Filepath = '/home/linux/Desktop/Hello/'
# Create a regex that matches files with the American data format.
# example : *****01-01-1984****.txt
datePattern = re.compile(r'''
    ^(.*?)                    # all text before the data
    ((0|1)?\d)                # one or two digits for the month
    -             
    ((0|1|2|3)?\d)            # one or two digits for the day
    -         
    ((19|20)\d\d)             # four digits for the year
    (.*?)$                    # all text after the date
    ''', re.VERBOSE)
# print(os.listdir(Filepath))

# Loop over the files in the working directory
for amerFilename in os.listdir(Filepath):
    mo = datePattern.search(amerFilename)
    # print(mo)
    # Skip files without a date
    if mo == None:
        continue
    
    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the Euroapean-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths
    absWorkingDir = os.path.abspath(Filepath)
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files
    print('Renaming "%s" to "%s" ...' % (amerFilename, euroFilename))
    
    # shutil.move(amerFilename, euroFilename)  # uncomment after testing



