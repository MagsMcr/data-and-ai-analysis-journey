# Student Dropout Analysis

**Open University Learning Analytics Dataset (OULAD)**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![pandas](https://img.shields.io/badge/pandas-2.0+-green)
![Dataset](https://img.shields.io/badge/Dataset-32,593_students-orange)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 📊 Project Overview

### The Challenge
Why do students drop out of online courses? When do they make the decision to leave? Are there early warning signals that could enable intervention?

This analysis examines 32,593 Open University student records across multiple courses to identify patterns in student unregistration and engagement behaviors.

### Key Findings
- **Timing matters:** Most dropouts occur in first month, suggesting early engagement critical
- **Course variation:** Dropout rates range from 15-40% across different courses
- **Engagement signal:** Students who submit at least one assessment before dropping show different demographic patterns than those who never engage
- **Demographic patterns:** Significant variations by age, prior attempts, and disability status

---

## 🎯 Business Value

**For Educational Institutions:**
- Identifies high-risk courses requiring intervention design
- Highlights critical first-month engagement window
- Provides demographic profiles for targeted support programs
- Demonstrates value of early assessment submission as retention signal

**For Learning Analytics:**
- Shows how data joins reveal hidden patterns in student behavior
- Demonstrates exploratory analysis for hypothesis generation
- Illustrates importance of engagement vs. enrollment metrics

---

## 📁 Project Files

**Analysis script:** [`w2d3-dropout-patterns.py`](w2d3-dropout-patterns.py)

**Dataset:** Open University Learning Analytics Dataset (OULAD)
- 32,593 student records
- Multiple courses and presentations
- Demographic data, assessment submissions, registration status

---

## 🔍 Research Questions

### Part 1: Unregistration Profile
1. **When** do students typically drop out? (timing analysis)
2. **Which courses** have the highest dropout rates?
3. **Who** drops out? (demographic patterns: age, gender, education, disability, previous attempts, region)

### Part 2: Engagement Patterns Among Dropouts
4. What proportion of dropouts **submitted assessments** before leaving?
5. How do demographics differ between dropouts who **engaged** vs. those who **never engaged**?
6. For students who submitted before dropping:
   - What types of assessments did they submit?
   - How many assessments did they complete?
   - What were their score patterns?
   - When did they drop out relative to submissions?

---

## 🛠️ Technical Approach

### Dataset Structure

**OULAD consists of multiple related tables:**
- `studentInfo` - Demographics and registration details
- `studentRegistration` - Unregistration dates
- `courses` - Course metadata
- `studentAssessment` - Assessment submission records
- `assessments` - Assessment type and weight information

### Data Integration Strategy

**Multi-table joins demonstrating Week 2 skills:**

```python
# Merge student demographics with registration status
students_unreg = studentInfo.merge(
    studentRegistration,
    on=['code_module', 'code_presentation', 'id_student']
)

# Filter for dropouts only
dropouts = students_unreg[students_unreg['date_unregistration'].notna()]

# Add course details (multiple join keys)
dropouts_with_courses = dropouts.merge(
    courses,
    on=['code_module', 'code_presentation']
)

# Semi-join concept: Dropouts who submitted assessments
dropouts_who_submitted = dropouts[
    dropouts['id_student'].isin(studentAssessment['id_student'])
]

# Anti-join concept: Dropouts who never submitted
dropouts_never_submitted = dropouts[
    ~dropouts['id_student'].isin(studentAssessment['id_student'])
]
```

### Skills Demonstrated

**pandas join techniques:**
- `.merge()` with single and multiple keys
- Semi-join pattern using `.isin()`
- Anti-join pattern using `~.isin()`
- Sequential merges across multiple tables
- Filtering and boolean indexing

**Data exploration methods:**
- `.groupby()` for demographic segmentation
- `.value_counts()` for frequency analysis
- Timing analysis with date variables
- Comparative analysis between cohorts

---

## 📈 Key Findings

### 1. Critical First Month Window
Majority of student unregistrations occur within the **first 30 days** of course start.

**Implication:** Retention interventions should focus heavily on early engagement period. Students who persist past first month show much higher completion rates.

### 2. Course-Level Variation
Dropout rates vary significantly by course (15-40% range), suggesting:
- Course design factors matter
- Some subjects inherently more challenging for self-paced learning
- Opportunity for cross-course learning (what do low-dropout courses do differently?)

### 3. Engagement as Signal
**Students who submit at least one assessment before dropping:**
- Show different demographic profile than never-submitters
- Indicate initial course engagement despite eventual withdrawal
- May respond differently to retention interventions

**Students who never submit:**
- Likely decided to withdraw before engaging with content
- May have enrolled exploratorily or faced immediate barriers
- Different intervention strategy needed (pre-enrollment support vs. mid-course retention)

### 4. Demographic Patterns

**Age variations:**
- Younger students (under 25) show different dropout patterns than mature learners
- Suggests age-appropriate support strategies needed

**Previous attempt patterns:**
- Students with prior course attempts show different persistence
- Indicates learning from past experience (both positive and negative)

**Disability status:**
- Variations suggest need for proactive accessibility support
- Early identification and accommodation critical

---

## 🔬 Methodology Notes

### Analytical Approach
This is **exploratory analysis** focused on pattern identification, not confirmatory hypothesis testing.

**Strengths:**
- Large dataset (32k+ students) enables subgroup analysis
- Real-world institutional data (not simulated)
- Multiple dimensions for pattern exploration
- Demonstrates complex data integration skills

**Limitations:**
- **Correlation not causation** - patterns identified but not statistically tested
- **Selection bias** - Only includes students who enrolled (not those who considered and didn't)
- **Confounding variables** - No controls for socioeconomic factors, prior education quality, time availability
- **No statistical significance testing** - Would require hypothesis tests (chi-square, logistic regression)

### Next Steps for Rigorous Analysis
1. **Survival analysis** - Model time-to-dropout with censoring
2. **Logistic regression** - Control for confounding, identify independent predictors
3. **Propensity score matching** - Compare similar students who drop vs. persist
4. **Longitudinal tracking** - Follow cohorts across multiple course presentations
5. **Intervention testing** - A/B test retention strategies based on findings

---

## 💡 Insights for Stakeholders

### For Course Designers:
- First month experience is make-or-break period
- Early assessment submission may be protective factor
- Consider low-stakes early assessment to encourage engagement
- Examine low-dropout courses for design elements to replicate

### For Student Support Services:
- **Segment interventions** by engagement level:
  - Never-submitters: Pre-enrollment support, onboarding clarity
  - Submitters-who-drop: Academic support, workload management
- **Timing:** Proactive outreach in weeks 2-4 critical
- **Demographics:** Age-appropriate and accessibility-aware support design

### For Institutional Leadership:
- Dropout rates vary significantly by course (quality/design issue, not just student characteristics)
- Early engagement metrics predict retention (useful KPI)
- Investment in first-month experience has high ROI
- Data integration reveals insights not visible in single tables

---

## 🤖 AI Collaboration Statement

This analysis was developed collaboratively with Claude (Anthropic AI).

**Human contributions (Magda):**
- Research question formulation
- Strategic analytical direction
- Data integration approach design
- Interpretation of findings and business implications

**AI contributions (Claude):**
- Code implementation based on specifications
- pandas syntax for complex joins
- Documentation structure

**All analytical decisions and interpretations made by human analyst.** This reflects professional practice where AI assists with technical implementation while human judgment guides analytical strategy.

---

## 📂 Repository Context

**Part of:** 18-Week Data Analysis Career Development Program  
**Week focus:** Week 2 - Data joining and merging strategies  
**Skills demonstrated:** Multi-table joins, semi/anti-joins, exploratory analysis

**Learning objective:** Demonstrate ability to integrate multiple data sources to answer complex research questions using real-world educational dataset.

**View complete program:** [Main Repository](https://github.com/MagsMcr/data-and-ai-analysis-journey)

---

## 📫 Contact

**Author:** Magda McCrimmon  
**GitHub:** [@MagsMcr](https://github.com/MagsMcr)  
**Career focus:** AI Strategy/Product roles in education sector  
**Why this dataset:** Demonstrates analytical skills directly relevant to target roles in educational technology and learning analytics

---

*Analysis completed: February 2026 | Dataset: Open University Learning Analytics Dataset | Tools: Python, pandas, multi-table joins*
