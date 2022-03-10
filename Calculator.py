import math
from ErrorMessages import ErrorMessages


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return ErrorMessages.DivZero

    @staticmethod
    def power(a, b):
        if a > 0:
            return a ** b
        if a == 0:
            if b > 0:
                return a ** b
            else:
                return ErrorMessages.ZeroBadPow
        return ErrorMessages.NegBasePow

    @staticmethod
    def log(a, b):
        if a < 0:
            return ErrorMessages.InNumber
        elif b <= 0:
            return ErrorMessages.InBase
        try:
            return math.log(a, b)
        except:
            return ErrorMessages.InvalidOperand
