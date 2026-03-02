# PORTFOLIO ROADMAP
## Strategic Portfolio Development Plan

**Created:** March 2, 2026  
**Program:** 18-Week Data Analysis & AI Career Development  
**Strategy:** One substantial portfolio project per week (Weeks 4+)  
**Current Status:** 3 showcase projects complete (Weeks 1-3)

---

## CURRENT PORTFOLIO STATUS

### Completed Showcase Projects (3)

**1. Food Choices & Nutrition Analysis** (Week 3)
- **Skills:** Data cleaning, exploratory analysis, demographic patterns
- **Dataset:** 125 college students, 61 variables (Kaggle)
- **Tools:** Python, pandas, matplotlib
- **Location:** `portfolio-projects/01-food-choices-analysis/`

**2. Student Dropout Analysis** (Week 2)
- **Skills:** Multi-table joins, semi/anti-joins, engagement analysis
- **Dataset:** 32,593 Open University students (OULAD)
- **Tools:** Python, pandas, statistical exploration
- **Location:** `portfolio-projects/02-student-dropout-analysis/`

**3. Education Publishing Analysis** (Week 1)
- **Skills:** Data creation, aggregation, business metrics
- **Dataset:** Simulated book orders (8 schools, 3 quarters)
- **Tools:** Python, pandas, DataFrame creation
- **Location:** `portfolio-projects/03-education-publishing-analysis/`

---

## SKILLS GAP ANALYSIS

### What Portfolio Currently Demonstrates

✅ **Data cleaning & validation**  
✅ **Exploratory data analysis**  
✅ **Multi-table joins (pandas)**  
✅ **Basic visualization (matplotlib)**  
✅ **Demographic pattern analysis**  
✅ **Business metric calculation**  
✅ **Professional documentation**  
✅ **Transparent AI collaboration**  

### What Portfolio Does NOT Yet Demonstrate

❌ **SQL / database queries**  
❌ **Advanced data visualization** (seaborn, interactive plots)  
❌ **Statistical analysis** (hypothesis testing, regression)  
❌ **API usage / web scraping**  
❌ **Machine learning models**  
❌ **NLP / text analysis**  
❌ **Time series analysis**  
❌ **R programming**  
❌ **LLM/AI applications**  
❌ **RAG systems**  
❌ **End-to-end data pipelines**  

### Data Types Not Yet Covered

✅ Survey data (food choices)  
✅ Educational records (OULAD)  
✅ Simulated business data  
❌ Time series data  
❌ Text/NLP data  
❌ API-sourced data  
❌ Geographic/spatial data  
❌ Real-time streaming data  

### Project Types Not Yet Covered

✅ Exploratory analysis  
✅ Data cleaning demonstration  
❌ Predictive modeling  
❌ Classification/regression ML  
❌ Dashboard/visualization showcase  
❌ End-to-end data pipeline  
❌ Comparative analysis (Python vs R)  
❌ Research-grade statistical report  
❌ AI-powered application  

---

## WEEKLY PORTFOLIO PROJECT PLAN

**Strategy:** Each week, initialize ONE substantial portfolio project aligned with that week's learning content. Build progressively throughout week, complete by Friday.

---

### PHASE 1: FOUNDATIONS (Weeks 1-4)

#### ✅ Week 1: Python Fundamentals
**Project Completed:** Education Publishing Analysis  
**Skills:** Data creation, aggregation, pandas basics

#### ✅ Week 2: Data Manipulation with Pandas
**Project Completed:** Student Dropout Analysis (OULAD)  
**Skills:** Multi-table joins, filtering patterns, engagement analysis

#### ✅ Week 3: Data Cleaning
**Project Completed:** Food Choices & Nutrition Analysis  
**Skills:** Data cleaning, missing data, type validation, demographic patterns

#### Week 4: Advanced Python & APIs
**Proposed Project:** **EdTech Product Review Aggregator**

**Concept:** Collect and analyze product reviews from educational technology platforms using web scraping and/or APIs.

**Skills to demonstrate:**
- API calls (requests library)
- Web scraping (BeautifulSoup) if API unavailable
- JSON data parsing
- Text data cleaning
- Aggregation and sentiment detection (basic keyword analysis)
- Time-stamped data handling

