#!/usr/bin/python3
"""FizzBuzz implementation"""
import sys


def fizzbuzz(n):
    """Print FizzBuzz sequence up to n"""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    print(" ".join(result))


if __name__ == "__main__":
    fizzbuzz(int(sys.argv[1]))
