import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# WEEK 1 WRAP-UP PROJECT: Education Publishing Analysis
# Comprehensive demonstration of pandas Chapters 1-4 concepts
# Dataset: Book sales across multiple schools
# =============================================================================

# -----------------------------------------------------------------------------
# SECTION 1: DATA CREATION (Chapter 4 - Creating DataFrames)
# -----------------------------------------------------------------------------

# Create school information dataset
schools_data = {
    'school_id': ['SCH001', 'SCH002', 'SCH003', 'SCH004', 'SCH005', 'SCH006', 'SCH007', 'SCH008'],
    'school_name': ['Riverside Primary', 'Hillside Academy', 'Greenfield School', 'Oakwood Primary',
                    'Meadow View', 'Sunset Academy', 'Park Lane School', 'Valley Primary'],
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'student_count': [450, 380, 520, 310, 425, 395, 480, 340],
    'library_budget': [15000, 12000, 18000, 9500, 14500, 11800, 16500, 10200]
}

schools = pd.DataFrame(schools_data)

# Create book orders dataset
orders_data = {
    'order_id': range(1, 25),
    'school_id': ['SCH001', 'SCH002', 'SCH003', 'SCH004', 'SCH005', 'SCH006', 'SCH007', 'SCH008',
                  'SCH001', 'SCH002', 'SCH003', 'SCH004', 'SCH005', 'SCH006', 'SCH007', 'SCH008',
                  'SCH001', 'SCH003', 'SCH005', 'SCH002', 'SCH004', 'SCH006', 'SCH007', 'SCH008'],
    'genre': ['Fiction', 'Fiction', 'Non-Fiction', 'Fiction', 'Science', 'Non-Fiction', 'Fiction', 'Science',
              'Science', 'Non-Fiction', 'Fiction', 'Science', 'Fiction', 'Fiction', 'Non-Fiction', 'Fiction',
              'Non-Fiction', 'Science', 'Non-Fiction', 'Science', 'Non-Fiction', 'Science', 'Science', 'Non-Fiction'],
    'quantity': [45, 32, 28, 38, 25, 30, 42, 20, 35, 27, 40, 22, 33, 29, 31, 36, 26, 24, 38, 30, 28, 25, 34, 27],
    'price_per_book': [12.99, 14.50, 18.75, 11.99, 22.50, 16.25, 13.50, 21.00, 20.99, 17.50, 12.50, 23.75, 
                       13.99, 15.25, 19.50, 12.75, 17.99, 24.50, 18.25, 22.99, 16.75, 23.25, 21.50, 19.75],
    'quarter': ['Q1', 'Q1', 'Q1', 'Q1', 'Q1', 'Q1', 'Q1', 'Q1',
                'Q2', 'Q2', 'Q2', 'Q2', 'Q2', 'Q2', 'Q2', 'Q2',
                'Q3', 'Q3', 'Q3', 'Q3', 'Q3', 'Q3', 'Q3', 'Q3']
}

orders = pd.DataFrame(orders_data)

print("\n" + "="*80)
print("DATASETS CREATED")
print("="*80)
print(f"\nSchools dataset: {schools.shape[0]} schools, {schools.shape[1]} columns")
print(f"Orders dataset: {orders.shape[0]} orders, {orders.shape[1]} columns")

# -----------------------------------------------------------------------------
# SECTION 2: DATA INSPECTION (Chapter 1 - Inspecting DataFrames)
# -----------------------------------------------------------------------------

print("\n" + "="*80)
print("SECTION 1: DATA INSPECTION")
print("="*80)

print("\n--- Schools Dataset Overview ---")
print(schools.head())
print("\nSchools Info:")
print(schools.info())
print("\nSchools Statistical Summary:")
print(schools.describe())

print("\n--- Orders Dataset Overview ---")
print(orders.head(10))
print("\nOrders Info:")
print(orders.info())

# -----------------------------------------------------------------------------
# SECTION 3: SORTING & SUBSETTING (Chapter 1)
# -----------------------------------------------------------------------------

print("\n" + "="*80)
print("SECTION 2: SORTING & SUBSETTING")
print("="*80)

# Sort schools by student count
print("\n--- Schools Sorted by Student Count (Descending) ---")
schools_sorted = schools.sort_values('student_count', ascending=False)
print(schools_sorted[['school_name', 'student_count', 'library_budget']])

# Sort orders by multiple columns
print("\n--- Orders Sorted by Quarter and Quantity ---")
orders_sorted = orders.sort_values(['quarter', 'quantity'], ascending=[True, False])
print(orders_sorted[['order_id', 'school_id', 'quarter', 'quantity']].head(10))

# Subset specific columns
print("\n--- School Names and Regions Only ---")
schools_subset = schools[['school_name', 'region']]
print(schools_subset)

# Boolean filtering - schools with over 400 students
print("\n--- Large Schools (>400 students) ---")
large_schools = schools[schools['student_count'] > 400]
print(large_schools[['school_name', 'student_count']])

