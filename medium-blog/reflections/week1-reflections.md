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