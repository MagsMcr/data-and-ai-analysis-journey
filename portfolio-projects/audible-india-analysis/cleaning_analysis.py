"""
Audible India — Catalogue Analysis: Data Cleaning & Preparation
===============================================================
Dataset: Audible India Uncleaned Dataset (audible_uncleaned.csv)
Source: https://www.kaggle.com/datasets/snehangsude/audible-dataset
Market: India | Scraped from Audible.in

Business Question:
What does Audible India's catalogue reveal about the structure and
evolution of the Indian audiobook market?

Identifying factors influencing audiobook popularity and commercial
performance to inform content acquisition and pricing strategy.

Analytical Agenda (to be addressed in future analysis phase):
1. Market evolution over time — length, language, price trends
2. Content length and popularity patterns
3. Price, length and ratings relationship
4. Language landscape and market penetration
5. Narrator performance flags
6. Author concentration and catalogue dependency
7. Rating completeness as market maturity indicator
8. Publisher activity and competitive dynamics

Secondary Objective:
To identify data quality issues in collection and storage that may
affect the reliability of future analyses, and to recommend improvements
that would streamline future exports and business reporting.

Note on market scope: This analysis covers the Indian market only.
Methodology is transferable to other regional markets with equivalent
catalogue data.

Author: Magda McCrimmon | GitHub: MagsMcr
Date: March 2026
"""

import pandas as pd
import numpy as np
import os

audible_df = pd.read_csv('datasets/audible-india/audible_uncleaned.csv')
print(audible_df.shape)

# =============================================================================
# SECTION 1: INITIAL INSPECTION
# =============================================================================

print("=" * 60)
print("SECTION 1: INITIAL INSPECTION")
print("=" * 60)

# First rows — get a feel for the data
print("\n--- First 5 rows ---")
print(audible_df.head())

# Column names, data types, non-null counts
print("\n--- DataFrame info ---")
print(audible_df.info())

# Summary statistics for numeric columns
print("\n--- Descriptive statistics ---")
print(audible_df.describe())

# Missing values per column
print("\n--- Missing values per column ---")
print(audible_df.isna().sum())

# =============================================================================
# COLUMN REFERENCE — AUDIBLE INDIA CATALOGUE
# =============================================================================
# Dataset: audible_uncleaned.csv
# Source: Audible India catalogue export (87,489 rows, 8 columns)
# No formal data dictionary available — column notes based on inspection
#
# CONTENT IDENTIFIERS:
#   name         — audiobook title (string)
#                  note: duplicates to be investigated during audit
#
#   author       — author name(s) (string)
#                  note: appears to contain "Written by:" prefix — requires stripping
#
#   narrator     — narrator name(s) (string)
#                  note: appears to contain "Narrated by:" prefix — requires stripping
#                  "anonymous" observed as a value — treat as missing
#
# CONTENT ATTRIBUTES:
#   time         — audiobook duration (string)
#                  note: stored as text e.g. "2 hrs 30 mins" — requires conversion
#                  to numeric (total minutes) for analysis
#
#   releasedate  — publication date (string)
#                  note: stored as text e.g. "16-05-18" — requires conversion
#                  to datetime; format and consistency to be confirmed
#
# MARKET / COMMERCIAL VARIABLES:
#   language     — language of audiobook (string)
#                  note: key variable for language landscape analysis (thread 4)
#                  36 unique values observed — investigate non-standard entries
#
#   stars        — listener rating (string)
#                  note: contains "Not rated yet" as string value (72,417 of 87,489 rows — 83%)
#                  rated entries in format e.g. "4.5 out of 5 stars181 ratings"
#                  three pieces of information in one field:
#                    — numeric rating
#                    — scale ("out of 5 stars") — confirm consistent before discarding
#                    — review count
#                  requires splitting into separate columns during cleaning
#
#   price        — audiobook price in INR (string)
#                  note: stored as text despite appearing numeric
#                  requires conversion — check for currency symbols or text entries

# =============================================================================

# =============================================================================
# SECTION 2: UNIQUE VALUES AUDIT
# =============================================================================

print("=" * 60)
print("SECTION 2: UNIQUE VALUES AUDIT")
print("=" * 60)

