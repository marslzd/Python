# Python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import re

# Create phone regex 

# phone number : 400-800-7200
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # area code
    (\s|-|\.)?           # separator
    (\d{3})              # first 3 digits
    (\s|-|\.)            # separator
    (\d{4})              # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?   #extension
)''', re.VERBOSE)

# Create email regex
# email : in12fo@nostarch.com
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+        # username
    @                        # @ symbol
    [a-zA-Z0-9.-]+           # domain name
    (\.[a-zA-Z]{2,4})        # dot-something
)''', re.VERBOSE)

# Find matches in clipboard
# text 
text = '400-128-7200 500-899-8989 in12fo@nostarch.com mmwr@163.com'
# print(type(text))
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[7] != '':
        phoneNum += ' x' + groups[7]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])
    print(matches)

# Copy resutls to the clipboard
if len(matches) > 0:
    print('Phone numbers or emial addresses found : ')
    print('\n'.join(matches))
else:
    print('No phone numbers or emial addresses found.')