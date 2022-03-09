from Calculator import Calculator
from ErrorMessages import ErrorMessages
from Operator import Operator
from Parser import Parser

calculator = Calculator()
parser = Parser()

while True:
    print("Please enter your command, for exit type EXIT")
    inp = str(input())
    if inp == 'EXIT':
        break
    else:
        parse_result = parser.parse(inp)
        out = ''
        if type(parse_result) is ErrorMessages:
            out = parse_result
        else:
            if parse_result[2] == Operator.Plus.value:
                out = calculator.add(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Minus.value:
                out = calculator.subtract(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Multiply.value:
                out = calculator.multiply(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Division.value:
                out = calculator.divide(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.log.value:
                out = calculator.log(parse_result[0], parse_result[1])
        print(out)
