"""
WEEK 2 DAY 2: JOIN TYPES PRACTICE SCRIPT
Student Engagement Analysis by Age Group

PERSONAL NOTE:
This analysis explores how age relates to online learning engagement.
As a woman in my 40s retraining through online education, I'm personally
interested in understanding how different age groups engage with digital
learning platforms. Does engagement decline with age? Do older learners
interact differently with online materials? This dataset from the Open
University provides real-world insights into these questions.

TRANSPARENCY NOTE:
This script was created with AI assistance (Claude). The joins and analysis
use techniques covered in DataCamp Weeks 1-2. The random sampling section
uses advanced techniques not yet covered in my learning and was written by
Claude with my directional input. When I eventually share this publicly,
I will clearly state the level of AI assistance used.

SCRIPT STRUCTURE:
1. Load and explore ALL 7 datasets
2. Analyze VLE presentation distribution
3. Decide on sampling strategy
4. Perform joins (inner and left)
5. Analyze age vs engagement
"""

import pandas as pd
import os

# =============================================================================
# SECTION 1: INITIAL EXPLORATION - LOAD ALL DATASETS
# Skill Level: ADVANCED (Written by Claude for exploration purposes)
# =============================================================================

print("="*80)
print("PART 1: DATASET EXPLORATION")
print("="*80)
print()

# Set the path to your dataset folder
dataset_path = '/Users/magdalenapirowska/learning/career/data-and-ai-analysis-journey/datasets/open_uni_data'

# List all CSV files in the folder
csv_files = [f for f in os.listdir(dataset_path) if f.endswith('.csv')]
print(f"Found {len(csv_files)} CSV files:")
for file in csv_files:
    print(f"  - {file}")

print("\n" + "="*80 + "\n")

# Load all CSV files into a dictionary
dataframes = {}
for file in csv_files:
    # Create a clean name for the dataframe (remove .csv)
    df_name = file.replace('.csv', '')
    # Load the CSV
    dataframes[df_name] = pd.read_csv(os.path.join(dataset_path, file))
    print(f"Loaded: {file}")

print("\n" + "="*80 + "\n")

# Explore each dataframe
print("EXPLORING EACH DATASET:")
print("="*80)
for name, df in dataframes.items():
    print(f"\n{'='*80}")
    print(f"DATAFRAME: {name}")
    print(f"{'='*80}")
    print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nFirst 3 rows:")
    print(df.head(3))
    print(f"\nData types:")
    print(df.dtypes)
    print("\n")

# =============================================================================
# SECTION 2: ANALYZE VLE PRESENTATIONS
# Skill Level: Week 1-2 (Grouping and sorting)
# Understanding the data before deciding sampling strategy
# =============================================================================

print("\n" + "="*80)
print("PART 2: EXPLORING COURSE PRESENTATIONS IN VLE DATA")
print("="*80)
print()

print("Why are we doing this?")
print("The studentVle table has 10.6 MILLION rows - too large to work with.")
print("We need to decide: filter to one presentation OR random sample across all?")
print()

# Check unique presentations in studentVle (the huge table)
presentations = dataframes['studentVle'][['code_module', 'code_presentation']].drop_duplicates()
print(f"Unique course presentations in studentVle ({len(presentations)} total):")
print(presentations.sort_values(['code_module', 'code_presentation']))

# Count rows per presentation
print("\n" + "="*80)
print("ROW COUNTS PER PRESENTATION:")
print("="*80)
vle_counts = dataframes['studentVle'].groupby(['code_module', 'code_presentation']).size().sort_values(ascending=False)
print(vle_counts)

print("\n" + "="*80)
print(f"TOTAL studentVle rows: {len(dataframes['studentVle']):,}")
print("="*80)
print()

print("DECISION:")
print("Data spans 2013-2014 across multiple courses (AAA through GGG).")
print("Different presentations have very different row counts (117K to 1.2M).")
print("→ Random sampling across ALL presentations is best to avoid bias!")
print()

# =============================================================================
# SECTION 3: EXTRACT THE 3 TABLES WE NEED FOR ANALYSIS
# Skill Level: Week 1-2 (Basic data manipulation)
# =============================================================================

print("="*80)
print("PART 3: PREPARING DATA FOR ANALYSIS")
print("="*80)
print()

print("Extracting the 3 tables we'll use:")
print("  1. studentInfo - demographics including age_band")
print("  2. studentRegistration - when students enrolled")
print("  3. studentVle - engagement data (will sample this)")
print()

student_info = dataframes['studentInfo']
student_registration = dataframes['studentRegistration']
student_vle = dataframes['studentVle']

