# Week 2 Day 1 - Monday, February 3, 2026

## Daily Summary
**Focus:** Inner Joins (Joining Data with pandas - Chapter 1)  
**Hours:** ~7-8 hours  
**Mood:** Challenging but ultimately successful - emotional rollercoaster with breakthrough moments  
**Completion:** Chapter 1 COMPLETE ✅ | Practice script COMPLETE ✅ | Coding practice COMPLETE ✅

---

## What I Learned Today

### DataCamp: Joining Data with pandas - Chapter 1

**Main Concept:** Inner joins combine data from two DataFrames, keeping only rows where the key exists in BOTH tables.

#### Basic Merge Syntax
```python
# When column names are the same
merged_df = df1.merge(df2, on='column_name')

# When column names differ
merged_df = df1.merge(df2, left_on='col_in_df1', right_on='col_in_df2')

# Specifying join type (inner is default)
merged_df = df1.merge(df2, on='column', how='inner')
```

#### Merging on Multiple Columns
```python
# Both columns must match for rows to merge
merged_df = df1.merge(df2, on=['column1', 'column2'])

# With different column names
merged_df = df1.merge(
    df2,
    left_on=['col1_df1', 'col2_df1'],
    right_on=['col1_df2', 'col2_df2']
)
```

#### Chaining Multiple Merges
```python
# Merge three tables together
full_data = df1.merge(df2, on='key1') \
               .merge(df3, on='key2')
# Use backslash for readability across lines
```

#### One-to-Many Relationships
**Key Understanding:** When one table has unique values and another has multiple rows per value:
- Students table: 1 row per student
- Enrollments table: Multiple rows per student (one per course)
- After merge: Result has MORE rows than students table

**Example:**
- 6 students + 11 enrollments = 11 rows in merged data
- Each student appears multiple times (once per enrollment)

#### Filtering After Merge
**Important pattern to remember:**
```python
# Create filter criteria as a variable (saves it for reuse/readability)
filter_criteria = ((df['column1'] == 'value1') 
                   & (df['column2'] == 'value2')
                   & (df['column3'] == 'value3'))

# Use .loc with the filter
result = df.loc[filter_criteria, ['col_to_display']]

# Can then aggregate
total = df.loc[filter_criteria, 'numeric_column'].sum()
```

**CRITICAL:** Parentheses around EACH condition are required when using `&` (AND) or `|` (OR) operators!

#### Aggregating After Merge
```python
# Dictionary format for aggregation
df.groupby('category').agg({'column': 'function'})

# Examples:
student_totals = merged.groupby('student_name').agg({'credits': 'sum'})
course_avg = merged.groupby('course').agg({'grade': 'mean'})

# Multiple aggregations
dept_stats = merged.groupby('department').agg({
    'grade': 'mean',
    'student_id': 'count'
})
```

#### Sorting Merged Results
```python
# Single column
df.sort_values('column', ascending=False)

# Multiple columns with different directions
df.sort_values(
    ['column1', 'column2', 'column3'],
    ascending=[True, False, True]
)
# Remember: Both lists must be same length!
```

---

## New Python Concepts Learned Today

### Dictionary as Instructions (Not Just Storage)
**Week 1 dictionaries = Storage:**
```python
student = {'name': 'Maria', 'age': 20}  # Holds data
```

**Week 2 dictionaries = Instructions:**
```python
# Tells .agg() what to do
df.groupby('category').agg({'sales': 'sum', 'customers': 'count'})
# Key = which column, Value = what function to apply
```

This is a common pandas pattern - using dictionaries to configure operations!

### The Accumulator Pattern (From Codewars)
**Critical programming pattern learned:**
```python
# Pattern for multiplying all values in a list
def grow(arr):
    result = 1              # Start with initial value
    for x in arr:           # Loop through collection
        result = result * x # Accumulate (can use result *= x)
    return result           # Return accumulated result
```

**Why start with 1?** Because 1 * anything = anything (neutral for multiplication)  
**For addition:** Start with 0  
**For strings:** Start with ""  
**For lists:** Start with []

### String Parsing with .split()
```python
command = "insert 0 5"
parts = command.split()      # ["insert", "0", "5"]

cmd = parts[0]               # "insert"
position = int(parts[1])     # 0 (converted to integer)
value = int(parts[2])        # 5 (converted to integer)
```

