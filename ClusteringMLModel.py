import pandas as pd
import json
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
sales_data = pd.read_csv('C:\\Users\\suren\\OneDrive\\Documents\\GitHub\\sampleBabylonStockingShelf\\data\\mock_sales_data.csv')
inventory_data = pd.read_csv('C:\\Users\\suren\\OneDrive\\Documents\\GitHub\\sampleBabylonStockingShelf\\data\\mock_inventory_data.csv')
customer_data = pd.read_csv('C:\\Users\\suren\\OneDrive\\Documents\\GitHub\\sampleBabylonStockingShelf\\data\\mock_customer_data.csv')
store_layout_data = pd.read_csv('C:\\Users\\suren\\OneDrive\\Documents\\GitHub\\sampleBabylonStockingShelf\\data\\mock_store_layout_data.csv')

# Example: Using KMeans clustering to find patterns in sales and inventory data
# Combining sales and inventory data for analysis
combined_data = pd.merge(sales_data, inventory_data, on=['AisleNumber', 'StockingSection'])

# Selecting relevant features for clustering (example: sales and inventory levels)
features = combined_data[['SalesIn365Days', 'CurrentInventoryLevels']]

# Clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(features)
clusters = kmeans.predict(features)

# Adding cluster information to the data
combined_data['Cluster'] = clusters

# Assigning a recommended aisle based on clustering
# Here, we simply use the next aisle in the same cluster as a recommendation
combined_data['RecommendedAisle'] = combined_data.groupby('Cluster')['AisleNumber'].shift(-1).fillna(combined_data.groupby('Cluster')['AisleNumber'].shift(1))

#Visualization Plotting of Clusters
colors = ['blue', 'green', 'red']  # Define different colors for each cluster
for cluster in set(clusters):
    cluster_data = combined_data[combined_data['Cluster'] == cluster]
    plt.scatter(cluster_data['SalesIn365Days'], cluster_data['CurrentInventoryLevels'], color=colors[cluster], label=f'Cluster {cluster}')

plt.xlabel('Annual Sales')
plt.ylabel('Current Inventory Levels')
plt.title('Aisle Clustering based on Sales and Inventory')
plt.legend()  # Add a legend
plt.savefig('C:\\Users\\suren\\OneDrive\\Documents\\GitHub\\sampleBabylonStockingShelf\\data\\aisle_clustering_plot.png')
plt.show()

# Compute the mean values for sales and inventory in each cluster
cluster_means = combined_data.groupby('Cluster').mean()[['SalesIn365Days', 'CurrentInventoryLevels']]

print(cluster_means)

# Attempt to identify the cluster with high sales and low inventory
try:
    high_sales_low_inventory_cluster = cluster_means[
        (cluster_means['SalesIn365Days'] > cluster_means['SalesIn365Days'].median()) & 
        (cluster_means['CurrentInventoryLevels'] < cluster_means['CurrentInventoryLevels'].median())
    ].index[0]
    print(f"Cluster with high sales and low inventory: Cluster {high_sales_low_inventory_cluster}")
except IndexError:
    print("No cluster found with high sales and low inventory based on the median criteria.")

# If the above fails, inspect cluster_means manually to determine the appropriate cluster

# Making recommendations based on clusters
# Example: Aisles in high-sales, low-inventory cluster might need a layout reset
recommendations = combined_data[combined_data['Cluster'] == 1]  # Assumption: Cluster 1 is high-sales, low-inventory

# Preparing data for JSON conversion
recommendations_json = []
for index, row in recommendations.iterrows():
    recommendation = {
        "stockingSection": row['StockingSection'],
        "currentAisle": row['AisleNumber'],
        "recommendedAisle": row['RecommendedAisle']
    }
    recommendations_json.append(recommendation)

# Convert to JSON
recommendations_json_str = json.dumps(recommendations_json, indent=4)

# Print or save the JSON data
print(recommendations_json_str)
