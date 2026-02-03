"""
Week 2 Day 1 - Inner Joins Practice Script
Created: February 3, 2026
Course: Joining Data with pandas - Chapter 1

This script demonstrates:
1. Basic inner joins with .merge()
2. One-to-many relationships
3. Merging on multiple columns
4. Sorting and filtering merged data
5. Aggregating after joins

Dataset: Education sector - Students, Courses, and Enrollments
"""

import pandas as pd

# ============================================================================
# CREATE SAMPLE DATASETS - Education Sector
# ============================================================================

print("=" * 70)
print("CREATING SAMPLE EDUCATION DATASETS")
print("=" * 70)

# Students dataset
students = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 
             'Diana Prince', 'Ethan Hunt', 'Fiona Green'],
    'age': [20, 22, 21, 23, 20, 22],
    'year': [2, 4, 3, 4, 2, 3]
})

# Courses dataset
courses = pd.DataFrame({
    'course_id': ['CS101', 'MATH201', 'ENG150', 'HIST100', 'BIO210'],
    'course_name': ['Intro to Computer Science', 'Calculus II', 
                    'Creative Writing', 'World History', 'Biology'],
    'credits': [4, 4, 3, 3, 4],
    'department': ['Computer Science', 'Mathematics', 'English', 
                   'History', 'Biology']
})

# Enrollments dataset (one-to-many: one student can enroll in many courses)
enrollments = pd.DataFrame({
    'student_id': [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6],
    'course_id': ['CS101', 'MATH201', 'CS101', 'ENG150', 'HIST100', 
                  'MATH201', 'BIO210', 'ENG150', 'CS101', 'MATH201', 'BIO210'],
    'semester': ['Fall', 'Fall', 'Fall', 'Fall', 'Spring', 
                 'Fall', 'Spring', 'Fall', 'Fall', 'Spring', 'Fall'],
    'grade': [85, 90, 78, 88, 92, 95, 87, 91, 76, 89, 93]
})

print("\nStudents DataFrame:")
print(students)
print("\nCourses DataFrame:")
print(courses)
print("\nEnrollments DataFrame:")
print(enrollments)

# ============================================================================
# EXAMPLE 1: Basic Inner Join - Students and Enrollments
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 1: BASIC INNER JOIN")
print("=" * 70)
print("\nMerging students with enrollments on 'student_id'")

# Merge students with their enrollments
students_enrollments = students.merge(enrollments, on='student_id')

print("\nResult of students.merge(enrollments, on='student_id'):")
print(students_enrollments)

print("\nNotice:")
print("- Each student appears multiple times (once per enrollment)")
print("- This is a ONE-TO-MANY relationship")
print(f"- Original students: {len(students)} rows")
print(f"- After merge: {len(students_enrollments)} rows")

# ============================================================================
# EXAMPLE 2: Chaining Merges - Three Tables
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 2: MERGING THREE TABLES")
print("=" * 70)
print("\nMerging students → enrollments → courses")

# First merge: students + enrollments
# Then merge: result + courses
full_data = students.merge(enrollments, on='student_id') \
                    .merge(courses, on='course_id')

print("\nComplete enrollment data with all details:")
print(full_data[['name', 'course_name', 'semester', 'grade', 'credits']])

print(f"\nTotal rows in merged dataset: {len(full_data)}")

# ============================================================================
# EXAMPLE 3: Merging on Multiple Columns
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 3: MERGING ON MULTIPLE COLUMNS")
print("=" * 70)

# Create a semester schedule dataset
semester_schedule = pd.DataFrame({
    'course_id': ['CS101', 'CS101', 'MATH201', 'ENG150', 'BIO210'],
    'semester': ['Fall', 'Spring', 'Fall', 'Fall', 'Spring'],
    'instructor': ['Dr. Smith', 'Dr. Jones', 'Prof. Wilson', 
                   'Dr. Martinez', 'Prof. Lee'],
    'room': ['Tech-101', 'Tech-102', 'Math-205', 'Eng-150', 'Bio-210']
})

print("\nSemester Schedule:")
print(semester_schedule)

# Merge enrollments with schedule on BOTH course_id AND semester
enrollments_with_schedule = enrollments.merge(
    semester_schedule, 
    on=['course_id', 'semester']
)

print("\nEnrollments with instructor and room info:")
print(enrollments_with_schedule)

print("\nNotice:")
print("- Rows only match when BOTH course_id AND semester match")
print("- CS101 has different instructors in Fall vs Spring")

# ============================================================================
# EXAMPLE 4: Filtering After Merge
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 4: FILTERING MERGED DATA")
print("=" * 70)

# Find all Computer Science enrollments in Fall semester
filter_criteria = ((full_data['department'] == 'Computer Science') & 
                   (full_data['semester'] == 'Fall'))

