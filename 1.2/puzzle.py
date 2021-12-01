import functools as fn
import itertools as it
import sys


def read_input(file: str) -> list[int]:
    with open(file) as f:
        return [int(line.strip()) for line in f]


def main():
    try:
        values = read_input(sys.argv[1])
    except IndexError:
        print('Please provide an input file as the first argument', file=sys.stderr)
        exit(1)
    for combo in it.combinations(values, 3):
        if sum(combo) == 2020:
            print(fn.reduce(int.__mul__, combo))
            exit(0)
    print("No valid combination found")
    exit(1)


if __name__ == '__main__':
    main()