**Use case:** HackerRank/Codewars problems (not typical data analysis)

### Binary Conversion
```python
# Convert binary string to decimal
decimal = int("101", 2)  # 5
decimal = int("1010", 2) # 10

# The 2 means "interpret this string as base-2 (binary)"
```

### List/Array Subsetting (Slicing)
```python
my_list = [10, 20, 30, 40, 50, 60, 70]

my_list[1:4]     # [20, 30, 40] - index 1 to 3 (4 is exclusive)
my_list[:3]      # [10, 20, 30] - first 3 elements
my_list[2:]      # [30, 40, 50, 60, 70] - from index 2 to end
my_list[-3:]     # [50, 60, 70] - last 3 elements
my_list[:-2]     # [10, 20, 30, 40, 50] - all except last 2
my_list[::2]     # [10, 30, 50, 70] - every other element
my_list[::-1]    # [70, 60, 50, 40, 30, 20, 10] - reversed

# Format: [start:stop:step]
# start = inclusive, stop = exclusive
```

---

## Practice Script Created

**File:** `w2d1-inner-joins.py`  
**Dataset:** Education sector (students, courses, enrollments)  
**Demonstrates:**
- Basic inner joins
- Chaining three tables
- Merging on multiple columns
- Filtering merged data
- Aggregating after merge (department performance, student rankings)
- Semester comparisons
- All Chapter 1 concepts with working examples

**Script has 8 comprehensive examples** with detailed comments and explanations.

---

## Coding Practice Completed

### HackerRank: List Commands Problem
**Challenge:** Parse command strings and execute list operations  
**Skills practiced:**
- `.split()` to parse strings
- Converting strings to integers with `int()`
- Conditional logic with if/elif
- List methods: insert, remove, append, sort, pop, reverse

**Outcome:** Initially felt impossible, requested code, analyzed solution, understood the pattern

**Key learning:** This was a CODING PUZZLE skill (parsing stdin), not a DATA ANALYSIS skill. Real data analysts work with pandas DataFrames and CSV files, not command-line input parsing.

### Codewars Problems (Multiple - solved independently!)
**Problems solved:**
1. Binary to decimal conversion - learned `int(string, 2)` syntax
2. Multiply array values - learned the accumulator pattern
3. Additional problems (solved on my own after learning accumulator!)

**Major breakthrough:** After getting help on accumulator pattern, solved subsequent problems INDEPENDENTLY. This proved that asking for help on ONE concept enables solving MANY problems.

---

## Challenges Faced & Overcome

### Challenge 1: Filter Criteria Variable Confusion
**Issue:** Didn't understand the pattern of saving filter as a variable first  
**Resolution:** Learned this improves readability and allows reuse  
**Key insight:** Parentheses around each condition are REQUIRED with `&` and `|`

### Challenge 2: Dictionary as Instructions (Not Storage)
**Issue:** Confused by `{'column': 'function'}` syntax in .agg()  
**Resolution:** Understood distinction between dictionaries for storage vs instructions  
**Impact:** Will see this pattern frequently in pandas - now understand it!

### Challenge 3: HackerRank Problem Felt Impossible
**Issue:** Didn't know `.split()` syntax or input parsing patterns  
**Emotional impact:** "Maybe I'm not made for this" spiral  
**Resolution:** Got code, analyzed it, learned the pattern  
**Critical realization:** This was new syntax, not evidence of inability

### Challenge 4: Confidence Crisis
**Trigger:** Hit a problem using techniques never explicitly taught  
**Pattern recognized:** Every time I encounter something new, I spiral into self-doubt  
**Breakthrough insight:** Professional developers:
- Google syntax they've forgotten DAILY
- Look up documentation CONSTANTLY
- Ask for help on new patterns REGULARLY
- Feel confused when learning new things ALWAYS
- They just don't question their entire capability when they don't know something

**Key learning:** "I don't know this YET" ≠ "I can't do this"

### Challenge 5: Accumulator Pattern
**Issue:** Didn't know how to multiply all values in array  
**Resolution:** Learned accumulator pattern (start with initial value, loop and accumulate)  
**Major win:** After learning pattern once, solved multiple problems independently!

---

## Major Wins Today

