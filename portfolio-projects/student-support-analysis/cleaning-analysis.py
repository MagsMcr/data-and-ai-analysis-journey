"""
Student Support and Academic Outcomes — Data Cleaning Project
=============================================================
Dataset: UCI Student Performance (student-mat.csv — Maths cohort)
Source: https://archive.ics.uci.edu/dataset/320/student+performance
Students: 395 | Variables: 33

Business Question:
What does this dataset allow us to say responsibly about the relationship
between additional educational support and academic outcomes — and what
are the limits of that interpretation?

Cleaning tasks covered:
- Initial inspection
- Column standardisation
- Categorical dtype conversion
- Validation checks
- Duplicate identification
- Feature flagging

Author: Magda McCrimmon | GitHub: MagsMcr
Date: March 2026
"""

import numpy as np
import pandas as pd
import os

student_data = pd.read_csv('datasets/student-performance/student-mat.csv', sep=';')
print(student_data.shape)

# ============================================================
# SECTION 1: INITIAL INSPECTION
# ============================================================

print(student_data.head())
print(student_data.info())
print(student_data.describe())
print(student_data.isna().sum())

# ============================================================
# COLUMN REFERENCE — KEY VARIABLES FOR THIS ANALYSIS
# ============================================================
# Full variable descriptions available in: datasets/student-performance/student.txt
#
# INTERVENTION VARIABLES (central to business question):
#   schoolsup  — whether student receives extra educational support from school (yes/no)
#   famsup     — whether student receives educational support from family (yes/no)
#   paid       — whether student attends extra paid classes in this subject (yes/no)
#   higher     — whether student wants to pursue higher education (yes/no)
#                note: used as moderating variable — support may mean different things
#                depending on whether a student is motivated toward further study
#
# OUTCOME VARIABLES:
#   G1         — first period grade (0-20)
#   G2         — second period grade (0-20)
#   G3         — final grade (0-20)
#                note: three grades allow us to track progression, not just final result
#
# COLUMNS FLAGGED FOR CLEANING:
#   Pstatus, Medu, Fedu, Mjob, Fjob — inconsistent capitalisation vs rest of dataset
#   traveltime, studytime, famrel, freetime, goout, Dalc, Walc, health
#                — stored as integers but represent ordered categories (1-4 or 1-5 scale)
#                  mathematical operations (e.g. mean) are not meaningful on these
#   absences   — numeric but max value of 75 is a significant outlier vs mean of 5.7
#                  requires investigation before analysis
# ============================================================

# ============================================================
# SECTION 2: DATA AUDIT
# ============================================================

# --- 2a: Check unique values for all object (categorical) columns ---
# Purpose: identify inconsistent entries, unexpected values, or formatting issues
# We check object columns only here — numeric ranges checked separately in 2b

print("\n=== CATEGORICAL COLUMNS — UNIQUE VALUES ===\n")
for col in student_data.select_dtypes(include='object').columns:
    print(f"{col}: {student_data[col].unique()}")

# --- 2b: Check numeric columns against expected ranges ---
# Purpose: confirm values fall within documented ranges, flag potential outliers
# Expected ranges sourced from student.txt documentation

print("\n=== NUMERIC COLUMNS — MIN/MAX CHECK ===\n")
numeric_cols = student_data.select_dtypes(include='int64').columns
print(student_data[numeric_cols].agg(['min', 'max']))