**Dataset sources:**
- G2 Crowd API (EdTech category)
- Capterra API (education software)
- Product Hunt API (education tools)
- Alternative: Scrape public review pages (with robots.txt compliance)

**Deliverables:**
- API data collection script
- Review aggregation and cleaning pipeline
- Analysis of rating patterns across products
- Keyword frequency analysis (which features users mention most)
- Time-based trends (reviews over time)

**Portfolio value:** Shows API integration, real-time data collection, practical business application (competitor analysis for EdTech companies)

---

### PHASE 2: CORE DATA ANALYSIS SKILLS (Weeks 5-8)

#### Week 5: SQL Fundamentals
**Proposed Project:** **UK School Performance Database Analysis**

**Concept:** Create SQLite database from UK education datasets, demonstrate query techniques for school performance insights.

**Skills to demonstrate:**
- Database creation and schema design
- SQL queries (SELECT, WHERE, JOIN, GROUP BY, aggregates)
- Subqueries and CTEs
- Query optimization
- Python-SQL integration (sqlite3 module)
- Exporting query results for visualization

**Dataset sources:**
- UK Department for Education data (school performance tables)
- Ofsted inspection ratings
- Student demographics by region
- Attainment gap data

**Deliverables:**
- SQLite database with normalized schema (3-4 related tables)
- 10-15 analytical SQL queries answering education policy questions
- Python script demonstrating database interaction
- Query results exported for visualization
- Documentation of schema design decisions

**Portfolio value:** SQL proficiency demonstration, education sector domain knowledge, database design thinking

---

#### Week 6: Data Visualization
**Proposed Project:** **Education Inequality Dashboard**

**Concept:** Visual analysis of UK education attainment gaps across demographics (ethnicity, socioeconomic status, region).

**Skills to demonstrate:**
- Advanced matplotlib customization
- Seaborn statistical plots (violin plots, box plots, heatmaps)
- Multi-panel layouts (subplots)
- Color theory for accessibility
- Annotation and storytelling with visuals
- Publication-quality figure export

**Dataset sources:**
- UK Department for Education attainment gap data
- Regional deprivation indices
- School demographics
- Results from Week 5 SQL database

**Deliverables:**
- 5-7 publication-quality visualizations
- Multi-panel dashboard layout
- Narrative explanations for each visualization
- Accessibility considerations documented
- Color palette justification

**Portfolio value:** Shows visualization sophistication beyond basic plots, education inequality awareness, design thinking

---

#### Week 7: Statistics for Data Analysis
**Proposed Project:** **Gender Gap in STEM Education: Statistical Analysis**

**Concept:** Statistical investigation of gender representation patterns in STEM subjects across UK schools.

**Skills to demonstrate:**
- Hypothesis testing (t-tests, chi-square)
- Correlation analysis
- Simple linear regression
- P-values and confidence intervals interpretation
- Statistical significance assessment
- Assumption checking (normality, homogeneity of variance)

**Dataset sources:**
- UK A-level subject choice data by gender
- GCSE results by gender and subject
- University STEM enrollment by gender
- Regional variation data

**Deliverables:**
- Statistical analysis report with methodology section
- Hypothesis tests with interpretation
- Regression analysis of gender representation trends
- Visualization of statistical results
- Discussion of limitations and confounding variables

**Portfolio value:** Statistical rigor demonstration, research-grade analysis, education policy relevance

---

#### Week 8: End-to-End Portfolio Project
**Proposed Project:** **Comprehensive UK Education Access Analysis**

**Concept:** Integrate Weeks 5-7 skills in complete analysis pipeline: SQL data extraction, statistical analysis, visualization storytelling.

**Skills to demonstrate:**
- Full data pipeline (collection → cleaning → analysis → visualization → reporting)
- SQL + Python integration
- Statistical hypothesis testing
- Advanced visualization
- Executive summary writing
- Reproducible research documentation

**Dataset sources:**
- Combine datasets from Weeks 5-7
- Add: Higher education progression rates
- Add: Educational mobility data
- Add: Regional economic indicators