✅ **Completed entire DataCamp Chapter 1** - Inner joins mastered  
✅ **Created comprehensive practice script** - 8 examples with education data  
✅ **Solved HackerRank problem** - Even though required new syntax  
✅ **Learned accumulator pattern** - Then applied it independently to solve more problems  
✅ **Emotional breakthrough** - Recognized confidence spiral pattern and pushed through  
✅ **Maintained daily habits** - Git commit, learning notes, Jira updates  
✅ **Strategic decision-making** - Moved Chapter 2 to tomorrow for sustainable pace

---

## What's Working Well

✅ **One chapter per day pace** - Sustainable, prevents overwhelm, allows deep learning  
✅ **Asking for appropriate help** - Knowing when to request code vs guidance  
✅ **Systematic approach** - Complete each day fully, create practice scripts, document learning  
✅ **Pattern recognition** - Identifying when I'm spiraling and choosing to push through  
✅ **Applying learned concepts** - Accumulator pattern learned once, used multiple times  
✅ **Strategic flexibility** - Moving tasks between days to maintain quality over rigid schedule

---

## What I'm Proud Of

🎉 **Emotional resilience** - Had a confidence crisis, asked for honest assessment, chose to continue  
🎉 **Learning transfer** - Got help on one problem, solved others independently  
🎉 **Self-awareness** - Recognized the "I'm not made for this" pattern and didn't let it win  
🎉 **Quality over speed** - Chose to move Chapter 2 to maintain learning depth  
🎉 **Problem-solving** - Multiple Codewars problems solved after learning one key pattern

---

## Investigate Further / Revise

### Questions for Future Learning:
1. **What happens if a key exists in df1 but NOT in df2 during inner join?**
   - Those rows are dropped (not included in result)
   - Chapter 2 will cover LEFT JOIN to keep those rows!

2. **When should I use .merge() vs .join()?**
   - Both do similar things, .merge() is more flexible
   - .join() is shorthand for specific merge patterns
   - Will explore difference as I gain experience

3. **What's the difference between `on=` and `left_on=`/`right_on=`?**
   - `on=` when column names are SAME in both DataFrames
   - `left_on=`/`right_on=` when column names DIFFER
   - Can use both! `on=['col1']` with `left_on=['col2']` for mixed scenarios

4. **When should I save filter criteria as a variable vs inline?**
   - Variable: Complex filters, reused filters, improves readability
   - Inline: Simple one-time filters
   - Best practice: Use variables for clarity (even if not reusing)

5. **Why does accumulator pattern start with 1 for multiplication but 0 for addition?**
   - 1 is the "identity" for multiplication (1 × x = x)
   - 0 is the "identity" for addition (0 + x = x)
   - Starting value must not change the first operation

6. **How do I know when to use as_index=False in groupby?**
   - Use it when you want grouped column as regular column (not index)
   - Helpful when you want to do more operations on the result
   - Makes result look more like a "normal" DataFrame

### Syntax to Practice More:
- Multiple column merges with different directions in sort
- Chaining more than 2 merges
- Complex filter criteria with multiple conditions
- Dictionary format in .agg() with multiple functions

### Concepts to Revisit:
- **Filter criteria pattern** - Practice saving as variable, using with .loc
- **One-to-many relationships** - Understanding why row count increases
- **Accumulator pattern** - Practice with different starting values and operations

---

## Tomorrow's Plan (Tuesday, Day 2)

**Main focus:** DataCamp Chapter 2 - Left, Right, Outer, Cross Joins  
**Practice:** Create w2d2-join-comparison.py demonstrating different join types  
**Industry research:** Double session (80 min) - catching up from today  
**Coding practice:** Continue Codewars, focus on pandas-related problems  

**Goal:** Understand WHEN to use each join type and HOW they differ from inner joins

---

## Reflections

### On Today's Emotional Journey:
Started confident → Hit unknown syntax → Spiraled into self-doubt → Got honest feedback → Pushed through → Solved problems independently → Ended strong

**Key realization:** My technical ability is not the issue. My confidence crisis when facing new concepts is the real challenge. Professional developers don't know everything - they know how to learn and when to ask for help.

### On Learning Progress:
Two weeks ago I knew almost no Python. Today I:
- Completed 5 pandas chapters (Chapters 1-4 + Chapter 1 of Joining Data)
- Understand merging, grouping, filtering, aggregating
- Can read and write moderately complex pandas code
- Solved coding problems independently after learning patterns
- Created portfolio-quality practice scripts

