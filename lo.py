from string import ascii_uppercase
from time import sleep
from sys import stdin

operators = ['NOT', '~', '¬', 'AND', '&', '∧', 'OR,' '|', '∨', 'IMPLIES', '→', 'IFF', '↔', 'XOR', '⊕']
predicts = ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
functions = ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
quantifiers = ['FORALL', '∀', 'EXISTS', '∃']
consts = ['a', 'b', 'c', 'd', 'e']
variables = list(ascii_uppercase)


def is_operand(token: str):
    return token in consts + variables + functions + predicts


def handle_function_or_predict(size: int, stack: list):
    name = stack.pop()
    listed_arguments = []
    for i in range(size):
        listed_arguments.append(stack.pop())

    # reversed because of appeared order
    return name + '(' + ', '.join(reversed(listed_arguments)) + ')'


def handle_quantifier(quantifier: str, stack: list):
    expression = stack.pop()
    variable = stack.pop()
    return '({} {} {})'.format(quantifier, variable, expression)


def handle_not(token: str, stack: list):
    return '(' + token + ' ' + stack.pop() + ')'


def handle_double_operators(token: str, stack: list):
    op_expression1 = stack.pop()
    op_expression2 = stack.pop()
    return '({} {} {})'.format(op_expression2, token, op_expression1)


def evaluate(expression: str):
    tokens = expression.replace('/', ' ').split()
    stack = []
    for token in tokens:

        if is_operand(token):
            stack.append(token)

        elif token.isdigit():
            output = handle_function_or_predict(int(token), stack)
            stack.append(output)

        elif token in quantifiers:
            output = handle_quantifier(token, stack)
            stack.append(output)

        elif token in operators:
            if token in ['NOT', '~', '¬']:
                output = handle_not(token, stack)
                stack.append(output)
            else:
                output = handle_double_operators(token, stack)
                stack.append(output)

    return stack.pop()


print('Computational logic RPN converter by Adrian Madajewski I6.2')
print('Enter expressions or "exit" to exit: ')
isRunning = True

try:
    while stdin and isRunning:
        user_expression = input()
        if user_expression == 'exit':
            isRunning = False
        else:
            print(evaluate(user_expression))
    else:
        print('Quitting...')
        sleep(1)
except EOFError:
    print('EOFError - quitting...')
    sleep(1)
