import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def clean_data(df):

    print("\n----- DATA CLEANING -----")

    
    print("-------Handling Missing Values-------")
    
    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum())

    print("-------Fill numeric missing values with mean-------")
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())

    print("\nMissing Values After Filling:")
    print(df.isnull().sum())

    
    print("-------Remove Duplicate Records-------")
    
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]

    print("\nDuplicate Rows Removed:", before - after)

    
    print("-------Outlier Detection (Boxplot)-------")
    
    for col in numeric_cols:
        plt.figure()
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot for {col}")
        plt.show()

        print("-------IQR Method-------")
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

    print("\nOutliers handled using IQR method")

    return df
