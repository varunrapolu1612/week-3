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
    Return a list of all column names, sorted by missing values (least -> most).
    Fix gender column issue. Preserve original column order for ties.
    """
    df = df_bellevue.copy()

    # Clean gender column
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.strip().str.upper()
        print("Cleaned gender column: stripped spaces and uppercased values.")

    # Count missing values
    missing_counts = df.isna().sum()

    # Use stable sort to preserve original column order in case of tie
    sorted_cols = missing_counts.sort_values(kind="stable").index.tolist()

    return sorted_cols

# Task 2

def task_2():
    """
    Return a dataframe with year and total_admissions per year.
    Extracts year from 'date_in'.
    """
    df = df_bellevue.copy()

    if "year" not in df.columns:
        if "date_in" in df.columns:
            # Convert to datetime
            df["date_in"] = pd.to_datetime(df["date_in"], errors="coerce")
            # Drop rows where date_in could not be parsed
            df = df.dropna(subset=["date_in"])
            df["year"] = df["date_in"].dt.year
        else:
            print("Error: No 'year' or 'date_in' column found.")
            return pd.DataFrame(columns=["year", "total_admissions"])

    admissions = (
        df.groupby("year")
          .size()
          .reset_index(name="total_admissions")
          .sort_values("year")  # sort by year ascending
          .reset_index(drop=True)
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
    Ignores missing values.
    """
    df = df_bellevue.copy()

    if "profession" not in df.columns:
        print("Warning: No 'profession' column found.")
        return []

    # Strip and lowercase, but keep NaN as NaN
    df["profession_clean"] = df["profession"].str.strip().str.lower()

    # Drop missing values before counting
    common_prof = (
        df["profession_clean"]
        .dropna()
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    print("Cleaned profession column: lowercased and stripped whitespace (NaNs ignored).")
    return common_prof


