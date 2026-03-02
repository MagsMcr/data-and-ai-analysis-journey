# Week 3 Reflections
## Data Cleaning & Portfolio Building
**Dates:** February 9-13, 2026
**Course:** Data Cleaning in Python (DataCamp)

---

## DAY 1 - Tuesday, February 11, 2026
*(Note: Calendar Day 2 of the week, but treated as Program Day 1)*

### What I Worked On Today
- DataCamp: Data Cleaning in Python - Chapter 1
- Built first portfolio-oriented practice script: `w3d1-calorie-knowledge.py`
- Dataset: Food Choices of College Students (Kaggle)
- Codewars coding challenges (Python fundamentals practice)

---

### Key Concepts Learned

#### Data Cleaning Fundamentals (Chapter 1)

**Data Type Conversions:**
```python
df['col'].astype('int')           # Convert to integer
df['col'].astype('float')         # Convert to float
df['col'].astype('category')      # Convert to category (saves memory)
pd.to_numeric(df['col'], errors='coerce')  # Safe conversion, NaN for errors
pd.to_datetime(df['col'])         # Convert to datetime
pd.to_datetime(df['col']).dt.date # Extract date only (ATTRIBUTE - no parentheses!)
```

**String Cleaning:**
```python
df['col'].str.strip()             # Remove whitespace both ends
df['col'].str.lstrip()            # Remove whitespace left only
df['col'].str.rstrip()            # Remove whitespace right only
df['col'].str.lower()             # Convert to lowercase
df['col'].str.upper()             # Convert to uppercase
df['col'].str.replace('old', 'new')  # Replace substring
```

**Handling Missing Data:**
```python
df['col'].isna()                  # Check for missing (returns Boolean)
df.dropna()                       # Drop rows with ANY missing values
df.dropna(subset=['col'])         # Drop rows missing in specific column
df['col'].fillna(value)           # Fill with specific value
df['col'].fillna(method='ffill')  # Forward fill
df['col'].fillna(method='bfill')  # Backward fill
df['col'].fillna(df['col'].mean()) # Fill with mean
```

**Handling Duplicates:**
```python
df.duplicated()                   # Boolean - True for duplicates
df.duplicated(subset='col')       # Check specific column only
df.duplicated(keep='last')        # Mark all but last as duplicate
df.duplicated(keep=False)         # Mark ALL duplicates as True
df.drop_duplicates()              # Remove duplicates (keep first)
df.drop_duplicates(subset='col')  # Based on specific column
df.drop_duplicates(inplace=True)  # Modify DataFrame directly (no reassignment)
```

**Data Validation with Assert:**
```python
assert df.duplicated().sum() == 0        # Verify no duplicates
assert df['age'].max() <= 100            # Verify valid range
assert df['col'].dtype == 'float64'      # Verify data type
assert set(df['col'].unique()) == {'a', 'b'}  # Verify allowed values
# Note: Assert STOPS execution if condition is False - use for critical checks!
```

#### New Methods Learned Today

**`.isin()` with `~` NOT operator:**
```python
# Keep rows where value is NOT in a list
df = df.loc[~df['col'].isin(['bad_value1', 'bad_value2'])]
# ~ flips the Boolean (NOT operator)
# .isin() checks if value is in list → True/False
```

**`.cat` accessor for categorical columns:**
```python
# Similar to .str for strings, .dt for dates
df['col'].cat.rename_categories({1: 'Female', 2: 'Male'})
df['col'].cat.categories     # View category labels
df['col'].cat.codes          # View underlying codes
```

**`pd.cut()` for creating groups from continuous data:**
```python
gpa_bins = [0, 2.5, 3.0, 3.5, 4.0]
gpa_labels = ['Below 2.5', '2.5-3.0', '3.0-3.5', '3.5-4.0']
df['GPA_group'] = pd.cut(df['GPA'],
                          bins=gpa_bins,
                          labels=gpa_labels,
                          include_lowest=True)
```

**f-strings (new Python concept):**
```python
# Clean way to mix text and variables in print statements
name = "Magda"
score = 3.75
print(f"Student {name} scored {score}")  # Student Magda scored 3.75
# Put f before quote, variables/expressions inside {}
```

**`.query()` method:**
```python
df.query('Age > 25')                    # Numerical condition
df.query('Gender == "Female"')          # String condition
df.query('Age > 25 and GPA >= 3.0')    # Multiple conditions
# Alternative to .loc[] for simple, readable conditions
# .loc[] is better for complex conditions involving .isin() etc.
```

**`inplace=True` parameter:**
```python
df.drop_duplicates(inplace=True)  # Modifies DataFrame directly
df.dropna(inplace=True)           # No need to reassign!
# Available on many pandas methods
# Alternative to: df = df.drop_duplicates()
```

