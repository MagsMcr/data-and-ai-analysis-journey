"""
=============================================================================
EXERCISE VS EATING HABITS ANALYSIS - COLLEGE STUDENTS
=============================================================================
Part of: Food Choices & Nutrition Awareness Portfolio Project
Author: Magda McCrimmon | GitHub: MagsMcr
Date: February 2026
Week: 3, Day 2 | 18-Week Data Analysis Career Development Program

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
This script is the second in a series analysing the Food Choices dataset.
Script 1 (w3d1-calorie-knowledge.py) examined relationships between
demographic factors and nutritional knowledge. This script investigates
whether exercise frequency is associated with different food choices and
eating behaviours, using a focused subset of 8 columns.

The series will culminate in a comprehensive portfolio project
(food-choices-complete-analysis.py) combining findings across all scripts.

AI Collaboration Note:
This analysis was developed with Claude AI assistance (Anthropic).
All code was written or reviewed by the author. AI was used for
guidance, syntax support, and methodological discussion.
=============================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for script execution


# =============================================================================
# SECTION 1: ANALYSIS SCOPE & RESEARCH QUESTION
# =============================================================================

print("=" * 70)
print("SECTION 1: ANALYSIS SCOPE & RESEARCH QUESTION")
print("=" * 70)

print("""
RESEARCH QUESTION:
"Do students who exercise more frequently make different food choices?"

Specifically, this analysis examines:
  - Is exercise frequency associated with healthier eating habits?
  - Do food choices and health behaviours differ by gender?
  - Is there a relationship between exercise frequency and
    nutritional awareness?

IMPORTANT METHODOLOGICAL NOTE:
This is DESCRIPTIVE analysis only. We are observing patterns in the data
and cannot make claims about statistical significance or causation.
All findings describe observable tendencies in this specific sample only.

VARIABLES IN THIS ANALYSIS:
  exercise          - Exercise frequency (1=every day, 5=never)
  Gender            - Gender (1=Female, 2=Male)
  fruit_day         - Daily fruit consumption frequency (1=never, 5=always)
  veggies_day       - Daily vegetable consumption frequency (1=never, 5=always)
  eating_out        - Frequency of eating out (1=never, 5=every day)
  cook              - How often student cooks (1=every day, 5=never)
  nutritional_check - Checks nutritional information (1=never, 5=always)
  healthy_feeling   - Self-rated health score (1=very unhealthy, 10=very healthy)
""")


# =============================================================================
# SECTION 2: LOADING AND SUBSETTING THE DATA
# =============================================================================

print("=" * 70)
print("SECTION 2: LOADING AND SUBSETTING THE DATA")
print("=" * 70)

# Load the full dataset
food_df = pd.read_csv('datasets/food_coded.csv', encoding='latin-1')

# Subset to only the 8 columns relevant to this research question
exercise_df = food_df[['exercise', 'Gender', 'fruit_day', 'veggies_day',
                        'eating_out', 'cook', 'nutritional_check', 'healthy_feeling']]

print(f"\nFull dataset: {food_df.shape[0]} rows, {food_df.shape[1]} columns")
print(f"Analysis subset: {exercise_df.shape[0]} rows, {exercise_df.shape[1]} columns")
print(f"Columns retained: {list(exercise_df.columns)}")

print("\nFirst 10 rows of analysis dataset:")
print(exercise_df.head(10))

print("\nColumn information:")
print(exercise_df.info())


# =============================================================================
# SECTION 3: DATA CLEANING AND TRANSFORMATION
# =============================================================================

print("=" * 70)
print("SECTION 3: DATA CLEANING AND TRANSFORMATION")
print("=" * 70)

# --- 3a: Missing Values Assessment ---
print("\n--- 3a: Missing Values Assessment ---\n")

print("Missing Values Count:")
print(exercise_df.isna().sum())

print("\nMissing Values as Percentage of Dataset:")
# Note: With only 125 rows, percentages are obvious from counts above.
# Included here for completeness and to demonstrate standard practice.
# In larger datasets, percentages are essential for decision-making.
print((exercise_df.isna().sum() / len(exercise_df) * 100).round(2))

# Store row count before cleaning for accurate documentation
rows_before = exercise_df.shape[0]

# Drop rows with missing values in key columns
exercise_df = exercise_df.dropna(subset=['exercise', 'cook'])

rows_after = exercise_df.shape[0]
rows_removed = rows_before - rows_after

print(f"""
MISSING DATA ASSESSMENT:
  exercise:  13 missing values (10.4%) - PRIMARY variable for this analysis
  cook:       3 missing values (2.4%)  - SECONDARY behavioural variable

