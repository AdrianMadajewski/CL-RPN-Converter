"""
This scripts transforms given expression of predicate calculus in RPN to it's infix equivalent

:creator Adrian Madajewski Politechnika Poznanska 2019 (C)
:date 2019-11-16
:version 1.0.1
"""

from functions import transform_rpn
from sys import stdin

print('Predicate calculus RPN converter by Adrian Madajewski I6.1')
print('Enter expressions or "exit" to exit: ')
isRunning: bool = True

if __name__ == '__main__':
    try:
        while stdin and isRunning:
            user_expression: str = input()
            if user_expression == 'exit':
                isRunning = False
            else:
                print(transform_rpn(user_expression))
        else:
            print('Quitting...')
    except EOFError:
        print('EOFError - quitting...')