---

### Professional Workflow Insights

#### On Observation Before Cleaning
Learned the importance of **observing ALL data quality issues first** before
fixing anything. This gives you the full picture and helps you understand
relationships between problems before acting.

Professional workflow:
1. Inspect entire dataset (`.info()`, `.head()`, `.describe()`)
2. Document all issues systematically
3. Define analysis scope (what columns do you actually need?)
4. Clean ONLY what you need for the specific question
5. Then analyse

#### On Redundant Code
Challenged myself to think critically about **when code adds value vs. when
it's redundant**. Example: `.dtypes` is redundant after `.info()` because
`.info()` already shows data types. Professional coding means avoiding
unnecessary repetition.

However, some "redundant" checks are worth keeping for:
- Portfolio demonstration purposes
- Standard practice in larger datasets
- Future-proofing when dataset size changes

#### On Scope Definition
Real-world analysts don't clean everything - they define a research question
first, then clean only the relevant columns. With 61 columns, cleaning
everything without purpose would be wasteful and unfocused.

#### On Missing Value Percentages
Percentages matter more in larger datasets. With only 125 rows:
- 2 missing = 1.6% (obviously tiny from count alone)
- In a 100,000-row dataset: 2,000 missing = also 2% but much harder to
  judge from count alone

#### On `.query()` vs `.loc[]`
- `.query()` is cleaner for simple numerical or string conditions
- `.loc[]` is more powerful for complex filtering (e.g., combined with `.isin()`)
- Choose based on what makes code most readable

---

### Methodological Concepts

#### Descriptive vs Statistical Analysis
Learned important distinction between:
- **Descriptive analysis**: Observing patterns, calculating averages,
  comparing groups - NO statistical claims
- **Statistical analysis**: Hypothesis testing, correlation coefficients,
  p-values, confidence intervals (Week 7+)

Using "relate" rather than "correlate" when describing patterns without
formal statistical testing is more methodologically precise.

#### Why Float vs Integer for GPA
GPA requires float because values have meaningful decimal places (3.654).
Even whole number GPAs (4.0) should be stored as float for consistency
with the scale. Integers would lose information.

#### Pandas NaN Behaviour
**Important pandas behaviour:** When a column contains NaN values, pandas
automatically stores it as float64 because integers cannot represent NaN.
Once NaN values are removed, the column can safely be converted to int64.

---

### Coding Practice (Codewars)

**Key patterns practiced:**

**Reversing a sequence:**
```python
# Long way (loop):
def reverse_seq(n):
    result = []
    for x in range(n, 0, -1):
        result.append(x)
    return result

# Short way (Pythonic):
def reverse_seq(n):
    return list(range(n, 0, -1))
```

**Inverting a list (additive inverse):**
```python
def invert(lst):
    return [-x for x in lst]  # List comprehension
# Key: use -x or x * -1 (NOT x**-1 which gives reciprocal!)
```

**range() with step parameter:**
```python
range(start, stop, step)
range(5, 0, -1)    # 5, 4, 3, 2, 1  (count down)
range(10, 0, -2)   # 10, 8, 6, 4, 2 (count down by 2)
# Default step is +1 (counts UP)
```

---

### Common Mistakes Made Today

1. **Wrong operator for sign flipping:** Used `x**-1` (reciprocal) instead
   of `-x` or `x * -1` (additive inverse)

2. **Assigning whole DataFrame to single column:**
   ```python
   # WRONG:
   df['col'] = df.loc[condition]  # Right side is whole DataFrame!
   # CORRECT:
   df = df.loc[condition]         # Reassign whole DataFrame
   ```

3. **Nesting too much inside `.dropna()`:**
   ```python
   # WRONG (overcomplicated):
   df.dropna(subset=[df.loc[df['col'].isna()]])
   # CORRECT (simple):
   df.dropna(subset=['col1', 'col2'])
   ```

4. **Variable naming inconsistency:** Used `calorie_df` and `calories_df`
   interchangeably - caused NameError. Always check naming is consistent!

---

### Portfolio Project Progress

**Script created:** `w3d1-calorie-knowledge.py`

**Analysis:** Calorie Estimation Accuracy Among College Students

**Research question:**
"What is the relationship between demographic factors (gender, GPA)
and nutritional knowledge among college students?"

**Dataset cleaned from 125 → 119 rows:**
- Removed 2 rows: invalid GPA text ('Personal ', 'Unknown')
- Salvaged 1 row: cleaned '3.79 bitch' → '3.79'
- Removed 2 rows: NaN GPA values
- Removed 1 row: duplicate
- Removed 1 row: missing calorie values

