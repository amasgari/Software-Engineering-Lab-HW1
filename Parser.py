import re
import unittest
from ErrorMessages import *
from Operator import Operator


class Parser:

    @staticmethod
    def getNumber(n):
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

    @staticmethod
    def parse(str_inp):
        t_inputs = str_inp.split(' ')
        inputs = []
        for inp in t_inputs:
            inputs.append(inp.strip())
        if len(inputs) != 3:
            return ErrorMessages.UnknownFormat
        else:
            operand1, operand2 = Parser.getNumber(inputs[0]), Parser.getNumber(inputs[2])
            operator = inputs[1]
            if not operand1 or not operand2:
                return ErrorMessages.InvalidOperand
            if operator not in ['+', '-', '/', '*', '^', 'log']:
                return ErrorMessages.UnsupportedOperator
            return operand1, operand2, operator


class TestParser(unittest.TestCase):
    def test_correct_operands_format(self):
        self.assertEqual(Parser.parse('2e1 + -3e0'), (20.0, -3, Operator.Plus.value))
        self.assertEqual(Parser.parse('3.2e2 * 5.0'), (320.0, 5.0, Operator.Multiply.value))
        self.assertEqual(Parser.parse('1.1 - 6E-0'), (1.1, 6.0, Operator.Minus.value))
        self.assertEqual(Parser.parse('8.4 / 11'), (8.4, 11.0, Operator.Division.value))
        self.assertEqual(Parser.parse('3e1 ^ 2'), (30.0, 2.0, Operator.Power.value))

    def test_invalid_operand_err(self):
        self.assertEqual(Parser.parse('2f1 + -4e0'), ErrorMessages.InvalidOperand)
        self.assertEqual(Parser.parse('13 % 0.3'), ErrorMessages.UnsupportedOperator)
        self.assertEqual(Parser.parse('1 3 * 0.3'), ErrorMessages.UnknownFormat)


if __name__ == '__main__':
    unittest.main()
