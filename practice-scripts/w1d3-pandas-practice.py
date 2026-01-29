import pandas as pd

# Load the student AI usage dataset
students = pd.read_csv('datasets/students_ai_usage.csv')

print("=" * 60)
print("WEEK 1 DAY 3 - PANDAS CHAPTER 3 PRACTICE")
print("Dataset: Student AI Usage")
print("=" * 60)

print("\n=== DATASET OVERVIEW ===")
print(students.head())
print("\n", students.info())
print("\nDataset shape:", students.shape)

# ============================================
# CHAPTER 3 CONCEPT 1: Sorting Values
# ============================================

print("\n" + "=" * 60)
print("CONCEPT 1: SORTING VALUES")
print("=" * 60)

# Sort by grade change (who improved most with AI?)
print("\nTop 10 students by grade improvement after using AI:")
students_sorted = students.sort_values('grade_change_post_ai', ascending=False)
print(students_sorted[['age', 'grade_before_ai', 'grade_after_ai', 'grade_change_post_ai']].head(10))

# Sort by multiple columns
print("\nStudents sorted by education level, then study hours:")
students_multi_sort = students.sort_values(['education_level', 'study_hours_per_day'], 
                                           ascending=[True, False])
print(students_multi_sort[['education_level', 'study_hours_per_day', 'grade_after_ai']].head(10))

# ============================================
# CHAPTER 3 CONCEPT 2: Subsetting with .iloc[]
# ============================================

print("\n" + "=" * 60)
print("CONCEPT 2: POSITION-BASED SUBSETTING WITH .iloc[]")
print("=" * 60)

# Get first 5 rows, columns 3-5
print("\nFirst 5 students, columns 3-5:")
subset_positions = students.iloc[:5, 2:5]
print(subset_positions)

# Get last 3 rows, first 4 columns
print("\nLast 3 students, first 4 columns:")
print(students.iloc[-3:, :4])

# Get every 50th student
print("\nEvery 50th student (sample):")
print(students.iloc[::50, :5])

# ============================================
# CHAPTER 3 CONCEPT 3: Pivot Tables
# ============================================

print("\n" + "=" * 60)
print("CONCEPT 3: PIVOT TABLES")
print("=" * 60)

# Pivot 1: Average grades by education level and screen time category
print("\n=== PIVOT TABLE 1: Average Grade After AI ===")
print("Rows: Education Level | Columns: Screen Time Category")

# First, create screen time categories
students['screen_time_category'] = pd.cut(students['screen_time_hours'], 
                                          bins=[0, 3, 6, 12], 
                                          labels=['Low (0-3h)', 'Medium (3-6h)', 'High (6-12h)'])

grade_pivot = students.pivot_table(
    values='grade_after_ai',
    index='education_level',
    columns='screen_time_category',
    aggfunc='mean'
)
print(grade_pivot.round(2))

# Pivot 2: Average study hours by age group and purpose of AI
print("\n=== PIVOT TABLE 2: Average Study Hours ===")
print("Rows: Age Group | Columns: Purpose of AI")

# Create age groups
students['age_group'] = pd.cut(students['age'], 
                               bins=[0, 20, 25, 30, 100], 
                               labels=['18-20', '21-25', '26-30', '30+'])

study_pivot = students.pivot_table(
    values='study_hours_per_day',
    index='age_group',
    columns='purpose_of_ai',
    aggfunc='mean',
    fill_value=0
)
print(study_pivot.round(2))

# ============================================
# CHAPTER 3 CONCEPT 4: Subsetting Pivot Tables
# ============================================

print("\n" + "=" * 60)
print("CONCEPT 4: SUBSETTING PIVOT TABLES")
print("=" * 60)

# Subset by rows (education levels)
print("\nGraduate and PhD students only:")
print(grade_pivot.loc[['Graduate', 'PhD']])

# Subset by columns (screen time categories)
print("\nHigh screen time students only:")
print(grade_pivot['High (6-12h)'])

# Subset both rows and columns
print("\nUndergraduate students with Medium screen time:")
print(grade_pivot.loc['Undergraduate', 'Medium (3-6h)'])

# ============================================
# CHAPTER 3 CONCEPT 5: Calculating Means Across Axes
# ============================================

print("\n" + "=" * 60)
print("CONCEPT 5: MEAN CALCULATIONS ACROSS AXES")
print("=" * 60)

# Mean by education level (across all screen time categories)
print("\n=== Mean grade by education level (across all screen times) ===")
mean_by_education = grade_pivot.mean(axis='columns')
print(mean_by_education.round(2))

# Mean by screen time category (across all education levels)
print("\n=== Mean grade by screen time category (across all education levels) ===")
mean_by_screen_time = grade_pivot.mean()
print(mean_by_screen_time.round(2))

# Find which education level had highest average grade
print("\n=== Education level with highest average grade ===")
highest_grade_education = mean_by_education[mean_by_education == mean_by_education.max()]
print(highest_grade_education)

# Find which screen time category had lowest average grade
print("\n=== Screen time category with lowest average grade ===")
lowest_grade_screen_time = mean_by_screen_time[mean_by_screen_time == mean_by_screen_time.min()]
print(lowest_grade_screen_time)

# ============================================
# ADDITIONAL ANALYSIS: Combining Concepts
# ============================================

print("\n" + "=" * 60)
print("BONUS: COMBINING MULTIPLE CONCEPTS")
print("=" * 60)

# Create comprehensive pivot with margins (totals)
print("\n=== Grade improvement by education and AI purpose (with totals) ===")
comprehensive_pivot = students.pivot_table(
    values='grade_change_post_ai',
    index='education_level',
    columns='purpose_of_ai',
    aggfunc='mean',
    margins=True,
    margins_name='Overall Average'
)
print(comprehensive_pivot.round(2))

# Find students who improved most (top 5%)
print("\n=== Top 5% students by grade improvement ===")
top_5_percent = students.nlargest(int(len(students) * 0.05), 'grade_change_post_ai')
print(top_5_percent[['age', 'education_level', 'study_hours_per_day', 
                     'ai_tools_used', 'grade_change_post_ai']].head(10))

# ============================================
# SUMMARY STATISTICS
# ============================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(f"\nTotal students analyzed: {len(students)}")
print(f"Average grade before AI: {students['grade_before_ai'].mean():.2f}")
print(f"Average grade after AI: {students['grade_after_ai'].mean():.2f}")
print(f"Average grade improvement: {students['grade_change_post_ai'].mean():.2f}%")
print(f"Students who improved: {len(students[students['grade_change_post_ai'] > 0])}")
print(f"Students who declined: {len(students[students['grade_change_post_ai'] < 0])}")
print(f"\nEducation levels represented: {students['education_level'].nunique()}")
print(f"AI tools used: {students['ai_tools_used'].nunique()}")
print(f"Purpose categories: {students['purpose_of_ai'].nunique()}")

print("\n" + "=" * 60)
print("CHAPTER 3 CONCEPTS PRACTICED:")
print("✓ Sorting values (single and multiple columns)")
print("✓ Position-based subsetting with .iloc[]")
print("✓ Creating pivot tables")
print("✓ Subsetting pivot tables by rows and columns")
print("✓ Calculating means across different axes")
print("✓ Finding maximum and minimum values")
print("=" * 60)


