# python3
# pw.py - An insecure password locker program(口令保管箱)

# Step1 程序设计和数据结构
# 字典是组织的帐号和口令的数据结构

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VMALvQyKAxiVH5G8v01if1MLZF3std',
             'luggage':'123456'}

# Step2 处理命令行参数
import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: Python pw.py [accout] - copy accout password')
    sys.exit()

account = sys.argv[1]

# Step3 复制正确口令

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else :
    print('There is no account named ' + account)