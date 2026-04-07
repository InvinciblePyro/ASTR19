import numpy as np
import sys

def log_10(x): 
    return np.log(x)

def print_log10(n):
    for i in range(n):
        print(log_10(i))

def main():
    n = 10

    if len(sys.argv) > 1: 
        n = int(sys.argv[1])

    print_log10(n)


if __name__ == '__main__':
    main()