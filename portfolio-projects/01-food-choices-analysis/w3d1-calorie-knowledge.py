"""
=============================================================================
CALORIE KNOWLEDGE ANALYSIS - COLLEGE STUDENTS
=============================================================================
Part of: Food Choices & Nutrition Awareness Portfolio Project
Author: Magda McCrimmon | GitHub: MagsMcr
Date: February 2026
Week: 3, Day 1 | 18-Week Data Analysis Career Development Program

Dataset: Food Choices of College Students
Source: Kaggle - https://www.kaggle.com/datasets/borapajo/food-choices
Context: Survey of 125 college students about their food preferences,
         habits, and nutrition knowledge.

This dataset was deliberately chosen for its messy, real-world properties:
- Mix of coded categorical, numerical, and open-text responses
- Missing data across multiple variables
- Inconsistent data types requiring cleaning
- Result of survey design that welcomed diverse response formats

Portfolio Note:
This script is a subset of a larger planned project examining nutrition
awareness among college students. The full project will explore multiple
dimensions of eating habits, health behaviors, and food knowledge,
including: gender health behaviors, grade level progression, and
living situation impact on eating habits.

AI Collaboration Note:
This analysis was developed with Claude AI assistance (Anthropic).
All code was written or reviewed by the author. AI was used for
guidance, syntax support, and methodological discussion.
=============================================================================
"""

import pandas as pd
import numpy as np

# Load the dataset
food_df = pd.read_csv('datasets/food_coded.csv', encoding='latin-1')


# =============================================================================
# SECTION 1: INITIAL DATA EXPLORATION - FULL DATASET
# =============================================================================

print("=" * 70)
print("SECTION 1: INITIAL DATA EXPLORATION - FULL DATASET")
print("=" * 70)

print(f"\nDataset Shape: {food_df.shape}")
print("125 students, 61 variables")

print("\n" + "-" * 70)
print("Dataset Information:")
print("-" * 70)
print(food_df.info())

print("\n" + "-" * 70)
print("First 10 Rows:")
print("-" * 70)
print(food_df.head(10))


# =============================================================================
# SECTION 2: DATA QUALITY ISSUES - FULL DATASET OVERVIEW
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 2: DATA QUALITY ISSUES - FULL DATASET OVERVIEW")
print("=" * 70)

print("""
Based on initial inspection, this dataset exhibits several data quality
challenges typical of real-world survey data:

1. MISSING DATA
   - Highly variable across columns (ranging from 0 to 26 missing values)
   - Notable examples:
     * GPA: 2 missing values (123/125 complete)
     * exercise: 13 missing values (112/125 complete)
     * type_sports: 26 missing values (99/125 complete)
   - Missing data patterns suggest incomplete survey responses and
     question skip logic

2. DATA TYPE INCONSISTENCIES
   - GPA stored as 'object' (text) instead of numeric
     * Contains non-numeric entries ('Personal ', 'Unknown', '3.79 bitch')
   - weight stored as 'object' instead of numeric
     * Contains text responses alongside numerical values
   - Several numeric columns stored as float64 that should be integers
     * Survey response codes (1-5 scales) stored with unnecessary decimals
     * Caused by pandas behaviour: integer columns containing NaN values
       are automatically stored as float64

3. MIXED DATA TYPES IN TEXT COLUMNS (NLP Candidates)
   - Open-ended responses (comfort_food, diet_current, eating_changes etc.)
     contain free-text entries ideal for future NLP analysis:
     * Varied response lengths and styles
     * Inconsistent capitalisation
     * Potential typos and spelling variations
     * Multiple items listed in single fields

4. POTENTIAL CODING ERRORS
   - Some variables have both coded and uncoded versions
     e.g., comfort_food_reasons (text) and comfort_food_reasons_coded (numeric)
   - Requires verification that coded values match text responses

5. SURVEY DESIGN ARTIFACTS
   - 61 columns reflect a comprehensive survey
   - Question skip patterns likely explain some missing data clusters
   - Open-ended questions create natural data cleaning challenges

NOTE ON SCOPE:
This script does NOT address all of the above issues. The analysis focuses
on a specific research question requiring only a subset of well-structured
variables. Full dataset cleaning would be part of the larger portfolio
project.
""")


