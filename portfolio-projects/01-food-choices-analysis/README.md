# Food Choices & Nutrition Analysis

**College Student Health Behaviors and Nutrition Knowledge**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![pandas](https://img.shields.io/badge/pandas-2.0+-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 📊 Project Overview

### The Challenge
Do college students understand basic nutrition? Can they estimate their daily calorie intake? This two-part analysis investigates nutrition knowledge and eating behaviors among 125 college students using messy, real-world survey data.

### Key Findings
- **77% of students** cannot estimate their daily calorie intake
- **Zero students** reported "never exercising" despite anonymous survey (revealing systematic self-reporting bias)
- Students whose parents cook frequently show **lower** calorie awareness (counter-intuitive finding)
- Exercise frequency shows associations with vegetable consumption and health perceptions

---

## 🎯 Business Value

**For Campus Health Programs:**
- Identifies significant gaps in basic nutrition literacy (77% cannot estimate calories)
- Reveals self-reporting bias in health behavior surveys (affects program evaluation)
- Suggests engagement-based interventions more effective than passive exposure

**For Education Research:**
- Demonstrates importance of data quality assessment before analysis
- Shows value of exploratory analysis for hypothesis generation
- Highlights need for longitudinal data to understand causation

---

## 📁 Project Structure

This analysis consists of two complementary scripts:

### Part 1: Calorie Knowledge Analysis
**File:** [`w3d1-calorie-knowledge.py`](w3d1-calorie-knowledge.py)

**Research questions:**
- What proportion of students can estimate their calorie intake?
- Does knowledge differ by gender or year in school?
- How does parental cooking frequency relate to nutrition knowledge?

**Sample size:** 125 → 119 students (after removing missing data)

**Key finding:** Only 23% could estimate daily calories within reasonable range (1,600-2,400)

---

### Part 2: Exercise & Eating Habits
**File:** [`w3d2-exercise-habits.py`](w3d2-exercise-habits.py)

**Research questions:**
- Do students who exercise more make different food choices?
- How does exercise relate to perceptions of healthy eating?
- What patterns exist in self-reported health behaviors?

**Sample size:** 125 → 109 students (after removing missing exercise/cooking data)

**Key finding:** Self-reporting bias detected - no students reported "never exercising" despite anonymous survey

**Visualizations:**
- [Food choices by exercise frequency](w3d2-plot1-food-by-exercise.png)
- [Healthy eating perceptions](w3d2-plot2-healthy-feeling.png)
- [Health perception distribution](w3d2-plot3-healthy-histogram.png)

---

## 🛠️ Technical Approach

### Dataset
- **Source:** Kaggle - Food Choices of College Students
- **Format:** Survey responses (125 students, 61 variables)
- **Characteristics:** Deliberately messy real-world data
  - Mixed data types (categorical, numerical, text)
  - Missing values across multiple variables
  - Inconsistent response formats
  - Special character encoding issues

### Data Cleaning Pipeline

**Part 1 (Calorie Knowledge):**
1. Subset to 9 relevant columns (gender, year, calories_day, parents_cook, etc.)
2. Handle missing data: Drop 6 rows with NaN in key variables (125 → 119)
3. Type conversion: Map gender codes (1/2) to labels (Male/Female)
4. Text standardization: Clean year-in-school responses
5. Categorical mapping: Transform numeric codes to readable categories

**Part 2 (Exercise Habits):**
1. Subset to 8 columns (exercise, cooking_frequency, healthy_feeling, etc.)
2. Drop 16 rows with missing exercise/cooking data (125 → 109)
3. Map gender codes to labels
4. Validate and clean categorical variables
5. Create exercise frequency bins for analysis
6. Generate visualizations using matplotlib

### Technologies
```python
# Core libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

**Skills demonstrated:**
- Data cleaning and validation
- Missing data handling (`.dropna()`, `.isna()`)
- Type conversion (`.astype()`, `.replace()`)
- Text standardization (`.str` methods)
- Boolean filtering and subsetting
- Categorical data analysis
- Data visualization (matplotlib)
- Statistical exploration (`.groupby()`, `.value_counts()`)

---

## 📈 Methodology

### Sample Size Decisions
- **Deliberate choice** to drop rows with missing data rather than impute
- Justification: Small dataset (125 rows) + exploratory analysis + no strong theory to guide imputation
- Alternative: Could use mean/median imputation (demonstrated understanding but chose conservative approach)

### Classification Approach
**Calorie knowledge definition:**
- "Knows calories" = Estimate within 1,600-2,400 range
- Based on USDA guidelines for adults
- Binary classification simplifies analysis but may miss nuances

### Statistical Rigor
**Important caveat:** This is exploratory analysis, not confirmatory research.

**What this analysis does:**
- Identifies patterns and associations
- Generates hypotheses for future testing
- Demonstrates data cleaning and exploration skills

**What this analysis does NOT claim:**
- Statistical significance (no hypothesis tests performed)
- Causation (cross-sectional data, no controls for confounding)
- Generalizability (convenience sample, small n)

**Next steps for rigorous analysis:**
- Chi-square tests for categorical relationships
- Logistic regression controlling for confounders
- Larger sample size for subgroup comparisons
- Longitudinal design for causal inference

---

## 🔍 Key Insights

### 1. Widespread Nutrition Illiteracy
77% of college students cannot estimate their daily calorie intake - a fundamental metric for nutrition awareness.

**Implication:** Campus health programs may need to start with more basic nutrition education than currently assumed.

### 2. Self-Reporting Bias in Health Surveys
Despite anonymous survey design, **zero students** reported never exercising. This is statistically implausible given:
- National data showing ~25% of college students are physically inactive
- Anonymous survey format (no social pressure)
- Other health behaviors showing normal variance

**Implication:** Self-reported health behavior data may systematically overestimate healthy behaviors, affecting program evaluation validity.

### 3. Engagement vs. Exposure
Counter-intuitively, students whose parents cook very frequently (5-7x/week) showed **lower** calorie awareness than those with moderate parental cooking (1-2x/week).

**Hypothesis:** Active engagement with food choices matters more than passive exposure. Students who rely entirely on parents for meal preparation may not develop personal nutrition knowledge.

---

## 💡 Lessons Learned

### Technical
- Real-world survey data requires extensive cleaning before analysis
- Always check data types early (`.info()` catches type mismatches)
- Document cleaning decisions explicitly (reproducibility)
- Missing data strategy should align with research goals

### Analytical
- Exploratory analysis is valuable for hypothesis generation
- Transparency about limitations builds credibility
- Unexpected patterns (self-reporting bias) often most interesting findings
- Simple visualizations can reveal complex patterns

### Professional
- Clear documentation enables stakeholder understanding
- Business context (campus health programs) frames technical work
- Honest assessment of statistical limitations demonstrates rigor
- AI collaboration transparency reflects real-world work practices

---

## 🤖 AI Collaboration Statement

This analysis was developed with assistance from Claude (Anthropic AI).

**Division of responsibilities:**
- **Human (Magda):** Research questions, analytical decisions, data interpretation, methodology choices, statistical caveats
- **AI (Claude):** Code syntax guidance, pandas method suggestions, documentation structure, methodological discussion

**All code reviewed and approved by human analyst.** This collaboration approach reflects how data analysts work with AI tools in professional settings - using AI for technical support while maintaining human judgment for analytical decisions.

---

## 📂 Repository Context

This project is part of an 18-week data analysis career development program documenting the transition from business development to data analyst roles.

**Learning objectives demonstrated:**
- Week 3: Data cleaning and missing data handling
- pandas methods: subsetting, type conversion, categorical mapping
- Data validation and quality assessment
- Professional documentation practices
- Transparent AI collaboration

**View complete learning journey:** [Main Repository](https://github.com/MagsMcr/data-and-ai-analysis-journey)

---

## 📫 Contact

**Author:** Magda McCrimmon  
**GitHub:** [@MagsMcr](https://github.com/MagsMcr)  
**Focus:** Transitioning to AI Strategy/Product roles in education sector

---

*Analysis completed: February 2026 | Dataset: Kaggle Food Choices | Tools: Python, pandas, matplotlib*