**Deliverables:**
- Complete analysis report (R Markdown or Jupyter Notebook)
- SQL queries documented
- Statistical tests justified
- Publication-quality visualizations
- Executive summary (1 page)
- Full technical appendix
- GitHub repository with reproducible workflow

**Portfolio value:** Demonstrates end-to-end capability, research quality, professional reporting, education sector expertise

---

### PHASE 3: AI/ML SPECIALIZATION (Weeks 9-12)

#### Week 9: Machine Learning Foundations
**Proposed Project:** **Student Performance Prediction Model**

**Concept:** Build classification models predicting student academic outcomes using OULAD or similar dataset.

**Skills to demonstrate:**
- Scikit-learn model pipeline
- Train-test split and cross-validation
- Classification models (logistic regression, decision trees, random forest)
- Regression models (predicting grades)
- Feature engineering
- Model evaluation metrics (accuracy, precision, recall, F1, RMSE)
- Hyperparameter tuning

**Dataset sources:**
- OULAD (Open University Learning Analytics)
- Alternative: Kaggle student performance datasets
- Alternative: UK school value-added measures data

**Deliverables:**
- 3 trained models with comparison
- Feature importance analysis
- Model evaluation report
- Confusion matrices and ROC curves
- Discussion of ethical implications (bias, fairness)
- Model limitations and appropriate use cases

**Portfolio value:** ML capability demonstration, education application, ethical AI awareness

---

#### Week 10: Introduction to NLP & LLMs
**Proposed Project:** **Educational Content Sentiment & Topic Analyzer**

**Concept:** Analyze student feedback, course reviews, or educational forums using NLP and transformer models.

**Skills to demonstrate:**
- Text preprocessing and tokenization
- Sentiment analysis with pre-trained transformers
- Topic modeling (LDA or BERTopic)
- Named entity recognition
- Text classification
- Hugging Face transformers library

**Dataset sources:**
- Course evaluation comments (synthetic or public datasets)
- Educational forum posts (Reddit r/education, r/teaching)
- EdTech product reviews (from Week 4 project)
- Student survey open-ended responses

**Deliverables:**
- Sentiment analysis pipeline
- Topic model with interpretation
- Visualization of themes in educational feedback
- Comparison of manual coding vs. automated analysis
- Discussion of NLP limitations in education context

**Portfolio value:** NLP skills, transformer usage, education text analysis, research methodology awareness

---

#### Week 11: Prompt Engineering & LLM Applications
**Proposed Project:** **AI-Powered Education Data Assistant**

**Concept:** Build LLM application that answers questions about education datasets using natural language queries.

**Skills to demonstrate:**
- OpenAI/Anthropic API integration
- Prompt engineering techniques
- Function calling / tool use
- Streaming responses
- Error handling and rate limiting
- User interface (Streamlit or Gradio)

**Application features:**
- Natural language queries about education data
- Automatic SQL query generation
- Data visualization on demand
- Summary statistics generation
- Interpretation assistance

**Deliverables:**
- Functional LLM-powered application
- Prompt templates documented
- User interface
- Example query demonstrations
- Discussion of accuracy and limitations
- Cost analysis and optimization

**Portfolio value:** LLM application development, practical AI tool building, education sector application

---

#### Week 12: RAG Systems & Synthetic Data
**Proposed Project:** **Education Policy RAG Q&A System**

**Concept:** Build RAG system that answers questions about UK education policy documents using vector search and LLM synthesis.

**Skills to demonstrate:**
- Document chunking and embedding
- Vector database usage (ChromaDB or similar)
- Retrieval strategies
- Context construction for LLM
- Citation tracking
- Synthetic data generation for testing

**Document sources:**
- UK Department for Education policy papers
- Ofsted framework documents
- Education white papers and green papers
- Research reports on education interventions

**Deliverables:**
- RAG system with vector database
- Document ingestion pipeline
- Query interface
- Citation mechanisms
- Evaluation of retrieval quality
- Synthetic test queries for benchmarking

**Portfolio value:** Advanced AI capability, document processing, education policy knowledge, production-ready system design

---