print(f"✓ studentInfo: {student_info.shape[0]:,} rows")
print(f"✓ studentRegistration: {student_registration.shape[0]:,} rows")
print(f"✓ studentVle: {student_vle.shape[0]:,} rows (will sample)")
print()

print("Age bands available in dataset:")
print(student_info['age_band'].value_counts().sort_index())
print()

# =============================================================================
# SECTION 4: SAMPLING THE VLE DATA
# Skill Level: ADVANCED (Not yet covered - written by Claude)
# =============================================================================

print("="*80)
print("PART 4: SAMPLING VLE DATA")
print("="*80)
print()

print("⚠️  ADVANCED TECHNIQUE USED HERE:")
print("Taking a 1% random sample (~106,000 rows) for manageable analysis.")
print()
print("Method: pandas .sample() with random_state for reproducibility")
print("This technique will be covered in future DataCamp courses.")
print("Code written by Claude based on Magda's directional input.")
print()

# =============================================================================
# ADVANCED: Random sampling code by Claude
# This uses the .sample() method which hasn't been covered yet
# random_state=42 ensures we get the same sample every time we run this
# frac=0.01 means take 1% of rows
# =============================================================================

student_vle_sample = student_vle.sample(frac=0.01, random_state=42)

print(f"✓ Sampled {student_vle_sample.shape[0]:,} rows from studentVle (1% sample)")
print(f"  This represents data from all courses and presentations proportionally")
print()

# =============================================================================
# SECTION 5: JOINING THE TABLES
# Skill Level: Week 2 (DataCamp Joining Data with pandas)
# =============================================================================

print("="*80)
print("PART 5: JOINING TABLES")
print("="*80)
print()

# JOIN 1: INNER JOIN
# Connect student demographics with registration data
# Inner join keeps only students who appear in BOTH tables
print("JOIN 1: Inner Join - studentInfo + studentRegistration")
print("-" * 80)
print("Purpose: Connect student demographics with registration dates")
print("Join type: INNER - keeps only students with registration records")
print("Join keys: code_module, code_presentation, id_student")
print()

students_with_registration = student_info.merge(
    student_registration,
    on=['code_module', 'code_presentation', 'id_student'],
    how='inner'
)

print(f"✓ Result: {students_with_registration.shape[0]:,} rows")
print(f"  Original studentInfo: {student_info.shape[0]:,} rows")
print(f"  Original studentRegistration: {student_registration.shape[0]:,} rows")
print(f"  After inner join: {students_with_registration.shape[0]:,} rows")
print(f"  → All students had registration records (tables match perfectly)")
print()

# JOIN 2: LEFT JOIN
# Add VLE engagement data to our student information
# Left join keeps ALL students from the left table, even if they have no VLE clicks
print("JOIN 2: Left Join - students_with_registration + studentVle_sample")
print("-" * 80)
print("Purpose: Add engagement (clicks) data to student information")
print("Join type: LEFT - keeps all students, even if they have no recorded clicks")
print("Join keys: code_module, code_presentation, id_student")
print()

student_engagement = students_with_registration.merge(
    student_vle_sample,
    on=['code_module', 'code_presentation', 'id_student'],
    how='left'
)

print(f"✓ Result: {student_engagement.shape[0]:,} rows")
print(f"  Left table: {students_with_registration.shape[0]:,} rows")
print(f"  Right table (sample): {student_vle_sample.shape[0]:,} rows")
print(f"  After left join: {student_engagement.shape[0]:,} rows")
print(f"  → More rows because students can have multiple VLE interactions")
print()

# =============================================================================
# SECTION 6: ANALYSIS - AGE AND ENGAGEMENT
# Skill Level: Week 1-2 (Grouping, aggregation, filtering)
# =============================================================================

print("="*80)
print("PART 6: ANALYSIS - AGE GROUP vs ONLINE ENGAGEMENT")
print("="*80)
print()

# Calculate total clicks per student per age group
print("Research Question: How does engagement (total clicks) vary by age group?")
print()

# Group by age_band and student, sum their clicks
engagement_by_age = student_engagement.groupby(['age_band', 'id_student'])['sum_click'].sum().reset_index()

# Now group by age_band to get statistics
age_stats = engagement_by_age.groupby('age_band')['sum_click'].agg(['count', 'mean', 'median', 'sum'])

# Rename columns for clarity
age_stats.columns = ['students_in_sample', 'avg_clicks', 'median_clicks', 'total_clicks']

# Round for readability
age_stats = age_stats.round(2)