**This is objectively excellent progress.** I need to trust the process.

### On the Systematic Approach:
The decision to move Chapter 2 to tomorrow was SMART, not lazy. Quality learning > rigid schedule adherence. One chapter per day = deep understanding. Rushing through multiple chapters = knowledge loss and the exact paralysis pattern I'm trying to avoid.

**The systematic approach is working. I just need to believe in it.**

---

## Key Takeaway
"I don't know this YET" is different from "I can't do this." Every struggle is a normal part of learning, not evidence of failure. Today proved that asking for help on ONE concept enables solving MANY problems independently. That's exactly how learning works.

---

**Day 1 Status: COMPLETE ✅**  
**Mindset for Day 2:** Trust the process, one chapter at a time, struggles are normal  
**Tomorrow's motto:** "I'm learning, not failing"

## Week 2 Day 2 - Tuesday, February 4, 2026

### Today's Accomplishments

**DataCamp:**
- ✅ Completed Joining Data with pandas - Chapter 2 (Left, Right, Outer, Cross Joins)
- ✅ W3Schools practice (done at start of day)

**Practice Script:**
- ✅ Created `w2d2-join-comparison.py` - Student Engagement Analysis by Age Group
- ✅ Used real OULAD dataset (Open University Learning Analytics Dataset)
- ✅ Worked with 7 interconnected tables (114,970+ responses)
- ✅ Demonstrated inner join and left join with real education data
- ✅ Analyzed age groups and online learning engagement

**Industry Research (Double Session - 80 min):**
- ✅ Researched UK education sector trends
- ✅ Found National Literacy Trust as target organization
- ✅ Downloaded full 2025 reading survey report
- ✅ Created summary notes for 2 articles (Tes + NLT)

**Project Organization:**
- ✅ Created new `job-research/` directory structure
- ✅ Set up subdirectories: companies/, job-descriptions/
- ✅ Created first target company notes: National Literacy Trust

**Daily Habits:**
- ✅ GitHub commits
- ✅ DataCamp progress
- ✅ W3Schools practice
- ✅ Learning notes
- ✅ Jira updates

---

### Technical Concepts Learned

#### Join Types Mastered Today:

**Left Join:**
- Keeps ALL rows from left DataFrame
- Adds matching data from right DataFrame
- Non-matching rows get NaN for right columns
- Use when: You want ALL records from primary dataset

**Right Join:**
- Keeps ALL rows from right DataFrame
- Adds matching data from left DataFrame
- Non-matching rows get NaN for left columns
- Use when: You want ALL records from secondary dataset
- **Key insight:** Right joins are just backwards left joins! Most analysts just swap table order and use left join instead

**Outer Join (Full Outer Join):**
- Keeps ALL rows from BOTH DataFrames
- Matches where possible
- NaN where no match exists
- Use when: You want complete picture from both datasets

**Cross Join:**
- Every row in left matched with EVERY row in right
- Creates Cartesian product
- Can create HUGE DataFrames quickly
- Use when: You need all possible combinations

**Self-Join:**
- Joining a table to itself
- Allows comparing rows WITHIN same table by putting them side-by-side
- Example: Matching directors with their crew members
- Use when: Need to compare values in same column to each other

#### Key Understanding:

**WHEN to use each join type is more important than HOW to write the syntax!**

This is about decision-making, not just mechanics.

---

### Important Clarifications Today

#### Inner Joins and Missing Values:
- Inner joins discard rows where JOIN KEY doesn't match
- Missing values (NaN) in OTHER columns are preserved
- The join key must exist in both tables, but other columns can have NaN

#### Multiple Join Keys:
- Join on multiple columns when COMBINATION uniquely identifies a match
- Example: `['country', 'city']` because just 'city' isn't unique
- NOT for handling missing values in join keys

---

### Real-World Project Experience

#### Working with OULAD Dataset:

**Dataset Details:**
- 7 interconnected CSV files
- 114,970 student responses
- Open University Learning Analytics Dataset
- Real academic research data

**Tables Used:**
1. `studentInfo` - Demographics (32,593 students)
2. `studentRegistration` - Enrollment data
3. `studentVle` - 10.6 MILLION click interactions (sampled to 1%)

