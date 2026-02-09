import pandas as pd

studentAssessment = pd.read_csv('datasets/open_uni_data/studentAssessment.csv')
studentVle = pd.read_csv('datasets/open_uni_data/studentVle.csv')
assessments = pd.read_csv('datasets/open_uni_data/assessments.csv')

files = {
    'studentAssessment': studentAssessment,
    'studentVle': studentVle,
    'assessments': assessments
}

for name, df in files.items():
    print(f"\n=== {name} ===")
    print(df.head())
    print(df.info())
    print(df.shape)

student_performance = studentAssessment.merge(assessments,on='id_assessment',how='inner')

# After merging studentAssessment with assessments
student_performance_filtered = student_performance[(student_performance['code_module'] == 'AAA') & 
                                                 (student_performance['code_presentation'] == '2013J')]

assessments_filtered = assessments[(assessments['code_module'] == 'AAA') & 
                                   (assessments['code_presentation'] == '2013J')]

student_vle_filtered = studentVle[(studentVle['code_module'] == 'AAA') & 
                                  (studentVle['code_presentation'] == '2013J')]

student_assessment_date = student_performance_filtered.groupby('date_submitted').size()
student_assessment_date = student_assessment_date.reset_index()
student_assessment_date = student_assessment_date.rename(columns={
    'date_submitted': 'date',
    0: 'submission_count'
})

assessments_dates = assessments_filtered[['id_assessment','date']]
print(student_assessment_date.head())
print(assessments_dates.head())

submissions = pd.merge_ordered(student_assessment_date,assessments_dates,left_on='date',right_on='date',how='outer',fill_method='ffill')
submissions.sort_values(by='date',inplace=True)
print(submissions.head(20))