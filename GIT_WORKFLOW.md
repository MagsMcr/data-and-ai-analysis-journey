# Git Workflow Guide

**Created:** 4 March 2026  
**Purpose:** Document the branching and commit workflow used in this repository  
**Audience:** Myself (and anyone reviewing this portfolio)

---

## Overview

This repository uses a feature branch workflow. All substantive work is done on a dedicated branch, then merged into `main` once complete. This keeps `main` stable and reflects professional team practices.

---

## The Core Workflow

### 1. Start from a clean main

Before creating a branch, make sure you're on `main` and everything is up to date:

```bash
git checkout main
git status
```

`git status` should show "nothing to commit, working tree clean" before you start new work.

---

### 2. Create a new branch

```bash
git checkout -b branch-name
```

The `-b` flag creates the branch and switches to it in one step. You are now working on your branch — `main` is untouched.

Verify with:

```bash
git branch
```

The `*` shows which branch you are currently on.

---

### 3. Do your work and commit

Work as normal. When ready to commit:

```bash
git add .
git commit -m "Descriptive message explaining what this commit does"
```

**Good commit messages** complete the sentence: *"If applied, this commit will..."*

Examples:
- `Add Century Tech company profile`
- `Complete Week 4 pandas practice script`
- `Restructure portfolio folder organisation`

---

### 4. Merge back into main

When the work is complete, switch back to `main` and merge:

```bash
git checkout main
git merge branch-name
```

---

### 5. Push to GitHub

```bash
git push origin main
```

This pushes the merged result to GitHub. The branch itself does not need to be pushed for solo work — GitHub receives the end result via `main`.

---

### 6. Delete the branch

Once merged, delete the local branch to keep things tidy:

```bash
git branch -d branch-name
```

The `-d` flag is a safe delete — it will only delete if the branch has already been merged.

---

## Branch Naming Conventions

Branches are named descriptively in lowercase with hyphens. The format used in this repository is:

```
category/short-description
```

Examples:
- `research/century-tech`
- `research/week3-catchup`
- `portfolio/restructure`
- `practice/week4-scripts`

---

## When to Create a Branch

A branch should represent one coherent piece of work. If you are doing two unrelated things, they deserve two separate branches.

**Create a branch for:**
- A new portfolio project or practice script
- A research or documentation task
- Any significant restructuring of the repository
- Anything experimental you might want to discard

**Not necessary for:**
- Tiny typo fixes
- Minor README edits directly on main

---

## Key Commands Reference

| Command | What it does |
|---|---|
| `git branch` | List all branches, shows current branch with `*` |
| `git checkout -b branch-name` | Create and switch to a new branch |
| `git checkout branch-name` | Switch to an existing branch |
| `git merge branch-name` | Merge a branch into your current branch |
| `git branch -d branch-name` | Delete a branch (safe — only if already merged) |
| `git push origin main` | Push main to GitHub |

---

## A Note on Branches and GitHub

Branches created locally do not appear on GitHub unless explicitly pushed with `git push origin branch-name`. For solo work, this is rarely necessary — the branch is a local working tool, and only the merged result on `main` needs to reach GitHub.

In team settings, branches are pushed to GitHub so colleagues can review work before it is merged. This review process is called a **pull request (PR)** — a concept to return to when working collaboratively.

---

*File location: `GIT_WORKFLOW.md` (root of repository)*  
*Last updated: 4 March 2026*