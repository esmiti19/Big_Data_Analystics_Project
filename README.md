# **Big Data ETL Pipeline Project**

This project demonstrates how to build an **ETL (Extract, Transform, Load) pipeline** for processing large e-commerce datasets using **Pandas** and **PostgreSQL**. The dataset is **automatically downloaded from Kaggle** and cleaned using a series of scripts.

---

## **📌 Project Workflow**
1. **Step 1:** Create a folder named `data` inside `BIBI_ASSIGNMENT` directory.
1. **Step 2:** Run `step_1_run_this_file_to_install_the_raw_dataset.py` to download and store the raw dataset in the `data/` folder.
2. **Step 3:** Run `extract_data.py` to extract and process the raw data.
3. **Step 4:** Run `transform_data.py` to clean and structure the dataset.
4. **Step 5:** Run `load_data.py` to load the cleaned dataset into a **PostgreSQL database**.
5. **Step 6:** The cleaned dataset is saved as `cleaned_final_data.csv` inside the `data/` folder.

---

## **🛠 Prerequisites**

Before running the scripts, ensure you have the following installed:

1. **Python 3.x**  
   [Download Python](https://www.python.org/downloads/)

2. **PostgreSQL**  
   [Download PostgreSQL](https://www.postgresql.org/download/)

3. **VS Code** (Recommended for running scripts)  
   [Download VS Code](https://code.visualstudio.com/download)

---

## **📦 Required Python Packages**

To install all the required Python libraries, run:

```bash
pip install pandas psycopg2 SQLAlchemy kaggle
```

---

## **🚀 Step-by-Step Setup and Execution**

### **1️⃣ Step 1: Download the Raw Dataset from Kaggle**
Run the following command in the terminal to download the dataset:

```bash
python step_1_run_this_file_to_install_the_raw_dataset.py
```

- This script will:
  - **Download** the dataset from Kaggle.
  - **Save** it in the `data/` folder.

---

### **2️⃣ Step 2: Extract the Data**
Once the dataset is downloaded, run:

```bash
python scripts/extract_data.py
```

- This script **loads the raw dataset** into Pandas DataFrames.

---

### **3️⃣ Step 3: Transform the Data**
Clean and structure the extracted data by running:

```bash
python scripts/transform_data.py
```

- This script:
  - Removes missing values and duplicates.
  - Standardizes data formats.
  - Saves the cleaned data as **`cleaned_final_data.csv`** in the `data/` folder.

---

### **4️⃣ Step 4: Load the Data into PostgreSQL**
To load the cleaned dataset into **PostgreSQL**, run:

```bash
python scripts/load_data.py
```

- This script:
  - Connects to the **PostgreSQL** database.
  - Loads **cleaned_final_data.csv** into the database.

---

## **📊 Visualizations and Reports**
Visualization and reports are saved in the `reports` folder.

---

## **📌 Additional Notes**
- **Data Folder (`data/`)**: Contains both raw and cleaned datasets.
- **Scripts Folder (`scripts/`)**: Contains all ETL Python scripts.
- **Database Folder (`db/`)**: Includes the SQL schema for PostgreSQL.

---

## **👨‍💻 Contributing**
Feel free to **fork** the repository, suggest improvements, or submit **pull requests**!

---
