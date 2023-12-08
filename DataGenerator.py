import pandas as pd
import numpy as np
import random
import json

# Load the JSON data
file_path = '/Store_Stocking_Data.json'
with open(file_path, 'r') as file:
    stocking_data = json.load(file)

# Define the columns for each data type
sales_data_columns = ['AisleNumber', 'StockingSection', 'SalesIn30Days', 'SalesIn90Days', 'SalesIn365Days', 'HistoricSalesIn2Years', 'HistoricSalesIn5Years']
inventory_data_columns = ['AisleNumber', 'StockingSection', 'CurrentInventoryLevels', 'InventoryTurnoverRate', 'StockOutFrequency', 'ProductRestockRates']
customer_data_columns = ['AisleNumber', 'StockingSection', 'CustomerInteractions', 'CustomerDemographics', 'CustomerFeedback']
store_layout_data_columns = ['AisleNumber', 'StockingSection', 'AisleTrafficFlow', 'ShelfSpaceUtilization', 'ProductPlacementEfficiency']
external_factors_columns = ['AisleNumber', 'StockingSection', 'LocalEvents', 'EconomicIndicators']
supply_chain_data_columns = ['AisleNumber', 'StockingSection', 'SupplierPerformance', 'DeliveryTimes']

# Create DataFrames for each data type
sales_data = pd.DataFrame(columns=sales_data_columns)
inventory_data = pd.DataFrame(columns=inventory_data_columns)
customer_data = pd.DataFrame(columns=customer_data_columns)
store_layout_data = pd.DataFrame(columns=store_layout_data_columns)
external_factors_data = pd.DataFrame(columns=external_factors_columns)
supply_chain_data = pd.DataFrame(columns=supply_chain_data_columns)

# Populate DataFrames with mock data
for aisle_data in stocking_data:
    aisle_number = aisle_data['aisleNumber'] if 'aisleNumber' in aisle_data else 'A0'
    stocking_section = aisle_data['stockingSection']

    sales_data = sales_data.append({**{'AisleNumber': aisle_number, 'StockingSection': stocking_section}, **{col: np.random.randint(1000, 10000) for col in sales_data_columns[2:]}}, ignore_index=True)
    inventory_data = inventory_data.append({**{'AisleNumber': aisle_number, 'StockingSection': stocking_section}, **{col: np.random.random() * 100 for col in inventory_data_columns[2:]}}, ignore_index=True)
    customer_data = customer_data.append({**{'AisleNumber': aisle_number, 'StockingSection': stocking_section}, **{col: random.choice(['High', 'Medium', 'Low']) for col in customer_data_columns[2:]}}, ignore_index=True)
    store_layout_data = store_layout_data.append({**{'AisleNumber': aisle_number, 'StockingSection': stocking_section}, **{col: np.random.random() for col in store_layout_data_columns[2:]}}, ignore_index=True)
    external_factors_data = external_factors_data.append({**{'AisleNumber': aisle_number, 'StockingSection': stocking_section}, **{col: random.choice(['Event1', 'Event2', 'None']) for col in external_factors_columns[2:]}}, ignore_index=True)
    supply_chain_data = supply_chain_data.append({**{'AisleNumber': aisle_number, 'StockingSection': stocking_section}, **{col: random.choice(['Good', 'Average', 'Poor']) for col in supply_chain_data_columns[2:]}}, ignore_index=True)

# Save DataFrames to CSV files
sales_data.to_csv('/data/mock_sales_data.csv', index=False)
inventory_data.to_csv('/data/mock_inventory_data.csv', index=False)
customer_data.to_csv('/data/mock_customer_data.csv', index=False)
store_layout_data.to_csv('/data/mock_store_layout_data.csv', index=False)
external_factors_data.to_csv('/data/mock_external_factors_data.csv', index=False)
supply_chain_data.to_csv('/data/mock_supply_chain_data.csv', index=False)