# =============================================================================
# SECTION 3: ANALYSIS SCOPE & RESEARCH QUESTION
# =============================================================================

print("=" * 70)
print("SECTION 3: ANALYSIS SCOPE & RESEARCH QUESTION")
print("=" * 70)

print("""
RESEARCH QUESTION:
"What is the relationship between demographic factors (gender, GPA) and
nutritional knowledge among college students?"

Specifically, this analysis examines:
  - How accurately can students estimate calories in common restaurant foods?
  - Do calorie estimation patterns differ by gender?
  - Does academic performance (GPA) relate to nutrition knowledge?

IMPORTANT METHODOLOGICAL NOTE:
This is DESCRIPTIVE analysis only. We are observing patterns in the data
and cannot make claims of statistical significance. Terms such as
"correlate" (implying a formal correlation test) or "significant" (implying
hypothesis testing) are deliberately avoided. All findings describe
observable tendencies in this specific sample only.

This is also NOT a guessing game. We are measuring general knowledge about
calorie content in everyday foods that college students commonly consume -
a meaningful indicator of nutritional awareness.

FOODS TESTED (5 common restaurant items):
  1. Chicken Piadina (sandwich)      - Actual: 610 calories
  2. Starbucks Scone                 - Actual: 420 calories
  3. Chipotle Burrito                - Actual: 940 calories
  4. Panera Roasted Turkey BLT       - Actual: 690 calories
  5. Waffle Potato Sandwich          - Actual: 900 calories

Students selected from 4 calorie range options per food item.

ANALYSIS COLUMNS (7 variables):
  - GPA               (academic performance proxy)
  - Gender            (demographic grouping variable)
  - calories_chicken  (nutritional knowledge measure)
  - calories_scone    (nutritional knowledge measure)
  - tortilla_calories (nutritional knowledge measure)
  - turkey_calories   (nutritional knowledge measure)
  - waffle_calories   (nutritional knowledge measure)

LIMITATION:
This is a small sample (125 students, reduced further during cleaning).
Findings are descriptive and exploratory only - not generalisable to the
broader student population without further statistical validation.
""")


# =============================================================================
# SECTION 4: SELECT ANALYSIS COLUMNS
# =============================================================================

print("=" * 70)
print("SECTION 4: SELECT ANALYSIS COLUMNS")
print("=" * 70)

# Select only the 7 columns relevant to our research question
calories_df = food_df[['GPA', 'Gender', 'calories_chicken', 'calories_scone',
                        'tortilla_calories', 'turkey_calories', 'waffle_calories']]

print(f"\nReduced dataset from {food_df.shape[1]} to {calories_df.shape[1]} columns")
print(f"Analysis dataset shape: {calories_df.shape}")

print("\nFirst 10 rows of analysis dataset:")
print(calories_df.head(10))

print("\nColumn information:")
print(calories_df.info())


# =============================================================================
# SECTION 5: DATA QUALITY CHECKS - SELECTED COLUMNS
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 5: DATA QUALITY CHECKS - SELECTED COLUMNS")
print("=" * 70)

# --- Missing Values ---
print("\nMissing Values Count:")
print(calories_df.isna().sum())

print("\nMissing Values Percentage:")
# Note: With only 125 rows, percentages are obvious from counts above.
# Included here for completeness and to demonstrate standard practice.
# In larger datasets, percentages are essential for decision-making.
print((calories_df.isna().sum() / len(calories_df) * 100).round(2))

# --- Gender Distribution ---
print("\nGender - Unique Values and Distribution:")
print(calories_df['Gender'].unique())
print(calories_df['Gender'].value_counts())

