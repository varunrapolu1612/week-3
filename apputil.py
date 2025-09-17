import seaborn as sns
import pandas as pd

#EXERCOSE: 1

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#EXERCOSE: 2

def to_binary(n):
    # Base case
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return to_binary(n // 2) + str(n % 2)

#EXERCOSE: 3










