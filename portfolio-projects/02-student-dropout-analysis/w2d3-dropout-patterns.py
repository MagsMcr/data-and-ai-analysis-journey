"""
Week 2 Day 3: Student Unregistration Analysis
==============================================
Created: February 5, 2026
Dataset: Open University Learning Analytics Dataset (OULAD)

CONTEXT:
This script was created collaboratively by Magda McCrimmon and Claude (Anthropic).
Magda provided the strategic direction, research questions, and analytical approach.
Claude wrote the code implementation based on Magda's specific guidance.

PURPOSE:
This analysis demonstrates Week 2 Day 3 concepts from DataCamp's "Joining Data with pandas":
- Merging on different join keys (single columns and multiple column combinations)
- Semi joins (filtering based on existence in another table)
- Anti joins (filtering based on non-existence in another table)
- Multiple sequential merges with different join strategies

RESEARCH QUESTIONS:

Part 1 - Student Unregistration Profile:
  Q1: When do students typically drop out? (timing analysis)
  Q2: Which courses have the highest dropout rates?
  Q3: Are there demographic patterns among students who unregister?
      (age, gender, education level, disability, previous attempts, region)

Part 2 - Engagement Patterns Among Dropouts:
  Q4: What proportion of dropouts submitted assessments before leaving?
  Q5: How do demographics differ between dropouts who did vs. didn't submit assessments?
  Q6: For students who submitted before dropping:
      - What types of assessments did they submit?
      - How many assessments did they complete?
      - What were their score patterns?
      - When did they drop out relative to their submissions?

ANALYTICAL APPROACH:
- Merge studentInfo + studentRegistration to get demographics and unregistration dates
- Filter for students with non-null date_unregistration
- Add course details using multiple join keys (code_module + code_presentation)
- Use semi join concept to identify dropouts who submitted assessments
- Use anti join concept to identify dropouts who never submitted
- Compare patterns between these two groups

NOTE ON STATISTICAL RIGOR:
These are preliminary exploratory findings. The analysis identifies patterns that "seem to be"
correlated with dropping out, but proper statistical testing would be needed to confirm
relationships and control for confounding variables.
"""

import pandas as pd
import numpy as np

# Load all necessary datasets
print("=" * 80)
print("LOADING DATASETS")
print("=" * 80)

# Assuming datasets are in the datasets/open_uni_data/ directory
studentInfo = pd.read_csv('datasets/open_uni_data/studentInfo.csv')
studentRegistration = pd.read_csv('datasets/open_uni_data/studentRegistration.csv')
studentAssessment = pd.read_csv('datasets/open_uni_data/studentAssessment.csv')
courses = pd.read_csv('datasets/open_uni_data/courses.csv')
assessments = pd.read_csv('datasets/open_uni_data/assessments.csv')

print(f"✓ studentInfo: {studentInfo.shape[0]:,} rows")
print(f"✓ studentRegistration: {studentRegistration.shape[0]:,} rows")
print(f"✓ studentAssessment: {studentAssessment.shape[0]:,} rows")
print(f"✓ courses: {courses.shape[0]:,} rows")
print(f"✓ assessments: {assessments.shape[0]:,} rows")
print()

# ============================================================================
# PART 1: BUILDING THE UNREGISTERED STUDENTS DATASET
# ============================================================================
# Research Questions: When do students drop out? Which courses? What demographics?
# Demonstrates: Merging on different join keys, filtering, multiple sequential joins

print("=" * 80)
print("PART 1: ANALYZING STUDENT UNREGISTRATION PATTERNS")
print("=" * 80)
print()

# Step 1: Merge studentInfo with studentRegistration to get demographics + unregistration data
# Using inner join on id_student
students_with_reg = studentInfo.merge(
    studentRegistration,
    on='id_student',
    how='inner',
    suffixes=('_info', '_reg')
)

print("Step 1: Merged studentInfo + studentRegistration")
print(f"Combined dataset: {students_with_reg.shape[0]:,} rows")
print()

# Step 2: Filter for students who actually unregistered (date_unregistration is NOT NaN)
unregistered_students = students_with_reg[students_with_reg['date_unregistration'].notna()].copy()

print("Step 2: Filtered for students who unregistered")
print(f"Students who unregistered: {unregistered_students.shape[0]:,} rows")
print(f"Percentage of all students: {(len(unregistered_students) / len(studentInfo) * 100):.1f}%")
print()