cs_fall_enrollments = full_data.loc[filter_criteria, 
                                     ['name', 'course_name', 'grade']]

print("\nComputer Science enrollments in Fall semester:")
print(cs_fall_enrollments)

# ============================================================================
# EXAMPLE 5: Aggregating After Merge
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 5: AGGREGATING AFTER MERGE")
print("=" * 70)

# Calculate total credits per student
student_credits = full_data.groupby('name', as_index=False) \
                           .agg({'credits': 'sum'})

print("\nTotal credits enrolled per student:")
print(student_credits)

# Calculate average grade per course
course_averages = full_data.groupby('course_name', as_index=False) \
                           .agg({'grade': 'mean'})

# Sort by average grade descending
course_averages = course_averages.sort_values('grade', ascending=False)

print("\nAverage grade by course (sorted):")
print(course_averages)

# ============================================================================
# EXAMPLE 6: Complex Analysis - Department Performance
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 6: DEPARTMENT PERFORMANCE ANALYSIS")
print("=" * 70)

# Calculate average grade and total enrollments per department
dept_analysis = full_data.groupby('department', as_index=False) \
                         .agg({
                             'grade': 'mean',
                             'student_id': 'count'
                         })

# Rename columns for clarity
dept_analysis.columns = ['department', 'avg_grade', 'total_enrollments']

# Sort by average grade
dept_analysis = dept_analysis.sort_values('avg_grade', ascending=False)

print("\nDepartment Performance:")
print(dept_analysis)

# ============================================================================
# EXAMPLE 7: Finding Top Students
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 7: TOP PERFORMING STUDENTS")
print("=" * 70)

# Calculate average grade per student across all courses
student_performance = full_data.groupby(['student_id', 'name'], 
                                        as_index=False) \
                               .agg({'grade': 'mean'})

# Sort by average grade descending
student_performance = student_performance.sort_values('grade', 
                                                       ascending=False)

print("\nStudents ranked by average grade:")
print(student_performance)

# Find students with average above 85
high_performers = student_performance[student_performance['grade'] > 85]

print(f"\nHigh performers (avg > 85): {len(high_performers)} students")
print(high_performers)

# ============================================================================
# EXAMPLE 8: Semester Comparison
# ============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 8: FALL vs SPRING ENROLLMENT COMPARISON")
print("=" * 70)

# Count enrollments by semester
semester_counts = full_data.groupby('semester', as_index=False) \
                           .agg({'student_id': 'count'})

semester_counts.columns = ['semester', 'enrollment_count']

print("\nEnrollment counts by semester:")
print(semester_counts)

# Average grade by semester
semester_grades = full_data.groupby('semester', as_index=False) \
                           .agg({'grade': 'mean'})

print("\nAverage grade by semester:")
print(semester_grades)

# ============================================================================
# KEY CONCEPTS DEMONSTRATED
# ============================================================================

print("\n" + "=" * 70)
print("KEY CONCEPTS FROM CHAPTER 1")
print("=" * 70)

print("""
1. BASIC INNER JOIN:
   df1.merge(df2, on='column_name')
   - Only keeps rows where key exists in BOTH tables

2. ONE-TO-MANY RELATIONSHIPS:
   - One student can have many enrollments
   - Result has MORE rows than the "one" table

3. MERGING MULTIPLE TABLES:
   df1.merge(df2, on='key1').merge(df3, on='key2')
   - Chain merges with backslash for readability

4. MERGING ON MULTIPLE COLUMNS:
   df1.merge(df2, on=['col1', 'col2'])
   - Rows match only when ALL specified columns match

5. FILTERING MERGED DATA:
   filter = (condition1) & (condition2)
   merged_df.loc[filter, columns]

6. AGGREGATING AFTER MERGE:
   merged_df.groupby('column').agg({'col': 'function'})
   - Combine join + groupby for powerful analysis

7. SORTING MERGED RESULTS:
   merged_df.sort_values('column', ascending=False)
""")

print("\n" + "=" * 70)
print("SCRIPT COMPLETE - Review the output above!")
print("=" * 70)

# ============================================================================
# INVESTIGATION NOTES
# ============================================================================

"""
INVESTIGATE FURTHER / REVISE:

1. What happens if a student_id exists in students but NOT in enrollments?
   → Test this by adding a student with no enrollments

2. What if we wanted to keep ALL students even if they have no enrollments?
   → This requires a LEFT JOIN (Chapter 2!)

3. Can we merge on columns with different names?
   → Yes! Use left_on and right_on parameters (covered in Chapter 2)

4. What's the difference between .merge() and .join()?
   → Both do similar things, .merge() is more flexible

5. When should we use as_index=False in groupby?
   → When we want the grouped column to be a regular column, not the index
"""