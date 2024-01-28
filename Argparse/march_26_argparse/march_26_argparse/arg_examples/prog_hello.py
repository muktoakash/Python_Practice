import argparse

parser = argparse.ArgumentParser()
parser.add_argument('word', help='specify word to be printed')
args = parser.parse_args()

print(args.word)