**Project Approach:**
- Explored all 7 tables first
- Analyzed VLE presentation distribution to decide sampling strategy
- Used random sampling (1% - advanced technique by Claude)
- Performed joins to analyze age vs. engagement

**Key Finding:**
- 55<= age group showed HIGHEST average engagement (29.36 clicks)
- 0-35 age group showed LOWEST average engagement (12.26 clicks)
- BUT recognized need for proper statistical analysis due to outliers

**Statistical Limitations Acknowledged:**
- Large gaps between average and median suggest outliers
- Would need: box plots, standard deviation, significance tests
- Current analysis = preliminary observations only
- Proper validation requires statistical tools (coming in future weeks)

---

### Professional Collaboration Skills

**Today's Workflow:**
- Directed AI assistant to write code with specific requirements
- Made strategic decisions about data sampling
- Requested appropriate level of AI assistance
- Reviewed and understood all generated code
- Created transparent documentation about AI use

**This is realistic portfolio building!** Professional developers:
- Collaborate with colleagues
- Ask for help on specific tasks
- Delegate when appropriate
- Review and understand all code
- Document their process

---

### Industry Research Insights

#### UK Education Sector:

**Reading Crisis Findings:**
- Only 32.7% of children (8-18) enjoy reading - lowest in 20 years
- Daily reading at 18.7% - also lowest ever recorded
- Steepest decline in primary-aged children and boys (11-16)

**National Literacy Trust:**
- Runs Annual Literacy Survey (114,970+ responses in 2025)
- Evidence-based charity approach
- Data-rich organization = potential target employer
- Relevant roles: Data analyst, research analyst, AI strategy

**Connection:** The Tes article about reading pleasure decline is directly supported by NLT's comprehensive survey data

---

### Personal Insights & Reflections

**On Age and Online Learning:**
Created analysis exploring how age relates to online learning engagement as a woman in my 40s retraining through online education. Personal investment in understanding these patterns.

**On Confidence with New Concepts:**
- Right joins were confusing initially
- Understanding they're just "backwards left joins" helped
- Professional analysts rarely use them - just swap tables and use left join!
- This kind of clarification prevents overthinking

**On Statistical Thinking:**
Excellent self-awareness today recognizing that average vs. median gaps suggest outliers. The preliminary findings SUGGEST older students engage more, but proper statistical analysis needed to confirm. This is good scientific thinking!

**On Project Organization:**
Separating learning reflections (personal experience) from industry research notes (external knowledge) is excellent organization. Created new job-research directory to track target companies systematically.

---

### Investigate Further / Revise

**PRIORITY SKILL GAP IDENTIFIED:**
- **Loading multiple CSV files programmatically** (not manually one by one)
- File system operations (`os` module, listing files, path handling)
- Dictionary comprehension for storing multiple DataFrames
- List comprehensions for filtering files

**ACTION:** When I reach DataCamp course on "Importing Data in Python":
- Focus on `os.listdir()`, `os.path.join()`
- Practice loading multiple files in loops
- Understand how to dynamically work with file systems
- Goal: Write exploration scripts like today's independently

**Statistical Analysis Skills:**
- Need to learn: box plots, standard deviation, significance tests
- Coming in future DataCamp courses
- Will return to OULAD dataset with proper tools

**Right Join Understanding:**
- Fully understood now
- They're just backwards left joins
- Most analysts don't use them - swap table order instead

---

### What Went Well

✅ Completed Chapter 2 - all join types understood  
✅ Made strategic decision about sampling approach  
✅ Used real-world dataset with meaningful analysis  
✅ Recognized statistical limitations appropriately  
✅ Created transparent documentation about AI assistance  
✅ Excellent project organization (job-research directory)  
✅ Double industry research session completed  
✅ Found target organization (National Literacy Trust)  
✅ All daily habits maintained 100%  

---

### Challenges & Solutions

**Challenge:** Understanding right joins  
**Solution:** Realized they're just backwards left joins - most analysts just swap tables and use left join instead. This removed confusion!

**Challenge:** Working with 10.6 million row dataset  
**Solution:** Used 1% random sampling (advanced technique by Claude, clearly documented)

**Challenge:** Preliminary findings about age and engagement  
**Solution:** Recognized limitations, acknowledged need for proper statistical analysis, added caveat to script

**Challenge:** Organizing different types of notes  
**Solution:** Created separate directories: learning reflections vs. industry research vs. job research