# --- Calorie Columns: Value Ranges ---
print("\nCalorie Columns - Value Ranges and Unique Values:")
numeric_cols = ['calories_chicken', 'calories_scone', 'tortilla_calories',
                'turkey_calories', 'waffle_calories']

for col in numeric_cols:
    print(f"\n  Column: {col}")
    print(f"  Min: {calories_df[col].min()}")
    print(f"  Max: {calories_df[col].max()}")
    print(f"  Unique values: {calories_df[col].unique()}")

# --- Duplicates ---
print(f"\nDuplicate Rows: {calories_df.duplicated().sum()}")

# --- GPA: Check for Non-Numeric Entries ---
print("\nGPA - Unique Values (checking for invalid entries):")
print(calories_df['GPA'].unique())
print("""
Observations:
  - GPA stored as 'object' due to non-numeric entries
  - Found: 'Personal ' (trailing space), 'Unknown', '3.79 bitch'
  - Strategy: Remove 'Personal' and 'Unknown' entirely (no salvageable value)
              Salvage '3.79 bitch' by stripping the text (valid GPA preserved)
              Drop remaining NaN values (only 2 rows, 1.6% - acceptable loss)
""")


# =============================================================================
# SECTION 6: DATA CLEANING
# =============================================================================

print("=" * 70)
print("SECTION 6: DATA CLEANING")
print("=" * 70)

print(f"\nRows before cleaning: {calories_df.shape[0]}")

# --- Step 1: Clean GPA Column ---
print("\n--- Step 1: Clean GPA Column ---")

# Remove rows with completely unrecoverable GPA values
calories_df = calories_df.loc[~calories_df['GPA'].isin(['Personal ', 'Unknown'])]
print(f"After removing 'Personal' and 'Unknown': {calories_df.shape[0]} rows")

# Salvage '3.79 bitch' by stripping the invalid text
calories_df['GPA'] = calories_df['GPA'].str.replace(' bitch', '')
print("Cleaned '3.79 bitch' → '3.79' (value preserved)")

# Drop remaining NaN values in GPA
calories_df = calories_df.dropna(subset=['GPA'])
print(f"After dropping NaN GPA values: {calories_df.shape[0]} rows")

# Convert GPA from string to float (decimals required, e.g. 3.654)
calories_df['GPA'] = calories_df['GPA'].astype(float)

# Verify GPA cleaning
assert calories_df['GPA'].dtype == 'float64', "GPA should be float64!"
assert calories_df['GPA'].isna().sum() == 0, "GPA should have no missing values!"
assert calories_df['GPA'].max() <= 4.0, "GPA values should not exceed 4.0!"
print("GPA cleaning verified ✓")

# --- Step 2: Remove Duplicate Rows ---
print("\n--- Step 2: Remove Duplicate Rows ---")
calories_df.drop_duplicates(inplace=True)
print(f"After removing duplicates: {calories_df.shape[0]} rows")

# --- Step 3: Handle Missing Values in Calorie Columns ---
print("\n--- Step 3: Handle Missing Values in Calorie Columns ---")

# Identify which rows have missing calorie values
missing_rows = calories_df.loc[
    calories_df['calories_scone'].isna() | calories_df['tortilla_calories'].isna()
]
print(f"Rows with missing calorie values: {len(missing_rows)}")
print("Both missing values occur in the same row - dropping that row")

calories_df.dropna(subset=['calories_scone', 'tortilla_calories'], inplace=True)
print(f"After dropping missing calorie rows: {calories_df.shape[0]} rows")

# --- Step 4: Fix Data Types ---
print("\n--- Step 4: Fix Data Types ---")

# Convert float calorie columns to integer
# Note: These were float64 because pandas cannot store NaN in integer columns.
# Now that NaN values are removed, we can convert back to integers.
calories_df[['calories_scone', 'tortilla_calories']] = (
    calories_df[['calories_scone', 'tortilla_calories']].astype(int)
)

# Convert Gender to category with meaningful labels
calories_df['Gender'] = calories_df['Gender'].astype('category')
calories_df['Gender'] = calories_df['Gender'].cat.rename_categories({1: 'Female', 2: 'Male'})

