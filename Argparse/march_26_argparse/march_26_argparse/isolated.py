"""Better code."""
import argparse


def get_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser.parse_args(args)


def get_file_contents(path):
    with open(path) as file:
        return file.read()


def main(args=None):
    args = get_args(args)
    data = get_file_contents(args.filename)
    print(data)


if __name__ == '__main__':
    main()
