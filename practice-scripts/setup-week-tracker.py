import pandas as pd
import matplotlib.pyplot as plt

# Setup Week progress data
data = {
    'day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
    'hours_worked': [6.5, 4.0, 6.0, 0, 0],  # Update Day 4 when complete
    'datacamp_chapters': [1, 1, 1, 0, 0],
    'github_commits': [4, 2, 1, 0, 0],
    'platforms_setup': [0, 0, 5, 0, 0]
}

# Create DataFrame
progress = pd.DataFrame(data)

# Display current progress
print("=== SETUP WEEK PROGRESS ===\n")
print(progress)
print("\n=== SUMMARY STATISTICS ===")
print(f"Total hours worked: {progress['hours_worked'].sum()}")
print(f"Total DataCamp chapters: {progress['datacamp_chapters'].sum()}")
print(f"Total GitHub commits: {progress['github_commits'].sum()}")
print(f"Learning platforms set up: {progress['platforms_setup'].sum()}")

# Create visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Hours worked per day
axes[0, 0].bar(progress['day'], progress['hours_worked'], color='steelblue')
axes[0, 0].set_title('Hours Worked Per Day')
axes[0, 0].set_ylabel('Hours')

# Plot 2: DataCamp chapters completed
axes[0, 1].bar(progress['day'], progress['datacamp_chapters'], color='forestgreen')
axes[0, 1].set_title('DataCamp Chapters Completed')
axes[0, 1].set_ylabel('Chapters')

# Plot 3: GitHub commits
axes[1, 0].bar(progress['day'], progress['github_commits'], color='coral')
axes[1, 0].set_title('GitHub Commits Per Day')
axes[1, 0].set_ylabel('Commits')

# Plot 4: Cumulative hours
cumulative_hours = progress['hours_worked'].cumsum()
axes[1, 1].plot(progress['day'], cumulative_hours, marker='o', color='purple', linewidth=2)
axes[1, 1].set_title('Cumulative Hours Worked')
axes[1, 1].set_ylabel('Total Hours')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('practice-scripts/setup-week-progress.png')
print("\n✓ Visualization saved as 'setup-week-progress.png'")
plt.show()