DECISION: Drop rows with missing values in both columns.

RATIONALE:
  - exercise is the core independent variable. A row without it cannot
    contribute to answering the research question.
  - cook is a behavioural variable where imputation would be misleading -
    we cannot reliably infer cooking frequency from other columns.
  - With only 125 rows, every decision to drop must be documented.
  - rows_removed = {rows_removed} (not 15), confirming no row had both
    exercise AND cook missing simultaneously - all affected rows were unique.

Rows before cleaning: {rows_before}
Rows after dropping missing values: {rows_after}
Rows removed: {rows_removed}
""")

# --- 3b: Membership Constraint Check - Gender ---
print("--- 3b: Membership Constraint Check - Gender ---\n")

print("""
RATIONALE FOR CHECKING GENDER:
  Gender is coded as integers (1, 2) in the raw data. Before mapping to
  readable labels, we verify no invalid codes exist. Any value outside
  {1, 2} would represent a data entry error and must be removed.
""")

valid_genders = [1, 2]
invalid_count = len(exercise_df[~exercise_df['Gender'].isin(valid_genders)])
print(f"Invalid Gender values found: {invalid_count}")

# Filter to valid values only (no rows removed in this case)
exercise_df = exercise_df[exercise_df['Gender'].isin(valid_genders)]

# Map integer codes to readable labels
gender_map = {1: 'Female', 2: 'Male'}
exercise_df['Gender'] = exercise_df['Gender'].replace(gender_map)

print("\nGender distribution after mapping:")
print(exercise_df['Gender'].value_counts())

print("""
NOTE ON STRING CLEANING:
  No additional string cleaning (strip, lower) applied to Gender.
  The column was mapped directly from integers using a controlled
  dictionary - there was no opportunity for whitespace or case
  inconsistencies to enter. value_counts() confirms exactly two
  clean values: Female and Male.

NOTE ON GENDER DISTRIBUTION:
  Female: 63 (58%) | Male: 46 (42%)
  The uneven split should be considered when interpreting gender
  comparisons - groups are not equal in size.
""")

# --- 3c: Exercise Frequency Binning ---
print("--- 3c: Exercise Frequency Binning ---\n")

print("Exercise frequency distribution (raw values):")
print(exercise_df['exercise'].value_counts().sort_index())

# Bin exercise into three meaningful groups
exercise_df['exercise_group'] = pd.cut(exercise_df['exercise'],
                                        bins=[0, 2, 3, 5],
                                        labels=["Active", "Moderate", "Inactive"])

print("\nExercise group distribution after binning:")
print(exercise_df['exercise_group'].value_counts())

print("""
BINNING RATIONALE:
  Active   (1-2): Exercises every day or most days
  Moderate (3):   Exercises occasionally
  Inactive (4-5): Rarely or never exercises

NOTABLE FINDING - SELF-REPORTING BIAS:
  No students reported exercising rarely or never (values 4-5 absent).
  This suggests possible social desirability bias - students may
  over-report exercise habits in survey contexts.
  The 'Inactive' category is retained in the analysis structure to
  acknowledge this limitation transparently. Any comparative analysis
  between Active and Inactive groups is not possible with this data.
""")

# --- 3d: Nutritional Check Binning ---
print("--- 3d: Nutritional Check Binning ---\n")

print("Nutritional check distribution (raw values):")
print(exercise_df['nutritional_check'].value_counts().sort_index())

# Bin nutritional_check into three groups
exercise_df['nutritional_check_group'] = pd.cut(exercise_df['nutritional_check'],
                                                  bins=[0, 2, 3, 5],
                                                  labels=["Rarely", "Sometimes", "Regularly"])

print("\nNutritional check group distribution after binning:")
print(exercise_df['nutritional_check_group'].value_counts())

print("""
BINNING RATIONALE:
  Rarely    (1-2): Seldom or never checks nutritional information
  Sometimes (3):   Checks occasionally
  Regularly (4-5): Frequently checks nutritional information

  Binning nutritional_check enables direct comparison with exercise_group
  categories and produces more readable cross-tabulations.
