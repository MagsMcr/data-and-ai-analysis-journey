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
#               capitalisation regex
#               split into two new columns:
#               "authors" — primary authors only (segments with no role label)
#                           spaces recovered via capitalisation regex
#                           non-Latin names retained as-is
#               "contributors" — all tagged contributor segments retained
#                           as-is (translators, editors, illustrators, etc.)
#                           preserved for potential future analysis
#                           not cleaned — raw contributor strings minus prefix
#               role-keyword dictionary used to distinguish primary authors
#               from contributors — full list in author_field_investigation.py
#               original "author" column dropped
#               note: where ALL segments carry a role label, "authors" = "unknown"
#               post-cleaning: unique values exported for verification;
#               unknown/anonymous/various variants handled separately

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

# =============================================================================
# PHASE 4: CLEANING — AUTHOR
# =============================================================================
# full investigation of author field patterns in: author_field_investigation.py
# role-keyword dictionary used to separate primary authors from contributors

import re

ROLE_KEYWORDS = [
    'translator', 'Translator', 'translatedby', 'Translatedby',
    'Übersetzer', 'Übersetzung',
    'traductor', 'traductora', 'traductrice', 'traducteur',
    'tradução', 'traduttore', 'traductora',
    'editor', 'Editor', 'editedby', 'Editedby', 'editorandtranslator',
    'editortranslatorannotation', 'editorandcompiler', 'editor/translator',
    'editor/compilation', 'editortranslator', 'editorintroduction',
    'foreword', 'Foreword', 'forewordby', 'Forewordby', 'ForewordPhD',
    'foreward', 'forewardby', 'Forewardby',
    'introduction', 'Introduction',
    'illustrator', 'Illustrator', 'ilustrador', 'ilustrador', 'Illustrateur',
    'contributor', 'Contributor', 'contributions',
    'afterword', 'Afterword', 'afterwordby',
    'preface', 'with', 'With', 'scribe', 'adaptation', 'adaption',
    'creator', 'photographer', 'director', 'Director',
    'compilation', 'compilador', 'curatore',
    'forewordandcontributor', 'introductioncontributor',
    'translatorcontributor', 'translatorandeditor',
    'prefaceandnotes', 'commentaryby', 'commentaries',
    'Serieseditedby', 'translatorintroduction', 'translatorafterword',
    'editorforeword', 'forewordMDFAAP', 'translatorafterword',
]

def split_author_field(text):
    """
    Strip prefix, split into primary authors and contributors
    using role-keyword dictionary.
    Returns tuple: (authors_string, contributors_string)
    """
    # strip "Writtenby:" prefix (10 chars)
    text = text[10:]
    
    # split on comma to get individual segments
    segments = [s.strip() for s in text.split(',') if s.strip()]
    
    primary = []
    contributor = []
    
    for segment in segments:
        has_role = False
        if '-' in segment:
            parts = segment.split('-')
            for part in parts[1:]:
                part_clean = part.strip().rstrip('.,')
                if any(part_clean.startswith(role) for role in ROLE_KEYWORDS):
                    has_role = True
                    break
        if has_role:
            contributor.append(segment)
        else:
            primary.append(segment)
    
    # recover spaces from capitalisation for primary authors only
    authors_str = ', '.join(primary)
    authors_str = ' '.join(re.sub(r"([A-Z])", r" \1", authors_str).split())
    
    # contributors retained as-is (raw, uncleaned)
    contributors_str = ', '.join(contributor)
    
    return (authors_str if authors_str else 'unknown', contributors_str)


print("\n--- cleaning: author ---")
audible_df['authors'] = audible_df['author'].apply(
    lambda x: split_author_field(x)[0]
)
audible_df['contributors'] = audible_df['author'].apply(
    lambda x: split_author_field(x)[1]
)
audible_df = audible_df.drop('author', axis=1)

# verify
print(audible_df[['authors', 'contributors']].head(20).to_string())
print(f"\nUnknown authors: {(audible_df['authors'] == 'unknown').sum()}")
print(f"Entries with contributors: {(audible_df['contributors'] != '').sum()}")

