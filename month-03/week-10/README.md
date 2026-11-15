# Week 10: GeoPandas, layers as tables

## What this folder contains

- `explore_pandas.py`: first look at the ward population table
- `join_population.py`: joins population to ward polygons after cleaning names
- `facilities_map.png`: map of health facilities by ward

## How to run it

From the repository root:
`uv run month-03/week-10/join_population.py`

## What I found

Initial joins between the ward polygons and population tables missed several records due to naming format mismatches. After applying string cleaning routines to harmonize casing and whitespace, all records successfully matched, allowing for reliable spatial analysis and mapping of health facility distributions[cite: 8, 9, 11].

## What went wrong and how I fixed it

`uv add` failed initially because my project config expected a package structure at `src/geodev_lab_project/` that wasn't initialized yet; I fixed it by creating the missing directory structure and setting up my `.gitignore` to keep untracked workspace files clean[cite: 1, 2, 11].

The bounds of the ward study area used for my project are as follow: [3.36686455 6.52347934 3.40148813 6.55847896]. I can confirm that the bound put my data where I expect.

I used the health_facilities.csv, cleaned up the type column and ensure all PHC and Primary Health Centre becomes one value. When I print the value_counts() before cleanup, Primary Health Centre is 9 and PHC is 8. I decided that all PHC should be named "Primary Health Centre" so after cleanup, the value_count() has no PHC and there are 17 Primay Health Care Centre.

I couldn't really do any new join as I did not have any csv data I could add with a common field name to my layer.

For my_map.png, I used the Shomolu Ward and the Primary School layer and then created the map - my.map.png covering the study area.