---

### Tomorrow's Focus (Day 3)

**DataCamp:**
- Chapter 3: Different Join Keys, Semi/Anti Joins
- Start Chapter 4: Concatenating

**Practice:**
- Create w2d3 practice script

**Industry Research:**
- Continue building notes

**Keep in mind:**
- One chapter per day = sustainable pace
- Deep understanding over speed
- Systematic approach prevents knowledge loss

---

### Hours Worked Today
~7 hours ✓

**Breakdown:**
- DataCamp Chapter 2: ~90 min
- Dataset exploration: ~60 min
- Practice script creation & analysis: ~120 min
- Industry research (double session): ~80 min
- Project organization: ~20 min
- Wrap-up: ~30 min

---

### Confidence Level: 8/10

**Why 8/10:**
- ✅ All join types understood (including the confusing right join!)
- ✅ Successfully worked with complex real-world dataset
- ✅ Good statistical thinking (recognizing limitations)
- ✅ Professional collaboration approach
- ✅ Excellent organization and documentation

**What would make it 10/10:**
- Independent ability to load multiple files programmatically
- Statistical analysis skills to properly validate findings
- These are coming in future learning - on track!

---

**Overall: Excellent Day 2! Strong technical progress, professional approach, good self-awareness about limitations, and excellent project organization. The systematic approach is working perfectly!** 💪

# Week 2 Day 3 - Learning Notes

**Date:** Wednesday, February 5, 2026  
**Focus:** Joining Data with pandas - Chapter 3 (Different Join Keys, Semi/Anti Joins, Concatenation)  
**Hours Worked:** ~8 hours  
**Status:** ✅ All objectives complete

---

## 📚 What I Learned Today

### pandas Chapter 3 Concepts Mastered

**1. Merging on Different Column Names**

When join keys have different names in each DataFrame, use `left_on` and `right_on`:

```python
df1.merge(df2, left_on='student_id', right_on='id', how='inner')
```

**Important:** This creates BOTH columns in the result - you may need to drop one afterward.

**2. Merging on Multiple Columns**

Can merge on combinations of columns:

```python
df1.merge(df2, on=['code_module', 'code_presentation'], how='left')
```

This is useful when a single column isn't unique but the combination is.

**3. Semi Joins - "Filter Based on Match"**

**What it does:** Returns rows from left table that HAVE a match in right table, but ONLY left table columns.

**Use case:** "Show me students who submitted at least one assessment" (student data only, not assessment details)

**How to do it in pandas:**
```python
students_who_submitted = students[students['id'].isin(assessments['student_id'])]
```

**Key insight:** This is a FILTERING operation, not a data combining operation. You don't get any columns from the right table.

**4. Anti Joins - "Filter Based on NO Match"**

**What it does:** Returns rows from left table that DON'T have a match in right table.

**Use case:** "Show me students who NEVER submitted any assessments"

**How to do it in pandas:**
```python
students_no_submission = students[~students['id'].isin(assessments['student_id'])]
```

**The `~` operator:** Negates the boolean (flips True/False)

**5. Concatenating DataFrames Vertically**

**What it does:** Stacks rows from multiple DataFrames on top of each other.

```python
# Basic concatenation
combined = pd.concat([df1, df2, df3])

# With clean index (recommended!)
combined = pd.concat([df1, df2, df3], ignore_index=True)
```

**`ignore_index=True`:** Creates new sequential index (0, 1, 2, 3...) instead of keeping original indexes (which could have duplicates).

**When to use:** Combining data from same structure but different sources (e.g., student data from multiple years).

---

## 💻 Coding Practice Insights

### Solved Problems:

1. **Rock Paper Scissors function** - Used dictionary to store winning combinations instead of multiple if statements (cleaner!)
2. **Find needle in haystack** - Learned difference between `print()` vs `return` (again!)
3. **Split and join strings** - Missing `return` statement caused `None` output

### Key Learning: `print()` vs `return`

**`print()`** = Shows output on screen FOR YOU  
**`return`** = Sends value back to code FOR THE PROGRAM

**Tests always check return values!** If you print without returning, tests get `None`.

This is my second time making this mistake - need to remember: **Functions that produce results need `return`!**

### Dictionary Lookup Pattern