# =============================================================================
# AUTHOR: EXPORTING UNIQUE VALUES FOR VERIFICATION
# =============================================================================
# — post-cleaning verification revealed 329 entries where authors = 'unknown'
#   (cases where every author field segment carried a contributor role label)
# — decision taken to investigate further for any other missing/anonymous
#   variants before standardisation — particularly multi-language equivalents
#   not caught during Phase 2 audit (e.g. "N.N.", "Diverse", "Autori Vari")

output_path = 'portfolio-projects/audible-india-analysis/author_unique_values_cleaned.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(f"Total unique author values (cleaned): {audible_df['authors'].nunique()}\n\n")
    for val, count in audible_df['authors'].value_counts().items():
        f.write(f"{count}\t{val}\n")

print(f"Unique author values written to: {output_path}")

# Cleaned author unique values were exported to author_unique_values_cleaned.txt
# and fed to AI to review for any remaining anomalies requiring standardisation:
# - several entries were identified as potentially indicating unknown or anonymous
# authorship — expressed in different languages and conventions across the dataset
# - among these, N. N. entries were suspected to be the Latin "nomen nescio"
# (name unknown) — and are being verified in context before standardising.

# quick verification: checking N. N. entries in context
print("\n--- authors: N. N. verification sample ---")
pd.set_option('display.max_colwidth', None)
print(audible_df[audible_df['authors'] == 'N. N.'][['name', 'language', 'narrator']].sample(20, random_state=42).to_string())
pd.reset_option('display.max_colwidth')

# =============================================================================
# AUTHOR: STANDARDISING UNKNOWN AND VARIOUS AUTHORSHIP VALUES
# =============================================================================
# review of author_unique_values_cleaned.txt identified three categories
# of entries: 
#
# GENUINE UNKNOWNS — will be standardised to "unknown":
#   "unknown" (329)         — produced by cleaning function where no primary
#                             author segment was identifiable
#   "N. N." (128)           — Latin "nomen nescio" (name unknown),
#                             confirmed as anonymous authorship
#   "auteurinconnu" (17)    — French "unknown author"
#   "auteursinconnus" (1)   — French plural equivalent
#   "Anonymous" (15)        — English
#   "anonymous" (4)         — lowercase variant
#   "Anonimo" (2)           — Italian equivalent
#   "Unknown" (4)           — capitalised variant
#
# COLLECTIVE AUTHORSHIP — will be standardised to "various authors":
#   "div." / "Div." (274+7) — German/Dutch abbreviation for "diverse authors"
#   "Variousauthors" (88)   — spacing artefact from cleaning
#   "variousauthors" (4)    — lowercase variant
#   "Various" (22)          — abbreviated form
#   "various" (5)           — lowercase variant
#   "Various Authors" (3)   — spaced variant
#   "Autori Vari" (57)      — Italian equivalent
#   "Diverse" (34)          — German/Italian equivalent
#   "Diverse, Variousauthors" (5) — combined variant
#   retained as distinct category — anthology/compilation content may differ
#   meaningfully in ratings and pricing from single-author works
#
# EDGE CASES — retained as-is:
#   "Alcoholics Anonymous"           — organisation name, not missing value
#   "Unknown Soldier"                — known historical anonymous, not missing
#   "Anonymous(former Olympian)"     — attributed anonymous, not missing
#   "Karen Joy Hardwick M Div M S W" — "Div" is academic qualification
#   "Elijah C. Nealy Ph D M Div L C S W" — same
#   mixed entries e.g. "Hans Scholl, div." — real author with collective
#                             co-authors; context preserved as-is

# standardisation maps
UNKNOWN_AUTHORS = [
    'unknown', 'Unknown', 'N. N.', 'auteurinconnu', 'auteursinconnus',
    'Anonymous', 'anonymous', 'Anonimo', 'Anonimo'
]

VARIOUS_AUTHORS = [
    'div.', 'Div.', 'Variousauthors', 'variousauthors', 'Various',
    'various', 'Various Authors', 'Autori Vari', 'Diverse',
    'Diverse, Variousauthors'
]