# Step 3: Add course details using code_module and code_presentation as join keys
# This demonstrates merging on MULTIPLE columns with DIFFERENT names (Chapter 3 concept!)
# Note: After Step 1 merge, columns have suffixes (_info and _reg), so we use _info version
unregistered_with_courses = unregistered_students.merge(
    courses,
    left_on=['code_module_info', 'code_presentation_info'],
    right_on=['code_module', 'code_presentation'],
    how='left'
)

print("Step 3: Added course information")
print(f"Dataset with course details: {unregistered_with_courses.shape[0]:,} rows")
print()

# ============================================================================
# ANALYSIS: DROPOUT TIMING PATTERNS (Q1)
# ============================================================================
# Question: Is there a specific point in courses when students drop out more often?

print("-" * 80)
print("Q1: WHEN DO STUDENTS DROP OUT?")
print("-" * 80)
print()

# Basic statistics on dropout timing
print("Dropout Timing Statistics:")
print(unregistered_with_courses['date_unregistration'].describe())
print()

# Create categories: Early (before day 60), Mid (60-120), Late (120+)
def categorize_dropout_timing(days):
    if days < 60:
        return 'Early (< 60 days)'
    elif days < 120:
        return 'Mid (60-120 days)'
    else:
        return 'Late (120+ days)'

unregistered_with_courses['dropout_period'] = unregistered_with_courses['date_unregistration'].apply(categorize_dropout_timing)

dropout_timing = unregistered_with_courses['dropout_period'].value_counts().sort_index()
print("Dropout by Course Period:")
print(dropout_timing)
print()
print("Percentages:")
print((dropout_timing / dropout_timing.sum() * 100).round(1))
print()

# ============================================================================
# ANALYSIS: COURSES WITH HIGHEST DROPOUT RATES (Q2)
# ============================================================================
# Question: Are particular courses associated with higher dropout rates?

print("-" * 80)
print("Q2: WHICH COURSES HAVE HIGHEST DROPOUT RATES?")
print("-" * 80)
print()

# Count dropouts by course module
dropouts_by_module = unregistered_with_courses['code_module_info'].value_counts()
print("Dropouts by Course Module:")
print(dropouts_by_module)
print()

# Calculate dropout rate per module (need total enrollments)
enrollments_by_module = students_with_reg.groupby('code_module_info').size()
dropout_rate_by_module = (dropouts_by_module / enrollments_by_module * 100).sort_values(ascending=False)
print("Dropout Rate by Course Module (%):")
print(dropout_rate_by_module.round(1))
print()

# Also look at specific presentations (same course, different semester)
dropouts_by_presentation = unregistered_with_courses.groupby(['code_module_info', 'code_presentation_info']).size().sort_values(ascending=False)
print("Top 10 Course Presentations with Most Dropouts:")
print(dropouts_by_presentation.head(10))
print()

# ============================================================================
# ANALYSIS: DEMOGRAPHIC PATTERNS IN DROPOUTS (Q3)
# ============================================================================
# Question: Do any demographic factors seem correlated with dropping out?
# Examining: age, gender, education level, disability, previous attempts, region

print("-" * 80)
print("Q3: DEMOGRAPHIC PATTERNS IN DROPOUTS")
print("-" * 80)
print()

# Age band analysis
print("Dropouts by Age Band:")
age_dropouts = unregistered_with_courses['age_band'].value_counts()
print(age_dropouts)
print()
print("Percentage distribution:")
print((age_dropouts / age_dropouts.sum() * 100).round(1))
print()

# Gender analysis
print("Dropouts by Gender:")
gender_dropouts = unregistered_with_courses['gender'].value_counts()
print(gender_dropouts)
print()
print("Percentage distribution:")
print((gender_dropouts / gender_dropouts.sum() * 100).round(1))
print()

# Education level analysis
print("Dropouts by Highest Education:")
education_dropouts = unregistered_with_courses['highest_education'].value_counts()
print(education_dropouts)
print()
print("Percentage distribution:")
print((education_dropouts / education_dropouts.sum() * 100).round(1))
print()

# Disability analysis
print("Dropouts by Disability Status:")
disability_dropouts = unregistered_with_courses['disability'].value_counts()
print(disability_dropouts)
print()
print("Percentage distribution:")
print((disability_dropouts / disability_dropouts.sum() * 100).round(1))
print()