for col in audible_df.columns:
    print(f"\n--- {col} ---")
    print(f"Unique values: {audible_df[col].nunique()}")
    print(f"Sample values:\n{audible_df[col].value_counts().head(10)}")
    print()

# =============================================================================
# SECTION 2 FINDINGS: UNIQUE VALUES AUDIT SUMMARY
# =============================================================================

# This audit used value_counts().head(10) to sample the most frequent values
# per column rather than printing all unique values. With 82,767 unique titles
# and 48,374 unique author entries, printing every value would be unusable —
# the top 10 most frequent values per column is sufficient to surface patterns
# and problems at this stage. Where a column has few enough unique values to
# warrant full inspection (language: 36 unique values), this will be done in
# the deeper column investigation below.
#
# ISSUES IDENTIFIED:
#
# name (82,767 unique values)
#   — multiple entries per title observed (e.g. The Art of War: 20 entries)
#   — likely represents different editions, narrators, or language versions
#   — not straightforward duplicates — requires deeper investigation
#
# author (48,374 unique values)
#   — "Written by:" prefix present in all entries — requires stripping
#   — spaces removed between words in names (e.g. "WilliamShakespeare")
#   — non-Latin characters present (Japanese, Russian, others)
#   — non-Latin names are NOT a data quality issue — they reflect the
#     international scope of the catalogue and should be retained as-is
#   — any author-level analysis will be limited for non-Latin entries without
#     additional data enrichment; this will be stated as an explicit limitation
#
# narrator (29,717 unique values)
#   — "Narrated by:" prefix present in all entries — requires stripping
#   — same no-spaces issue as author column
#   — "anonymous" and "uncredited" observed — NOT to be treated as missing
#   — distinction matters: may reflect missing data at extraction, or may
#     accurately reflect what is shown on the platform (narrator not attributed)
#   — to be retained as a distinct category: "narrator not attributed"
#   — analytical note: narrator recognition is a documented factor in audiobook
#     purchasing and listener satisfaction; unattributed narrators may cluster
#     around lower ratings or review counts — worth examining against stars
#     column in analysis phase (connects to analytical thread 5)
#
# time (2,284 unique values)
#   — stored as string e.g. "2 mins", "1 hr 30 mins" — requires numeric conversion
#   — most frequent values are all under 20 minutes — unexpected for audiobooks
#   — may indicate presence of samples, previews, or single-chapter releases
#   — requires investigation before length analysis (analytical thread 2)
#
# releasedate (5,058 unique values)
#   — stored as string in DD-MM-YY format — requires conversion to datetime
#   — two-digit year requires careful handling
#   — format consistency to be confirmed across full column
#
# language (36 unique values)
#   — "English" capitalised, all other languages lowercase — inconsistent
#   — full list of 36 values to be inspected in deeper audit below
#
# stars (665 unique values)
#   — 72,417 of 87,489 rows (83%) contain "Not rated yet" string — not true NaN
#   — rated entries contain three pieces of information in one string:
#       numeric rating / scale confirmation ("out of 5 stars") / review count
#   — requires splitting into separate columns during cleaning
#   — scale consistency to be confirmed before discarding "out of 5 stars" portion
#
# price (1,011 unique values)
#   — stored as string despite appearing numeric — requires conversion
#   — comma present as thousands separator (e.g. "1,172.00") — requires stripping
#   — no currency symbols observed in top 10 — to be confirmed across full column

# =============================================================================

# =============================================================================
# SECTION 3: DEEPER COLUMN INVESTIGATION
# =============================================================================

print("=" * 60)
print("SECTION 3: DEEPER COLUMN INVESTIGATION")
print("=" * 60)

# --- Language: full unique values ---
# 36 unique values — small enough to print in full
# checking for non-standard entries, inconsistent capitalisation,
# or anything unexpected before planning cleaning approach

print("\n--- language: all unique values and counts ---")
print(audible_df['language'].value_counts().to_string())

# --- name: investigating multiple entries per title ---
# sample the most frequently appearing titles and examine
# what differs between entries — narrator? language? edition?

print("\n--- name: investigating multiple entries per title ---")

# look at all rows for a frequently appearing title
sample_title = 'The Art of War'
print(f"\nAll entries for '{sample_title}':")
print(audible_df[audible_df['name'] == sample_title].to_string())

