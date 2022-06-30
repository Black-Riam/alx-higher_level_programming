#!/usr/bin/python3
def calc(argv):
    length = len(argv) - 1
    operands = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = operands[op](a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))


if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    calc(argv)