# Previous attempts analysis (might indicate struggling students)
print("Dropouts by Number of Previous Attempts:")
prev_attempts_dropouts = unregistered_with_courses['num_of_prev_attempts'].value_counts().sort_index()
print(prev_attempts_dropouts)
print()
print("Average previous attempts for dropouts:", unregistered_with_courses['num_of_prev_attempts'].mean().round(2))
print()

# Region analysis
print("Top 5 Regions with Most Dropouts:")
region_dropouts = unregistered_with_courses['region'].value_counts().head(5)
print(region_dropouts)
print()

# ============================================================================
# PART 2: ENGAGEMENT PATTERNS - COMPARING DROPOUTS BY ASSESSMENT SUBMISSION
# ============================================================================
# Research Questions: Did dropouts submit assessments? How do submitters vs 
# non-submitters differ demographically and behaviorally?
# Demonstrates: Semi join (students who DID submit), Anti join (students who DIDN'T submit)

print("=" * 80)
print("PART 2: DROPOUTS - ASSESSMENT SUBMITTERS vs NON-SUBMITTERS")
print("=" * 80)
print()

# Step 1: Get list of students who submitted at least one assessment (SEMI JOIN concept!)
students_who_submitted = studentAssessment['id_student'].unique()
print(f"Students who submitted at least one assessment: {len(students_who_submitted):,}")
print()

# Step 2: Identify dropouts who DID submit (semi join result)
dropouts_who_submitted = unregistered_with_courses[
    unregistered_with_courses['id_student'].isin(students_who_submitted)
].copy()

print(f"Dropouts who SUBMITTED assessments: {len(dropouts_who_submitted):,}")
print()

# Step 3: Identify dropouts who DIDN'T submit (anti join result!)
dropouts_no_submission = unregistered_with_courses[
    ~unregistered_with_courses['id_student'].isin(students_who_submitted)
].copy()

print(f"Dropouts who NEVER submitted: {len(dropouts_no_submission):,}")
print()

# Calculate percentages
total_dropouts = len(unregistered_with_courses)
print(f"Percentage who submitted before dropping: {(len(dropouts_who_submitted) / total_dropouts * 100):.1f}%")
print(f"Percentage who never submitted: {(len(dropouts_no_submission) / total_dropouts * 100):.1f}%")
print()

# ============================================================================
# ANALYSIS: DEMOGRAPHIC COMPARISON (Q5)
# ============================================================================
# Question: How do demographics differ between dropouts who did vs didn't submit?
# Demonstrates: Comparing results from semi join vs anti join operations

print("-" * 80)
print("Q5: DEMOGRAPHIC COMPARISON - SUBMITTERS vs NON-SUBMITTERS")
print("-" * 80)
print()

# Age band comparison
print("Age Band Distribution:")
print("\nSubmitters who dropped:")
print((dropouts_who_submitted['age_band'].value_counts() / len(dropouts_who_submitted) * 100).round(1))
print("\nNon-submitters who dropped:")
print((dropouts_no_submission['age_band'].value_counts() / len(dropouts_no_submission) * 100).round(1))
print()

# Gender comparison
print("Gender Distribution:")
print("\nSubmitters who dropped:")
print((dropouts_who_submitted['gender'].value_counts() / len(dropouts_who_submitted) * 100).round(1))
print("\nNon-submitters who dropped:")
print((dropouts_no_submission['gender'].value_counts() / len(dropouts_no_submission) * 100).round(1))
print()

# Education level comparison
print("Education Level Distribution:")
print("\nSubmitters who dropped:")
print((dropouts_who_submitted['highest_education'].value_counts() / len(dropouts_who_submitted) * 100).round(1))
print("\nNon-submitters who dropped:")
print((dropouts_no_submission['highest_education'].value_counts() / len(dropouts_no_submission) * 100).round(1))
print()

# Disability comparison
print("Disability Status:")
print("\nSubmitters who dropped:")
print((dropouts_who_submitted['disability'].value_counts() / len(dropouts_who_submitted) * 100).round(1))
print("\nNon-submitters who dropped:")
print((dropouts_no_submission['disability'].value_counts() / len(dropouts_no_submission) * 100).round(1))
print()

# Previous attempts comparison
print("Average Previous Attempts:")
print(f"Submitters who dropped: {dropouts_who_submitted['num_of_prev_attempts'].mean():.2f}")
print(f"Non-submitters who dropped: {dropouts_no_submission['num_of_prev_attempts'].mean():.2f}")
print()

