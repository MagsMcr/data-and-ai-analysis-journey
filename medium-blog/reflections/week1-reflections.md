# Week 1 Learning Notes
Started: January 26, 2026


### Completed:
- DataCamp: Data Manipulation with pandas - Chapter 1 ✓
- Created w1d1-pandas-practice.py with sorting, filtering, new columns ✓
- Industry research completed ✓
- W3Schools practice ✓

### Key learnings:
- .sort_values() returns new DataFrame (doesn't modify original)
- Methods (with parentheses) vs attributes (without)
- Boolean filtering with & and |
- .isin() for categorical filtering

### Challenges:
- Overthinking simple instructions - need to try simplest answer first
- Attempted HackerRank problem that was too advanced for Day 1

### Tomorrow:

- Continue with pandas Chapter 2

## Week 1 Day 2 - Tuesday, January 28, 2026

### What I Accomplished Today

**Core Learning:**
- ✅ Completed DataCamp: Data Manipulation with pandas - Chapter 2
- ✅ Created comprehensive practice script (`w1d2-pandas-practice.py`)
- ✅ Completed 3 Codewars problems (8 kyu level)
- ✅ All daily habits maintained

**Context:** 
Started day after health flare-up on Day 1 (Tuesday Jan 27). Determined to stay on track week-wise. Took systematic approach to ensure proper reinforcement of learning.

---

### New Concepts Mastered - pandas Chapter 2

**Summary Statistics & Aggregation:**
- Using `.agg()` with multiple functions: `df[['col1', 'col2']].agg(['mean', 'median', 'std'])`
- Creating custom aggregation functions (like IQR)
- Understanding when to use built-in functions vs custom ones

**Grouping Data:**
- `.groupby()` for analyzing data by categories
- Grouping by single column: `df.groupby('category')['value'].mean()`
- Grouping by multiple columns: `df.groupby(['cat1', 'cat2'])['value'].agg(['min', 'max'])`
- Can apply multiple aggregation functions to groups

**Pivot Tables:**
- `.pivot_table()` restructures data into cross-tabulation format
- `index` parameter = existing column that becomes row labels
- `columns` parameter = existing column that becomes column headers
- `values` parameter = the data to aggregate
- `aggfunc` parameter = how to aggregate (default is 'mean')
- Similar to Excel pivot tables but in code

---

### Key Technical Insights

**NaN Handling:**
- NaN = "Not a Number" - represents missing data, not an actual value
- Cannot perform standard operations on NaN
- Use `.fillna()` to replace with meaningful values for analysis
- Example: Replaced NaN in 'ai_tools_used' with "None" to enable comparison of AI users vs non-users

**Double Brackets for Multiple Columns:**
```python
# Single brackets + one column = Series
df['column']

# Double brackets + multiple columns = DataFrame
df[['col1', 'col2', 'col3']]
```
Need DataFrame (not list) to use `.agg()` on multiple columns

**Rounding Results:**
```python
# Option 1: Round when creating
df['new_col'] = (calculation).round(2)

# Option 2: Round existing column
df['col'] = df['col'].round(2)
```

---

### Practice Script Highlights

**Dataset:** Student AI Usage (continuing from Day 1)

**Analyses Performed:**
1. Summary statistics on 5 numerical variables using `.agg()`
2. Grouped analysis of grade changes by AI tool used
3. Multi-variable grouping (age by AI tool and purpose)
4. Study hours analysis by age and AI tool
5. Pivot table comparing grades across education levels and AI tools
6. Additional explorations: screen time comparison, correlation analysis

**New Calculated Column:**
- Created `grade_change_post_ai` showing percentage change in grades
- Formula: (grades_after - grades_before) / grades_before
- Rounded to 2 decimal places for clarity

---

### Coding Practice - Key Learnings

**Problem 1: Multiply by Power**
- Learned: `**` is exponent operator (not `*`)
- Learned: `len()` only works on strings, must convert integers with `str()`
- Learned: `abs()` handles negative numbers for digit counting
- Pattern: Chaining operations: `len(str(abs(n)))`

**Problem 2: Sum of Positives**
- **CRITICAL DISCOVERY: `return` exits the entire function immediately**
- `return` doesn't just stop a loop - it stops everything
- Must accumulate values BEFORE returning
- Learned `+=` shorthand: `total += i` means `total = total + i`

**Problem 3: Sum of Multiples**
- Practice with `while` loops and incrementing values
- Multiple validation conditions (separate checks for different invalid cases)
- Pattern: Start with first multiple, add n each time, stop before m
- Learned: Test requirements don't always match problem description perfectly

**Common Arithmetic Shorthands:**
```python
total += 5    # total = total + 5
total -= 3    # total = total - 3
total *= 2    # total = total * 2
total /= 4    # total = total / 4
```

---

### Challenges & Realizations

**Challenge 1: Coding Practice Difficulty**
Felt frustrated that I couldn't solve coding problems independently. Had to remind myself:
- This is Day 2 of Week 1
- The goal is exposure and learning, not independent mastery yet
- Professional developers look things up constantly
- Learning from mistakes IS the learning process

**Challenge 2: Understanding Pivot Tables**
Initially confused that both `index` and `columns` parameters refer to existing columns in the DataFrame. Realized they're just reorganizing data into cross-tabulation format, not creating new data.

**Challenge 3: Return Statement Behavior**
Thought my loop was wrong when really `return` was exiting the function after first iteration. Important distinction between `return`, `break`, and `continue`.

---

### What Went Well

**Systematic Approach:**
- Completed Chapter 2 fully before moving to practice
- Created comprehensive practice script with multiple analyses
- Maintained all daily habits despite starting after health issue

**Problem-Solving:**
- Asked good clarifying questions (e.g., "what is pass?")
- Recognized when to ask for code vs guidance
- Caught own mistakes (like wrong line for error in pandas code)

**Persistence:**
- Came back strong after Day 1 interruption
- Pushed through coding frustration productively
- Maintained commitment to systematic learning approach

---

### Investigate Further / Revise

**For Later Review:**
- **w1d2-pandas-practice.py script** - Want to explore this dataset further, potentially develop into fuller project
- Practice more with `.groupby()` and `.pivot_table()` - these are powerful but need more repetition to become intuitive
- The relationship between `return`, `break`, and `continue` - would benefit from more examples

**Questions for Future:**
- When to use pivot tables vs groupby? What are the different use cases?
- How to handle more complex validation scenarios in functions?

---

### Key Takeaways

1. **Pivot tables reorganize existing data** - they don't create new data, just present it differently
2. **`return` exits the entire function** - critical to understand for loops
3. **NaN needs intentional handling** - can't just ignore missing data in analysis
4. **Shorthand operators are everywhere** - `+=`, `-=`, etc. are standard Python
5. **Day 2 expectations are about learning, not mastery** - struggling with new concepts is normal and expected

---

### Tomorrow (Day 3 - Wednesday, January 29)

**Planned Focus:**
- DataCamp: Data Manipulation with pandas - Chapter 3
- Continue building on student AI dataset
- Start Netflix Movies guided project if time allows
- Remember: Systematic approach over rushing ahead

**Mindset:**
- Build on today's solid foundation
- Each day of practice makes concepts clearer
- It's okay to need help - that's what Day 2 is for

---

### Time Spent
Approximately 7 hours (strong recovery day after health interruption)

### Daily Habits Completed
✅ GitHub commit  
✅ DataCamp progress  
✅ W3Schools practice  
✅ Learning notes  
✅ Jira updates  

---

**Overall Assessment:** Excellent Day 2. Completed all core learning objectives, created comprehensive practice work, and maintained habits despite starting from a difficult place. The frustration at the end is a sign of brain fatigue, not failure. Solid progress.

# Week 1 Day 3 - Wednesday, January 29, 2026

**Focus:** pandas Chapter 3 - Advanced Indexing & Pivot Tables

## What I Completed Today:
- ✅ DataCamp: Data Manipulation with pandas - Chapter 3
- ✅ Created w1d3-pandas-practice.py with student AI dataset
- ✅ Completed Netflix Movies guided project
- ✅ All 5 daily habits maintained

## Chapter 3 Key Concepts Learned:

### Setting and Sorting Indexes:
- `.set_index('column')` - convert column to index
- `.sort_index()` - sort by index values
- Multi-level indexes: `.sort_index(level=['col1', 'col2'], ascending=[True, False])`
- **Important:** Can only slice an index if the index is sorted (especially for multi-level)

### Slicing with .loc[]:
- `.loc['start':'end']` - slice by index labels (inclusive of both ends)
- Works with sorted indexes
- Multi-level slicing: `.loc[('country1', 'city1'):('country2', 'city2')]`

### Position-Based Subsetting with .iloc[]:
- `.iloc[:5, 2:4]` - first 5 rows, columns 2-3 (remember: 0-indexed, end-exclusive)
- More flexible than .loc[] - doesn't require sorted index
- Useful for "first N rows" or "every Nth row" type selections

### Pivot Tables:
```python
df.pivot_table(
    values='what_to_aggregate',
    index='row_grouping',
    columns='column_grouping',
    aggfunc='mean'  # or 'sum', 'count', etc.
)
```
- Reorganizes data into cross-tabulation format
- Good for summarizing relationships between two categorical variables
- **Note:** Pivot tables go against tidy data principles - not used super frequently in real analysis

### Subsetting Pivot Tables:
- By rows: `pivot.loc['row_label']` or `pivot.loc[['row1', 'row2']]`
- By columns: `pivot['column_name']` or `pivot[['col1', 'col2']]`
- Both: `pivot.loc['row', 'column']`

### Calculating Means Across Axes:
- `.mean()` (no axis specified) = mean DOWN columns (default: axis=0)
- `.mean(axis='columns')` or `.mean(axis=1)` = mean ACROSS columns
- Finding extremes: `.idxmax()` returns index of maximum, `.idxmin()` returns index of minimum
- Alternative filtering: `series[series == series.max()]`

## Technical Insights:

### GroupBy Object vs Executed GroupBy:
- `df.groupby('column')['value']` creates a GroupBy object (doesn't show data)
- Need to add aggregation to execute: `.mean()`, `.agg(['min', 'max'])`, etc.
- GroupBy only "executes" when you tell it what calculation to perform

### Mode with GroupBy:
- `.mode()` exists but is tricky with groupby (can return multiple values)
- Use: `df.groupby('col')['value'].agg(lambda x: x.mode()[0])` 
- For whole column: `df['column'].mode()[0]` (returns Series, need [0] for value)

### Print Statement Formatting:
- `\n` creates blank line for visual spacing
- Each `print()` automatically moves to next line
- Use `\n` when you want extra space between sections for readability

## Netflix Movies Project:

### Tasks Completed:
1. Found most frequent movie duration in 1990s using `.mode()[0]`
2. Counted short action movies (< 90 minutes) using `len()` on filtered DataFrame

### Key Pattern Learned:
- Filter first, then count: `len(df[conditions])`
- Filtering creates new DataFrame with only matching rows
- `len()` counts rows in that filtered DataFrame

## Common Mistakes Made (and Fixed!):
- Trying to use `.unique()` as DataFrame method instead of Series method
- Forgetting `[0]` after `.mode()` to extract the actual value
- Column name typos (`year` vs `release_year`)
- Missing parentheses in print statements
- **Reminder:** These are completely normal beginner mistakes that everyone makes!

## Challenges & Realizations:

### Multi-Level Indexes:
- Struggled to visualize multi-dimensional pivot tables mentally
- Decision: Practice with real data will help more than more explanations
- These aren't used frequently in real analysis anyway
- Understanding they exist is more important than mastering them right now

### Strategic Time Management:
- Running behind schedule and tired
- Made strategic choice: Let Claude write Day 3 practice script, focus energy on Netflix project
- This allowed completion of all core learning while managing fatigue
- Not cutting corners - prioritizing guided practice over redundant solo practice

### Netflix Project Scope:
- Only 2 required tasks (much lighter than expected)
- Completed quickly in DataCamp environment
- Good reinforcement of filtering and aggregation concepts

## What's Working Well:
- Understanding when to ask for help vs. push through
- Recognizing appropriate vs inappropriate problem difficulty
- Strategic time allocation when tired
- Applying concepts across different datasets
- Asking "why" questions about syntax and methods

## Investigate Further / Revise:
- Multi-level indexes: Know they exist, can look up when needed, but not priority
- Axis confusion (axis=0 vs axis=1): Will become clearer with more practice
- w1d3-pandas-practice.py: Review output to see how concepts apply to student data

## Hours Worked: ~8 hours
- DataCamp Chapter 3: ~2 hours
- Practice script creation & review: ~1.5 hours
- Netflix project: ~1 hour
- Strategic planning and time management: ~0.5 hour
- Questions and concept clarification: ~2 hours
- Documentation and wrap-up: ~1 hour

## Tomorrow (Day 4) Plan:
- pandas Chapter 4 (final chapter of Data Manipulation with pandas)
- Additional practice if needed
- Continue building toward Week 1 completion Friday

---

**Day 3 Status: COMPLETE ✓**  
**Momentum: Strong despite fatigue**  
**Strategic thinking: Excellent**

## Day 4 - Friday, January 31, 2026

### What I Learned Today

**DataCamp: Data Manipulation with pandas - Chapter 4 (COMPLETE!)**
- Creating DataFrames from dictionaries of lists
- Reading and writing CSV files with `.to_csv()` and `pd.read_csv()`
- Data visualization directly from pandas using `.plot()`
- Plot customization: titles, labels, legends, transparency (alpha), colors
- Different plot types: bar (`kind='bar'`), horizontal bar (`kind='barh'`), histogram (`kind='hist'`), line (`kind='line'`)
- Using `plt.show()` to display plots in scripts
- `.unstack()` to transform multi-index data for better visualization
- Stacked vs side-by-side bar charts

**Key Technical Concepts:**

**Dictionary of Lists for DataFrames:**
```python
data = {
    'column1': [value1, value2, value3],
    'column2': [value1, value2, value3]
}
df = pd.DataFrame(data)
```

**Saving DataFrames to CSV:**
```python
df.to_csv('filename.csv', index=False)  # index=False excludes row numbers
```

**Basic Plotting:**
```python
df['column'].plot(kind='bar', title='My Title', xlabel='X Label', ylabel='Y Label')
plt.show()  # Required in scripts to display plot
```

**Plot Customization:**
```python
df.plot(
    kind='hist',
    alpha=0.7,      # Transparency (0=invisible, 1=solid)
    color='blue',
    rot=45          # Rotate x-axis labels
)
plt.legend(['Label 1', 'Label 2'])  # Add legend labels
plt.show()
```

**Working with Multi-Index Data:**
```python
# Unstack to transform multi-index for better plotting
grouped_data.unstack().plot(kind='bar')
```

**HackerRank Practice:**

Completed 3-4 problems focusing on:
- Loops and range operations
- Understanding `for` vs `while` loops (nested loop behavior)
- Dictionary manipulation and subsetting
- Using `.items()` to iterate through dictionaries
- List operations: finding max values, filtering
- String formatting with f-strings and `.2f` for decimal places
- Understanding `map()` as an iterator (can only be used once)
- Importance of `list()` to convert iterators for multiple uses

**Critical Understanding - `for` and `while` Loop Relationship:**
When `while` is nested inside `for`, the `while` loop must complete before `for` can move to the next iteration. If `while` creates an infinite loop (condition always True, variable never changes), the `for` loop gets stuck and never progresses. The `for` loop doesn't "feed" numbers to `while` - it sets the variable once, then waits.

**Python Statistics Functions:**
- `mean()` is NOT a built-in function in base Python
- Must import from `statistics` module: `from statistics import mean`
- OR calculate manually: `sum(list) / len(list)`
- Base Python includes: `sum()`, `max()`, `min()`, `len()`
- Statistical functions require import or pandas/numpy

**Practice Script:**
Created comprehensive book sales analysis demonstrating:
- DataFrame creation from dictionary of lists (12 rows, 6 columns)
- Calculated columns using arithmetic operations
- Percentage calculations using `.groupby()` with `.transform('sum')`
- Multiple groupby aggregations with different functions
- Four different plot types with customization
- Saving results to CSV files

### Challenges Faced

**DataCamp Answer Checker Rigidity:**
Encountered multiple instances where valid Python syntax was rejected because DataCamp wanted specific syntax:
- `.plot.bar()` rejected in favor of `.plot(kind='bar')`
- Both work identically, but checker only accepts one
- Same with `kind=line` (needs quotes: `kind='line'`)
This is frustrating but not a reflection of code correctness - professional developers use multiple valid approaches interchangeably.

**HackerRank Challenges:**
- Initial confusion about `for` and `while` loop interaction when nested
- `map()` iterator issue - using it twice caused empty list errors
- Forgetting that `mean()` requires import from statistics module
- Syntax details like f-string formatting for decimals (`.2f`)

**Multi-Index Plotting:**
Initially struggled with plotting grouped data with multiple index levels. Learned that `.unstack()` transforms the data structure to make genres (or other second-level index) into separate columns, which then plot with different colors automatically.

### Aha Moments

**Understanding Nested Loop Behavior:**
Finally clicked that when `while` is inside `for`, the inner loop completely controls flow. The `for` loop sets `i=0` and then WAITS for `while` to finish. If `while` never changes `i`, it loops forever on that first value, preventing `for` from ever moving to `i=1`. They're not working in parallel - `while` is trapped inside one iteration of `for`.

**`map()` as Iterator:**
Realized that `map()` creates a one-time-use iterator, not a persistent list. After using it once (e.g., in `max(arr)`), it's exhausted and appears empty. Converting to `list()` immediately after creation solves this: `arr = list(map(int, input().split()))`.

**Transform vs Regular GroupBy:**
Discovered the power of `.transform('sum')` for percentage calculations. Regular `.groupby().sum()` returns aggregated totals, but `.transform()` broadcasts those totals back to every row, maintaining DataFrame shape. This enables row-by-row percentage calculations against group totals.

**`.unstack()` for Visualization:**
The moment `.unstack()` clicked as a transformation tool changed how I think about multi-index data. It pivots the second index level into columns, making each unique value a separate series that plots with its own color. Much clearer than trying to plot multi-index directly!

### What Went Well

**Chapter 4 Completion:**
Successfully completed the final chapter of Data Manipulation with pandas! The entire 4-chapter course is now done. Solid understanding of DataFrame creation, CSV I/O, and visualization basics.

**Problem-Solving Progress:**
On HackerRank challenges, consistently demonstrating correct problem-solving logic - knowing WHAT to do and WHICH tools to use. Syntax issues are normal at this stage and will improve with repetition. The thinking is sound.

**Practice Script Quality:**
Created a comprehensive, well-documented practice script with:
- Real-world relevant data (publishing industry)
- Multiple analysis techniques
- Four different visualization types
- Professional code organization and comments
- Proper CSV output

**Strategic Decision-Making:**
Made good choices about when to invest time (creating full analysis) vs when to request assistance (dictionary data generation) to maintain momentum and focus on learning objectives.

**Git Habits:**
Maintained daily commit streak with descriptive commit messages. Repository staying organized and up-to-date.

### Time Investment

Approximately 8 hours:
- DataCamp Chapter 4: ~2 hours
- W3Schools practice: ~15 minutes  
- HackerRank challenges: ~2 hours
- Practice script: ~2.5 hours (including plotting experimentation)
- Git commits and documentation: ~30 minutes
- Learning notes: ~1 hour

### Personal Reflections

**On Being "Behind Schedule":**
Today is actually Friday (Day 5), but I'm completing Day 4 work. Rather than seeing this as failure, recognizing this as realistic pacing. The systematic approach of completing each day fully is MORE important than rushing to stay on arbitrary schedule. Will catch up over weekend if possible, but quality learning beats checkbox completion.

**On Problem-Solving Confidence:**
Starting to feel genuinely hopeful about progress. Even when syntax is wrong, the problem-solving logic is increasingly correct. Understanding WHAT to do is the hard part - the HOW (syntax) comes with practice and is easily looked up. This is exactly the right learning trajectory for Day 4/Week 1.

**On Making Mistakes:**
Getting more comfortable with being wrong and trying anyway. The "I won't die if I'm wrong" mindset is healthy and necessary for learning. Professional developers make syntax errors constantly - it's not a reflection of capability, just part of the process.

**On Support and Guidance:**
The three-level guidance system continues to work well. Being able to request full code when tired, detailed guidance when engaged, or high-level direction when confident allows flexible progress without burning out. Strategic use of assistance maintains momentum.

### Investigate Further / Revise

**Topics for Deeper Understanding:**

1. **Iterator vs List Behavior**
   - Why does `map()` exhaust after one use?
   - What other Python objects behave this way?
   - When to use iterators vs when to convert to list?

2. **Transform vs Apply in GroupBy**
   - Understand `.transform()` more deeply
   - When to use `.apply()` vs `.transform()`
   - Practice more complex grouped calculations

3. **Multi-Index DataFrames**
   - More practice with `.stack()` and `.unstack()`
   - When to use multi-index vs when to avoid it
   - Best practices for multi-index manipulation

4. **Plot Customization**
   - Explore more `matplotlib` customization options
   - Color palettes and styling
   - Subplot layouts for multiple plots
   - Saving plots to files

5. **Dictionary Methods**
   - Review `.keys()`, `.values()`, `.items()` usage
   - Dictionary comprehensions
   - When to use dictionaries vs DataFrames

**Syntax to Practice:**

- f-string formatting variations (not just `.2f`)
- List comprehensions with conditions
- Multiple aggregation functions in single `.agg()` call
- Proper `import` statements for different modules

**Concepts to Revisit:**

- Loop control flow (especially nested loops)
- When built-in functions are available vs when imports needed
- Iterator behavior and best practices
- GroupBy mechanics and result structures

### Week 1 Status

**Completed:**
- ✅ Day 1: pandas Chapter 1
- ✅ Day 2: pandas Chapter 2  
- ✅ Day 3: pandas Chapter 3 + Netflix Movies project
- ✅ Day 4: pandas Chapter 4 + practice script + HackerRank (completed Friday)

**Remaining:**
- ☐ Day 5: Introduction to Functions in Python course (to complete Saturday/Sunday)

**Week 1 Achievement:**
Completed entire "Data Manipulation with pandas" course (4 chapters)! This is a major milestone. All fundamental pandas operations now covered: inspection, sorting, subsetting, aggregation, grouping, pivot tables, indexing, slicing, creating DataFrames, CSV I/O, and visualization.

### Looking Ahead

**Tomorrow/Weekend:**
Complete Introduction to Functions course to finish Week 1 core learning objectives. This will add Python function fundamentals to pandas mastery, creating solid foundation for Week 2.

**Week 2 Preview:**
- More advanced pandas (joining datasets)
- Data visualization with Seaborn
- Introduction to statistics
- Building on Week 1 pandas foundation

**Overall Feeling:**
Despite being a day behind schedule-wise, feeling positive about actual learning progress. The systematic approach is working - comprehensive understanding being built rather than superficial checkbox completion. Ready to finish Week 1 strong and enter Week 2 with confidence.

---

## Progress Tracker

**Daily Habits This Week:**
- GitHub commits: 4/4 days ✅
- DataCamp: 4/4 days ✅  
- W3Schools: 4/4 days ✅
- Learning notes: 4/4 days ✅
- Jira updates: 4/4 days ✅

**100% habit compliance maintained!**

## Week 1 Final Wrap-Up & Reflections
### January 26-31, 2026

---

## Week Overview

**Planned Focus:** Python Fundamentals (variables, control flow, functions)
**Actual Focus:** Data Manipulation with pandas + Introduction to Functions (Chapters 1-2)

**Why the Change:** 
The original Week 1 plan was designed before starting, but upon beginning the program, DataCamp's "Data Manipulation with pandas" course proved to be the more strategic starting point. This course builds the foundation needed for all future data analysis work and was more directly relevant to immediate career goals.

**Strategic Decision:** Prioritized pandas mastery over strict adherence to original plan. This flexibility demonstrates good judgment - following the learning path that makes most sense rather than rigidly sticking to a pre-made schedule.

---

## What Was Accomplished

### DataCamp Courses Completed:

**1. Data Manipulation with pandas (COMPLETE - 4 Chapters)**
- ✅ Chapter 1: Transforming DataFrames (sorting, subsetting, filtering)
- ✅ Chapter 2: Aggregating DataFrames (groupby, summary stats, pivot tables)
- ✅ Chapter 3: Slicing and Indexing (set_index, .loc, .iloc, multi-level indexing)
- ✅ Chapter 4: Creating and Visualizing DataFrames (from scratch, plotting, CSV I/O)

**2. Introduction to Functions in Python (Chapters 1-2)**
- ✅ Chapter 1: User-Defined Functions (def, parameters, return values, docstrings)
- ✅ Chapter 2: Default Arguments, Variable-length Args, Scope (global, nonlocal, closures)
- ☐ Chapters 3-4: Deferred until more Python experience (strategic decision)

### Guided Projects:
- ✅ Netflix Movies Analysis (completed Day 3)

### Practice Scripts Created:
- ✅ w1d1-pandas-practice.py (Chapter 1 concepts)
- ✅ w1d2-pandas-practice.py (Chapter 2 concepts)  
- ✅ w1d3-pandas-practice.py (Chapter 3 concepts)
- ✅ w1d4-pandas-practice.py (Chapter 4 concepts - comprehensive book sales analysis)
- ✅ week1_wrap_up_project.py (integration of all Week 1 concepts)

### Daily Habits Maintained:
- ✅ GitHub commits: 5/5 days (100% compliance)
- ✅ DataCamp progress: 5/5 days (100% compliance)
- ✅ W3Schools practice: 5/5 days (100% compliance)
- ✅ Learning notes: 5/5 days (100% compliance)
- ✅ Jira updates: 5/5 days (100% compliance)

### Coding Practice:
- ✅ HackerRank challenges: 3-4 problems completed
- ✅ Codewars: Multiple 8 kyu problems
- Focus: Basic Python syntax, loops, dictionaries, list operations

---

## Key Technical Concepts Mastered

### pandas Fundamentals (Chapters 1-4)

**DataFrame Inspection & Manipulation:**
- `.head()`, `.tail()`, `.info()`, `.describe()`, `.shape`, `.columns`
- Sorting: `.sort_values()` with single/multiple columns, ascending/descending
- Subsetting columns with `[]` and `[[]]`
- Boolean filtering with conditions, `&`, `|`, `.isin()`
- Creating calculated columns

**Aggregation & Analysis:**
- `.agg()` with multiple functions: `['mean', 'median', 'std', 'max', 'min']`
- Custom aggregation functions (e.g., IQR)
- `.groupby()` with single and multiple variables
- Combining groupby with `.agg()` for comprehensive analysis
- Understanding GroupBy objects vs executed results

**Pivot Tables:**
```python
df.pivot_table(
    values='column_to_aggregate',
    index='row_grouping',
    columns='column_grouping',
    aggfunc='mean',
    fill_value=0,
    margins=True
)
```
- Subsetting pivot tables with `.loc[]` and column selection
- Calculating means across axes (axis=0 vs axis=1)
- `.idxmax()` and `.idxmin()` for finding index of extremes

**Advanced Indexing:**
- `.set_index()` to convert column to index
- `.sort_index()` for sorting by index values
- `.loc[]` for label-based slicing (inclusive on both ends)
- `.iloc[]` for position-based slicing (exclusive end)
- Understanding when slicing requires sorted index

**DataFrame Creation & Output:**
- Creating DataFrames from dictionaries of lists
- `.to_csv()` for saving results (`index=False` to exclude row numbers)
- `pd.read_csv()` for loading data
- Direct plotting with `.plot()` method

**Visualization:**
```python
df['column'].plot(
    kind='bar',  # or 'hist', 'line', 'barh'
    title='Title',
    xlabel='X Label',
    ylabel='Y Label',
    alpha=0.7,
    color='blue',
    rot=45
)
plt.legend(['Label'])
plt.show()
```

### Python Functions (Chapters 1-2)

**Basic Function Structure:**
```python
def function_name(parameter1, parameter2):
    """Docstring explaining what function does."""
    result = parameter1 + parameter2
    return result
```

**Key Concepts:**
- Function definition with `def`
- Parameters vs arguments
- Return values (can return multiple values as tuple)
- Docstrings for documentation
- Tuple unpacking: `x, y, z = function_returning_three_values()`

**Default Arguments:**
```python
def power(number, pow=1):
    """Raise number to the power of pow."""
    return number ** pow

power(5)      # Uses default pow=1, returns 5
power(5, 2)   # Overrides default, returns 25
```

**Variable Scope:**
- **Local scope:** Variables created inside function
- **Global scope:** Variables created outside all functions
- **Enclosing scope:** Variables in outer function (for nested functions)

**Keywords:**
- `global variable_name`: Modify global variable from inside function
- `nonlocal variable_name`: Modify outer function variable from inner function

**Closures:**
Inner functions that "remember" variables from outer function even after outer function finishes:
```python
def make_multiplier(n):
    def multiply(x):
        return x * n  # 'n' is remembered
    return multiply

times_five = make_multiplier(5)
times_five(3)  # Returns 15
```

---

## Major Challenges & How They Were Overcome

### 1. DataCamp Answer Checker Rigidity
**Challenge:** Valid Python syntax rejected because DataCamp wanted specific syntax
- `.plot.bar()` rejected in favor of `.plot(kind='bar')`
- `kind=line` needed quotes: `kind='line'`

**Learning:** Multiple valid approaches exist in Python; DataCamp's checker is overly rigid. This is a tool limitation, not a code quality issue. Real-world coding is more flexible.

### 2. Understanding `map()` as Iterator
**Challenge:** Using `map()` twice caused empty list errors

**Solution:** Convert to list immediately:
```python
arr = list(map(int, input().split()))  # NOT just map()
```

**Learning:** `map()` creates one-time-use iterator. After first use, it's exhausted.

### 3. Nested Loop Behavior
**Challenge:** Confusion about `for` and `while` loop interaction when nested

**Breakthrough:** Understanding that when `while` is inside `for`, the `while` loop must COMPLETE before `for` can move to next iteration. If `while` creates infinite loop (variable never changes), `for` gets stuck forever.

### 4. Function Scope (global, nonlocal)
**Challenge:** Understanding when and why to use `global` vs `nonlocal`

**Key Learning:**
- `global`: Reach to top-level scope
- `nonlocal`: Reach to immediate parent function scope
- Declaration at top of function affects ALL uses of that variable below

### 5. Closures and Nested Functions
**Challenge:** Understanding why inner functions "remember" outer function variables

**Realization:** This is an intermediate Python concept not frequently used in data analysis work. Achieved functional understanding but recognized this isn't critical for immediate career goals.

**Strategic Decision:** Stopped Functions course at Chapter 2 to avoid paralysis over advanced concepts. Will return when more experienced.

### 6. Multi-Index Plotting
**Challenge:** Plotting grouped data with multiple index levels wasn't automatically color-coded

**Solution:** Use `.unstack()` to transform multi-index into format where second-level index becomes separate columns:
```python
grouped_data['values'].unstack().plot(kind='bar')
```

---

## Aha Moments & Breakthroughs

### 1. `.transform()` vs Regular GroupBy
**Discovery:** `.transform('sum')` broadcasts grouped sum back to every row, maintaining DataFrame shape. This enables row-by-row percentage calculations against group totals.
```python
# Regular groupby - returns aggregated totals
df.groupby('publisher')['sales'].sum()  # Returns one value per publisher

# Transform - returns value for every row
df['pct_of_publisher_sales'] = (
    df['sales'] / df.groupby('publisher')['sales'].transform('sum')
)
```

### 2. Methods vs Attributes
**Clarity:** Methods have `()` and execute actions. Attributes have no `()` and return stored information.
```python
df.shape        # Attribute - no parentheses
df.describe()   # Method - has parentheses
```

### 3. Pandas Operations Don't Modify by Default
Most pandas operations return NEW DataFrames rather than modifying originals:
```python
sorted_df = df.sort_values('column')  # df unchanged, sorted_df is new
df = df.sort_values('column')         # Reassign to actually change df
```

### 4. Boolean Indexing Automatically Filters
No need for separate filter step:
```python
# This IS the filtered DataFrame
high_sales = df[df['sales'] > 1000]
```

### 5. Dictionary Access Patterns
**Creating/defining dictionaries:** Use `{key: value}` with colon
**Adding/modifying entries:** Use `dict[key] = value` with brackets and equals

### 6. Simplest Interpretation First
**Pattern recognized:** Tendency to overthink exercises and assume complex solutions when simple, direct approaches work. Learning to try obvious solution first.

---

## What Went Exceptionally Well

### Technical Progress
- **Completed entire Data Manipulation with pandas course** - This is the foundation for ALL future data work
- **High-quality practice scripts** - Each day's script demonstrates solid understanding
- **Professional code organization** - Good commenting, clear structure, descriptive variable names
- **Problem-solving logic improving** - Understanding WHAT to do even when syntax isn't perfect yet

### Learning Approach
- **Systematic reinforcement working** - Completing each day fully before advancing prevents knowledge loss
- **"Investigate Further / Revise" sections** - Creating accountability for deeper learning
- **Strategic decision-making** - Choosing to stop Functions course at Chapter 2 shows good judgment
- **Healthy "I won't die if I'm wrong" mindset** - Encouraging experimentation and learning from mistakes

### Habits & Discipline
- **100% daily habit compliance** - Every single day hit all 5 non-negotiables
- **Consistent GitHub commits** - Professional commit messages, organized repository
- **Comprehensive documentation** - Notes are detailed and useful for future reference
- **Jira tracking maintained** - Good project management habits forming

### Adaptability
- **Switched from original Week 1 plan to pandas** - Recognized pandas was more strategic
- **Requested appropriate guidance levels** - Used three-level system effectively
- **Made strategic time-saving decisions** - Had Claude write Day 3 practice script when tired

---

## Areas for Continued Development

### Technical Skills to Strengthen

**1. Syntax Fluency**
- Still making typos and minor syntax errors (normal at this stage)
- Need more repetition to build muscle memory
- Solutions: More W3Schools practice, more coding problems

**2. Independent Problem-Solving**
- Often know WHAT to do but need help with HOW
- This improves naturally with practice and time
- Not a capability issue - just needs more experience

**3. Complex Nested Operations**
- Chaining multiple pandas operations together
- Multi-level groupby and complex aggregations
- Will strengthen with Week 2 (Joining Data)

**4. Debugging Skills**
- Building ability to read error messages
- Checking obvious things first (file saved? right directory?)
- Using print statements to check intermediate values

### Learning Process

**1. Overthinking Pattern**
- Still tendency to assume complex solutions for simple problems
- Need conscious effort to try simplest approach first
- Improving with awareness and practice

**2. Concept Integration**
- Understanding individual concepts well
- Need more practice combining multiple concepts
- Week 1 wrap-up project addresses this

**3. Confidence with Uncertainty**
- Getting better at accepting "I don't fully understand yet"
- Still some stress when concepts don't click immediately
- Functions Chapter 2 was good practice in moving forward anyway

---

## Time Investment & Pacing

### Actual vs Planned Schedule

**Original Plan:** Days 1-5 (Monday-Friday, January 26-30)
**Actual Execution:** Days 1-5 spread across January 26-31 (with Day 4 on Friday Jan 31)

**Why Behind:** 
- Health flare-up on Day 1 (Tuesday Jan 27) - took Day 2 off
- Learning takes longer than estimated when you're actually doing it vs planning it
- Quality learning prioritized over speed

**Hours Invested:**
- Day 1: ~7 hours (pandas Chapter 1, practice, research)
- Day 2: ~7 hours (pandas Chapter 2, Codewars practice)
- Day 3: ~8 hours (pandas Chapter 3, Netflix project)
- Day 4: ~8 hours (pandas Chapter 4, HackerRank, practice script)
- Day 5: ~6 hours (Functions Chapters 1-2, wrap-up project review)

**Total:** ~36 hours (close to planned 37.5, just spread over 6 days instead of 5)

### Pacing Insights

**What Worked:**
- Systematic daily completion prevents knowledge loss
- Not rushing when concepts are challenging
- Strategic decisions about when to request help vs push through

**What to Adjust:**
- Build in buffer time for concepts that take longer
- Recognize that plans made before starting are estimates, not contracts
- One day behind on timeline is NOT falling behind on learning

---

## Industry Research Summary

### Hours Invested
Approximately 2.5-3 hours spread across the week (slightly short of 3-hour goal)

### Key Insights

**1. Data Integration is Critical**
- Every data analyst role mentions combining multiple data sources
- pandas joins and merges are fundamental skills
- Understanding WHERE data comes from matters as much as HOW to analyze it

**2. Education Sector Trends**
- Student information systems + assessment data + attendance tracking
- Privacy regulations (GDPR, FERPA) important when handling student data
- Growing use of predictive analytics for student success interventions
- EdTech companies hiring data analysts to improve product features

**3. Publishing Sector Trends**
- Sales data + author information + distribution channels
- Digital vs print performance analytics
- Reader engagement metrics from e-books and apps
- Market trend analysis for acquisition decisions

**4. Common Tool Stack**
- Python + pandas (fundamental)
- SQL for database queries (coming in Week 5)
- Tableau/Power BI for visualization (later weeks)
- Excel still very present (but pandas > Excel for serious analysis)
- Git/GitHub for collaboration

**5. Soft Skills Emphasized**
- Communication: Translating analysis for non-technical stakeholders
- Business acumen: Understanding why data matters to organization
- Curiosity: Asking good questions about data
- Attention to detail: Catching data quality issues

---

## Investigate Further / Revise

### Concepts Requiring Deeper Understanding

**1. Transform vs Apply in GroupBy**
- Understand `.transform()` mechanics more deeply
- When to use `.apply()` vs `.transform()` vs `.agg()`
- Practice more complex grouped calculations
- **Action:** Week 2 will provide more groupby practice

**2. Multi-Index DataFrames**
- More practice with `.stack()` and `.unstack()`
- Understanding when multi-index is helpful vs complicating
- Best practices for working with hierarchical indexes
- **Action:** Look for multi-index examples in Week 2 joining operations

**3. Iterator vs List Behavior**
- Why does `map()` exhaust after one use?
- What other Python objects behave this way? (generators, file objects)
- When to use iterators vs when to convert to list?
- **Action:** Research Python generators when time allows

**4. Function Closures (Deeper Dive Later)**
- Return to closures when more Python experience built
- Understand practical use cases in data analysis
- How closures relate to decorators
- **Action:** Defer to Week 8+ when more comfortable with Python

**5. Advanced Plotting with matplotlib**
- Explore more customization options beyond basic `.plot()`
- Subplots for multiple visualizations
- Color palettes and professional styling
- Saving plots with specific dimensions/DPI
- **Action:** Week 6 focuses on Data Visualization - will cover this

### Syntax to Practice More

**1. f-string Formatting Variations**
```python
f"{value:.2f}"      # 2 decimal places
f"{value:,.0f}"     # Thousands separator, no decimals
f"{value:>10}"      # Right-aligned, 10 characters wide
```
**Action:** Use in practice scripts going forward

**2. List Comprehensions with Conditions**
```python
[x for x in list if condition]
[x*2 for x in list if x > 5]
```
**Action:** Practice with Codewars/HackerRank problems

**3. Dictionary Comprehensions**
```python
{k: v for k, v in dict.items() if condition}
```
**Action:** Use in Week 2 practice scripts

**4. Lambda Functions**
```python
df.groupby('col').agg(lambda x: x.mode()[0])
```
**Action:** Encountered in pandas, will see more in Functions Chapter 3

### pandas Operations to Revisit

**1. Handling Missing Data (NaN)**
- `.isna()`, `.notna()`, `.fillna()`, `.dropna()`
- Different strategies for different scenarios
- **Action:** Will come up naturally in real datasets

**2. String Operations**
- `.str` accessor for string methods
- Pattern matching, case conversion, splitting
- **Action:** Week 3-4 likely covers this

**3. Date/Time Operations**
- `pd.to_datetime()`
- `.dt` accessor for datetime methods
- Time series analysis basics
- **Action:** Later weeks will introduce this

**4. Merge vs Join vs Concat**
- Already know concat basics
- Week 2 will teach merge and join thoroughly
- **Action:** Main focus of Week 2

---

## Week 1 Achievement Assessment

### Goals Met

✅ **Master pandas fundamentals** - Complete Data Manipulation course finished
✅ **Build strong foundation** - Solid understanding of DataFrames, groupby, pivot tables
✅ **Create portfolio-quality work** - 5 practice scripts + wrap-up project
✅ **Maintain daily habits** - 100% compliance on all 5 habits
✅ **Professional practices** - Git, documentation, Jira all maintained
✅ **Strategic adaptability** - Made good decisions about pacing and focus

### Goals Partially Met

⚠️ **Industry research** - 2.5-3 hours vs 3-hour goal (close enough)
⚠️ **Functions course** - Completed 2/4 chapters (strategic decision to defer rest)

### What Success Looks Like

**Week 1 was objectively successful because:**

1. **Core skill mastered:** pandas fundamentals are THE foundation for data analysis
2. **Quality over speed:** Deep understanding prioritized over checkbox completion
3. **Professional habits formed:** Daily commits, documentation, project management
4. **Portfolio building:** Multiple demonstration scripts showing capability
5. **Strategic thinking:** Made smart decisions about where to focus effort
6. **Resilience:** Worked through health setback without derailing progress
7. **Self-awareness:** Recognized when to push through vs when to defer

**This is NOT measured by:**
- Staying exactly on arbitrary schedule
- Perfect understanding of every concept
- Zero mistakes or confusion
- Completing every single planned item

---

## Confidence & Capability Assessment

### What I Know I Can Do

✅ Load and inspect DataFrames
✅ Filter and subset data using boolean conditions
✅ Sort by single and multiple columns
✅ Create calculated columns
✅ Group data and calculate summary statistics
✅ Create pivot tables for cross-tabulation analysis
✅ Generate basic visualizations (bar, histogram, line plots)
✅ Save analysis results to CSV
✅ Write basic functions with parameters and return values
✅ Understand variable scope concepts
✅ Use Git for version control
✅ Maintain professional code documentation

### What I'm Building Confidence In

🔨 Chaining multiple pandas operations together
🔨 Complex groupby with multiple aggregation functions
🔨 Advanced indexing with .loc and .iloc
🔨 Independent problem-solving (knowing what to Google)
🔨 Debugging my own code
🔨 Writing efficient, clean code
🔨 Applying concepts to new scenarios

### What I Know I Don't Know Yet (And That's OK)

📚 Joining/merging multiple datasets (Week 2!)
📚 SQL for database queries (Week 5)
📚 Advanced statistical analysis (Week 7)
📚 Machine learning concepts (Week 9+)
📚 Data visualization with Seaborn (Week 6)
📚 Working with real messy data at scale

---

## Personal Reflections

### On Being "Behind Schedule"

**Initial reaction:** Anxiety about not finishing Week 1 by Friday
**Realization:** I completed 36 hours of quality learning in 6 days instead of 5
**New understanding:** Behind schedule ≠ Behind on learning

The systematic approach (completing each day fully, practicing concepts, building real understanding) is MORE valuable than rushing to hit arbitrary dates. The knowledge is what matters, not the timeline.

### On Struggling with Functions Chapter 2

**The spiral:** "I don't understand closures → Maybe I'm not smart enough → Maybe I can't do this"
**Reality check:** Closures are intermediate concepts, Day 5 is early to master them, professional developers still look these up
**Growth:** Learning to say "I don't fully understand this yet AND I can move forward anyway"

This was important practice in not letting one challenging concept derail entire program.

### On Problem-Solving Progress

**Week 1 Day 1:** "I have no idea how to approach this"
**Week 1 Day 5:** "I know WHAT to do, just need help with syntax"

This is huge progress! Understanding the logic and approach is the hard part. Syntax fluency comes with repetition and time.

### On Asking for Help

**Initial worry:** Asking for code makes me a cheater
**New understanding:** Strategic use of guidance (three-level system) maintains momentum while building skills
**Evidence:** Day 3 practice script (Claude-written) was thoroughly reviewed and understood. Day 4 practice script (self-written with guidance) demonstrated independent application.

### On Making Strategic Decisions

**Examples this week:**
- Switching from Python Fundamentals to pandas (better for career goals)
- Stopping Functions at Chapter 2 (avoiding paralysis)
- Requesting code for wrap-up project (getting ahead instead of constantly behind)
- Having Claude write Day 3 practice script when tired (smart energy management)

These decisions show developing judgment about what matters most.

---

## Looking Ahead to Week 2

### What's Coming

**Week 2 Focus:** Joining Data with pandas
- Inner, left, right, outer joins
- Merging datasets with different key columns
- Semi-joins and anti-joins
- Concatenating DataFrames
- Multi-dataset integration projects

**Why This Matters:**
Every data analyst role involves combining data from multiple sources. Week 2 builds directly on Week 1's manipulation skills.

### Goals for Week 2

**Technical:**
- Master all types of joins
- Understand when to use merge vs concat
- Handle mismatched column names in joins
- Build multi-dataset analysis project

**Process:**
- Maintain 100% daily habits
- Continue systematic day-by-day completion
- Use three-level guidance system appropriately
- Build on Week 1 pandas foundation

**Personal:**
- Start week on schedule (Monday Feb 2)
- Manage energy proactively
- Continue "I won't die if I'm wrong" mindset
- Trust the systematic approach

### Carrying Forward

**What worked in Week 1:**
✅ Systematic completion prevents knowledge loss
✅ Professional documentation and habits
✅ Strategic decision-making about effort allocation
✅ Requesting appropriate guidance levels
✅ Quality understanding over speed

**What to adjust:**
⚠️ Build buffer time into estimates
⚠️ Don't let one difficult concept derail momentum
⚠️ Industry research - spread more evenly across week
⚠️ Remember: slight schedule delays ≠ failure

---

## Final Week 1 Metrics

**Technical Achievement:**
- DataCamp courses: 1 complete (4 chapters), 1 partial (2/4 chapters)
- Practice scripts: 5 comprehensive scripts
- Guided projects: 1 complete (Netflix Movies)
- Integration project: 1 complete (Week 1 wrap-up)
- Coding problems: 6-8 completed

**Habit Compliance:**
- GitHub commits: 5/5 days (100%)
- DataCamp: 5/5 days (100%)
- W3Schools: 5/5 days (100%)
- Learning notes: 5/5 days (100%)
- Jira updates: 5/5 days (100%)

**Time Investment:**
- Total hours: ~36 hours
- Target: 37.5 hours
- Efficiency: 96%

**Repository Health:**
- Organized folder structure ✅
- Professional commit messages ✅
- Comprehensive README ✅
- Well-documented code ✅

---

## Celebration & Gratitude

### What to Celebrate

🎉 **Completed entire Data Manipulation with pandas course**
🎉 **Built portfolio-quality practice scripts**
🎉 **Maintained 100% daily habit compliance**
🎉 **Worked through health setback without quitting**
🎉 **Made strategic decisions showing good judgment**
🎉 **Recognized when to push through vs when to defer**
🎉 **Built systematic approach that prevents knowledge loss**
🎉 **Demonstrated resilience and adaptability**

### Gratitude

**For the systematic approach** that's working to build real understanding
**For the three-level guidance system** that maintains momentum
**For honest self-awareness** about capabilities and limitations
**For courage to ask "am I good enough?"** and face the answer
**For persistence** through confusion and frustration
**For flexibility** to adapt plans when needed

---

## Closing Thoughts

Week 1 was about much more than learning pandas syntax. It was about:

- **Building a sustainable learning system** that prevents knowledge loss
- **Developing professional habits** that will carry through entire career
- **Learning to make strategic decisions** about where to invest effort
- **Building confidence** through systematic achievement
- **Practicing resilience** when things don't go exactly as planned

**The pandas skills matter. The habits and mindset matter more.**

Every data analyst job requires pandas. But what makes someone succeed long-term is:
- The discipline to show up daily
- The judgment to know what's important
- The resilience to work through challenges
- The self-awareness to ask for help
- The flexibility to adapt when plans change

**Week 1 built ALL of these, not just pandas skills.**

---

## Ready for Week 2

**Technical foundation:** Solid pandas manipulation skills ✅
**Professional practices:** Git, documentation, Jira established ✅
**Learning system:** Systematic approach proven effective ✅
**Mindset:** Confident but realistic, resilient, adaptable ✅
**Habits:** 100% compliance on all dailies ✅

**Week 2 starts Monday, February 2, 2026.**
**Focus: Joining Data with pandas**
**Detailed plan: Ready in Week_2_Detailed_Plan.docx**

**Bring on the joins!** 🚀

---

**Week 1: COMPLETE** ✅
**Systematic approach: WORKING** ✅
**Momentum: BUILDING** ✅
**Confidence: GROWING** ✅

*You've got this, Magda.* 💪

---

## Progress Tracker

**Weeks Completed:** 1 / 18
**Courses Completed:** 1 full + 2 chapters
**Practice Scripts:** 5
**Daily Habits Streak:** 5 days
**GitHub Commits:** Professional and consistent
**Portfolio Projects:** 2 (Netflix + Week 1 wrap-up)

**Next milestone:** Complete Week 2 by Friday, February 6, 2026

---