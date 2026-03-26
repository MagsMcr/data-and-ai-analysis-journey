# =============================================================================
# AUTHOR COLUMN: PRE-CLEANING INVESTIGATION
# author_field_investigation.py
# =============================================================================
# Purpose: Audit of the author column conducted before finalising the cleaning
# approach in cleaning_analysis.py. Documents the hyphen pattern analysis that
# informed the decision to use a role-keyword dictionary for contributor removal.
#
# Findings summary:
#   — "Writtenby:" prefix present in all entries (10 chars)
#   — spaces removed between words throughout
#   — contributor roles appended as Name-role with no spaces
#   — role labels inconsistent: translator, Übersetzer, traductor, traductrice,
#     traducteur, tradução, traduttore, editor, foreword, illustrator, and more
#   — natural name hyphens also present (e.g. Jean-Christophe, Saint-Exupéry)
#   — Chinese/Japanese entries use hyphens as script separators
#   — cleaning approach: role-keyword dictionary to remove tagged contributors
#     while preserving natural name hyphens — see cleaning_analysis.py
# =============================================================================

import pandas as pd
import numpy as np

# load raw dataset
audible_df = pd.read_csv('datasets/audible-india/audible_uncleaned.csv')

# -----------------------------------------------------------------------------
# PART 1: Contributor role indicator frequency
# how widespread are role labels across the full author column?
# -----------------------------------------------------------------------------

print("=" * 60)
print("PART 1: CONTRIBUTOR ROLE INDICATOR FREQUENCY")
print("=" * 60)

patterns = [
    'translator', 'Translator',
    'editor', 'Editor',
    'foreword', 'Foreword',
    'introduction', 'Introduction',
    'illustrator', 'Illustrator',
    'Übersetzer', 'traductor', 'traductrice', 'traducteur',
    'tradução', 'traduttore'
]

for pattern in patterns:
    count = audible_df['author'].str.contains(pattern, na=False).sum()
    print(f"  '{pattern}': {count} entries")

# -----------------------------------------------------------------------------
# PART 2: Sample of translator entries — illustrating the pattern
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("PART 2: SAMPLE TRANSLATOR ENTRIES (25 entries)")
print("=" * 60)
print("Illustrates the Name-role pattern and ordering inconsistencies")
print()

pd.set_option('display.max_colwidth', None)
translator_entries = audible_df[
    audible_df['author'].str.contains('translator', na=False)
]['author'].unique()
print(f"Total unique entries containing 'translator': {len(translator_entries)}")
print()
for entry in translator_entries[:25]:
    print(f"  {entry}")
pd.reset_option('display.max_colwidth')

# -----------------------------------------------------------------------------
# PART 3: Full hyphen audit — all unique entries containing hyphens
# used to identify natural name hyphens vs role-separator hyphens
# full output written here; main script references findings only
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("PART 3: ALL UNIQUE ENTRIES CONTAINING HYPHENS (full output)")
print("=" * 60)
print("Used to confirm that role labels are consistently tagged as Name-role")
print("and to identify natural name hyphens that must be preserved")
print()

np.set_printoptions(threshold=np.inf)
hyphen_entries = audible_df[
    audible_df['author'].str.contains('-', na=False)
]['author'].unique()
print(f"Total unique entries with hyphens: {len(hyphen_entries)}")
print()
print(hyphen_entries)
np.set_printoptions(threshold=1000)

# =============================================================================
# PART 4: CHECKING FOR UNKNOWN/ANONYMOUS/MISSING AUTHOR VARIATIONS
# checking raw author column for any values indicating missing authorship
# =============================================================================

print("\n" + "=" * 60)
print("PART 4: UNKNOWN/ANONYMOUS/MISSING AUTHOR VARIATIONS")
print("=" * 60)

# write full unique author values to file for manual inspection
output_path = 'author_unique_values.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(f"Total unique author values: {audible_df['author'].nunique()}\n\n")
    for val, count in audible_df['author'].value_counts().items():
        f.write(f"{count}\t{val}\n")

print(f"Full unique author values written to: {output_path}")
print("Scan this file for any unknown/anonymous/missing variations")

# also do a quick targeted check for the most common suspect patterns
print("\nQuick check for common missing value indicators:")
suspects = ['anonymous', 'unknown', 'anon', 'n/a', 'none', 
            'various', 'div', 'N.N', 'N. N']
for s in suspects:
    count = audible_df['author'].str.contains(s, case=False, na=False).sum()
    if count > 0:
        print(f"  '{s}': {count} entries")
        print(audible_df[audible_df['author'].str.contains(s, case=False, na=False)]['author'].value_counts().head(5).to_string())