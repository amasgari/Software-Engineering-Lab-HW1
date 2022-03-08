import re
from ErrorMessages import *


class Parser:
    def __init__(self):
        pass

    def getNumber(self, n):
        try:
            if 'e' in n or 'E' in n:
                num_parts = re.split('e|E', n)
                mantissa = float(num_parts[0])
                exponent = float(num_parts[1])
                return mantissa * 10 ** exponent
            else:
                return float(n)
        except:
            return False

    def parse(self, str_inp):
        t_inputs = str_inp.split(' ')
        inputs = []
        for inp in t_inputs:
            inputs.append(inp.strip())
        if len(inputs) != 3:
            return ErrorMessages.UnknownFormat
        else:
            operand1, operand2 = self.getNumber(inputs[0]), self.getNumber(inputs[2])
            operator = inputs[1]
            if not operand1 or not operand2:
                return ErrorMessages.InOperand
            if operator not in ['+', '-', '/', '*']:
                return ErrorMessages.UnOperator
            return operand1, operand2, operator
