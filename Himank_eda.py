import pandas as pd

#loading the dataset

df = pd.read_csv("final_glof_prediction.csv")

print(df.head())

# # Counting the rows and columns
print("\nROWS AND COLUMNS")
print(df.shape)

# # Checking the column names and data types
print("\nDATA INFORMATION")
df.info()

# # Counting missing values in each column
print("\nMISSING VALUES")
print(df.isnull().sum())

# # Checking whether lake IDs are repeated
print("\nDUPLICATE LAKE IDs")
print(df["lake_id"].duplicated().sum())

# Summarizing the numerical columns
print("\nSUMMARY STATISTICS")
print(df.describe().round(4).to_string())