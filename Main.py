from Calculator import Calculator
from ErrorMessages import ErrorMessages
from Operator import Operator
from Parser import Parser

calculator = Calculator()
parser = Parser()

while True:
    inp = str(input())
    if inp == 'EXIT':
        break
    else:
        parse_result = parser.parse(inp)
        out = ''
        if type(parse_result) is ErrorMessages:
            out = parse_result
        else:
            if parse_result[2] == Operator.Plus:
                out = calculator.add(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Minus:
                out = calculator.subtract(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Multiply:
                out = calculator.multiply(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Division:
                out = calculator.divide(parse_result[0], parse_result[1])
        print(out)
