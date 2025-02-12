import pandas as pd

# Load the dataset
final_df = pd.read_csv('./data/cleaned_final_data.csv')

# Debugging: Check column names and dataset structure
print("Columns in final_df:", final_df.columns)
print("First few rows of final_df:\n", final_df.head())

# Step 1: Handle timestamp column
# Convert the 'timestamp' column to datetime format
final_df['timestamp'] = pd.to_datetime(final_df['timestamp'], errors='coerce')

# Drop rows with invalid timestamps (if any)
final_df = final_df.dropna(subset=['timestamp'])

# Step 2: Add 'day_of_week' column (as numbers)
# Extract the day of the week as an integer (Monday=0, Sunday=6)
final_df['day_of_week'] = final_df['timestamp'].dt.dayofweek

# Step 3: Clean the 'property' column
# Filter out rows where 'property' is not a numerical value
final_df = final_df[final_df['property'].astype(str).str.isnumeric()]

# Convert the 'property' column to integers (since it should now contain only numbers)
final_df['property'] = final_df['property'].astype(int)

# Step 4: Clean the 'value' column
# Standardize numerical values in the 'value' column
# Remove prefixes like 'n' and suffixes like '.000' and convert to numerical values
final_df['value'] = final_df['value'].astype(str).str.replace('n', '').str.replace('.000', '').str.strip()
final_df['value'] = pd.to_numeric(final_df['value'], errors='coerce')  # Convert to numeric, set invalid values to NaN

# Handle zero values in the 'value' column
# Replace zeros with NaN if they represent missing data
final_df['value'] = final_df['value'].replace(0, pd.NA)

# Step 5: Drop the 'status' column (if it exists)
if 'status' in final_df.columns:
    final_df.drop(columns=['status'], inplace=True)

# Step 6: Handle missing values
# Drop rows with missing values in essential columns
final_df.dropna(subset=['visitor_id', 'action', 'item_id', 'property', 'value'], inplace=True)

# Step 7: Remove duplicates
final_df.drop_duplicates(inplace=True)

# Step 8: Ensure all columns have consistent and meaningful values
# Replace any remaining 'NaN' or 'None' values in the 'value' column with 0 (if appropriate)
final_df['value'].fillna(0, inplace=True)

# Debugging: Check final dataset structure
print("Columns after cleaning:", final_df.columns)
print("First few rows after cleaning:\n", final_df.head())

# Save the further cleaned data to a new CSV file
final_df.to_csv('./data/cleaned_final_data.csv', index=False)

print("Data cleaning completed!")