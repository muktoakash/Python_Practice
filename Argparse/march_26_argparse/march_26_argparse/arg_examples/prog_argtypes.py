import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=False)
parser.add_argument('-o', '--output', required=True)
parser.add_argument('-q', '--quiet', action='store_true')
parser.add_argument('-v', '--verbose', action='count')

args = parser.parse_args()

print('Input file:', args.input)
print('Output file:', args.output)