""")

# --- 3e: Data Type Corrections ---
print("--- 3e: Data Type Corrections ---\n")

print("""
exercise and cook are stored as float64 because pandas automatically
converts integer columns containing NaN values to float. Now that
missing rows have been dropped, these columns should be correctly
stored as integers.
""")

exercise_df[['cook', 'exercise']] = exercise_df[['cook', 'exercise']].astype(int)
exercise_df['Gender'] = exercise_df['Gender'].astype('category')

print("Data types after corrections:")
print(exercise_df.dtypes)

# --- 3f: Range Constraint Checks ---
print("\n--- 3f: Range Constraint Checks ---\n")

print("""
Checking remaining numeric columns for out-of-range values.
All columns use 1-5 Likert scales except healthy_feeling (1-10).
Whitespace issues are not possible in numeric columns - confirmed
by all columns having int64 or float64 dtype.
""")

cols_to_check = ['fruit_day', 'veggies_day', 'eating_out',
                 'cook', 'nutritional_check', 'healthy_feeling']

for col in cols_to_check:
    print(f"\n{col}:")
    print(exercise_df[col].value_counts().sort_index())
    print("-" * 40)

print("""
RANGE CHECK RESULT:
  All columns contain valid values within expected survey scale ranges:
  - fruit_day, veggies_day, eating_out, cook, nutritional_check: values 1-5 only
  - healthy_feeling: values 1-10 only
  No out-of-range values detected. No further cleaning required.
""")


# =============================================================================
# SECTION 4: VERIFICATION - ASSERT STATEMENTS
# =============================================================================

print("=" * 70)
print("SECTION 4: VERIFICATION - ASSERT STATEMENTS")
print("=" * 70)

print("\nRunning verification checks...\n")

# No missing values in key columns
assert exercise_df['exercise'].isna().sum() == 0, "ERROR: Missing values in exercise"
assert exercise_df['cook'].isna().sum() == 0, "ERROR: Missing values in cook"

# Gender contains only valid mapped values
assert exercise_df['Gender'].isin(['Female', 'Male']).all(), "ERROR: Invalid values in Gender"

# Binned columns created with no nulls
assert exercise_df['exercise_group'].isna().sum() == 0, "ERROR: Nulls in exercise_group"
assert exercise_df['nutritional_check_group'].isna().sum() == 0, "ERROR: Nulls in nutritional_check_group"

# Row count as expected
assert exercise_df.shape[0] == 109, f"ERROR: Expected 109 rows, got {exercise_df.shape[0]}"

# Data types correct
assert exercise_df['cook'].dtype == 'int64', "ERROR: cook should be int64"
assert exercise_df['exercise'].dtype == 'int64', "ERROR: exercise should be int64"
assert str(exercise_df['Gender'].dtype) == 'category', "ERROR: Gender should be category"

print("All verification checks passed.")
print(f"\nFinal cleaned dataset: {exercise_df.shape[0]} rows, {exercise_df.shape[1]} columns")


# =============================================================================
# SECTION 5: CLEANED DATASET OVERVIEW
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 5: CLEANED DATASET OVERVIEW")
print("=" * 70)

print("\nFinal dataset info:")
print(exercise_df.info())

print("\nStatistical summary (numeric columns):")
print(exercise_df.describe().round(2))

print("""
CLEANING SUMMARY:
  Starting dataset:    125 rows, 61 columns
  After subsetting:    125 rows,  8 columns
  After dropping NaN:  109 rows,  8 columns
  New columns added:   exercise_group, nutritional_check_group
  Final dataset:       109 rows, 10 columns

  Changes made:
  - Dropped 16 rows with missing values in exercise (13) and cook (3)
  - Mapped Gender from integer codes (1/2) to labels (Female/Male)
  - Converted Gender dtype to category
  - Converted exercise and cook from float64 to int64
  - Binned exercise into Active/Moderate/Inactive groups
  - Binned nutritional_check into Rarely/Sometimes/Regularly groups
  - No invalid membership constraint values found in Gender
  - No out-of-range values found in any numeric column
