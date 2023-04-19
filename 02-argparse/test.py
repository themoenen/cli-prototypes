"""
Commands & their output:
-------

$ python3 main.py
# Formatted help


"""
import argparse
from inspect import isfunction
from collections import deque


# def calc(*args):
#     """
#     Process some integers!!
#     """
#     print(*args)
parser = argparse.ArgumentParser(prog='calc', description='This is a test')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('--mult', dest='multiply', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))


# print("Type 'calc N N N'")
# COMMAND = ''
# while COMMAND.lower() != 'quit':
#     COMMAND = input('> ')
#     args = COMMAND.split()
#     try:
#         f = eval(args[0])
#         print(f)
#         print(isfunction(f))
#         args = deque(args).popleft()
#         f(args)
#     except:
#         print('Invalid command')
