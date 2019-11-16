"""
Examples.py provided to test RPN to infix transform function
'Z X X a f/2 p/1 ∃ Y Y Z f/1 p/2 FORALL → FORALL' this one can't be properly decoded
that's why it's removed from the data file
"""
from functions import transform

with open('data', 'r') as data:
    try:
        for line in data:
            print(transform(line))
    except UnicodeDecodeError:
        print('Invalid expression - charmap codec cant decode')
