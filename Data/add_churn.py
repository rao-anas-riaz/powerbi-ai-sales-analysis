import pandas as pd
import numpy as np

# This assumes you have a 'customers.csv' in the same directory
try:
    customers_df = pd.read_csv('customers.csv')
    
    # Add a churn column. We'll simulate a 15% churn rate.
    customers_df['IsChurned'] = np.random.rand(len(customers_df)) < 0.15
    
    # Save the updated DataFrame back to the same file
    customers_df.to_csv('customers.csv', index=False)
    
    print("Successfully added 'IsChurned' column to customers.csv and saved it.")
except FileNotFoundError:
    print("Error: 'customers.csv' not found. Make sure it's in the same folder as this script.")
