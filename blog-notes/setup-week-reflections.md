# Setup Week Learning Notes
Started: January 19, 2026

## Day 1 - Monday Jan 19
### Morning accomplishments:
- Git and GitHub set up! ✓
- First repository created ✓
- Python environment configured ✓
- VS Code set up ✓

### What I learned today:
- Terminal navigation (pwd, cd, ls, mkdir)
- Git workflow (add, commit, push)
- Virtual environments keep projects separate
- Import statements load Python libraries
- [will add more after DataCamp session]
- [will add more after DataCamp session]

### Afternoon accomplishments:
- DataCamp Intermediate Python Chapter 1 (Matplotlib) completed ✓
- Learned about basic plotting with matplotlib
- Understanding line plots, scatter plots, and customization

### What I learned today:
- **Terminal Navigation:** pwd (where am I), cd (change directory), ls (list contents), mkdir (make directory)
- **Git Workflow:** The three-step process - add (stage), commit (snapshot), push (upload to GitHub)
- **Virtual Environments:** Keep project dependencies separate - like separate toolboxes for different projects
- **Python Imports:** Loading libraries with import statements (import pandas as pd)
- **Directories vs Folders:** Proper technical term is "directory" in terminal/coding contexts
- **Commit Messages:** Each commit needs a unique message describing what changed - like email subject lines
- **Matplotlib/pyplot:** pyplot is a module inside matplotlib - already installed when I installed matplotlib

### Challenges faced:
- Initially confused about whether I had VS Code installed (it was there!)
- Understanding the difference between local changes and GitHub (local = my computer, GitHub = cloud backup)
- Git authentication - learned about Personal Access Tokens
- Realizing that file edits UPDATE the same file, not create new ones

### Aha moments:
- Git commits are like snapshots/save points in time, not folders!
- The (career_env) in terminal means my virtual environment is active
- I can work in Terminal OR VS Code terminal - they access the same things
- PATH means "where the computer looks for programs"
- When I push to GitHub, my local files don't change because they already HAVE the changes

### Technical terms I learned:
- Repository (repo): Project directory tracked by Git
- Commit: Saved snapshot with message
- Push: Upload to GitHub
- Clone: Download repo from GitHub to computer
- Stage: Prepare files for commit (git add)
- Virtual environment: Isolated Python setup for a project
- Directory: Technical term for folder

### Tools now configured:
- Git (version control)
- GitHub account (MagsMcr)
- Python 3.11.5
- Virtual environment (career_env)
- Libraries: pandas, numpy, matplotlib, seaborn, jupyter, scikit-learn
- VS Code with Python extension

### GitHub commits today: 3
1. Initial repository structure
2. Python environment test
3. Day 1 learning notes

### Thougts on AI
1. So far enjoying wokring wiht Claude
2. Need to streamline my ability to set its tone and look into its sustainability - Claude keeps dropping techincal spec of communication 
3. Beware of the errors - took 4 attempts for it to fix the documents to display the correct dates on the planning documents 

### Time spent: ~6.5 hours (extended due to late start)

### Tomorrow's focus:
- R and RStudio installation
- Git practice
- DataCamp Chapter 2
- Python practice scripts (moved from today)

## Day 2 - Tuesday, January 20, 2026

### Completed:
- ✅ Created first practice script (day1-practice.py) with real education dataset
- ✅ Loaded UC Irvine Student Performance dataset successfully
- ✅ Verified R (4.4.0) and RStudio installation
- ✅ Confirmed R packages installed (tidyverse, ggplot2, dplyr, readr)
- ✅ Tested R environment with simple plotting script
- ✅ Completed DataCamp Intermediate Python Chapter 2
- ✅ Learned dictionaries, nested dictionaries, and pandas DataFrames

### Technical Learning:
- Troubleshot VS Code Insiders vs regular VS Code
- Configured Python interpreter in VS Code for virtual environment
- Understood virtual environment concept vs physical folder
- Created .gitignore to exclude virtual environment from Git
- Practiced Terminal navigation and file management

### Time: [4 hours]

### Notes on AI
- Had issues with the chat randomly lagging despite the fact that it was not too long and I was noweher near the response limit
- Definitely feeling like it provides me with extra accountability - even though I am only talking to "the machine" it still helps when I am reporting my progress and need to help for help at a specific time 
- Still need to work on the prompt generation, specifically whwen it comes to techincal help. I have neglected alternating between different chats for different purposes and I need to revisit this idea tomorrow. This is due to the fact that Claude keeps defaulting into provodong solutions in a moment to the very latest prompt, speciifcally when it comes to troubleshooting. It does not intuitively account for previous responses to allow smooth work flow, it has to be directed.
- It seems to be defualting into time saving solutions rather than more in depth, sustainable solutions. Recommended to just keepo using VS Code Inisders even thought the full version is the better option. Then recommended abandoning attempts to solve the issue of lack of communication between VS code and Python and finding a manual workaround to the task at hand even though more sustainable option was to solving the issue for smooth workflow later. 
- it just had a hiccup when wriitng a code for the github commit - and i know i should be doing this mysef but we are on day 2 and i am tired. It incorrectly provided the GitHUb location path. two points here:
  -  it clearly didn't know it, it assumed
  - The knowledge should have transfered from another chat within the project as yesterday the code was correct. But it did not 

  ## Day 3 - Wednesday Jan 21

