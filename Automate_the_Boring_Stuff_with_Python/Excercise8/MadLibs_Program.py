# Python3
# 习题8.9.2 疯狂填词 MadLibs_Program.py

import re
import os

# Change the working path == File path
Filepath = os.path.join(os.getcwd(), 'Excercise8')
print(Filepath)
os.chdir(Filepath)
print(os.getcwd())

# Read the text file
ReadText = open('TestTextFile.txt', 'r')
TextContent = ReadText.read()
ReadText.close()
# print(type(TextContent))
print(TextContent)

# Update textcontent
# Text_split = TextContent.split()
WordRegex = re.compile(r'(\w+)')
# WordRegex = re.compile(r'.*\.')
Text_split = WordRegex.findall(TextContent)
# Text_split = TextContent.split('.')
print(Text_split)

for i in range(len(Text_split)):
    if Text_split[i] == "ADJECTIVE":
        print('Enter a adjective :')
        Text_split[i] = input()
    if Text_split[i] == 'NOUN':
        print('Enter a noun :')
        Text_split[i] = input()
    if Text_split[i] == 'VERB':
        print('Enter a verb: ')
        Text_split[i] = input()

print(Text_split)
print(' '.join(Text_split))