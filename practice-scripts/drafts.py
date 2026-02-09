import pandas as pd
import seaborn as sns

# Load the tips dataset (built-in to seaborn)
tips = sns.load_dataset('tips')

print("=== DATASET OVERVIEW ===")
print(tips.head())
print("\n", tips.info())

# ============================================
# CHAPTER 3 CONCEPT 1: Setting and Sorting Index
# ============================================

print("\n=== SORTING BY INDEX ===")
# Set 'day' as index and sort
tips_by_day = tips.set_index('day').sort_index()
print(tips_by_day.head(10))

# ============================================
# CHAPTER 3 CONCEPT 2: Slicing with .loc[]
# ============================================

print("\n=== SLICING ROWS ===")
# Get all tips from Thursday to Saturday (requires sorted index)
tips_thur_to_sat = tips_by_day.loc['Thur':'Sat']
print(tips_thur_to_sat.head())
print(f"Number of meals Thursday-Saturday: {len(tips_thur_to_sat)}")

# ============================================
# CHAPTER 3 CONCEPT 3: Subsetting with .iloc[]
# ============================================

print("\n=== POSITION-BASED SUBSETTING ===")
# Get first 5 rows, columns 2-4
subset_positions = tips.iloc[:5, 1:4]
print(subset_positions)

# ============================================
# CHAPTER 3 CONCEPT 4: Pivot Tables
# ============================================

print("\n=== PIVOT TABLE: Average Tip by Day and Time ===")
# Create pivot table: rows=day, columns=time, values=tip amount
tips_pivot = tips.pivot_table(
    values='tip',
    index='day',
    columns='time',
    aggfunc='mean'
)
print(tips_pivot)

print("\n=== SUBSETTING PIVOT TABLE ===")
# Get tips for Friday and Saturday only
print("Friday & Saturday tips:")
print(tips_pivot.loc[['Fri', 'Sat']])

# Get dinner tips only (subset by column)
print("\nDinner tips across all days:")
print(tips_pivot['Dinner'])

# ============================================
# CHAPTER 3 CONCEPT 5: Calculating Means Across Axes
# ============================================

print("\n=== MEAN CALCULATIONS ===")
# Mean tip by day (average down each column)
mean_tip_by_day = tips_pivot.mean()
print("Mean tip by time of day (across all days):")
print(mean_tip_by_day)

# Mean tip by time (average across each row)
mean_tip_by_time = tips_pivot.mean(axis='columns')
print("\nMean tip by day (across lunch and dinner):")
print(mean_tip_by_time)

# Find which day had highest average tip
highest_tip_day = mean_tip_by_time[mean_tip_by_time == mean_tip_by_time.max()]
print(f"\nDay with highest average tip: {highest_tip_day}")

# ============================================
# SUMMARY STATISTICS
# ============================================

print("\n=== SUMMARY ===")
print(f"Total meals in dataset: {len(tips)}")
print(f"Average tip amount: ${tips['tip'].mean():.2f}")
print(f"Date range: Thursday to Sunday")
print(f"Meal times: Lunch and Dinner")

print("hello world".split('o'))     # ['hell', ' w', 'rld']