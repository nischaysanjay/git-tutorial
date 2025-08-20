# gfg.py - A simple calculator module
# This module provides basic arithmetic operations: addition, subtraction,
# multiplication, and division.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

if __name__ == "__main__":
    print("Basic Calculator")
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
    print("6 * 7 =", multiply(6, 7))
    print("20 / 5 =", divide(20, 5))