**Future project directions identified (planned for end-of-week portfolio session):**
1. Gender Health Behaviors - "Do dietary patterns differ by gender?"
2. Grade Level Progression - "How do eating habits change through college?"
3. Living Situation Impact - "How does where students live affect eating habits?"

---

### Investigate Further / Revise

- [ ] **List comprehensions** - used today but want to understand fully:
      `[-x for x in lst]` - what exactly is happening here?
- [ ] **`pd.cut()` parameters** - `include_lowest=True` - what does this do
      exactly? What happens without it?
- [ ] **`.cat` accessor** - explore other `.cat` methods beyond
      `.rename_categories()`
- [ ] **`inplace=True`** - are there situations where it behaves differently
      than reassignment? Any gotchas?
- [ ] **NLP methods** - dataset has several open-ended text columns flagged
      as "perfect for NLP" - research what NLP actually involves in practice
- [ ] **Statistical testing** - understand what tests would be appropriate
      for this dataset when Week 7 statistics skills are acquired

---

### Hours Today
Approximately 8 hours (full day including Codewars practice)

### Daily Habits Completed
- [x] DataCamp: Data Cleaning in Python - Chapter 1
- [x] Codewars: Coding practice (reverse_seq, invert)
- [x] Practice script: w3d1-calorie-knowledge.py created and committed
- [x] Learning notes: This document
- [x] GitHub commit: All work committed
- [x] Jira: Tasks updated

---

*Next: Day 2 - Chapter 2 (Handling Missing Data) + w3d2 practice script*

# Week 3 Day 2 - Learning Reflections
**Date:** Thursday, February 12, 2026
**Focus:** Data Cleaning Chapter 2 + Practice Script + AI Collaboration Insights

---

## DataCamp Chapter 2 - Key Concepts

### Membership Constraints
Validating that column values belong to a predefined set of acceptable values.
- Think of it as a guest list - if a value isn't on the list, it doesn't belong
- `.unique()` - check what values actually exist
- `.isin(valid_list)` - check which rows have valid values
- `~df["col"].isin(valid_list)` - find rows with INVALID values (~ flips True/False)

```python
valid_genders = [1, 2]
invalid = df[~df["Gender"].isin(valid_genders)]
df = df[df["Gender"].isin(valid_genders)]  # keep only valid
```

### Dictionary Mapping with `.replace()`
Collapsing or converting categorical values using a dictionary.

```python
gender_map = {1: "Female", 2: "Male"}
df["Gender"] = df["Gender"].replace(gender_map)
```

### Binning Continuous Data with `pd.cut()`
Creating meaningful categories from numeric ranges.

```python
df["exercise_group"] = pd.cut(df["exercise"],
                               bins=[0, 2, 3, 5],
                               labels=["Active", "Moderate", "Inactive"])
```
- Bins are exclusive on the left, inclusive on the right - so (0, 2] captures 1 and 2
- Returns category dtype automatically

### String Methods
- `.str.contains("pattern")` - Boolean check for pattern in strings
- `.str.len()` - length of each string value
- `.str.replace("old", "new")` - remove or replace text
- `.str.strip()` - remove leading/trailing whitespace
- `.str.lower()` / `.str.upper()` / `.str.title()` - case standardisation

### CRITICAL: Column Assignment Pattern
The most important technical insight from Chapter 2:

```python
# CORRECT:
df["col"] = df["col"].str.strip()          # column = transformed column
df = df[df["age"] > 18]                    # DataFrame = filtered DataFrame

# WRONG - overwrites entire DataFrame with a Series:
df = df["col"].str.strip()
```

Left side and right side must match - column on left = column transformation on right.
DataFrame on left = DataFrame operation on right.

### DataCamp Video Error Spotted
The Chapter 2 video showed `demographics = demographics['marriage_status'].str.strip()` - 
this is incorrect. Should be `demographics['marriage_status'] = demographics['marriage_status'].str.strip()`.
Spotting this kind of inconsistency between video instruction and exercise is good analytical instinct.

---

## Practice Script - w3d2-exercise-food-choices.py

**Research question:** "Do students who exercise more frequently make different food choices?"

**Key decisions made:**
- Dropped GPA from column selection - not relevant to research question (good methodological call)
- Skipped string cleaning on Gender after `.replace()` mapping - value_counts() proved it was unnecessary
- Retained empty "Inactive" exercise category rather than quietly removing it - honest analysis
- Added `nutritional_check_group` binning as it enables meaningful comparison with exercise_group

**Notable finding:** No students reported exercising rarely or never (values 4-5 absent). Self-reporting bias - students likely over-report exercise frequency in survey contexts. This became a documented limitation rather than something to hide.

