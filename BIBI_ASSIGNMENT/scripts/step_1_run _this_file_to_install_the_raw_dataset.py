import kagglehub
import shutil
import os

# Define target directory
target_dir = "data"

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)

# Download the dataset
path = kagglehub.dataset_download("retailrocket/ecommerce-dataset")

# Move the downloaded dataset to data/raw
for file in os.listdir(path):
    shutil.move(os.path.join(path, file), os.path.join(target_dir, file))

print(f"Dataset saved to: {target_dir}")
