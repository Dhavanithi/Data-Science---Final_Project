import matplotlib.pyplot as plt

def basic_visualization(df):

    print("\n----- BASIC VISUALIZATION -----")

    numeric_cols = df.select_dtypes(include='number').columns

    
    print("-------Line Plot-------")
    
    plt.figure(figsize=(8,5))
    plt.plot(df[numeric_cols[0]], label=numeric_cols[0])
    plt.title("Line Plot of " + numeric_cols[0])
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.show()

    
    print("-------Bar Chart-------")
    
    plt.figure(figsize=(8,5))
    plt.bar(df.index[:10], df[numeric_cols[0]].head(10), edgecolor='black')
    plt.title("Bar Chart of " + numeric_cols[0])
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

    
    print("-------Histogram-------")
    
    plt.figure(figsize=(8,5))
    plt.hist(df[numeric_cols[0]], bins=10, edgecolor='black')
    plt.title("Histogram of " + numeric_cols[0])
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