# Multiple conditions - Northern schools with budget over £14000
print("\n--- Northern Schools with High Budgets ---")
north_high_budget = schools[(schools['region'] == 'North') & (schools['library_budget'] > 14000)]
print(north_high_budget[['school_name', 'library_budget']])

# Using .isin() for categorical filtering
print("\n--- Fiction and Science Orders Only ---")
fiction_science = orders[orders['genre'].isin(['Fiction', 'Science'])]
print(f"Total Fiction/Science orders: {len(fiction_science)}")

# -----------------------------------------------------------------------------
# SECTION 4: CALCULATED COLUMNS (Chapter 1)
# -----------------------------------------------------------------------------

print("\n" + "="*80)
print("SECTION 3: CALCULATED COLUMNS")
print("="*80)

# Add total order value column
orders['total_value'] = (orders['quantity'] * orders['price_per_book']).round(2)
print("\n--- Orders with Total Value Calculated ---")
print(orders[['order_id', 'quantity', 'price_per_book', 'total_value']].head(10))

# Add budget per student column
schools['budget_per_student'] = (schools['library_budget'] / schools['student_count']).round(2)
print("\n--- Schools with Budget Per Student ---")
print(schools[['school_name', 'student_count', 'library_budget', 'budget_per_student']])

# -----------------------------------------------------------------------------
# SECTION 5: AGGREGATION & GROUPING (Chapter 2)
# -----------------------------------------------------------------------------

print("\n" + "="*80)
print("SECTION 4: AGGREGATION & GROUPING")
print("="*80)

# Summary statistics on orders
print("\n--- Order Summary Statistics ---")
order_stats = orders[['quantity', 'price_per_book', 'total_value']].agg(['mean', 'median', 'min', 'max', 'std'])
print(order_stats.round(2))

# Group by genre
print("\n--- Sales by Genre ---")
genre_sales = orders.groupby('genre')['total_value'].agg(['sum', 'mean', 'count'])
genre_sales.columns = ['total_sales', 'avg_order_value', 'num_orders']
print(genre_sales.round(2))

# Group by quarter
print("\n--- Sales by Quarter ---")
quarter_sales = orders.groupby('quarter')['total_value'].sum().round(2)
print(quarter_sales)

# Multiple grouping variables
print("\n--- Sales by Quarter and Genre ---")
quarter_genre_sales = orders.groupby(['quarter', 'genre'])['total_value'].agg(['sum', 'count'])
print(quarter_genre_sales.round(2))

# Group by region (requires merging first)
orders_with_region = orders.merge(schools[['school_id', 'region']], on='school_id')
print("\n--- Sales by Region ---")
region_sales = orders_with_region.groupby('region')['total_value'].sum().sort_values(ascending=False).round(2)
print(region_sales)

# -----------------------------------------------------------------------------
# SECTION 6: PIVOT TABLES (Chapter 2)
# -----------------------------------------------------------------------------

print("\n" + "="*80)
print("SECTION 5: PIVOT TABLES")
print("="*80)

# Pivot: Quarter by Genre
print("\n--- Pivot Table: Total Sales by Quarter and Genre ---")
pivot_quarter_genre = orders.pivot_table(
    values='total_value',
    index='quarter',
    columns='genre',
    aggfunc='sum',
    fill_value=0
)
print(pivot_quarter_genre.round(2))

# Pivot: Region by Genre (using merged data)
print("\n--- Pivot Table: Total Sales by Region and Genre ---")
pivot_region_genre = orders_with_region.pivot_table(
    values='total_value',
    index='region',
    columns='genre',
    aggfunc='sum',
    fill_value=0,
    margins=True  # Add totals
)
print(pivot_region_genre.round(2))

# Calculate mean across axis
print("\n--- Mean Sales by Genre (Across All Quarters) ---")
genre_means = pivot_quarter_genre.mean(axis=0).round(2)
print(genre_means)

# -----------------------------------------------------------------------------
# SECTION 7: ADVANCED INDEXING (Chapter 3)
# -----------------------------------------------------------------------------

print("\n" + "="*80)
print("SECTION 6: ADVANCED INDEXING")
print("="*80)

# Set index and sort
schools_indexed = schools.set_index('school_id').sort_index()
print("\n--- Schools with school_id as Index ---")
print(schools_indexed.head())

# Slicing with .loc
print("\n--- Slice Schools SCH002 to SCH005 ---")
sliced_schools = schools_indexed.loc['SCH002':'SCH005', ['school_name', 'region', 'student_count']]
print(sliced_schools)

# Position-based indexing with .iloc
print("\n--- First 3 Schools, Columns 1-3 (Position-Based) ---")
position_subset = schools_indexed.iloc[:3, 1:4]
print(position_subset)

# -----------------------------------------------------------------------------
# SECTION 8: VISUALIZATION (Chapter 4)
# -----------------------------------------------------------------------------

print("\n" + "="*80)
print("SECTION 7: DATA VISUALIZATION")
print("="*80)