# ============================================================================
# ANALYSIS: ASSESSMENT SUBMISSION PATTERNS (Q6)
# ============================================================================
# Question: For dropouts who submitted - what types, how many, what scores?
# Demonstrates: Merging semi join results with additional tables for deeper analysis

print("-" * 80)
print("Q6: ASSESSMENT PATTERNS FOR DROPOUTS WHO SUBMITTED")
print("-" * 80)
print()

# Get assessment details for dropouts who submitted
dropout_submissions = studentAssessment[
    studentAssessment['id_student'].isin(dropouts_who_submitted['id_student'])
].copy()

print(f"Total assessment submissions from eventual dropouts: {len(dropout_submissions):,}")
print()

# Merge with assessments table to get assessment types
dropout_submissions_detailed = dropout_submissions.merge(
    assessments,
    on='id_assessment',
    how='left'
)

# Assessment type analysis
print("Assessment Types Submitted by Dropouts:")
assessment_type_counts = dropout_submissions_detailed['assessment_type'].value_counts()
print(assessment_type_counts)
print()
print("Percentage distribution:")
print((assessment_type_counts / assessment_type_counts.sum() * 100).round(1))
print()

# How many assessments did they submit before dropping?
submissions_per_dropout = dropout_submissions.groupby('id_student').size()
print("Number of Assessments Submitted Before Dropping:")
print(submissions_per_dropout.describe())
print()
print("Distribution:")
print(submissions_per_dropout.value_counts().sort_index().head(10))
print()

# Score patterns - did they have lower scores?
print("Score Statistics for Dropouts Who Submitted:")
print(dropout_submissions['score'].describe())
print()

# Average score comparison (would need non-dropout scores for full comparison)
avg_dropout_score = dropout_submissions['score'].mean()
print(f"Average score for dropouts who submitted: {avg_dropout_score:.2f}")
print()

# ============================================================================
# ANALYSIS: DROPOUT TIMING COMPARISON (Q4 extended)
# ============================================================================
# Question: When did submitters vs non-submitters drop out?

print("-" * 80)
print("Q4: DROPOUT TIMING - SUBMITTERS vs NON-SUBMITTERS")
print("-" * 80)
print()

print("When did they drop out?")
print("\nSubmitters - Dropout Period Distribution:")
print(dropouts_who_submitted['dropout_period'].value_counts().sort_index())
print("\nNon-submitters - Dropout Period Distribution:")
print(dropouts_no_submission['dropout_period'].value_counts().sort_index())
print()

print("Average dropout timing (days):")
print(f"Submitters: {dropouts_who_submitted['date_unregistration'].mean():.1f} days")
print(f"Non-submitters: {dropouts_no_submission['date_unregistration'].mean():.1f} days")
print()

# ============================================================================
# KEY INSIGHTS SUMMARY
# ============================================================================

print("=" * 80)
print("KEY INSIGHTS SUMMARY")
print("=" * 80)
print()

print("CHAPTER 3 CONCEPTS DEMONSTRATED:")
print("✓ Merging on different column combinations (id_student, code_module + code_presentation)")
print("✓ Semi join: Filtering dropouts who exist in assessment submissions")
print("✓ Anti join: Filtering dropouts who DON'T exist in assessment submissions")
print("✓ Multiple sequential merges with different join keys")
print("✓ Left joins to add course and assessment details")
print()

print("ANALYTICAL INSIGHTS:")
print(f"1. {len(unregistered_students):,} students ({(len(unregistered_students)/len(studentInfo)*100):.1f}%) unregistered from courses")
print(f"2. {(len(dropouts_who_submitted)/total_dropouts*100):.1f}% of dropouts submitted at least one assessment")
print(f"3. {(len(dropouts_no_submission)/total_dropouts*100):.1f}% dropped without ever submitting")
print(f"4. Most common dropout period: {unregistered_with_courses['dropout_period'].mode()[0]}")
print(f"5. Course with highest dropout rate: {dropout_rate_by_module.index[0]} ({dropout_rate_by_module.iloc[0]:.1f}%)")
print()

print("Note: These are preliminary observations. Proper statistical analysis would be needed")
print("to confirm correlations and control for confounding variables.")
print()

print("=" * 80)
print("ANALYSIS COMPLETE!")
print("=" * 80)