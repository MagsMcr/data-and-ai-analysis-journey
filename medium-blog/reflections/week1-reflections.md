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