### PHASE 4: R SPECIALIZATION (Weeks 13-14)

#### Week 13: R Fundamentals & Advanced Statistics
**Proposed Project:** **Education Attainment Statistical Modeling in R**

**Concept:** Reproduce and extend one of the Python statistical analyses (Week 7 or 8) using R, demonstrating comparative capability.

**Skills to demonstrate:**
- R syntax and data structures
- dplyr and tidyr for data manipulation
- Advanced statistical tests (ANOVA, multiple regression)
- Statistical modeling in R
- R Markdown for reproducible research
- R vs Python comparative approach

**Dataset:**
- Same as Python statistical project (Week 7 or 8)
- Allows direct comparison of approaches

**Deliverables:**
- R Markdown report with full analysis
- ANOVA and regression models
- Comparative commentary (R vs Python approaches)
- Statistical visualizations in R
- Discussion of when R vs Python preferable

**Portfolio value:** R proficiency, statistical depth, bilingual capability, research-grade documentation

---

#### Week 14: Research-Grade R Projects
**Proposed Project:** **Longitudinal Education Outcomes: ggplot2 Visualization & Advanced Modeling**

**Concept:** Advanced R project combining publication-quality ggplot2 visualizations with sophisticated modeling (time series, logistic regression).

**Skills to demonstrate:**
- ggplot2 publication-quality visualizations
- Advanced regression (logistic, polynomial)
- Time series analysis basics
- R + Python integration (reticulate)
- Research-grade statistical reporting

**Dataset sources:**
- Longitudinal Educational Outcomes (LEO) data
- National Pupil Database (if accessible)
- Cohort study data (e.g., Millennium Cohort Study education variables)

**Deliverables:**
- Publication-quality ggplot2 visualizations
- Advanced regression models
- Time series analysis
- R Markdown research report
- Comparative Python/R analysis on same dataset
- Discussion of tool selection for different analyses

**Portfolio value:** Research-grade R capability, advanced visualization, dual-language sophistication

---

### PHASE 5: CAREER LAUNCH (Weeks 15-18)

#### Week 15: Capstone Project Planning
**Proposed Project Planning:** **AI-Enhanced Education Analytics Platform**

**Concept:** Design comprehensive capstone combining Python, R, SQL, ML, and LLM skills in unified education analytics application.

**Planning deliverables:**
- Project specification document
- Technical architecture design
- Data requirements and sources
- Sprint planning in Jira
- Feature prioritization
- Success criteria definition

**Scope:** Dashboard + API + ML models + RAG system for education decision-makers

---

#### Week 16: Capstone Implementation
**Capstone Development:** Begin building platform

**Core features:**
- SQL database backend
- ML prediction models (student outcomes)
- LLM-powered insights generation
- RAG-based policy Q&A
- Visualization dashboard
- API for data access

**Target:** 80% functional by end of week

---

#### Week 17: Portfolio Polish & Professional Presence
**Activities:**
- Complete capstone project
- Finalize all portfolio project READMEs
- Create portfolio navigation guide
- Update main README with all projects
- LinkedIn profile optimization
- Research-focused resume creation
- Portfolio presentation deck

**Target:** 5-7 complete portfolio projects professionally documented

---

#### Week 18: Job Applications & Interview Prep
**Focus:** Application execution, not new portfolio work

---

## PORTFOLIO REVIEW SCHEDULE

### Mid-Program Review (Week 9-10)
**When:** After completing Phase 2, before starting ML  
**Focus:**
- Review Weeks 1-8 portfolio projects
- Assess skill demonstration completeness
- Identify any critical gaps
- Adjust Weeks 9-18 projects if needed

### Pre-Career Launch Review (Week 14-15)
**When:** After R specialization, before capstone  
**Focus:**
- Comprehensive portfolio audit
- Cross-reference with target job descriptions
- Ensure education sector focus evident
- Verify technical depth demonstrated
- Check documentation quality consistency

### Final Portfolio Polish (Week 17)
**When:** Capstone complete, before job applications  
**Focus:**
- Professional presentation review
- Navigation and usability testing
- README consistency check
- Link verification
- GitHub profile optimization
- Screenshot/visual previews for major projects