""")


# =============================================================================
# SECTION 6: DESCRIPTIVE ANALYSIS
# =============================================================================

print("=" * 70)
print("SECTION 6: DESCRIPTIVE ANALYSIS")
print("=" * 70)

# --- 6a: Exercise Group Overview ---
print("\n--- 6a: Exercise Group Overview ---\n")

print("Distribution of students by exercise group:")
print(exercise_df['exercise_group'].value_counts())
print("\nNote: 'Inactive' group is empty - see self-reporting bias finding in Section 3.")

# --- 6b: Food Behaviour by Exercise Group ---
print("\n--- 6b: Food Behaviour by Exercise Group ---\n")

food_cols = ['fruit_day', 'veggies_day', 'eating_out', 'cook']

print("Mean food behaviour scores by exercise group:")
print("(Higher fruit/veggies = more frequent | Higher eating_out = eats out more | Higher cook = cooks more)")
print()
print(exercise_df.groupby('exercise_group', observed=True)[food_cols].mean().round(2))

# --- 6c: Health Awareness by Exercise Group ---
print("\n--- 6c: Health Awareness & Wellbeing by Exercise Group ---\n")

print("Mean nutritional_check and healthy_feeling scores by exercise group:")
print(exercise_df.groupby('exercise_group', observed=True)[['nutritional_check', 'healthy_feeling']].mean().round(2))

# --- 6d: Cross-tabulation: Exercise Group vs Nutritional Check Group ---
print("\n--- 6d: Cross-tabulation: Exercise Group vs Nutritional Check Group ---\n")

print("Number of students by exercise group and nutritional check frequency:")
print(pd.crosstab(exercise_df['exercise_group'],
                  exercise_df['nutritional_check_group']))

# --- 6e: Cross-tabulation: Exercise Group vs Gender ---
print("\n--- 6e: Cross-tabulation: Exercise Group vs Gender ---\n")

print("Number of students by exercise group and gender:")
print(pd.crosstab(exercise_df['exercise_group'],
                  exercise_df['Gender']))

# --- 6f: Full Summary Pivot Table by Exercise Group ---
print("\n--- 6f: Summary Pivot Table - All Variables by Exercise Group ---\n")

all_numeric = ['fruit_day', 'veggies_day', 'eating_out', 'cook',
               'nutritional_check', 'healthy_feeling']

print("Mean scores for all variables by exercise group:")
print(exercise_df.groupby('exercise_group', observed=True)[all_numeric].mean().round(2))

# --- 6g: Summary Pivot Table by Gender ---
print("\n--- 6g: Summary Pivot Table - All Variables by Gender ---\n")

print("Mean scores for all variables by gender:")
print(exercise_df.groupby('Gender', observed=True)[all_numeric].mean().round(2))

# --- 6h: Correlation Matrix ---
print("\n--- 6h: Correlation Matrix ---\n")

print("""
Correlation matrix for all numeric variables.
Values range from -1 (perfect negative) to +1 (perfect positive).
Values close to 0 indicate little or no linear relationship.
Note: This is a small sample (109 students) - interpret with caution.
""")
print(exercise_df[all_numeric + ['exercise']].corr().round(2))


# =============================================================================
# SECTION 7: VISUALISATIONS
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 7: VISUALISATIONS")
print("=" * 70)

print("\nGenerating visualisations...\n")

# --- Plot 1: Bar chart - Mean food behaviours by exercise group ---
fig, ax = plt.subplots(figsize=(9, 5))

means = exercise_df.groupby('exercise_group', observed=True)[food_cols].mean()
means.plot(kind='bar', ax=ax, width=0.7, edgecolor='white')

ax.set_title('Mean Food Behaviour Scores by Exercise Group',
             fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Exercise Group', fontsize=11)
ax.set_ylabel('Mean Score (1-5 scale)', fontsize=11)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.legend(['Fruit/day', 'Veggies/day', 'Eating out', 'Cooking'], loc='upper right')
ax.set_ylim(0, 6)
ax.axhline(y=3, color='grey', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('practice-scripts/w3d2-plot1-food-by-exercise.png', dpi=150)
plt.close()
print("Plot 1 saved: w3d2-plot1-food-by-exercise.png")
print("  Bar chart - mean food behaviour scores by exercise group.")

# --- Plot 2: Bar chart - Mean healthy_feeling by exercise group and gender ---
fig, axes = plt.subplots(1, 2, figsize=(11, 5))

# Left: healthy_feeling by exercise group
hf_exercise = exercise_df.groupby('exercise_group', observed=True)['healthy_feeling'].mean()
hf_exercise.plot(kind='bar', ax=axes[0], color='steelblue', edgecolor='white', width=0.5)
axes[0].set_title('Mean Healthy Feeling\nby Exercise Group', fontsize=11, fontweight='bold')
axes[0].set_xlabel('Exercise Group')
axes[0].set_ylabel('Mean Score (1-10 scale)')
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0)
axes[0].set_ylim(0, 10)

# Right: healthy_feeling by gender
hf_gender = exercise_df.groupby('Gender', observed=True)['healthy_feeling'].mean()
hf_gender.plot(kind='bar', ax=axes[1], color='coral', edgecolor='white', width=0.4)
axes[1].set_title('Mean Healthy Feeling\nby Gender', fontsize=11, fontweight='bold')
axes[1].set_xlabel('Gender')
axes[1].set_ylabel('Mean Score (1-10 scale)')
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0)
axes[1].set_ylim(0, 10)

plt.suptitle('Self-Reported Health Score Comparisons',
             fontsize=13, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('practice-scripts/w3d2-plot2-healthy-feeling.png', dpi=150, bbox_inches='tight')
plt.close()
print("\nPlot 2 saved: w3d2-plot2-healthy-feeling.png")
print("  Side-by-side bars - healthy_feeling by exercise group and gender.")

# --- Plot 3: Histogram - Distribution of healthy_feeling scores ---
fig, ax = plt.subplots(figsize=(8, 5))

active = exercise_df[exercise_df['exercise_group'] == 'Active']['healthy_feeling']
moderate = exercise_df[exercise_df['exercise_group'] == 'Moderate']['healthy_feeling']

ax.hist(active, bins=10, range=(1, 11), alpha=0.6, color='steelblue',
        edgecolor='white', label=f'Active (n={len(active)})')
ax.hist(moderate, bins=10, range=(1, 11), alpha=0.6, color='coral',
        edgecolor='white', label=f'Moderate (n={len(moderate)})')

ax.set_title('Distribution of Healthy Feeling Scores\nActive vs Moderate Exercise Groups',
             fontsize=12, fontweight='bold', pad=10)
ax.set_xlabel('Healthy Feeling Score (1=very unhealthy, 10=very healthy)', fontsize=10)
ax.set_ylabel('Number of Students', fontsize=10)
ax.legend()
ax.set_xticks(range(1, 11))
plt.tight_layout()
plt.savefig('practice-scripts/w3d2-plot3-healthy-histogram.png', dpi=150)
plt.close()
print("\nPlot 3 saved: w3d2-plot3-healthy-histogram.png")
print("  Histogram - healthy_feeling distribution, Active vs Moderate.")
print("  Note: Inactive group excluded (0 students - see self-reporting bias finding).")


# =============================================================================
# SECTION 8: CONCLUSIONS & LIMITATIONS
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 8: CONCLUSIONS & LIMITATIONS")
print("=" * 70)

print("""
RESEARCH QUESTION: "Do students who exercise more frequently make
different food choices?"