audible_df['authors'] = audible_df['authors'].replace(UNKNOWN_AUTHORS, 'unknown')
audible_df['authors'] = audible_df['authors'].replace(VARIOUS_AUTHORS, 'various authors')

# verify
print("\n--- authors: standardisation verification ---")
print(f"'unknown' entries: {(audible_df['authors'] == 'unknown').sum()}")
print(f"'various authors' entries: {(audible_df['authors'] == 'various authors').sum()}")

# =============================================================================
# PHASE 4: CLEANING — NARRATOR
# =============================================================================

def clean_narrator_field(text):
    # strip "Narratedby:" prefix (11 chars) and recover spaces from capitalisation
    stripped = text[11:]
    return ' '.join(re.sub(r"([A-Z])", r" \1", stripped).split())

print("\n--- cleaning: narrator ---")
audible_df['narrators'] = audible_df['narrator'].apply(clean_narrator_field)
audible_df = audible_df.drop('narrator', axis=1)

print(audible_df['narrators'].head(20).to_string())
print(f"\nTotal unique narrator values: {audible_df['narrators'].nunique()}")

# export unique values for systematic review before standardisation
# same approach as author column — reviewing full unique value list avoids
# missing language variants and unconventional expressions of unknown/anonymous
output_path = 'portfolio-projects/audible-india-analysis/narrator_unique_values_cleaned.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(f"Total unique narrator values (cleaned): {audible_df['narrators'].nunique()}\n\n")
    for val, count in audible_df['narrators'].value_counts().items():
        f.write(f"{count}\t{val}\n")

print(f"Unique narrator values written to: {output_path}")

# Cleaned narrator unique values were exported to narrator_unique_values_cleaned.txt
# and reviewed with AI for any remaining anomalies requiring standardisation:
# - several entries were identified as potentially indicating unknown or anonymous
# narration — expressed in different conventions across the dataset.
# - "uncredited" entries (326) are standardised to "unknown"

# GENUINE UNKNOWNS — standardised to "unknown":
#   "anonymous" (1,034)     — lowercase variant
#   "Anonymous" (160)       — capitalised variant
#   "unknown" (9)           — already correct
#   "uncredited" (326)      — narrator exists but not credited by platform
#   "Sylvia Browne, uncredited" (1) — named narrator with uncredited co-narrator

# COLLECTIVE/VARIOUS — standardised to "various narrators":
#   "div." (230)             — German/Dutch abbreviation
#   "various" (11)           — lowercase variant
#   "Various" (11)           — capitalised variant
#   "variousnarrators" (1)   — spacing artefact from cleaning
#   "Various Narrators" (1)  — spaced variant
#   "variousvarious" (1)     — data entry error, same meaning
#   "Diverse Diverse" (1)    — same

# EDGE CASES — retained as-is:
#   "Anonymousmembersof Al- Anon Family Groups" — organisation name
#   mixed entries e.g. "Marc Thompson, Various" — named narrator with
#                       various co-narrators; context preserved as-is

UNKNOWN_NARRATORS = [
    'anonymous', 'Anonymous', 'unknown', 'uncredited'
]

VARIOUS_NARRATORS = [
    'div.', 'various', 'Various', 'variousnarrators',
    'Various Narrators', 'variousvarious', 'Diverse Diverse'
]

# handle "Sylvia Browne, uncredited" separately — replace uncredited portion
audible_df['narrators'] = audible_df['narrators'].str.replace(
    ', uncredited', '', regex=False
)

audible_df['narrators'] = audible_df['narrators'].replace(
    UNKNOWN_NARRATORS, 'unknown'
)
audible_df['narrators'] = audible_df['narrators'].replace(
    VARIOUS_NARRATORS, 'various narrators'
)

# verify
print("\n--- narrators: standardisation verification ---")
print(f"'unknown' narrators: {(audible_df['narrators'] == 'unknown').sum()}")
print(f"'various narrators' entries: {(audible_df['narrators'] == 'various narrators').sum()}")