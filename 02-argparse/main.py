
import argparse

parser = argparse.ArgumentParser(description='This is a test')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()

if args:
    print(args.accumulate(args.integers))
else:
    print("""
Try the following commands:
---------------------------

python3 main.py 1 3 5

python3 main.py 10 20 40 5 --sum

python3 main.py -h
""")
