from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def kmeans_clustering(df):

    print("\n----- K-MEANS CLUSTERING -----")

    print("-------Select numeric columns-------")
    numeric_cols = df.select_dtypes(include='number').columns

    # Use first two numeric columns for visualization
    X = df[numeric_cols[:2]]

    # Apply K-Means
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    # Scatter Plot of Clusters
    plt.figure(figsize=(8,5))
    plt.scatter(
        X.iloc[:, 0],
        X.iloc[:, 1],
        c=df['Cluster']
    )
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.title("K-Means Clustering Visualization")
    plt.show()

    # Cluster centers
    print("\nCluster Centers:")
    print(kmeans.cluster_centers_)

    return df
