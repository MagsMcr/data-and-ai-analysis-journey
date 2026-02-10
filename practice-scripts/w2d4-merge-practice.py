"""
Week 2 Day 4 Practice Script
Demonstrating Chapter 4 Concepts: merge_ordered, merge_asof, and melt
Using OULAD (Open University Learning Analytics Dataset)
Course: AAA 2013J (Social Sciences, February 2013 presentation)
"""

import pandas as pd

# ============================================
# STEP 1-2: LOAD OULAD TABLES
# ============================================

print("=" * 60)
print("LOADING OULAD DATASET")
print("=" * 60)

# Load the three required tables
studentAssessment = pd.read_csv('datasets/open_uni_data/studentAssessment.csv')
studentVle = pd.read_csv('datasets/open_uni_data/studentVle.csv')
assessments = pd.read_csv('datasets/open_uni_data/assessments.csv')

# ============================================
# STEP 3: INITIAL EXPLORATION
# ============================================

print("\n" + "=" * 60)
print("INITIAL DATA EXPLORATION")
print("=" * 60)

# Create dictionary for easy iteration
files = {
    'studentAssessment': studentAssessment,
    'studentVle': studentVle,
    'assessments': assessments
}

# Display basic info for each table
for name, df in files.items():
    print(f"\n=== {name} ===")
    print(df.head())
    print(df.info())
    print(df.shape)

# ============================================
# STEP 4: MERGE AND FILTER TO ONE COURSE
# ============================================

print("\n" + "=" * 60)
print("MERGING TABLES AND FILTERING TO COURSE AAA 2013J")
print("=" * 60)

# Merge studentAssessment with assessments to add course information
# studentAssessment only has id_assessment, not course details
student_performance = studentAssessment.merge(
    assessments,
    on='id_assessment',
    how='inner'
)

# Filter all three tables to one specific course and presentation
# AAA = Social Sciences, 2013J = February 2013 presentation
student_performance_filtered = student_performance[
    (student_performance['code_module'] == 'AAA') & 
    (student_performance['code_presentation'] == '2013J')
]

assessments_filtered = assessments[
    (assessments['code_module'] == 'AAA') & 
    (assessments['code_presentation'] == '2013J')
]

student_vle_filtered = studentVle[
    (studentVle['code_module'] == 'AAA') & 
    (studentVle['code_presentation'] == '2013J')
]

print(f"\nFiltered data summary:")
print(f"Student submissions: {len(student_performance_filtered)} rows")
print(f"Assessments: {len(assessments_filtered)} assessments")
print(f"VLE interactions: {len(student_vle_filtered)} interactions")

# ============================================
# STEP 5-6: PREPARE DATA FOR merge_ordered
# ============================================

print("\n" + "=" * 60)
print("PREPARING DATA FOR merge_ordered DEMONSTRATION")
print("=" * 60)

# Create daily submission counts
# Group submissions by date and count how many happened each day
student_assessment_date = student_performance_filtered.groupby('date_submitted').size()
student_assessment_date = student_assessment_date.reset_index()
student_assessment_date = student_assessment_date.rename(columns={
    'date_submitted': 'date',
    0: 'submission_count'
})

# Extract assessment deadlines
assessments_dates = assessments_filtered[['id_assessment', 'date']]

print("\nDaily submission counts:")
print(student_assessment_date.head())
print("\nAssessment deadlines:")
print(assessments_dates.head())

# ============================================
# STEP 7: DEMONSTRATE merge_ordered
# ============================================

print("\n" + "=" * 60)
print("CHAPTER 4 CONCEPT 1: merge_ordered")
print("=" * 60)

# merge_ordered: Merges time-series data with automatic sorting
# Uses forward fill to propagate assessment IDs to all subsequent dates
# This shows which assessment is "active" at each point in time

submissions = pd.merge_ordered(
    student_assessment_date,
    assessments_dates,
    left_on='date',
    right_on='date',
    how='outer',              # Keep all dates from both DataFrames
    fill_method='ffill'       # Forward fill: propagate last known assessment ID
)

submissions.sort_values(by='date', inplace=True)

print("\nMerged submissions with assessments (forward filled):")
print(submissions.head(20))

print("\nWhat this shows:")
print("- Days 7-18: Submissions before first deadline (id_assessment = NaN)")
print("- Day 19: First assessment deadline (id_assessment = 1752)")
print("- Day 19: HUGE spike in submissions (138 submissions!)")
print("- Days 20+: Forward fill keeps showing assessment 1752")
print("- Pattern: Students submit heavily on deadline day, some submit late")

# ============================================
# STEP 8: PREPARE DATA FOR merge_asof
# ============================================

print("\n" + "=" * 60)
print("PREPARING DATA FOR merge_asof DEMONSTRATION")
print("=" * 60)

# Sample of student submissions (first 100 to keep manageable)
student_performance_sample = (
    student_performance_filtered[['id_student', 'id_assessment', 'date_submitted']]
    .head(100)
    .sort_values(['id_student', 'date_submitted'])
    .reset_index(drop=True)
)

# Aggregate VLE activity: total clicks per student per day
vle_activity = (
    student_vle_filtered[['id_student', 'date', 'sum_click']]
    .groupby(['id_student', 'date'])
    .sum()
    .reset_index()
    .sort_values(['id_student', 'date'])
)

