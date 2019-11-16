from typing import List
from constants import *


def is_symbolic(token: str) -> bool:
    """
    Checks whether given token is either a predict symbol or function name or a variable or a constant

    :param token: value to be checked
    :return: boolean value
    """
    return token in constants + variables + functions + predicts


def make_function(size: int, stack: list) -> str:
    """
    Creates symbolic str representation of a function as f(a1, a2, a3, ..., an).

    :param size: how many times to iterate over given stack
    :param stack: list with values to create arguments for given function
    :return: str object that represents created function
    """
    name: str = stack.pop()
    listed_arguments: List[str] = []
    for i in range(size):
        listed_arguments.append(stack.pop())

    # reversed because of appeared order (latest was on top of the stack)
    return name + '(' + ', '.join(reversed(listed_arguments)) + ')'


def make_quantifier(quantifier: str, stack: list) -> str:
    """
    Creates symbolic str representation of a quantifier expression such as
    FORALL X f(X), EXISTS X f(X, a) where 'X' stands for a variable, 'a' for a constant

    :param quantifier: symbol representing quantifier
    :param stack: list with values to get quantifier's expression and variable
    :return: str object that represents created quantifier
    """
    expression: str = stack.pop()
    variable: str = stack.pop()
    return '({} {} {})'.format(quantifier, variable, expression)


def make_not(token: str, stack: list) -> str:
    """
    Creates symbolic str representation of negation (LOGICAL NOT) such as
    ~ p(Z, f(Y), NOT p(X) etc.

    :param token: value or expression to be negated
    :param stack: list with values to get needed NOT expression example: ['NOT', '~', '¬']
    :return: str object that represents negation of the given expression
    """
    return '(' + token + ' ' + stack.pop() + ')'


def make_expression(operator: str, stack: list) -> str:
    """
    Creates symbolic str representation of a binary expression (2 arguments) for example:
    p(X, a) AND f(c, b), f(X) XOR p(a) etc.

    :param operator: binary operator (2 arguments needed) for an expression such as AND, OR etc.
    :param stack: list with values to get 2 arguments (operands) in order to create expression
    :return: str object that represents proper expression
    """
    operand1: str = stack.pop()
    operand2: str = stack.pop()
    # reversed because of appeared order (latest was on top of the stack)
    return '({} {} {})'.format(operand2, operator, operand1)


def transform_rpn(expression: str) -> str:
    """
    Transforms given expression of predicate calculus in RPN to infix notation

    :param expression: predicate calculus' expression given in reversed polish notation (RPN)
    :return: str object representing transformed expression to infix notation
    """
    tokens: List[str] = expression.replace('/', ' ').split()
    stack: List[str] = []
    value: str = ''

    for token in tokens:

        if is_symbolic(token):
            value = token
        elif token.isdigit():
            value = make_function(int(token), stack)
        elif token in quantifiers:
            value = make_quantifier(token, stack)
        elif token in binary_operators:
            value = make_expression(token, stack)
        elif token in negation:
            value = make_not(token, stack)
        else:
            return 'Invalid expression'

        stack.append(value)

    return stack.pop()
