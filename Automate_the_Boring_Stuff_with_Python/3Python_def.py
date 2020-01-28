# The first example

# def hello():
#     print("Howdy!")
#     print("Howdy!!")
#     print("Howdy!!!")

# hello()

def hello(name):
    print("Hello, " + name)

hello("Bob")

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again "
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9 :
        return "Very doubtful"

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

spam = print("Hello!")
print(None == spam)

# 关键字参数
print("Hello, ", end='')
print("World")

print("cats", 'dogs', 'mice')
print("cats", 'dogs', 'mice', sep=',')

# 局部和全局作用
def spam():
    eggs = 31337 # 局部
spam()
# print(eggs)

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
spam()

def spam():
    eggs = "spam local"
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)

def spam():
    global eggs
    eggs = "spam"
def bacon():
    eggs = "bacon"
def ham():
    print(eggs)

eggs = 'global'
spam()
print(eggs)

# This is a guess the number game.
import random

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20. ")

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print("Take a guess. ")
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too slow! ')
    elif guess > secretNumber:
        print('Your guess is too high! ')
    else:
        break
if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + ' guesses')
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))

# 习题3.11.1 Collatz序列
def collatz(number):
    if number >= 0:
        if number % 2 == 0:  # number is 偶数
            print(number // 2)
            return number // 2
        if number % 2 == 1:  # number is 奇数
            print(number*3 + 1)
            return number*3 + 1
    else:
        print("The number is not a ZHENGSHU")

print("Please Enter a number : ")
while True:
    User_input = input()
    try:
        User_input = int(User_input)
        collatz(User_input)
    except ValueError:
        print("You must input a 整数")
        break
    


