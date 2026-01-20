import pandas as pd
import requests
import zipfile
import io

# Download the zip file
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
response = requests.get(url)

# Extract the zip file in memory
zip_file = zipfile.ZipFile(io.BytesIO(response.content))

# Load the Math students data
students = pd.read_csv(zip_file.open('student-mat.csv'), sep=';')

# Check what we've got
print(students.head())
print("\nDataset shape:", students.shape)
print("\nColumn names:", students.columns.tolist())