# Verify all data types
assert calories_df['GPA'].dtype == 'float64', "GPA should be float64!"
assert calories_df['Gender'].dtype.name == 'category', "Gender should be category!"
assert calories_df['calories_scone'].dtype == 'int64', "calories_scone should be int64!"
assert calories_df['tortilla_calories'].dtype == 'int64', "tortilla_calories should be int64!"
print("All data type conversions verified ✓")

# --- Cleaning Summary ---
print("\n--- Cleaning Summary ---")
print(f"  Original rows:           125")
print(f"  Removed (invalid GPA):     2  ('Personal ', 'Unknown')")
print(f"  Salvaged (cleaned GPA):    1  ('3.79 bitch' → '3.79')")
print(f"  Removed (NaN GPA):         2")
print(f"  Removed (duplicate):       1")
print(f"  Removed (missing calories):1")
print(f"  Final rows:              {calories_df.shape[0]}")

print("\nFinal cleaned dataset info:")
print(calories_df.info())
print("\nGender distribution after cleaning:")
print(calories_df['Gender'].value_counts())


# =============================================================================
# SECTION 7: ANALYSIS - CALORIE ESTIMATION ACCURACY
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 7: CALORIE ESTIMATION ACCURACY ANALYSIS")
print("=" * 70)

# --- Step 1: Define Correct Answers ---
correct_answers = {
    'calories_chicken': 610,
    'calories_scone': 420,
    'tortilla_calories': 940,
    'turkey_calories': 690,
    'waffle_calories': 900
}

# --- Step 2: Create Accuracy Columns (Boolean: True = correct) ---
accuracy_cols = []
for col, correct_value in correct_answers.items():
    accuracy_col = col.replace('calories_', '').replace('_calories', '') + '_correct'
    calories_df[accuracy_col] = calories_df[col] == correct_value
    accuracy_cols.append(accuracy_col)

# Rename for clarity
col_mapping = {
    'chicken_correct': 'chicken_correct',
    'scone_correct': 'scone_correct',
    'tortilla_correct': 'tortilla_correct',
    'turkey_correct': 'turkey_correct',
    'waffle_correct': 'waffle_correct'
}

# --- Step 3: Overall Accuracy by Food Item ---
print("\n--- Overall Accuracy by Food Item ---")
print(f"{'Food Item':<35} {'% Correct':>10} {'n Correct':>10} {'n Total':>10}")
print("-" * 70)

food_labels = {
    'chicken_correct': 'Chicken Piadina (610 cal)',
    'scone_correct': 'Starbucks Scone (420 cal)',
    'tortilla_correct': 'Chipotle Burrito (940 cal)',
    'turkey_correct': 'Panera Turkey BLT (690 cal)',
    'waffle_correct': 'Waffle Potato Sandwich (900 cal)'
}

for col, label in food_labels.items():
    pct = (calories_df[col].mean() * 100).round(1)
    n_correct = calories_df[col].sum()
    n_total = len(calories_df)
    print(f"{label:<35} {pct:>9}% {n_correct:>10} {n_total:>10}")

# --- Step 4: Overall Score per Student ---
print("\n--- Overall Calorie Knowledge Score per Student (out of 5) ---")
calories_df['total_correct'] = calories_df[accuracy_cols].sum(axis='columns')
print(calories_df['total_correct'].describe().round(2))
print(f"\nOverall mean score: {calories_df['total_correct'].mean().round(2)} / 5")
print(f"Overall accuracy:   {(calories_df['total_correct'].mean() / 5 * 100).round(1)}%")

# --- Step 5: Accuracy by Gender ---
print("\n--- Accuracy by Gender ---")
gender_accuracy = calories_df.groupby('Gender')[accuracy_cols + ['total_correct']].mean() * 100
gender_accuracy = gender_accuracy.round(1)
print("\nPercentage correct by gender (%):")
print(gender_accuracy.rename(columns={
    'chicken_correct': 'Chicken',
    'scone_correct': 'Scone',
    'tortilla_correct': 'Burrito',
    'turkey_correct': 'Turkey',
    'waffle_correct': 'Waffle',
    'total_correct': 'Overall Score (/5 x 100)'
}))