When you have `winning_moves[p1]`:
1. **Left side (`winning_moves`):** The dictionary
2. **Square brackets `[p1]`:** Subsetting/lookup operation  
3. **Inside brackets (`p1`):** The key
4. **Returns:** The value for that key

This is just like `df['column']` or `my_list[0]` - subsetting works the same way!

---

## 🎯 Practice Script: Student Unregistration Analysis

### What I Created:

Comprehensive analysis of OULAD (Open University Learning Analytics Dataset) examining:
- WHO unregisters (demographics)
- WHEN they unregister (timing patterns)
- WHICH courses have high dropout rates
- Comparing students who DID vs DIDN'T submit assessments before dropping

### Concepts Demonstrated:

✅ **Different join keys:** Merged using `code_module + code_presentation` together  
✅ **Semi join:** Filtered dropouts who exist in assessment submissions  
✅ **Anti join:** Filtered dropouts who DON'T exist in assessment submissions  
✅ **Multiple sequential merges:** studentInfo → studentRegistration → courses  
✅ **Left joins:** Added course and assessment details  

### Research Questions Explored:

**Part 1 - Dropout Profile:**
- Timing: When do students typically drop out?
- Courses: Which courses have highest dropout rates?
- Demographics: Any patterns by age, gender, education, disability?

**Part 2 - Engagement Comparison:**
- What % of dropouts submitted assessments?
- How do demographics differ between submitters vs non-submitters?
- For submitters: What assessment types? How many? What scores?

### Key Insight from Analysis:

**Understanding WHEN to use each join type is more important than HOW to write the syntax.**

- **Semi/Anti joins** = Filtering operations (asking "does it exist?")
- **Regular joins** = Data combining operations (adding columns from both tables)

### Technical Challenge Solved:

**Error:** `KeyError: 'code_module'` 

**Cause:** After merging studentInfo + studentRegistration, both had `code_module` columns, so pandas added suffixes (`_info` and `_reg`).

**Solution:** Use `left_on` and `right_on` to specify which suffixed version to use:
```python
df.merge(courses, left_on=['code_module_info', 'code_presentation_info'], 
         right_on=['code_module', 'code_presentation'], how='left')
```

**Lesson:** Pay attention to column name conflicts when merging!

---

## 📰 Industry Research

### Article 1: Digital Maturity in Education (Tes)

**Source:** Tes, February 4, 2026  
**Author:** Shoaib Raza (senior international leader)

**Main Point:** Education needs to shift from teaching "digital literacy" (HOW to use technology) to "digital maturity" (WHEN to use technology) because of AI proliferation.

**Why This Matters:**
- Shows UK education sector thinking strategically about AI
- "Digital maturity" = new framework I can reference in interviews
- Clear data opportunity: How do you MEASURE digital maturity?
- This is mainstream thinking (published in Tes), not fringe

**For My Job Search:**
- Language to use: "digital maturity" not just "digital literacy"
- Potential to develop assessment tools/analytics for measuring this
- Validates focus on education sector for AI strategy roles

### Article 2: 5 UK EdTech Startups (Career Teachers)

**Companies Identified:**

1. **Century Tech** - AI-powered personalized learning, automates homework/marking, provides student data
2. **Lexplore** - AI + eye-tracking for reading assessment, addresses UK literacy crisis
3. **Peergrade** - Peer feedback platform with teacher analytics dashboard
4. **Firefly** - All-in-one teacher portal, 2/3 of UK independent schools use it
5. **Mondly** - AR/VR language learning

**Target Companies for Job Search:**
- **Century Tech** ← Heavy AI/data focus!
- **Lexplore** ← Heavy AI/data focus!

Both are UK EdTech companies solving real educational problems with data analytics - perfect fit for my background and goals.

---

## 🎓 What Went Well

✅ **Chapter 3 completed** - Semi/anti joins make sense now!  
✅ **DataCamp explanation was poor** - but I asked for help and got clear explanations  
✅ **Practice script is comprehensive** - Real research questions, professional collaboration approach  
✅ **Coding practice** - Solved multiple problems, reinforced `return` vs `print`  
✅ **Industry research** - Found 2 target companies (Century, Lexplore)  
✅ **Strategic thinking** - Used EdTech list to identify data-heavy companies  
✅ **All 5 daily habits maintained** - 100% compliance continues!  

---