### What I accomplished today:
- Created practice script (day2-practice.py) reinforcing Chapter 2 concepts
- Set up 5 learning platform accounts (LeetCode, HackerRank, Codewars, Kaggle, Medium)
- Completed DataCamp Intermediate Python Chapter 3 (Logic & Control Flow)
- Completed W3Schools practice exercises (Conditions, Booleans, Operators)
- Solved 3 HackerRank problems and earned my first star! 🎉

### Key technical concepts learned:

#### Boolean Indexing - CRITICAL CONCEPT (not explained clearly in DataCamp!)
- When you pass a Series of True/False values to a DataFrame using `df[boolean_series]`, pandas automatically keeps only rows where the value is True
- You never need to write `== True` - it's implied by the syntax
- This is THE standard way to filter data in pandas
- Example:
```python
  dr = cars['drives_right']  # Series of True/False
  sel = cars[dr]  # Automatically filters to keep only True rows
```

#### Comparison and Logical Operators
- `==` tests equality, `!=` tests inequality
- `and`, `or`, `not` for combining conditions
- `%` (modulo) returns remainder: `n % 2 == 0` tests if n is even
- Can combine multiple conditions: `n >= 2 and n <= 5`

#### Integer vs Float Division
- **Float division (`/`)**: Normal division with decimals (e.g., `7 / 2 = 3.5`)
- **Integer division (`//`)**: Rounds DOWN to whole number (e.g., `7 // 2 = 3`)
- Integer division is NOT rounding to nearest - it's "floor division" (always rounds down)
- Use case: "How many complete times does this fit?" (e.g., items per box)
- Example: `3 / 5 = 0.6` but `3 // 5 = 0` (not 1, because it rounds DOWN)

#### Control Flow
- if/elif/else structure for conditional logic
- Each `print()` statement creates a new line of output
- Importance of proper indentation in Python

### Practice and Problem Solving:
- Created day2-practice.py demonstrating dictionaries, nested dictionaries, dictionary of lists, and DataFrame operations
- Solved HackerRank problems: Hello World, Python If-Else, Arithmetic Operators
- Learning to read problem descriptions carefully and translate requirements into code

### Platforms set up today:
- **LeetCode**: Profile created, exploring problem sets
- **HackerRank**: Active - completed first 3 problems
- **Codewars**: Account ready, 8 kyu level
- **Kaggle**: Profile created, ready for datasets and competitions
- **Medium**: Blog account ready for bi-weekly learning posts

### New daily habit added:
- W3Schools practice exercises (15 mins after each DataCamp chapter)
- Provides reinforcement through repetition and immediate feedback

### Challenges faced:
- Understanding boolean indexing in pandas - figured out the implicit filtering mechanism
- HackerRank interface initially confusing (understanding pre-populated code and input handling)
- Integer division concept - learned it rounds down, not to nearest

### Aha moments:
- Boolean indexing "just works" because pandas interprets True/False Series as filters automatically
- Integer division is about "complete groups" not "closest number"
- Breaking problems into logical steps makes coding challenges more manageable
- Each print() statement = new line (fundamental but important!)

### What's working well:
- Daily practice script creation reinforces concepts immediately
- W3Schools exercises provide good repetition after DataCamp
- HackerRank problems apply learning in practical scenarios
- Asking "why does this work?" leads to deeper understanding

### Time management:
- DataCamp + W3Schools combo worked well (~1.25 hours)
- HackerRank problems engaging and good practice (~1.5 hours)
- Total productive time: ~6 hours

### Tomorrow's focus:
- DataCamp Intermediate Python Chapter 4 (Loops)
- Continue building practice scripts
- More HackerRank problems to reinforce concepts

### AI notes:

- It defaulted to providing me with code when I only asked for general guidance in a certain problem. I followed with clear instructions on how to respond when I am asking for help and guided it to clarify with me what precisely is it that I need - complete answer or tips. Let's see if it follows this going forward. 
- I am baffled by how it measures the passage of time as it inacurately measured the time it took me to complete a certain task. Will keep monitoring it as well as ask for provision of logic behind estimation of time needed to complete the task tomorrow. 