---

## NEXT PORTFOLIO REVIEW SESSION

**📅 SCHEDULED: March 16-17, 2026** (~2 weeks from now)

**Agenda:**
- Review Week 4 portfolio project (API/web scraping)
- Assess whether weekly portfolio project approach working
- Make any adjustments to Weeks 5-8 project proposals
- Update this roadmap based on actual experience
- Check progress against March 31 checkpoint

---

## PORTFOLIO SUCCESS METRICS

### By Phase 1 Completion (End of Week 4)
- ✅ 4 portfolio projects demonstrating foundations
- ✅ Professional documentation for all projects
- ✅ Education sector focus evident
- ✅ Transparent AI collaboration documented
- ✅ GitHub repository well-organized

### By Phase 2 Completion (End of Week 8)
- ✅ SQL proficiency demonstrated
- ✅ Advanced visualization skills shown
- ✅ Statistical analysis capability proven
- ✅ End-to-end project pipeline complete
- ✅ 8 total portfolio projects

### By Phase 3 Completion (End of Week 12)
- ✅ Machine learning models built
- ✅ NLP/transformer skills demonstrated
- ✅ LLM application created
- ✅ RAG system functioning
- ✅ 12 total portfolio projects

### By Phase 4 Completion (End of Week 14)
- ✅ R statistical capability demonstrated
- ✅ Bilingual (Python/R) portfolio
- ✅ Research-grade documentation
- ✅ Publication-quality visualizations
- ✅ 14 total portfolio projects

### By Program Completion (End of Week 18)
- ✅ Capstone project complete
- ✅ 5-7 flagship projects (subset of 14+)
- ✅ Professional online presence
- ✅ Portfolio ready for employer review
- ✅ Interview-ready technical demonstrations

---

## IMPLEMENTATION NOTES

### Weekly Portfolio Project Workflow

**Monday (Week start):**
1. Review week's DataCamp content outline
2. Initialize portfolio project for the week
3. Create project folder: `portfolio-projects/##-project-name/`
4. Create initial README.md with project concept
5. Identify dataset sources
6. Set up basic file structure

**Tuesday-Thursday (Development):**
1. Complete DataCamp chapters
2. Build portfolio project progressively
3. Apply new concepts learned each day
4. Document decisions and challenges
5. Commit progress regularly

**Friday (Completion):**
1. Finalize portfolio project code
2. Complete comprehensive README
3. Add visualizations/outputs
4. Test all code runs cleanly
5. Final commit and push
6. Week reflection notes

### Project Naming Convention

`portfolio-projects/##-descriptive-name/`

**Examples:**
- `04-edtech-review-aggregator/`
- `05-uk-schools-sql-analysis/`
- `06-education-inequality-dashboard/`
- `07-stem-gender-gap-statistics/`

**Numbering:** Sequential by week (01 = Week 1, 02 = Week 2, etc.)

### README Template Structure

Each portfolio project README should include:
1. Project title and badges
2. Business question / problem statement
3. Key findings
4. Dataset description
5. Skills demonstrated
6. Technical approach
7. Deliverables
8. Methodology notes
9. Lessons learned
10. AI collaboration statement
11. Repository context

---

## APPENDIX: ALIGNMENT WITH MASTER PLAN

### Master Plan Portfolio Deliverables

**Original 18-week plan specified:**
- 5-7 substantial projects in Python and R
- Research-grade documentation
- Professional portfolio on GitHub

**This roadmap delivers:**
- 14+ projects across 18 weeks (1 per week after Week 4)
- Subset of 5-7 will be highlighted as flagship projects
- Progressive skill demonstration
- Education sector focus throughout
- Transparent AI collaboration documented

**Enhancement over original plan:**
- Weekly portfolio projects (not just phase-end projects)
- Systematic skill gap closure
- Consistent education sector application
- Integrated rather than separate portfolio building
- Better interview preparation (more examples to discuss)

---

**Status:** Living document - update after each portfolio review session  
**Next Update:** March 16-17, 2026 (post-Week 4 review)  
**Owner:** Magda McCrimmon | GitHub: MagsMcr