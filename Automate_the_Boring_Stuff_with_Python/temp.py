# 习题7.18.2 strip()的正则表达式

import re

def strip_manual(str_case, str_design=None):
    print('No error')

stripRegex = re.compile(r'(\S+)')
print(stripRegex.findall(' Hello worlld Hel_lo'))