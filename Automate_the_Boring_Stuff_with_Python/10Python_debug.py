# Debug

# 抛出异常
# raise语句 - Execption()
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single chatacter string. ')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol*width)
    for i in range(height -2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

# 取得反向跟踪的字符串
# def spam():
#     bacon()

# def bacon():
#     raise Exception('This is the error message. ')

# spam()

import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('/home/linux/Desktop/errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')

# 断言
# assert语句
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that. '
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open"' 

# 在交通灯模拟中使用断言
# 'ns' north south 'ew' east west
# market_2nd = {'ns': 'green', 'ew': 'red'}
# mission_16th = {'ns': 'red', 'ew': 'green'}

# def switchLights(stoplight):
#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] == 'red'
#         elif stoplight[key] == 'red':
#             stoplight[key] = 'green'

# switchLights(market_2nd)

# 禁用断言
# 日志
# 使用日志模块
import logging
logging.basicConfig(filename='/home/linux/Desktop/myprogramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program. ')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *=  i
        logging.debug('i is ' + str(i) +', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program. ')
# 不要用print调试
# 日志级别
# 禁用日志
logging.disable(logging.CRITICAL)
# 将日志记录到文件
# import logging
# logging.basicConfig(filename='/home/linux/Desktop/myprogramLog.txt', level=logging.DEBUG, \
#     format='%(asctime)s - %(levelname)s - %(message)s')
