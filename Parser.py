import re
from ErrorMessages import *


class Parser:
    def __init__(self):
        pass

    def isNumber(self, n):
        try:
            a = float(n)
            return True
        except:
            return False

    def parse(self, str_inp):
        t_inputs = str_inp.split(' ')
        inputs = []
        for inp in t_inputs:
            inputs.append(inp.strip())
        if len(inputs) < 3:
            return ErrorMessages.UnknownFormat
        else:
            if self.isNumber(inputs[0]) & self.isNumber(inputs[2]):
                operand1, operand2 = float(inputs[0]), float(inputs[2])
                operator = inputs[1]
                if operator in ['+', '-', '/', '*']:
                    return operand1, operand2, operator
                else:
                    return ErrorMessages.UnOperator
            else:
                return ErrorMessages.InOperand
