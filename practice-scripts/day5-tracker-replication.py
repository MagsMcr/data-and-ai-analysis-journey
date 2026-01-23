import pandas as pd
import matplotlib.pyplot as plt

tracking = {
    'day' : ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
    'hours_worked' : [6.4, 4.5, 5, 4, 5],
    'data_camp_chapters' : [1, 1, 1, 1, 1],
    'github_commits' : [5, 4, 2, 3, 3],
    'platforms_setup' : [1, 2, 5, 0, 1]
}

setup = pd.DataFrame(tracking)
print("=== SETUP WEEK SUMMARY ===\n")
print(setup)
print("\n=== SUMMARY STATISTICS ===")
print(f" Total hours worked: {setup['hours_worked'].sum()}")
print(f" Total Data Camp chapters: {setup['data_camp_chapters'].sum()}")
print(f" Total GitHub commits: {setup['github_commits'].sum()}")
print(f" Total platforms setup: {setup['platforms_setup'].sum()}")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].bar(setup['day'], setup['hours_worked'], color='blue')
axes[0, 0].set_title('Hours worked per day')
axes[0, 0].set_ylabel('Hours')

axes[0, 1].bar(setup['day'], setup['data_camp_chapters'], color='green')
axes[0, 1].set_title('Data Camp Chapters Completed')
axes[0, 1].set_ylabel('Chapters')

axes[1, 0].bar(setup['day'], setup['github_commits'], color='orange')
axes[1, 0].set_title('Number of GitHub commits')
axes[1, 0].set_ylabel('Commits')

cumulative_hours = setup['hours_worked'].cumsum()
axes[1, 1].plot(setup['day'], cumulative_hours, marker='o', color='purple', linewidth=2)
axes[1, 1].set_title('Cumulative Hours Worked')
axes[1, 1].set_ylabel('Total Hours')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('practice-scripts/setup-week-summary.png')
print("\n✓ Visualization saved as 'setup-week-summary.png'")
plt.show()