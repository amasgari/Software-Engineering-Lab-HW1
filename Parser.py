import re

class Parser:
    def __init__(self):
        pass

    def parse(self, str_inp):
        if re.search("[0-9]+[+\-*/][0-9]+", str_inp) is not None:
            pass
        else:
            print("Invalid format of input")
