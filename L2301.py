import argparse

parser = argparse.ArgumentParser(
    prog='ls',
    description='List  information about the FILEs.',
    add_help=True)
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')


parser.add_argument('path', nargs=)
parser.add_argument('-l')
parser.add_argument('-a', '--all')
args = parser.parse_args()
parser.print_help()
print(args)