KEY FINDINGS:
  Based on descriptive analysis of 109 college students:

  1. EXERCISE & DIET:
     Active students show higher mean fruit and vegetable consumption
     compared to the Moderate group, suggesting a possible association
     between exercise frequency and dietary quality.

  2. COOKING:
     Active students report cooking slightly more frequently than
     Moderate exercisers, suggesting a possible link between activity
     level and food preparation habits.

  3. NUTRITIONAL AWARENESS:
     Active students show marginally higher nutritional_check scores,
     suggesting more frequent attention to food labels and nutrition
     information.

  4. HEALTH PERCEPTION:
     Active students report higher healthy_feeling scores on average.
     The histogram (Plot 3) shows the Active group's scores are more
     spread across the scale, while the Moderate group clusters in
     the mid-range.

  5. GENDER:
     Female students report slightly higher fruit and vegetable
     consumption. Male students report slightly higher eating out
     frequency. Differences are modest and should not be overstated
     given the uneven group sizes (63F / 46M).

LIMITATIONS:
  1. SELF-REPORTING BIAS: All variables are self-reported. Exercise
     frequency in particular shows no students claiming to rarely or
     never exercise - likely over-reporting.

  2. SAMPLE SIZE: 109 students from a single institution is a small,
     non-representative sample. Findings cannot be generalised.

  3. DESCRIPTIVE ONLY: No statistical significance testing has been
     applied. Observed differences may be due to chance.

  4. INACTIVE GROUP: The empty 'Inactive' category means a key
     comparison (Active vs Inactive) is not possible with this data.

  5. SURVEY DESIGN: Scale directions are not consistent across columns
     (e.g., for exercise 1=most active, but for fruit_day 1=least
     frequent). Care is needed when interpreting means.

NEXT STEPS (Future Scripts):
  - w3d3/4: Exploring the relationship between upbringing
    (parents_cook, food_childhood) and current eating habits
  - food-choices-complete-analysis.py: Full portfolio project
    combining findings from all scripts
""")

print("=" * 70)
print("SCRIPT COMPLETE")
print("=" * 70)