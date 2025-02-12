import pandas as pd

# Load the behavior data (what users did)
events_df = pd.read_csv('./data/events.csv')

# Load the two parts of item properties (info about the products)
item_properties_part1 = pd.read_csv('./data/item_properties_part1.csv')
item_properties_part2 = pd.read_csv('./data/item_properties_part2.csv')

# Combine the two item properties files
item_properties_df = pd.concat([item_properties_part1, item_properties_part2], ignore_index=True)

# Load the category tree (how items are grouped)
category_tree_df = pd.read_csv('./data/category_tree.csv')

# Print to check if the data is loaded correctly
print(events_df.head())
print(item_properties_df.head())
print(category_tree_df.head())
