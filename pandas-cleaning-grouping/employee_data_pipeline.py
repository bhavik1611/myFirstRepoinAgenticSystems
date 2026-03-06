"""
AI Employee Data Cleaning & Aggregation Pipeline
Simulate the first stage of an AI data workflow using Pandas.
"""
import pandas as pd
import numpy as np

# Step 1: Create the sample DataFrame
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\n---\n")

# Step 2: Detect and print missing values
print("Missing values per column:")
print(df.isnull().sum())
print("\n---\n")

# Step 3: Fill missing Salary values with the mean
mean_salary = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean_salary)
print("DataFrame after filling missing Salary values with mean:")
print(df)
print("\n---\n")

# Step 4: Drop the Temporary_Notes column
df = df.drop(columns=["Temporary_Notes"])
print("DataFrame after dropping 'Temporary_Notes' column:")
print(df)
print("\n---\n")

# Step 5: Rename Salary to Annual_Salary
df = df.rename(columns={"Salary": "Annual_Salary"})
print("DataFrame after renaming 'Salary' to 'Annual_Salary':")
print(df)
print("\n---\n")

# Step 6: Group by Department and compute mean salary and count
summary = df.groupby("Department").agg(
    Mean_Annual_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)
print("Final summary table (Mean salary and employee count by Department):")
print(summary)
