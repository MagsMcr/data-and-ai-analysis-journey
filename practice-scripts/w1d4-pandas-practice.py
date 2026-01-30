import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# CHAPTER 4 PRACTICE: CREATING AND MANIPULATING DATAFRAMES
# Dataset: Monthly Book Sales by Publisher
# Concepts: DataFrame creation, calculated columns, groupby, plotting
# =============================================================================

# -----------------------------------------------------------------------------
# SECTION 1: DATAFRAME CREATION
# -----------------------------------------------------------------------------

# Create dictionary of lists containing book sales data
book_sales = {
    'publisher': ['Penguin', 'HarperCollins', 'Bloomsbury', 'Scholastic', 
                  'Penguin', 'HarperCollins', 'Bloomsbury', 'Scholastic', 
                  'Penguin', 'HarperCollins', 'Bloomsbury', 'Scholastic'],
    'genre': ['Fantasy', 'Mystery', 'Children\'s', 'Non-Fiction', 
              'Romance', 'Fantasy', 'Mystery', 'Children\'s', 
              'Non-Fiction', 'Romance', 'Fantasy', 'Mystery'],
    'format': ['Hardcover', 'Paperback', 'eBook', 'Hardcover', 
               'Paperback', 'eBook', 'Hardcover', 'Paperback', 
               'Hardcover', 'eBook', 'Paperback', 'Hardcover'],
    'month': ['January', 'January', 'February', 'March', 
              'February', 'March', 'January', 'February', 
              'March', 'January', 'March', 'February'],
    'units_sold': [2400, 1850, 3200, 1200, 2950, 4100, 980, 3750, 
                   1450, 2180, 2670, 820],
    'price': [18.99, 9.99, 6.99, 22.50, 8.99, 12.99, 19.99, 7.50, 
              24.99, 9.50, 11.99, 21.50]
}

# Convert dictionary to DataFrame
book_sales = pd.DataFrame(book_sales)

# Display full dataset (12 rows)
print("\n" + "="*80)
print("FULL DATASET: Book Sales Data")
print("="*80)
print(book_sales)

# -----------------------------------------------------------------------------
# SECTION 2: DATA MANIPULATION - CREATING CALCULATED COLUMNS
# -----------------------------------------------------------------------------

# Calculate total sales revenue (units × price)
book_sales['total_sales'] = book_sales['units_sold'] * book_sales['price']

# Calculate each row's percentage of its publisher's total sales
# Uses .transform() to broadcast grouped sum back to all rows
book_sales['annual_sales_percentage'] = (
    book_sales['total_sales'] / 
    book_sales.groupby('publisher')['total_sales'].transform('sum')
).round(2)

print("\n" + "="*80)
print("DATASET WITH CALCULATED COLUMNS")
print("="*80)
print(book_sales)

# -----------------------------------------------------------------------------
# SECTION 3: SUMMARY STATISTICS
# -----------------------------------------------------------------------------

# Units sold statistics by publisher
print("\n" + "="*80)
print("UNITS SOLD STATISTICS BY PUBLISHER")
print("="*80)
sales_by_publisher = book_sales.groupby('publisher')['units_sold'].agg(
    ['max', 'min', 'mean', 'median']
)
print(sales_by_publisher)

# Total sales and units by publisher and genre
print("\n" + "="*80)
print("SALES BREAKDOWN BY PUBLISHER AND GENRE")
print("="*80)
sales_by_genre_and_publisher = book_sales.groupby(
    ['publisher', 'genre']
)[['units_sold', 'price', 'total_sales', 'annual_sales_percentage']].sum()
print(sales_by_genre_and_publisher)

# Average price by format type
print("\n" + "="*80)
print("AVERAGE PRICE BY FORMAT")
print("="*80)
avg_price_by_format = book_sales.groupby('format')['price'].mean().round(2)
print(avg_price_by_format)

# Total revenue by month
print("\n" + "="*80)
print("TOTAL REVENUE BY MONTH")
print("="*80)
revenue_by_month = book_sales.groupby('month')['total_sales'].sum().round(2)
print(revenue_by_month)

# -----------------------------------------------------------------------------
# SECTION 4: DATA VISUALIZATION
# -----------------------------------------------------------------------------

# Plot 1: Stacked horizontal bar - Total sales by publisher and genre
print("\nGenerating Plot 1: Total Sales by Publisher and Genre (Stacked)...")
sales_by_genre_and_publisher['total_sales'].unstack().plot(
    kind='barh', 
    title='Total Sales by Publisher and Genre', 
    xlabel='Total Sales (£)',
    ylabel='Publisher',
    stacked=True,
    figsize=(10, 6)
)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Plot 2: Side-by-side bar - Compare genre performance across publishers
print("\nGenerating Plot 2: Genre Performance Comparison by Publisher...")
sales_by_genre_and_publisher['total_sales'].unstack().plot(
    kind='bar', 
    title='Genre Performance by Publisher', 
    xlabel='Publisher',
    ylabel='Total Sales (£)',
    stacked=False,
    figsize=(10, 6),
    rot=0
)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Plot 3: Histogram - Distribution of unit prices
print("\nGenerating Plot 3: Distribution of Book Prices...")
book_sales['price'].plot(
    kind='hist',
    bins=8,
    title='Distribution of Book Prices',
    xlabel='Price (£)',
    ylabel='Frequency',
    alpha=0.7,
    color='steelblue',
    edgecolor='black',
    figsize=(8, 5)
)
plt.show()

# Plot 4: Line plot - Total sales by month
print("\nGenerating Plot 4: Monthly Sales Trend...")
revenue_by_month_ordered = book_sales.groupby('month')['total_sales'].sum().reindex(
    ['January', 'February', 'March']
)
revenue_by_month_ordered.plot(
    kind='line',
    title='Monthly Sales Trend',
    xlabel='Month',
    ylabel='Total Sales (£)',
    marker='o',
    color='darkgreen',
    linewidth=2,
    figsize=(8, 5)
)
plt.grid(True, alpha=0.3)
plt.show()

# -----------------------------------------------------------------------------
# SECTION 5: SAVE TO CSV
# -----------------------------------------------------------------------------

# Save the complete dataset with calculated columns
book_sales.to_csv('book_sales_analysis.csv', index=False)
print("\n" + "="*80)
print("Dataset saved to: book_sales_analysis.csv")
print("="*80)

# Save summary statistics
sales_by_genre_and_publisher.to_csv('sales_by_publisher_genre.csv')
print("Summary statistics saved to: sales_by_publisher_genre.csv")
print("="*80 + "\n")