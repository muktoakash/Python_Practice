import argparse

parser = argparse.ArgumentParser()
parser.add_argument('value', help='value to be squared', type=float)
args = parser.parse_args()

print(args.value ** 2)
