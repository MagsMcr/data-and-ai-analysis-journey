import pandas as pd

# Load dataset
student_ai_usage = pd.read_csv('/Users/magdalenapirowska/learning/career/data-and-ai-analysis-journey/datasets/students_ai_usage.csv')

# Inspect dataset
print("First 5 rows:")
print(student_ai_usage.head())
print("\nDataset info:")
print(student_ai_usage.info())
print("\nDataset shape (rows, columns):")
print(student_ai_usage.shape)

# Sort by study hours (descending)
students_sorted = student_ai_usage.sort_values('study_hours_per_day', ascending=False)
print("\nTop students by study hours:")
print(students_sorted.head())

# Sort by multiple columns
hours_vs_grade = student_ai_usage.sort_values(['study_hours_per_day', 'grades_before_ai'], ascending=[False, False])
print("\nSorted by study hours and grades:")
print(hours_vs_grade.head())

# Subset single column
education = student_ai_usage["education_level"]
print("\nEducation level column:")
print(education.head())

# Check unique values
print("\nUnique ages:")
print(student_ai_usage['age'].unique())
print("\nUnique AI tools:")
print(student_ai_usage['ai_tools_used'].unique())

# Filter for teenagers (age <= 16)
teenager = student_ai_usage[student_ai_usage['age'] <= 16] 
print("\nTeenagers (age <= 16):")
print(teenager.head())

# Filter with AND condition - teenagers who study more than 3 hours
studious_teenagers = student_ai_usage[(student_ai_usage['age'] <= 16) & (student_ai_usage['study_hours_per_day'] > 3)]
print("\nStudious teenagers (age <= 16 AND study > 3 hours):")
print(studious_teenagers.head())

# Filter with OR condition - either high grades or high study hours
high_performers = student_ai_usage[(student_ai_usage['grades_after_ai'] >= 75) | (student_ai_usage['study_hours_per_day'] >= 4)]
print("\nHigh performers (grades >= 75 OR study >= 4 hours):")
print(high_performers.head())

# Filter with isin - specific AI tools
ai_tools_list = ['ChatGPT', 'Gemini']
selected_tools = student_ai_usage[student_ai_usage['ai_tools_used'].isin(ai_tools_list)]
print("\nStudents using ChatGPT or Gemini:")
print(selected_tools.head())

# Add new columns
student_ai_usage['grade_change_post_ai'] = (student_ai_usage['grades_after_ai'] - student_ai_usage['grades_before_ai']) / student_ai_usage['grades_before_ai']
student_ai_usage['study_efficiency'] = student_ai_usage['grades_after_ai'] / student_ai_usage['study_hours_per_day']

# Final view with new columns
print("\nDataset with new columns:")
print(student_ai_usage.head())
print("\nFinal statistics:")
print(student_ai_usage.describe())