print("\nStudent submissions sample:")
print(student_performance_sample[['id_student', 'date_submitted']].head(10))
print("\nVLE activity (clicks per student per day):")
print(vle_activity[['id_student', 'date']].head(10))

# ============================================
# STEP 9: DEMONSTRATE merge_asof
# ============================================

print("\n" + "=" * 60)
print("CHAPTER 4 CONCEPT 2: merge_asof")
print("=" * 60)

# merge_asof: Fuzzy matching for time-series data
# Matches each submission to the most recent prior VLE activity
# Direction='backward' means "look backward in time for nearest match"

submissions_vs_vle_activity = pd.merge_asof(
    student_performance_sample.sort_values('date_submitted'),
    vle_activity.sort_values('date'),
    left_on='date_submitted',
    right_on='date',
    direction='backward',      # Match to most recent prior date
    suffixes=('_submission', '_vle')
)

print("\nSubmissions matched to most recent VLE activity:")
print(submissions_vs_vle_activity.head(15))

print("\nWhat this shows:")
print("- Each submission is matched to the nearest prior VLE activity date")
print("- 'backward' direction = find most recent activity BEFORE submission")
print("- Shows student engagement (clicks) leading up to submission")
print("- This helps analyze: Were students active on platform before submitting?")

# ============================================
# STEP 10-11: DEMONSTRATE melt
# ============================================

print("\n" + "=" * 60)
print("CHAPTER 4 CONCEPT 3: melt (Reshaping Data)")
print("=" * 60)

# First create WIDE format: each assessment is a column
scores_wide = (
    student_performance_filtered[['id_student', 'id_assessment', 'score']]
    .pivot_table(
        values='score',
        index='id_student',
        columns='id_assessment',
        aggfunc='mean'
    )
    .head(10)  # Just first 10 students for demonstration
)

print("\nWIDE FORMAT (each assessment is a column):")
print(scores_wide)

# Now melt to LONG format: one row per student-assessment combination
scores_long = (
    scores_wide
    .reset_index()
    .melt(
        id_vars='id_student',           # Keep student ID as identifier
        var_name='id_assessment',        # Old column names become values here
        value_name='score'              # Old cell values go here
    )
    .dropna()  # Remove missing scores
)

print("\nLONG FORMAT (one row per student-assessment pair):")
print(scores_long.head(15))

print("\nWhat this shows:")
print("- Wide format: Easy to compare assessments side-by-side")
print("- Long format: Better for analysis, filtering, grouping (tidy data)")
print("- melt() is the opposite of pivot_table()")

# ============================================
# STEP 12: SUMMARY
# ============================================

print("\n" + "=" * 60)
print("WEEK 2 DAY 4 PRACTICE SCRIPT SUMMARY")
print("=" * 60)

print("\n📊 DATASET USED:")
print(f"   Course: AAA (Social Sciences)")
print(f"   Presentation: 2013J (February 2013)")
print(f"   Total student submissions: {len(student_performance_filtered)}")
print(f"   Total assessments: {len(assessments_filtered)}")
print(f"   Total VLE interactions: {len(student_vle_filtered)}")
print(f"   Date range: Day {student_performance_filtered['date_submitted'].min()} to Day {student_performance_filtered['date_submitted'].max()}")

print("\n🔧 CHAPTER 4 CONCEPTS DEMONSTRATED:")

print("\n1. merge_ordered:")
print("   • Purpose: Merge time-series data with gaps")
print("   • Key feature: Automatic sorting + optional forward fill")
print("   • Use case: Match daily submissions to assessment deadlines")
print("   • Result: Shows submission patterns around deadlines")
print("   • Insight: Massive spike (138 submissions) on deadline day!")

print("\n2. merge_asof:")
print("   • Purpose: Fuzzy matching on sorted data (nearest neighbor)")
print("   • Key feature: Match to nearest date (backward/forward/nearest)")
print("   • Use case: Match submissions to most recent VLE activity")
print("   • Result: Shows student engagement before submitting")
print("   • Critical: Both DataFrames MUST be sorted!")

print("\n3. melt:")
print("   • Purpose: Reshape data from wide to long format")
print("   • Key feature: Convert columns to rows (opposite of pivot)")
print("   • Use case: Transform assessment scores for analysis")
print("   • Result: Tidy data format (one observation per row)")
print("   • When to use: When variables are stored as columns instead of rows")

print("\n✅ SKILLS PRACTICED:")
print("   • Merging multiple tables to combine information")
print("   • Filtering data to specific subsets")
print("   • Aggregating data (groupby, sum, count)")
print("   • Working with time-series patterns")
print("   • Reshaping data structures")
print("   • Real-world data analysis workflow")

print("\n🎯 KEY TAKEAWAYS:")
print("   • merge_ordered: Best for time-series with gaps")
print("   • merge_asof: Best for fuzzy time matching (sorted data required)")
print("   • melt: Converts wide → long (tidy data principle)")
print("   • Real data requires preparation: merging, filtering, cleaning")
print("   • Different merge types solve different problems")

print("\n" + "=" * 60)
print("PRACTICE SCRIPT COMPLETE!")
print("=" * 60)