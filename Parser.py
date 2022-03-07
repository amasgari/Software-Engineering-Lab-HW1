import re
from ErrorMessages import *

class Parser:
    def __init__(self):
        pass

    def parse(self, str_inp):
        if re.search("[0-9]+[+*/-][0-9]+", str_inp):
            operand1, operand2 = [int(x) for x in re.split("[+*/-]", str_inp)]
            operator = re.findall("[+*/-]", str_inp)[0]
            return operand1, operand2, operator
        elif re.search("[0-9]+[^+*/-][0-9]+", str_inp):
            return ErrorMessages.UnOperator
        elif re.search("[^0-9]*[+*/-][0-9]+") or re.search("[0-9]+[+*/-][^0-9]*"):
            return ErrorMessages.InOperand
        else:
            return