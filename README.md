# Instagram Text Parser

This repository contains a simple Python script written as a learning exercise to
parse raw, unstructured Instagram profile text into structured data and extract
basic insights within a group of profiles.

## What it does
Given a text file containing multiple Instagram profiles in a consistent format,
the script:
- Extracts usernames, names, post counts, follower counts, and following counts
- Normalizes values such as `12.5K` into integers
- Categorizes profiles based on account type
- Answers basic comparative questions within the dataset

## Questions answered
- Who has the maximum number of posts?
- Who has the maximum followers?
- Who follows the maximum people?
- What categories of accounts exist, and how many profiles belong to each?

## How to use
1. Place the raw Instagram profile text in a `.txt` file (see `sample_small.txt`).
2. Ensure the file follows the same spacing and ordering format.
3. Run the script:

```bash
python parser.py
```

## Note
This project is intended as a concept demonstration and learning exercise.
