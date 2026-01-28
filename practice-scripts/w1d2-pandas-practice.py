import pandas as pd

# ===========================
# 1. LOAD AND INSPECT DATA
# ===========================

# Load dataset
student_ai_usage = pd.read_csv('/Users/magdalenapirowska/learning/career/data-and-ai-analysis-journey/datasets/students_ai_usage.csv')

# Initial inspection
print("=" * 50)
print("DATASET INSPECTION")
print("=" * 50)
print("\nFirst 5 rows:")
print(student_ai_usage.head())
print("\nDataset info:")
print(student_ai_usage.info())
print("\nDataset shape (rows, columns):")
print(student_ai_usage.shape)

# ===========================
# 2. DATA CLEANING & TRANSFORMATION
# ===========================

print("\n" + "=" * 50)
print("DATA CLEANING")
print("=" * 50)

# Replace NaN values with "None" for students who don't use AI tools
# This allows us to compare AI users vs non-users in analysis
student_ai_usage['ai_tools_used'] = student_ai_usage['ai_tools_used'].fillna("None")
student_ai_usage['purpose_of_ai'] = student_ai_usage['purpose_of_ai'].fillna("None")

# Create new column: percentage change in grades after AI introduction
# Formula: (new - old) / old = percentage change
student_ai_usage['grade_change_post_ai'] = (
    (student_ai_usage['grades_after_ai'] - student_ai_usage['grades_before_ai']) / 
    student_ai_usage['grades_before_ai']
).round(2)

print("\nSample of cleaned data with new grade_change_post_ai column:")
print(student_ai_usage[['grades_before_ai', 'grades_after_ai', 'grade_change_post_ai']].head())

# ===========================
# 3. SUMMARY STATISTICS
# ===========================

print("\n" + "=" * 50)
print("SUMMARY STATISTICS - Key Numerical Variables")
print("=" * 50)

# Select numerical columns for aggregate analysis
quant_values = student_ai_usage[[
    'age', 
    'study_hours_per_day',
    'grades_before_ai',
    'grades_after_ai',
    'daily_screen_time_hours'
]]

# Calculate multiple statistics at once
print(quant_values.agg(["mean", "median", "std", "max", "min"]))

# ===========================
# 4. GROUPING ANALYSIS
# ===========================

print("\n" + "=" * 50)
print("GROUPING ANALYSIS")
print("=" * 50)

# Analysis 1: Impact of AI tool usage on grade changes
print("\n--- Grade Change by AI Tool Used ---")
print("Question: How do grades change based on which AI tool students use?")
ai_impact = student_ai_usage.groupby('ai_tools_used')['grade_change_post_ai'].agg([
    'min', 'max', 'mean', 'median'
])
print(ai_impact)

# Analysis 2: Age distribution by AI tool and purpose
print("\n--- Age by AI Tool and Purpose ---")
print("Question: What's the age profile for different AI tools and purposes?")
ai_tool_purpose_vs_age = (
    student_ai_usage
    .groupby(['ai_tools_used', 'purpose_of_ai'])['age']
    .agg(['min', 'max', 'median', 'mean'])
).round(2)
print(ai_tool_purpose_vs_age)

# Analysis 3: Study hours by age and AI tool usage
print("\n--- Study Hours by Age and AI Tool ---")
print("Question: How do study hours vary by age and AI tool usage?")
study_efficiency_by_age = (
    student_ai_usage
    .groupby(['age', 'ai_tools_used'])['study_hours_per_day']
    .agg(['min', 'max', 'mean', 'median'])
).round(2)
print(study_efficiency_by_age)

# ===========================
# 5. PIVOT TABLE ANALYSIS
# ===========================

print("\n" + "=" * 50)
print("PIVOT TABLE ANALYSIS")
print("=" * 50)

# Pivot 1: Grades before AI by tool and education level
print("\n--- Average Grades Before AI: By Tool and Education Level ---")
print("Question: How did grades vary before AI across education levels and tools?")
grades_before_pivot = student_ai_usage.pivot_table(
    values='grades_before_ai',
    index='ai_tools_used',
    columns='education_level',
    aggfunc='mean'
).round(2)
print(grades_before_pivot)

# ===========================
# 6. ADDITIONAL SUGGESTED ANALYSES
# ===========================

print("\n" + "=" * 50)
print("ADDITIONAL INSIGHTS")
print("=" * 50)

# Analysis 4: Compare grades AFTER AI by tool and education level
print("\n--- Average Grades After AI: By Tool and Education Level ---")
grades_after_pivot = student_ai_usage.pivot_table(
    values='grades_after_ai',
    index='ai_tools_used',
    columns='education_level',
    aggfunc='mean'
).round(2)
print(grades_after_pivot)

# Analysis 5: Screen time comparison - AI users vs non-users
print("\n--- Screen Time: AI Users vs Non-Users ---")
print("Question: Do AI users spend more time on screens?")
screen_time_comparison = student_ai_usage.groupby('ai_tools_used')['daily_screen_time_hours'].agg([
    'mean', 'median', 'std'
]).round(2)
print(screen_time_comparison)

# Analysis 6: Count of students by AI tool
print("\n--- Student Count by AI Tool ---")
print("Question: How many students use each AI tool?")
tool_counts = student_ai_usage['ai_tools_used'].value_counts()
print(tool_counts)

# Analysis 7: Correlation between study hours and grade improvement
print("\n--- Correlation: Study Hours vs Grade Change ---")
print("Question: Does studying more correlate with grade improvement?")
correlation = student_ai_usage[['study_hours_per_day', 'grade_change_post_ai']].corr()
print(correlation)

print("\n" + "=" * 50)
print("ANALYSIS COMPLETE")
print("=" * 50)