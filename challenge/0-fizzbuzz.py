#!/usr/bin/python3
"""FizzBuzz implementation"""
import sys


def fizzbuzz(n):
    """Print FizzBuzz sequence up to n"""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()


if __name__ == "__main__":
    fizzbuzz(int(sys.argv[1]))
