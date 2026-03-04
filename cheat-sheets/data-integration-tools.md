# Data Integration Tools — Orientation Notes

**Created:** 3 March 2026  
**Purpose:** Conceptual orientation — what data integration is, why it exists, what the tools are called, and how relevant it is to target roles  
**Level:** Complete beginner  
**Next review:** March 16–17 portfolio review session

---

## What Is Data Integration?

Data integration is the process of bringing data from multiple separate systems into one place so it can be analysed together. Most organisations don't store all their data in one place — they use different software tools for different purposes, and each tool holds its own data in its own format. Without integration, getting a complete picture requires manually copying and combining data from each system, which is slow, error-prone, and doesn't scale. Data integration automates that process, so data flows from its various sources into a central location where analysts can work with it. Think of it like a plumbing system: the data integration layer is the pipes that connect everything up, so the analyst doesn't have to carry buckets.

**A concrete example:** A school uses three separate systems — one for tracking student attendance, one for recording grades, and one for SEND (Special Educational Needs and Disabilities) support notes. A headteacher wants to understand which students are falling behind across all three areas. Without data integration, someone has to manually export each system's data, paste it into a spreadsheet, and try to match students across all three. With data integration in place, all three systems feed automatically into a central database, and the headteacher can query it directly.

**Source:** [IBM — What is Data Integration?](https://www.ibm.com/think/topics/data-integration) | [AWS — What is Data Integration?](https://aws.amazon.com/what-is/data-integration/)

---

## The Main Types (Approaches)

There are several different ways to achieve data integration. They all solve the same core problem — getting data from A to B — but they do it in different orders and suit different situations. You don't need to be able to implement any of these; knowing what the terms mean is enough at this stage.

---

### ETL — Extract, Transform, Load

**ETL** stands for **Extract, Transform, Load** — and the name describes the order of operations. First you *extract* data from its source systems, then you *transform* it (clean it, reformat it, standardise it) in a separate processing area, and finally you *load* the cleaned data into a destination such as a database or data warehouse. ETL has been around since the 1970s and was the standard approach for decades, particularly when organisations stored data on physical servers with limited processing power. The transformation step happening *before* loading means the data arrives clean and ready to use, but it also means you have to decide upfront exactly what format you want — which limits flexibility later. ETL still works well for structured, well-defined data with strict quality requirements.

**Source:** [AWS — What is ETL?](https://aws.amazon.com/what-is/etl/) | [IBM — ETL](https://www.ibm.com/think/topics/etl)

---

### ELT — Extract, Load, Transform

**ELT** stands for **Extract, Load, Transform** — the same three steps, but in a different order. The key difference is that raw data is loaded into the destination *first*, and transformation happens afterwards, inside the destination system. ELT became practical with the rise of cloud computing, which gave organisations cheap, scalable processing power in the cloud warehouse itself — meaning you no longer needed a separate server to do the transformation work. The advantage of ELT is flexibility: because the raw data is always stored, you can transform it in different ways for different purposes, and you can ask new questions without re-running the whole pipeline from scratch. ELT is now considered the modern standard for most analytics work.

**Source:** [Databricks — ETL vs ELT](https://www.databricks.com/discover/etl/vs-elt) | [AWS — ETL vs ELT](https://aws.amazon.com/compare/the-difference-between-etl-and-elt/)

---

### APIs — Application Programming Interfaces

**API** stands for **Application Programming Interface** — it is essentially a standardised way for two pieces of software to talk to each other. When one system wants data from another, it sends a request via the API, and the other system sends back the data in a structured format. Most modern software tools (CRMs, learning management systems, publishing platforms) have APIs that allow other tools or analysts to pull data from them programmatically, without needing to manually export a file. APIs are particularly relevant to AI agents, because an agent that needs to check a calendar, log a task, or retrieve a record is using an API to do so — the agent sends a request, the external system responds with data. This is the direct connection between data integration concepts and the agent architecture research you did in February.

**Source:** [MuleSoft — What is Data Integration?](https://www.mulesoft.com/integration/what-is-data-integration)

---

### Data Virtualisation

Data virtualisation is an approach where data is *not* physically moved or copied anywhere — instead, a software layer creates a unified *view* of all the data sources, as if they were one single database. When an analyst queries it, the system fetches the relevant data from each source in real time and presents it together. The advantage is that there is no duplication of data and no delay in syncing — you are always looking at live data. The disadvantage is that it can be slower for complex queries, and it depends on all the source systems being available and responsive. It is less common than ETL or ELT but worth knowing the term.

**Source:** [AWS — What is Data Integration?](https://aws.amazon.com/what-is/data-integration/)

---

## The Tools You Will See Named in Job Postings

These are the specific products that do data integration work. They appear in job postings, LinkedIn profiles, and tech stack descriptions. You do not need to be able to use any of these at entry level — but knowing what category each one belongs to and what problem it solves means you will not be blank if they come up.

- **Fivetran** — A managed ELT tool that automates the "extract and load" part of the pipeline. It has hundreds of pre-built connectors to common data sources (Salesforce, Google Analytics, databases, etc.) and automatically moves data into a cloud data warehouse. It is designed to "just work" with minimal setup, which makes it popular in commercial settings. It appears frequently in data engineering and senior analyst job postings, less commonly in entry-level analyst roles. [fivetran.com](https://www.fivetran.com)

- **dbt (Data Build Tool)** — A transformation tool that handles the "T" part of ELT — it takes raw data that is already in a warehouse and transforms it into clean, structured tables that analysts can work with. It uses SQL, which means analysts (not just engineers) can use it, and it has built-in version control and testing. It is often paired with Fivetran: Fivetran moves the data in, dbt cleans and structures it. Increasingly appears in mid-level analyst postings. [getdbt.com](https://www.getdbt.com)

- **Airbyte** — An open-source alternative to Fivetran that does the same job (extract and load data from various sources into a warehouse) but is free to use and self-hosted. It has a larger library of connectors than Fivetran because the open-source community contributes to it. It requires more technical setup and maintenance than Fivetran, so it tends to appear in engineering-led organisations rather than analyst-led ones. [airbyte.com](https://airbyte.com)

- **Zapier / Make (formerly Integromat)** — Lighter-weight automation tools that connect applications together for operational workflows rather than large-scale data analysis. A good analogy: Fivetran moves data in bulk from a source into a warehouse for analysis; Zapier connects two apps so that when something happens in one (e.g. a form is submitted), something automatically happens in another (e.g. a row is added to a spreadsheet). More likely to appear in smaller organisations, nonprofits, and education charities. [zapier.com](https://zapier.com)

- **Microsoft Power Automate** — Microsoft's equivalent of Zapier, tightly integrated with the Microsoft 365 ecosystem (Excel, SharePoint, Teams, Dynamics). Relevant to your target sectors because many UK schools, charities, and publishers run on Microsoft infrastructure. Appears occasionally in education and nonprofit data roles. [powerautomate.microsoft.com](https://powerautomate.microsoft.com)

---

## How Relevant Is This to Your Target Roles?

**The honest answer: low to medium at entry level, and mostly as awareness rather than hands-on skill.**

Across UK entry-level data analyst job postings, the tools that appear consistently are SQL, Excel, and visualisation tools (Power BI or Tableau). Tools like Fivetran and dbt appear primarily in data engineering roles or senior analyst roles at larger, more technically mature organisations. A 2025 practitioner survey found that the overwhelming majority of day-to-day analyst work comes down to querying a database, cleaning a spreadsheet, and presenting a chart to a stakeholder — not building pipelines. In your specific target sectors (EdTech, publishing, education charities), organisations tend to be smaller and less likely to have sophisticated data engineering infrastructure, which means even less likelihood of needing hands-on integration tool experience.

**What you do need:**
- To understand what these tools are and what problem they solve (covered above)
- To not be blank if a hiring manager mentions their "data stack" in an interview
- To understand that data pipelines exist and that the data you analyse as an analyst was probably moved there by something like this

**What you do not need right now:**
- Hands-on experience with Fivetran, dbt, or Airbyte
- To add these to your 18-week learning plan
- To be able to build or maintain a data pipeline

**Source:** [Dataquest — 10 Data Analysis Tools for Entry-Level Analysts](https://www.dataquest.io/blog/10-data-analysis-tools-for-entry-level-analysts/) | [Prospects.ac.uk — Data Analyst Job Profile](https://www.prospects.ac.uk/job-profiles/data-analyst)

---

## The Connection to AI Agents

When you researched AI agent architecture in February, one of the key insights was that agents need to interact with external tools and systems to do useful work — checking a calendar, logging a task in a project management tool, retrieving a record from a database. The way agents do this is via APIs. This means data integration and agent architecture share the same underlying infrastructure: both rely on systems being able to talk to each other via standardised interfaces. The difference is that traditional data integration moves data in bulk on a schedule (e.g. sync all new records every hour), whereas an agent makes on-demand API calls in real time as part of completing a task. For AI strategy roles, understanding this connection — that agents are essentially using the same "plumbing" as data integration, just in a more dynamic way — is the kind of technical literacy that distinguishes a strategic thinker from someone who just knows the buzzwords.

---

## Key Terms Glossary

| Term | Stands for | Plain English |
|---|---|---|
| ETL | Extract, Transform, Load | Move data, clean it first, then store it |
| ELT | Extract, Load, Transform | Move data, store it first, then clean it |
| API | Application Programming Interface | A standardised way for two pieces of software to communicate |
| CRM | Customer Relationship Management | Software for tracking relationships with customers or clients |
| SEND | Special Educational Needs and Disabilities | UK education term for students needing additional support |
| BI | Business Intelligence | Tools and processes for analysing data to inform decisions |
| SQL | Structured Query Language | The language used to query databases |
| SaaS | Software as a Service | Software hosted in the cloud and accessed via subscription |

---

*File location: `cheat-sheets/data-integration-tools.md`*  
*Related files: `job-research/job-market-notes.md`*  
*Next update: March 16–17 portfolio review session, or when questions arise*