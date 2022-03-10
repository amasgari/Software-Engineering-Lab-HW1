from Calculator import Calculator
from Operator import Operator
from Parser import Parser

while True:
    print("Please enter your command, for exit type EXIT")
    inp = str(input())
    if inp == 'EXIT':
        break
    else:
        parse_result = Parser.parse(inp)
        out = ''
        if isinstance(parse_result, str):
            out = parse_result
        else:
            if parse_result[2] == Operator.Plus.value:
                out = Calculator.add(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Minus.value:
                out = Calculator.subtract(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Multiply.value:
                out = Calculator.multiply(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Division.value:
                out = Calculator.divide(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.Power.value:
                out = Calculator.power(parse_result[0], parse_result[1])
            elif parse_result[2] == Operator.log.value:
                out = Calculator.log(parse_result[0], parse_result[1])
        print(out)
