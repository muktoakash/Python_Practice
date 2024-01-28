"""Not ideal code."""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    with open(args.filename) as f:
        print(f.read())


if __name__ == '__main__':
    main()
