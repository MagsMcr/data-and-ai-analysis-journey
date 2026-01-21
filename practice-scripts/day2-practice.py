# day2-practice.py
# Chapter 2 Practice: Dictionaries and DataFrames
# Date: January 21, 2026
# Using UC Irvine Student Performance Dataset

import pandas as pd
import requests
import zipfile
import io

print("=" * 50)
print("CHAPTER 2 PRACTICE: Dictionaries & DataFrames")
print("=" * 50)

# ============================================================
# PART 1: Load the dataset (reusing code from day1-practice.py)
# ============================================================
print("\nPart 1: Loading the dataset...")

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
response = requests.get(url)
zip_file = zipfile.ZipFile(io.BytesIO(response.content))
students = pd.read_csv(zip_file.open('student-mat.csv'), sep=';')

print(f"✓ Dataset loaded: {len(students)} students")
print(f"✓ Columns: {len(students.columns)} variables")

# ============================================================
# PART 2: Dictionary Basics - Create a student profile
# ============================================================
print("\n" + "=" * 50)
print("PART 2: Dictionary Basics")
print("=" * 50)

# Create a dictionary for ONE student (let's use the first student in our dataset)
# This demonstrates nested dictionary structure

student_profile = {
    'name': 'Student_001',  # Anonymized
    'demographics': {
        'age': int(students.iloc[0]['age']),
        'sex': students.iloc[0]['sex'],
        'address': students.iloc[0]['address']
    },
    'family': {
        'family_size': students.iloc[0]['famsize'],
        'parent_status': students.iloc[0]['Pstatus']
    },
    'academics': {
        'grade_1': int(students.iloc[0]['G1']),
        'grade_2': int(students.iloc[0]['G2']),
        'final_grade': int(students.iloc[0]['G3']),
        'absences': int(students.iloc[0]['absences'])
    }
}

# Access nested dictionary values
print("\nStudent Profile (Nested Dictionary):")
print(f"Age: {student_profile['demographics']['age']}")
print(f"Address type: {student_profile['demographics']['address']}")
print(f"Final grade: {student_profile['academics']['final_grade']}")

# Use dictionary methods
print(f"\nTop-level keys: {list(student_profile.keys())}")
print(f"Academic info keys: {list(student_profile['academics'].keys())}")

# ============================================================
# PART 3: Dictionary of Lists → DataFrame
# ============================================================
print("\n" + "=" * 50)
print("PART 3: Dictionary of Lists → DataFrame")
print("=" * 50)

# Create a smaller dataset from our full dataset
# Select first 5 students and specific columns
# This demonstrates dictionary of lists structure (columnar data)

small_student_data = {
    'student_id': ['S001', 'S002', 'S003', 'S004', 'S005'],
    'age': list(students['age'].head(5)),
    'sex': list(students['sex'].head(5)),
    'studytime': list(students['studytime'].head(5)),
    'absences': list(students['absences'].head(5)),
    'G1': list(students['G1'].head(5)),
    'G2': list(students['G2'].head(5)),
    'G3': list(students['G3'].head(5))
}

# Convert dictionary to DataFrame
small_df = pd.DataFrame(small_student_data)

print("\nSmall DataFrame created from dictionary of lists:")
print(small_df)

# ============================================================
# PART 4: Basic DataFrame Operations
# ============================================================
print("\n" + "=" * 50)
print("PART 4: DataFrame Operations")
print("=" * 50)

# Select specific columns
print("\nGrades only (G1, G2, G3):")
grades_only = small_df[['student_id', 'G1', 'G2', 'G3']]
print(grades_only)

# Basic statistics
print("\nBasic statistics for our small dataset:")
print(small_df.describe())

# Info about DataFrame
print("\nDataFrame info:")
print(f"Shape: {small_df.shape} (rows, columns)")
print(f"Column names: {list(small_df.columns)}")
print(f"Data types:\n{small_df.dtypes}")

# ============================================================
# PART 5: Compare dictionary structures
# ============================================================
print("\n" + "=" * 50)
print("PART 5: Key Concept Review")
print("=" * 50)

print("\nDictionary of Dictionaries (hierarchical):")
print("- Used for: Single item with nested properties")
print("- Example: One student with demographics, family, academics")
print(f"- Structure: {type(student_profile)} with nested {type(student_profile['demographics'])}")

print("\nDictionary of Lists (columnar):")
print("- Used for: Multiple items with same properties")
print("- Example: Multiple students with same attributes")
print("- Converts easily to DataFrame for analysis")
print(f"- Structure: {type(small_student_data)} → {type(small_df)}")

print("\n" + "=" * 50)
print("✓ Chapter 2 practice complete!")
print("=" * 50)