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


import pandas as pd

#Load csv file
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)

# Task 1

def task_1():
    """
    Return a list of all column names, sorted so that 
    the first has the least missing values and the last the most.
    Fixes gender column issue.
    """
    df = df_bellevue.copy()

    # Clean gender column (strip spaces, uppercase values)
    if 'gender' in df.columns:
        df['gender'] = df['gender'].astype(str).str.strip().str.upper()
        print("Cleaned gender column: stripped spaces and uppercased values.")

    # Count missing values
    missing_counts = df.isna().sum()

    # Sort by missing count, then alphabetically to break ties
    sorted_cols = (
        pd.DataFrame({"col": missing_counts.index, "missing": missing_counts.values})
        .sort_values(by=["missing", "col"], ascending=[True, True])["col"]
        .tolist()
    )
    return sorted_cols


# Task 2

def task_2():
    """
    Return a dataframe with year and total_admissions per year.
    """
    df = df_bellevue.copy()

    if "year" not in df.columns:
        print("Warning: No 'year' column found in dataset.")
        return pd.DataFrame(columns=["year", "total_admissions"])

    admissions = (
        df.groupby("year")
          .size()
          .reset_index(name="total_admissions")
    )
    return admissions



# Task 2

def task_3():
    """
    Return a series with gender as index, average age as values.
    """
    df = df_bellevue.copy()

    if "gender" not in df.columns or "age" not in df.columns:
        print("Warning: Missing required columns (gender, age).")
        return pd.Series(dtype=float)

    df["gender"] = df["gender"].astype(str).str.strip().str.upper()
    avg_age = df.groupby("gender")["age"].mean()
    return avg_age


# # Task 4

def task_4():
    """
    Return a list of the 5 most common professions in order of prevalence.
    """
    df = df_bellevue.copy()

    if "profession" not in df.columns:
        print("Warning: No 'profession' column found in dataset.")
        return []

    df["profession"] = df["profession"].astype(str).str.strip().str.lower()
    print("Cleaned profession column: lowercased and stripped whitespace.")

    common_prof = df["profession"].value_counts().head(5).index.tolist()
    return common_prof