# =============================================================================
# SECTION 3 FINDINGS: DEEPER COLUMN INVESTIGATION SUMMARY
# =============================================================================

# LANGUAGE (36 unique values — full enumeration):
#   — capitalisation inconsistent: "English" and "Hindi" capitalised,
#     all others lowercase, "mandarin_chinese" uses underscore
#   — analytical finding: Hindi < 1% of catalogue on an Indian platform
#     — significant content gap flagged for thread 4 (see README)

# NAME (multiple entries per title):
#   — confirmed NOT duplicates — distinct products (different narrator,
#     duration, release date, price)
#   — name alone is not a reliable deduplication key
#   — all rows to be retained

# ADDITIONAL ISSUES SURFACED:
#   author   — translator/contributor roles baked into field, no consistent
#              separator — more complex than prefix strip alone
#   time     — "and" present in format ("1 hr and 8 mins"), singular/plural
#              variants — conversion logic must account for all variations
#   narrator — multiple narrators comma-separated within single field
#   narrator — "anonymous" and "uncredited" to be retained as distinct
#              category ("narrator not attributed") — not treated as missing
#   stars    — 72,417 rows (83%) contain "Not rated yet" string — not NaN
#              rated entries contain three values in one string:
#              numeric rating / scale / review count
#              scale consistency to be verified before discarding
#              "Not rated yet" retained as meaningful category (thread 7)
#   price    — wide range confirmed (32.00 to 1,003.00 for same title)
#              not a quality issue — reflects genuine product variation
#   price    — comma as thousands separator confirmed — requires stripping
#              before numeric conversion

# =============================================================================
# AUTHOR COLUMN: INVESTIGATION FINDINGS
# full investigation in: author_field_investigation.py
# =============================================================================
# Key findings from pre-cleaning audit:
#   — "Writtenby:" prefix consistent across all entries (10 chars)
#   — contributor roles tagged as Name-role (hyphen, no spaces)
#   — role labels vary by language: translator, Übersetzer, traductor,
#     traductrice, editor, foreword, illustrator, and variants
#   — natural name hyphens also present — must be preserved
#   — cleaning approach: strip prefix, recover spaces via capitalisation regex,
#     remove contributor segments using role-keyword dictionary
#     see Phase 4 for implementation

# =============================================================================
# PHASE 3: CLEANING PLAN
# =============================================================================

# name        — retain all rows; typo correction out of scope without external
#               reference; exact duplicates (identical across ALL columns)
#               checked and dropped post-cleaning

# author      — strip "Writtenby:" prefix (10 chars); recover spaces via
#               capitalisation regex; remove contributor segments using
#               role-keyword dictionary (translator, Übersetzer, traductor,
#               traductrice, traducteur, tradução, traduttore, editor, foreword,
#               illustrator, and variants — full list in author_field_investigation.py)
#               natural name hyphens preserved — dictionary matches role labels
#               only, not name components
#               non-Latin names retained — analytical limitation documented
#               → new col "authors"; original dropped

# narrator    — strip "Narratedby:" prefix (11 chars); recover spaces via
#               same capitalisation regex
#               "anonymous", "uncredited" and variants → "unknown"
#               multiple narrators retained as comma-separated string
#               → new col "narrators"; original dropped

# time        — convert to total minutes (integer)
#               handle all format variants: hrs/hr, mins/min, "and",
#               "Less than 1 minute" → 1
#               → new col "audible_length_m"; original dropped

# releasedate — convert to datetime; verify two-digit year interpretation
#               → in place

# language    — standardise to lowercase; "mandarin_chinese" → "mandarin chinese"
#               → in place

# stars       — split into two new columns:
#               "audible_rating": float, 0.0 where unrated
#               "rater_number": integer, 0 where unrated
#               verify scale consistency before discarding "out of 5 stars"
#               original "stars" dropped after validation

# price       — strip commas; handle "Free" → 0.0; convert to float
#               → new col "price_fixed"; original dropped

# deduplication — after all cleaning, drop rows identical across ALL columns

# output      — save as datasets/audible-india/audible_cleaned.csv
#               raw file never overwritten