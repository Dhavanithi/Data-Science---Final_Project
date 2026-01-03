import seaborn as sns
import matplotlib.pyplot as plt

def advanced_visualization(df):

    print("\n----- ADVANCED VISUALIZATION -----")

    numeric_cols = df.select_dtypes(include='number').columns

    
    print("-------Pair Plot-------")
    
    sns.pairplot(df[numeric_cols])
    plt.suptitle("Pair Plot of Numeric Features", y=1.02)
    plt.show()

    
    print("-------Correlation Heatmap-------")
    
    plt.figure(figsize=(8,5))
    corr_matrix = df[numeric_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

   

    print("\nCorrelation Matrix:")
    print(corr_matrix)

    print("-------Covariance Heatmap-------")
    
    plt.figure(figsize=(8,5))
    cov_matrix = df[numeric_cols].cov()
    sns.heatmap(cov_matrix, annot=True, cmap="viridis")
    plt.title("Covariance Heatmap")
    plt.show()

    print("\nCovariance Matrix:")
    print(cov_matrix)