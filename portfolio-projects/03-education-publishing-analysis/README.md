# Education Publishing Analysis

**Book Sales & Budget Utilization Across Schools**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![pandas](https://img.shields.io/badge/pandas-2.0+-green)
![Type](https://img.shields.io/badge/Type-Simulated_Data-yellow)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 📊 Project Overview

### The Challenge
How can educational publishers understand sales patterns across different school types, regions, and time periods? This project demonstrates end-to-end pandas skills by creating and analyzing a simulated book sales dataset.

### Purpose
**This is a demonstration project** designed to showcase pandas fundamentals (Chapters 1-4) within an education sector context relevant to target career roles in educational publishing and EdTech.

**Key distinction:** Unlike the other portfolio projects using real datasets, this project demonstrates **data creation** skills - building realistic synthetic data from scratch, then analyzing it using the full range of pandas techniques.

---

## 🎯 Business Value

**For Educational Publishers:**
- Revenue analysis by region and genre
- School budget utilization patterns
- Quarterly sales trend identification
- Genre performance across different school types

**For Data Analysts:**
- Demonstrates ability to create realistic test data for prototyping
- Shows comprehensive pandas skill coverage in single project
- Illustrates business metric design and KPI creation
- Professional code structure and documentation

---

## 📁 Project Files

**Analysis script:** [`w1d5-publishing-metrics.py`](w1d5-publishing-metrics.py)

**Dataset:** Simulated (created within script)
- 8 schools across 4 regions
- 24 book orders across 3 quarters
- Multiple genres (Fiction, Non-Fiction, Science)
- Budget and student count data

---

## 🛠️ Technical Approach

### Data Creation Strategy

**Two primary DataFrames constructed from dictionaries:**

```python
# Schools master data
schools_data = {
    'school_id': ['SCH001', 'SCH002', ...],
    'school_name': ['Riverside Primary', ...],
    'region': ['North', 'South', ...],
    'student_count': [450, 380, ...],
    'library_budget': [15000, 12000, ...]
}
schools = pd.DataFrame(schools_data)

# Book orders transactional data
orders_data = {
    'order_id': range(1, 25),
    'school_id': ['SCH001', ...],
    'genre': ['Fiction', 'Non-Fiction', ...],
    'quantity': [45, 32, ...],
    'price_per_book': [12.99, 14.50, ...],
    'quarter': ['Q1', 'Q2', ...]
}
orders = pd.DataFrame(orders_data)
```

**Why this approach:**
- Demonstrates DataFrame construction from scratch
- Realistic data relationships (schools → orders)
- Enables full pandas workflow without external data dependency
- Shows understanding of data structure design

### Skills Demonstrated

**pandas Chapters 1-4 comprehensive coverage:**

**Chapter 1: Inspection, Sorting, Subsetting**
- `.head()`, `.info()`, `.shape` for data exploration
- `.sort_values()` for ordering
- Boolean filtering and subsetting
- Column selection and filtering

**Chapter 2: Aggregation and Grouping**
- `.groupby()` for segmentation
- `.agg()` with multiple functions
- Summary statistics calculation
- Pivot table creation

**Chapter 3: Indexes and Slicing**
- `.set_index()` for index management
- `.loc[]` for label-based selection
- `.reset_index()` for index manipulation

**Chapter 4: DataFrame Creation**
- Dictionary to DataFrame conversion
- Calculated columns creation
- Data type handling

---

## 📈 Analysis Components

### 1. Revenue Analysis

**Total revenue calculation:**
```python
orders['total_revenue'] = orders['quantity'] * orders['price_per_book']
```

**Revenue by region:**
- Merged schools + orders on school_id
- Grouped by region
- Calculated regional revenue totals

**Revenue by genre:**
- Grouped orders by genre
- Analyzed performance across Fiction, Non-Fiction, Science

### 2. Budget Utilization

**Spending analysis:**
- Calculated total spending per school
- Compared against library budgets
- Identified under/over-budget schools

**Budget efficiency metrics:**
- Revenue per student
- Books per student
- Budget utilization percentage

### 3. Quarterly Trends

**Time-based analysis:**
- Revenue trends across Q1, Q2, Q3
- Genre shifts over time
- Seasonal purchasing patterns

### 4. Custom Aggregations

**Business KPIs:**
- Average order value
- Books per order
- Revenue per region
- Genre diversity by school

---

## 💡 Why Simulated Data?

**Demonstrates professional data skills:**
1. **Prototyping ability** - Creating test data for development before production deployment
2. **Data structure understanding** - Knows what realistic business data looks like
3. **Privacy awareness** - Can work with synthetic data when real data unavailable
4. **Communication skill** - Can design data to illustrate specific analytical concepts

**Real-world applications:**
- Testing new analysis pipelines before applying to production data
- Creating training datasets for team skill development
- Building proof-of-concept dashboards for stakeholder feedback
- Developing documentation with shareable examples

---

## 🔍 Key Insights (Synthetic Data)

**Note:** These insights are based on simulated data designed to demonstrate analytical techniques, not real market research.

### Regional Patterns
- North and East regions show higher library budgets
- West region shows lower student counts but comparable spending
- Regional differences suggest tailored sales strategies needed

### Genre Performance
- Fiction shows highest order frequency
- Science books command premium pricing
- Non-Fiction shows consistent quarterly demand

### Budget Utilization
- Most schools spend 60-80% of library budget
- Variation suggests opportunity for increased engagement
- Budget-to-student ratios vary significantly by region

---

## 🤖 AI Collaboration Statement

This project was created as a Week 1 wrap-up exercise demonstrating pandas fundamentals.

**Human contributions (Magda):**
- Completed DataCamp Chapters 1-4
- Practiced concepts through daily exercises
- Requested comprehensive demonstration project

**AI contributions (Claude):**
- Generated realistic education sector scenario
- Created structured code demonstrating all pandas concepts
- Provided extensive inline documentation

**Purpose:** Consolidate Week 1 learning through practical application in education sector context relevant to career goals.

---

## 📂 Repository Context

**Part of:** 18-Week Data Analysis Career Development Program  
**Week focus:** Week 1 - Python fundamentals and pandas basics  
**Skill level:** Foundational (pandas Chapters 1-4)

**Why this project:**
- Comprehensive demonstration of pandas fundamentals in single script
- Education sector context relevant to target roles
- Shows progression from data creation through analysis
- Professional code structure and documentation

**Learning progression:**
- Week 1: This project (pandas basics, simulated data)
- Week 2: Student dropout analysis (real data, complex joins)
- Week 3: Food choices analysis (real data, data cleaning)

**View complete program:** [Main Repository](https://github.com/MagsMcr/data-and-ai-analysis-journey)

---

## 🎯 Career Relevance

**Target roles:** AI Strategy Analyst / AI Product Manager in education/publishing

**Why education publishing data:**
- Demonstrates sector-specific knowledge and interest
- Shows understanding of education business metrics
- Relevant to target companies (Cambridge University Press & Assessment, educational publishers)
- Connects technical skills with business context

**Portfolio strategy:**
- This project shows **foundational technical skills**
- Other projects show **applied analytical thinking** with real data
- Together they demonstrate **progression and capability**

---

## 📫 Contact

**Author:** Magda McCrimmon  
**GitHub:** [@MagsMcr](https://github.com/MagsMcr)  
**Career focus:** Transitioning from Business Development to AI Strategy roles in education/publishing sectors  
**Current status:** Week 3 of 18-week data analysis intensive program

---

*Project completed: January 2026 | Type: Simulated data | Skills: pandas fundamentals (Chapters 1-4) | Context: Education sector business metrics*