# --- Step 6: Accuracy by GPA Group ---
print("\n--- Accuracy by GPA Group ---")

# Create GPA bands for grouping
gpa_bins = [0, 2.5, 3.0, 3.5, 4.0]
gpa_labels = ['Below 2.5', '2.5 - 3.0', '3.0 - 3.5', '3.5 - 4.0']
calories_df['GPA_group'] = pd.cut(calories_df['GPA'],
                                   bins=gpa_bins,
                                   labels=gpa_labels,
                                   include_lowest=True)

gpa_accuracy = calories_df.groupby('GPA_group')[accuracy_cols + ['total_correct']].mean() * 100
gpa_accuracy = gpa_accuracy.round(1)

print("\nPercentage correct by GPA group (%):")
print(gpa_accuracy.rename(columns={
    'chicken_correct': 'Chicken',
    'scone_correct': 'Scone',
    'tortilla_correct': 'Burrito',
    'turkey_correct': 'Turkey',
    'waffle_correct': 'Waffle',
    'total_correct': 'Overall Score (/5 x 100)'
}))

print("\nStudent count per GPA group:")
print(calories_df['GPA_group'].value_counts().sort_index())


# =============================================================================
# SECTION 8: SUMMARY & CONCLUSIONS
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 8: SUMMARY & CONCLUSIONS")
print("=" * 70)

# Calculate key stats for summary
best_food = max(food_labels.items(),
                key=lambda x: calories_df[x[0]].mean())
worst_food = min(food_labels.items(),
                 key=lambda x: calories_df[x[0]].mean())

female_score = calories_df[calories_df['Gender'] == 'Female']['total_correct'].mean().round(2)
male_score = calories_df[calories_df['Gender'] == 'Male']['total_correct'].mean().round(2)

print(f"""
DESCRIPTIVE FINDINGS:

1. OVERALL NUTRITIONAL KNOWLEDGE
   - Mean score: {calories_df['total_correct'].mean().round(2)} / 5 
     ({(calories_df['total_correct'].mean() / 5 * 100).round(1)}% overall accuracy)
   - Students demonstrated highly variable knowledge across food items

2. FOOD ITEM DIFFICULTY
   - Best estimated: {best_food[1]}
     ({(calories_df[best_food[0]].mean() * 100).round(1)}% correct)
   - Hardest to estimate: {worst_food[1]}
     ({(calories_df[worst_food[0]].mean() * 100).round(1)}% correct)
   - This suggests students have better knowledge of some food types than others

3. GENDER PATTERNS
   - Female students mean score: {female_score} / 5
   - Male students mean score:   {male_score} / 5
   - Observable difference: {abs(female_score - male_score).round(2)} points
   - Note: Descriptive observation only - no statistical significance claimed

4. GPA PATTERNS
   - See GPA group breakdown above for observable tendencies
   - Note: Small group sizes limit the reliability of these observations

IMPORTANT LIMITATIONS:
   - Small sample size (n={len(calories_df)}) limits generalisability
   - Descriptive analysis only - no causal claims can be made
   - Self-reported data may introduce response bias
   - Survey design (picture-based questions) may not reflect real-world
     nutritional knowledge

NEXT STEPS (Planned for Full Portfolio Project):
   - Expand analysis to include eating habits and health behaviors
   - Apply statistical testing once Week 7 statistics skills are acquired
   - Explore NLP columns (comfort_food, diet_current) for text patterns
   - Build visualisations for all findings
   - Investigate living situation and grade level dimensions
""")

print("=" * 70)
print("END OF ANALYSIS")
print(f"Final dataset: {calories_df.shape[0]} students, {calories_df.shape[1]} variables")
print("=" * 70)