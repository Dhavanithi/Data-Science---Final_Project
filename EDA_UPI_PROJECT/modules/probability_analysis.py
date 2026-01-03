import matplotlib.pyplot as plt
import seaborn as sns

def probability_analysis(df):

    print("\n----- PROBABILITY ANALYSIS -----")

    numeric_cols = df.select_dtypes(include='number').columns

    # Probability Distribution using Histogram + KDE
    plt.figure(figsize=(8,5))
    sns.histplot(df[numeric_cols[0]], kde=True, stat="density")
    plt.title("Probability Distribution of " + numeric_cols[0])
    plt.xlabel("Value")
    plt.ylabel("Probability Density")
    plt.show()
