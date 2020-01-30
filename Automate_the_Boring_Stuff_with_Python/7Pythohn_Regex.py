# 不用正则表达式来查找文本模式
# isPhoneNumber
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number : ')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is  a phone number: ')
print(isPhoneNumber('Moshi moshi'))

# 正则式表达
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My phone number is 415-555-4242')
print('Phone number found : ' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is 415-555-4242')
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group())
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# 用管道匹配多个分组|
heroRegx = re.compile(r'Batman|Tina Fey')
mo1 = heroRegx.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegx.search('Tina Fey and Batman')
print(mo2.group())

batRegx = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegx.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# 用问号实现可选匹配
batRegx = re.compile(r'Bat(wo)?man')
mo1 = batRegx.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegx.search('The adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# 用星号匹配零次或多次
batRegx = re.compile(r'Bat(wo)*man')
mo1 = batRegx.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegx.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegx.search('The advetures of  Batwowowowoman')
print(mo3.group())

# 用加号匹配一次或多次
batRegx = re.compile(r'Bat(wo)+man')
mo1 = batRegx.search('The adventures of Batwoman')
print(mo1.group())
mo2 = batRegx.search('The adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegx.search('The advetures of  Batman')
print(mo3 == None)

# 用花括号匹配特定次数
# (Ha){3} <=>  (Ha)(Ha)(Ha)
# (Ha){3, 5} <=> ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)

# 贪心和非贪心匹配
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# findall()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
mo = phoneNumRegex.search('Cell : 415-555-4242 Work : 215-555-0000')
print(mo.group())
print(phoneNumRegex.findall('Cell : 415-555-4242 Work : 215-555-0000'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
print(phoneNumRegex.findall('Cell : 415-555-4242 Work : 215-555-0000'))

# 字符分类
# \d   0到9任何数字
# \D   除0到9任何数字之外任何字符
# \w   任何字母、数字、下划线字符（单词）
# \W   除任何字母、数字、下划线字符之外任何字符
# \s   空格、制表位或换行符
# \S   除空格、制表位或换行符之外任何字符
xmasRegex = re.compile(r'\d+\s+\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids \
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# 建立自己的字符分类
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

consonantRegex = re.compile(r'[^aeiouAEIOU]')    # ^ 非
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# 插入字符和美元字符
## 匹配以字符串hello开始的字符串
beginWithHello = re.compile(r'^Hello')
beginWithHello.search('Hello world!')
print(beginWithHello.search('Hello world!'))
print(beginWithHello.search('He said hello.') == None)

## 匹配以数字0-9结束的字符串
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('You number is 42'))
print(endsWithNumber.search('You number is two') == None)

## 匹配从开始到结束都是数字的字符串
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('123xyz4567890') == None)
print(wholeStringIsNum.search('1234 567890') == None)

# 通配字符
## . 匹配除了换行以外的所有字符 
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat. '))

# 用点-星匹配所有字符
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# 用句点字符匹配换行
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the law.')
print(mo.group())

newlineRegex = re.compile('.*', re.DOTALL) # re.DOTALL匹配所有字符
mo1 = newlineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the law.')
print(mo1.group())

# 不区分大小写的匹配
regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent. ').group())
print(robocop.search('Al, why does you talk about robocop so ?').group())

# 用sub方法代替字符串
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub(r'CENSORED', 'Agent Alice gave the  secrect documents to Agent Bob'))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that \
Eve knew Agent Bob was a double agent.'))

# 管理复杂的正则表达式
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?         # separator
    \d{3}              # first 3 digits
    (\s|-|\.)          # separator
    \d{4}              # last 4 digits
    (\S*(ext|x|ext.)\s*\d{2,5})?   #extension
)''', re.VERBOSE)

# 组合使用re.IGNORECASE,re.DOTALL,re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
