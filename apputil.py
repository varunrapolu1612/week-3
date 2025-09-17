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
    #Load csv file
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

    df_bellevue = pd.read_csv(url)

    # Clean gender column
    if 'gender' in df_bellevue.columns:
        df_bellevue['gender'] = df_bellevue['gender'].astype(str).str.strip().str.upper()
        #print("Cleaned gender column: stripped spaces and uppercased values.")

    # Count missing values
    missing_counts = df_bellevue.isna().sum()

    # Create DataFrame with counts and column names
    col_info = pd.DataFrame({
        "col": missing_counts.index,
        "missing": missing_counts.values
    })

    # Sort by missing values, then alphabetically (to break ties)
    sorted_cols = col_info.sort_values(
        by=["missing", "col"],
        ascending=[True, True]
    )["col"].tolist()

    return sorted_cols






