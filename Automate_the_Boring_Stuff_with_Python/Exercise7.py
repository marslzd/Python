# 习题7.18.1 强口令检测

import re
passwords = '1234_ADFdddd'

# Create Regex
Upper_string = re.compile(r'[A-Z]+')    # Upper letters
Lower_string = re.compile(r'[a-z]+')    # lower letters
Num = re.compile(r'\d+')                # Numbers

def strong_passwords(passwords):
    if len(passwords) >= 8:
        if (Upper_string.search(passwords) != None) and (Lower_string.search(passwords) != None):
            if Num.search(passwords) != None:
                print("Strong Passwords")
            else:
                print('The passwords must contain number')
        else:
            print('The passwords must contain upper and lower case letters')
    else :
        print("The passwords must be at least eight characters in length.")

strong_passwords(passwords)