import pandas as pd

def descriptive_statistics(df):

    print("\n----- DESCRIPTIVE STATISTICS -----")

    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        print(f"\nStatistics for {col}")
        print("Mean:", df[col].mean())
        print("Median:", df[col].median())
        print("Mode:", df[col].mode()[0])
        print("Standard Deviation:", df[col].std())
        print("Minimum:", df[col].min())
        print("Maximum:", df[col].max())
        print("Range:", df[col].max() - df[col].min())

    print("\nOverall Summary Statistics:")
    print(df.describe())