## 💪 Challenges Overcome

**1. DataCamp's Poor Explanation of `indicator=True`**

DataCamp used `indicator=True` in merge without explaining it first. Had to ask Claude what it does.

**What I learned:** `indicator=True` automatically creates a `_merge` column showing where each row came from:
- `'left_only'` = Row only in left table
- `'right_only'` = Row only in right table  
- `'both'` = Row matched in both tables

This is useful for data quality checks!

**2. KeyError with Column Names After Merge**

When merging tables with same column names, pandas adds suffixes. Need to use `left_on`/`right_on` to specify which version.

**3. Syntax Issues in Coding Practice**

Made `return` vs `print` mistake again - but caught it faster this time and understood WHY tests were failing.

**4. Understanding Semi/Anti Joins Conceptually**

Initially confused about why you'd want "just the left table columns" - Claude's explanation about FILTERING vs COMBINING clicked.

---

## 🔍 Investigate Further / Revise

### Technical Concepts to Revisit:

1. **Column name conflicts in merges** - Practice more scenarios where both tables have overlapping columns
2. **When to use ignore_index=True** - Understand all implications of keeping vs. resetting indexes
3. **Dictionary lookup syntax** - Keep practicing `dict[key]` pattern until it's automatic
4. **`~` operator for negation** - Practice using this in different boolean contexts

### Industry Research Follow-up:

1. **Century Tech & Lexplore** - Create detailed company research files
   - Check their LinkedIn for data analyst job postings
   - Research their tech stack
   - Look for recent news/funding rounds
   
2. **Digital maturity measurement** - How would you actually measure this? 
   - What metrics distinguish mature vs immature digital decision-making?
   - Are there existing frameworks?
   - Research opportunity for future exploration

3. **Data integration research** - Scheduled for tomorrow
   - How UK schools integrate data across systems (SIMS, Google Classroom, etc.)
   - How publishers integrate editorial/sales/production data
   - Common data integration challenges in both sectors

### Skills to Practice:

1. **More semi/anti join scenarios** - Practice identifying when these are appropriate vs regular joins
2. **Complex multi-table merges** - Work through scenarios requiring 4+ table joins
3. **Return statements in functions** - Write 10 simple functions to reinforce this pattern

---

## 📊 Day 3 Statistics

**DataCamp:** Chapter 3 complete (Different Join Keys, Semi/Anti Joins, Concatenation)  
**W3Schools:** Practice exercises complete  
**Coding Practice:** 3+ problems solved (Codewars/HackerRank)  
**Practice Script:** w2d3-unregistration-analysis.py (350+ lines, comprehensive analysis)  
**Industry Research:** 2 articles, 5 companies identified, 2 targets selected  
**Git Commits:** Pending (end of day)  
**Jira Updates:** Pending (end of day)  

**Hours:** ~8 hours total  
**Daily Habits:** 5/5 complete ✅

---

## 💭 Reflections

**What I'm Learning About My Process:**

Today reinforced that **asking for help when DataCamp is unclear is the RIGHT approach** - not a sign of weakness. DataCamp used `indicator=True` without explanation, I asked, got clarity, moved forward. This is how professional developers work!

**Pattern Recognition:**

I'm getting faster at recognizing when I need different types of joins. The decision tree is becoming clearer:
- Need data from both tables? → Regular join
- Just checking if match exists? → Semi/anti join
- Stacking similar data? → Concatenation

**Confidence Building:**

Made the `print` vs `return` mistake again, but this time I:
1. Recognized the error pattern faster
2. Understood WHY it failed (tests check return values)
3. Fixed it immediately
4. Documented the lesson

This shows I'm learning from mistakes, not just repeating them.

**Strategic Thinking:**

Using the EdTech article to identify data-heavy companies (Century, Lexplore) shows I'm thinking strategically about job search, not just consuming information. This is exactly the kind of targeted research that will help in applications.

---

## ✅ Tomorrow's Focus (Day 4)

**Planned Activities:**
- DataCamp: Joining Data with pandas - Chapter 4 (final chapter!)
- Practice script demonstrating Chapter 4 concepts
- Continue industry research (data integration in target sectors)
- Coding practice
- All daily habits

**Key Goal:** Complete the entire "Joining Data with pandas" course by end of Day 4!

---

**End of Day 3 - Excellent Progress! 🚀**