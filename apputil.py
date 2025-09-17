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


def task_1():
  
    #Return a list of all column names, sorted by the number of missing values.

    df = df_bellevue.copy()

    # Clean gender column: sometimes might be inconsistent, e.g. 'M ', 'F', etc.
    if 'gender' in df.columns:
        df['gender'] = df['gender'].str.strip().str.upper()
        print("Cleaned gender column: stripped spaces and uppercased values.")

    # Count missing values
    missing_counts = df.isna().sum()

    # Sort columns by missing value counts
    sorted_cols = missing_counts.sort_values(ascending=True).index.tolist()
    return sorted_cols











