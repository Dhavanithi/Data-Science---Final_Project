from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

def data_transformation(df):

    print("\n----- DATA TRANSFORMATION -----")

    numeric_cols = df.select_dtypes(include='number').columns

    
    print("-------Normalization (Min-Max Scaling)-------")
    
    minmax_scaler = MinMaxScaler()
    df_normalized = pd.DataFrame(
        minmax_scaler.fit_transform(df[numeric_cols]),
        columns=numeric_cols
    )

    print("\nNormalized Data (First 5 Rows):")
    print(df_normalized.head())

    
    print("-------Standardization (Z-Score Scaling)-------")
    
    standard_scaler = StandardScaler()
    df_standardized = pd.DataFrame(
        standard_scaler.fit_transform(df[numeric_cols]),
        columns=numeric_cols
    )

    print("\nStandardized Data (First 5 Rows):")
    print(df_standardized.head())

    return df_normalized, df_standardized