# Plot 1: Bar chart - Sales by Genre
print("\nGenerating Plot 1: Sales by Genre...")
genre_sales['total_sales'].plot(
    kind='bar',
    title='Total Sales by Genre',
    xlabel='Genre',
    ylabel='Total Sales (£)',
    color='steelblue',
    rot=45
)
plt.tight_layout()
plt.savefig('week1_plot1_genre_sales.png')
plt.show()

# Plot 2: Bar chart - Sales by Quarter
print("\nGenerating Plot 2: Sales by Quarter...")
quarter_sales.plot(
    kind='bar',
    title='Total Sales by Quarter',
    xlabel='Quarter',
    ylabel='Total Sales (£)',
    color='darkgreen',
    rot=0
)
plt.tight_layout()
plt.savefig('week1_plot2_quarter_sales.png')
plt.show()

# Plot 3: Histogram - Order Quantities
print("\nGenerating Plot 3: Distribution of Order Quantities...")
orders['quantity'].plot(
    kind='hist',
    bins=10,
    title='Distribution of Order Quantities',
    xlabel='Quantity',
    ylabel='Frequency',
    color='coral',
    alpha=0.7,
    edgecolor='black'
)
plt.tight_layout()
plt.savefig('week1_plot3_quantity_distribution.png')
plt.show()

# Plot 4: Line plot - Quarterly trend
print("\nGenerating Plot 4: Quarterly Sales Trend...")
quarter_sales.plot(
    kind='line',
    title='Sales Trend by Quarter',
    xlabel='Quarter',
    ylabel='Total Sales (£)',
    marker='o',
    color='purple',
    linewidth=2,
    markersize=8
)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('week1_plot4_quarterly_trend.png')
plt.show()

# -----------------------------------------------------------------------------
# SECTION 9: SAVE RESULTS (Chapter 4)
# -----------------------------------------------------------------------------

print("\n" + "="*80)
print("SECTION 8: SAVING RESULTS")
print("="*80)

# Save enriched datasets
schools.to_csv('week1_schools_analysis.csv', index=False)
orders.to_csv('week1_orders_analysis.csv', index=False)

# Save summary statistics
summary_report = pd.DataFrame({
    'Metric': ['Total Orders', 'Total Schools', 'Total Revenue', 'Average Order Value', 'Genres Offered'],
    'Value': [
        len(orders),
        len(schools),
        f"£{orders['total_value'].sum():.2f}",
        f"£{orders['total_value'].mean():.2f}",
        orders['genre'].nunique()
    ]
})
summary_report.to_csv('week1_summary_report.csv', index=False)

print("\nFiles saved:")
print("  - week1_schools_analysis.csv")
print("  - week1_orders_analysis.csv")
print("  - week1_summary_report.csv")
print("  - week1_plot1_genre_sales.png")
print("  - week1_plot2_quarter_sales.png")
print("  - week1_plot3_quantity_distribution.png")
print("  - week1_plot4_quarterly_trend.png")

# -----------------------------------------------------------------------------
# SECTION 10: KEY FINDINGS SUMMARY
# -----------------------------------------------------------------------------

print("\n" + "="*80)
print("KEY FINDINGS SUMMARY")
print("="*80)

print("\n1. GENRE ANALYSIS:")
print(f"   - Most popular genre: {genre_sales['total_sales'].idxmax()}")
print(f"   - Highest revenue genre: £{genre_sales['total_sales'].max():.2f}")
print(f"   - Average order value by genre:")
for genre in genre_sales.index:
    print(f"     • {genre}: £{genre_sales.loc[genre, 'avg_order_value']:.2f}")

print("\n2. QUARTERLY TRENDS:")
print(f"   - Best performing quarter: {quarter_sales.idxmax()}")
print(f"   - Quarter with highest sales: £{quarter_sales.max():.2f}")
print(f"   - Quarter with lowest sales: £{quarter_sales.min():.2f}")

print("\n3. REGIONAL INSIGHTS:")
print(f"   - Highest spending region: {region_sales.idxmax()}")
print(f"   - Regional sales:")
for region in region_sales.index:
    print(f"     • {region}: £{region_sales[region]:.2f}")

print("\n4. SCHOOL ANALYSIS:")
print(f"   - Largest school: {schools_sorted.iloc[0]['school_name']} ({schools_sorted.iloc[0]['student_count']} students)")
print(f"   - Highest budget per student: £{schools['budget_per_student'].max():.2f}")
print(f"   - Average library budget: £{schools['library_budget'].mean():.2f}")

print("\n" + "="*80)
print("WEEK 1 WRAP-UP PROJECT COMPLETE!")
print("="*80)
print("\nThis project demonstrated:")
print("  ✓ Chapter 1: Inspection, sorting, subsetting, filtering")
print("  ✓ Chapter 2: Aggregation, groupby, pivot tables")
print("  ✓ Chapter 3: Advanced indexing (.loc, .iloc)")
print("  ✓ Chapter 4: DataFrame creation, visualization, CSV export")
print("\nAll Week 1 pandas concepts successfully applied! 🎉")
print("="*80 + "\n")