print("ENGAGEMENT STATISTICS BY AGE GROUP:")
print("="*80)
print(age_stats)
print()

# =============================================================================
# SECTION 7: INSIGHTS
# =============================================================================

print("="*80)
print("KEY INSIGHTS")
print("="*80)
print()

# Find age group with highest average engagement
highest_engagement = age_stats['avg_clicks'].idxmax()
lowest_engagement = age_stats['avg_clicks'].idxmin()

print(f"📊 Highest average engagement: {highest_engagement} age group")
print(f"   Average clicks: {age_stats.loc[highest_engagement, 'avg_clicks']:.2f}")
print(f"   Students in sample: {age_stats.loc[highest_engagement, 'students_in_sample']:.0f}")
print()

print(f"📊 Lowest average engagement: {lowest_engagement} age group")
print(f"   Average clicks: {age_stats.loc[lowest_engagement, 'avg_clicks']:.2f}")
print(f"   Students in sample: {age_stats.loc[lowest_engagement, 'students_in_sample']:.0f}")
print()

# Calculate engagement difference
engagement_range = age_stats['avg_clicks'].max() - age_stats['avg_clicks'].min()
print(f"📊 Range of average engagement: {engagement_range:.2f} clicks difference")
print(f"   between highest and lowest age groups")
print()

# Personal reflection space
print("="*80)
print("PERSONAL REFLECTION:")
print("="*80)
print("As someone in the 35-55 age group retraining online, these patterns")
print("are directly relevant to my learning journey. Understanding how")
print("different age groups engage with online platforms can help identify")
print("support needs and learning preferences across demographics.")
print()
print("This analysis shows real data from thousands of students, providing")
print("evidence-based insights into online learning behavior across ages.")
print("="*80)
print()

print("✓ Analysis complete!")
print()

# =============================================================================
# IMPORTANT STATISTICAL CAVEAT
# =============================================================================

print("="*80)
print("⚠️  STATISTICAL LIMITATIONS OF THIS ANALYSIS")
print("="*80)
print()

print("IMPORTANT: These findings are preliminary observations only!")
print()

print("Notice the gaps between average and median:")
for age in age_stats.index:
    avg = age_stats.loc[age, 'avg_clicks']
    med = age_stats.loc[age, 'median_clicks']
    gap = avg - med
    print(f"  {age}: Average = {avg:.2f}, Median = {med:.2f} (gap = {gap:.2f})")

print()
print("Large gaps suggest OUTLIERS are influencing the averages!")
print()

print("What we'd need for proper statistical analysis:")
print("  ✓ Box plots to visualize outlier distribution")
print("  ✓ Standard deviation to measure data spread")
print("  ✓ Statistical significance tests (t-test, ANOVA)")
print("  ✓ Percentile analysis (25th, 75th, 90th)")
print("  ✓ Outlier identification and handling")
print()

print("CURRENT CLAIM: 'Data SUGGESTS older students may engage more'")
print("PROPER CLAIM REQUIRES: Statistical tests to confirm significance")
print()

print("📝 NOTE: We will return to this dataset in future weeks with proper")
print("   statistical tools to validate these preliminary observations!")
print("="*80)
print()

# =============================================================================
# SUMMARY: WHAT WE DEMONSTRATED IN THIS SCRIPT
# 
# EXPLORATION PROCESS:
# 1. Loaded all 7 datasets from OULAD
# 2. Explored structure of each table
# 3. Analyzed VLE presentation distribution
# 4. Made informed decision about sampling strategy
#
# JOIN TYPES PRACTICED:
# 1. INNER JOIN - studentInfo + studentRegistration
#    - Kept only students with registration records
#    - Result: Same number of rows (all students had registrations)
#
# 2. LEFT JOIN - combined_data + studentVle_sample
#    - Kept ALL students from left table
#    - Added VLE click data where available
#    - Result: More rows (students can have multiple interactions)
#
# PANDAS TECHNIQUES USED (from Weeks 1-2):
# - .merge() with different join types and multiple keys
# - .groupby() with multiple levels
# - .agg() with multiple functions ['count', 'mean', 'median', 'sum']
# - .reset_index()
# - Column renaming for clarity
# - .round() for readability
# - .idxmax() and .idxmin() to find extremes
# - .value_counts() for categorical data
# - .drop_duplicates() for unique values
# - .sort_values() for ordering data
#
# ADVANCED TECHNIQUES (Claude-written, clearly marked):
# - os.listdir() for file operations
# - List comprehension for filtering files
# - Dictionary comprehension for loading multiple files
# - .sample() for random sampling with reproducibility
# =============================================================================