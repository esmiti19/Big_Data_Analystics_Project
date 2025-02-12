from sqlalchemy import create_engine
import pandas as pd

# Load the cleaned data
final_df = pd.read_csv('./data/cleaned_final_data.csv')

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:2011eb3465@localhost:5432/ecommerce1_db')

# Load data into the database
final_df.to_sql('ecommerce_data', engine, if_exists='replace', index=False)

print("Data loaded into PostgreSQL!")