**Script structure:** 8 sections including assert verification statements, correlation matrix, cross-tabulations, pivot tables, and 3 visualisations (bar chart, side-by-side bars, histogram).

**Visualisations used:** Bar charts and histograms - within current skill level. Heatmap flagged for Week 6 when seaborn is covered.

---

## Investigate Further

### On Prompting & AI Collaboration

**Communication style as a technical skill:**
Today's session surfaced something important about working with AI models. The switch to Opus mid-session introduced a "structured editorial" communication style that carried over into this Sonnet session via the handover document. This happened because the handover explicitly documented formatting preferences established in Opus, and Sonnet adopted them without flagging the change.

Key insight: handover documents don't just transfer factual context - they transfer *interaction patterns*. Being aware of this is genuinely useful for future AI product/strategy work.

**The overcorrection problem:**
When asked to return to a leaner style, the initial overcorrection went too far in the opposite direction - purely transactional, no initiative, waiting to be told next steps. This showed that "no cheerleading" and "no warmth" are not the same instruction. Worth remembering when prompting: be specific about what you don't want rather than leaving it open to interpretation.

**What the preferred style actually is:**
- Direct and honest, not performative
- Takes initiative (anticipates next steps, tracks session progress)
- Warmth without coddling - these are genuinely different things
- Emojis acceptable when natural, not as punctuation to every sentence
- Short labelled sections with inline code examples for technical explanations
- Momentum kept through a session, not just responding to individual queries

**Prompting observation worth developing:**
There's a pattern across sessions where the ideal collaboration style became clearer through noticing what wasn't working rather than being able to articulate it upfront. This is actually a sophisticated prompting skill - knowing how to diagnose and course-correct mid-session. Worth developing more intentionally.

### On Model Selection

**When to use which model:**
- Sonnet: daily learning sessions, practice scripts, step-by-step guidance, routine tasks
- Opus: complex strategic analysis, article verification, conceptually dense material, portfolio planning

**The costly lesson:**
Switching to Opus for a full day session drained usage limits significantly and disrupted established collaborative flow. The session rapport built over a month is carried partly in memory and partly in interaction texture - handover docs capture the former but not the latter. Rebuilding takes time.

**Practical rule going forward:**
Default to Sonnet. Switch to Opus for specific high-complexity tasks, then switch back. Don't use Opus as a daily driver.

---

## AI Industry Discussion - Matt Shumer Article

**Article:** "Something Big Is Happening" (~50M views)

**Verified claims:**
- GPT-5.3 Codex and Opus 4.6 launched February 5, 2026
- OpenAI confirmed GPT-5.3-Codex was "instrumental in creating itself"
- Dario Amodei predicted 50% of entry-level white-collar jobs eliminated within 1-5 years
- METR benchmark showing task-completion time doubling every ~7 months is real research

**Exaggerations identified:**
- METR benchmark is 50% success rate on primarily coding tasks - not general tasks
- Adoption speed overstated (Amodei predicted 90% AI-written code at Anthropic by end 2025 - true there, but only 25-40% at most companies)
- Shumer has financial incentive as AI startup CEO and investor

**Conclusion for the programme:**
Direction of AI disruption is real, timeline is debatable. No radical pivot needed. Slight emphasis shift: less syntax memorisation, more focus on analytical judgment. The strategic layer - framing questions, evaluating methodology, making decisions about scope - is hardest to automate and is already a demonstrated strength.

---

## Personal Development Notes

**Strengths demonstrated today:**
- Questioned GPA inclusion before being prompted - good methodological instinct
- Challenged redundant string cleaning step with evidence (value_counts output)
- Spotted self-reporting bias in exercise data independently
- Noticed and articulated the communication style shift clearly
- Identified the warmth/coddling distinction - nuanced observation

**Pattern to watch:**
Tendency to lose perspective on simple problems after extended focus - the contamination Codewars problem is an example. When stuck, stepping back to ask "is there a simpler approach entirely?" is more efficient than pushing harder on the current approach.

**Bigger picture:**
The ability to notice what kind of collaboration is and isn't working, articulate it precisely, and course-correct mid-session is a genuine skill. It's also exactly the kind of human judgment layer that matters in AI strategy roles - knowing how to direct, evaluate, and calibrate AI output rather than just consuming it.

---

## Daily Habits Completed
- [x] DataCamp Chapter 2
- [x] W3Schools practice
- [x] Practice script: w3d2-exercise-food-choices.py
- [x] Coding practice (Codewars x2)
- [ ] Git commit - TO DO
- [ ] Jira update - TO DO
- [ ] Week3-reflections.md - THIS FILE