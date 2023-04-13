import argparse

parser = argparse.ArgumentParser(prog='calc', description='This is a test')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))


print("""
Try the following commands:
---------------------------

calc 1 3 5

calc 10 20 40 5 --sum

calc -h
""")
