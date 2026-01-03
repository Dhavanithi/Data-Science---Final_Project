from modules.data_import import load_data, export_data
from modules.data_cleaning import clean_data
from modules.transformation import data_transformation
from modules.stats_analysis import descriptive_statistics
from modules.basic_visualization import basic_visualization
from modules.advanced_visualization import advanced_visualization
from modules.probability_analysis import probability_analysis
from modules.modeling import kmeans_clustering
from modules.interactive_visualization import dashboard_visualization


print("----- EDA PROJECT STARTED -----")

# 1. Load Data
df = load_data("data/upi_data_enhanced.csv")

# 2. Clean Data
df = clean_data(df)

# 3. Export Cleaned Data
export_data(df)

# 4. Descriptive Statistics
descriptive_statistics(df)

# 5. Data Transformation
df_norm, df_std = data_transformation(df)

# 6. Basic Visualization
basic_visualization(df)

# 7. Advanced Visualization
advanced_visualization(df)

# 8. Probability Analysis
probability_analysis(df)

# 9. Modeling – KMeans
df = kmeans_clustering(df)

# 10. Interactive Visualization (Dash)
app = dashboard_visualization(df)
app.run(debug=False)

print("\nEDA PROJECT COMPLETED SUCCESSFULLY")
