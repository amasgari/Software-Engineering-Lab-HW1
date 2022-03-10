import math
from ErrorMessages import ErrorMessages


class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return ErrorMessages.DivZero

    def power(self, a, b):
        if a > 0:
            return a ** b
        if a == 0:
            if b > 0:
                return a ** b
            else:
                return ErrorMessages.ZeroBadPow
        return ErrorMessages.NegBasePow

    def log(self, a, b):
        if a < 0:
            return ErrorMessages.InNumber
        elif b <= 0:
            return ErrorMessages.InBase
        try:
            return math.log(a, b)
        except:
            return ErrorMessages.InvalidOperand
