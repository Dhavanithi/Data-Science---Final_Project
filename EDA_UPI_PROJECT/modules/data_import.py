import pandas as pd

def load_data(path="E:/DATA SCIENCE/EDA_UPI_PROJECT/EDA_PROJECT/data/upi_data_enhanced.csv"):
    df = pd.read_csv(path)
    print("\nDataset Loaded Successfully")
    print(df.head())
    print(df.info())
    return df

def export_data(df, output_path=r"E:/DATA SCIENCE/EDA_UPI_PROJECT/EDA_PROJECT/outputs"):
    df.to_csv(f"{output_path}/upi_cleaned_data.csv", index=False)
    print("\ncleaned data saved as 'upi_cleaned_data.csv'")

