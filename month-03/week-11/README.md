# Week 11: CRS and Spatial Operations

## What this folder contains

- area_wrong_and_right.py: set a layer's area using geographic coordinate (wrong) and then projecte coordinate (right)
- set_vs_to.py: using to_crs to set correct projection and set_crs in the wrong way
- one_point.py: transform a single coordinate in geographic coordinate system to a projected coordinate system
- spatial_ops.py: perform buffer and then count schools per ward
- coverage_gap.py: using overlay to determine area and percentage of uncovered areas that is not within 2km of facilities from the wards centre point
- nearest.py: get the neares facility closest to the centroid of the wards
- clip_dissolve.py: clip road to study area to get the total length and dissolve wards to get the total area
- fix_geometry.py: find and fix invalid geometry
- my_crs.py: independent challenge to reproject CRS to right UTM zone for my study area
- my_count.py: independent challenge to count schools in wards
- my_reach.py: independent challenge that shows coverage gap in my study area.
- my_validity.py: independent challenge that counts invalid geometries in the wards layer
- make_map.py: script to create maps.
  week-11_map.png: map showing uncovered areas in the shomolu local government wards

## How to run it

From the repository root:

- uv run month-03/week-11/area_wrong_and_right.py
- uv run month-03/week-11/set_vs_to.py
- uv run month-03/week-11/one_point.py
- uv run month-03/week-11/spatial_ops.py
- uv run month-03/week-11/coverage_gap.py
- uv run month-03/week-11/nearest.py
- uv run month-03/week-11/clip_dissolve.py
- uv run month-03/week-11/fix_geometry.py
- uv run month-03/week-11/my_crs.py
- uv run month-03/week-11/my_count.py
- uv run month-03/week-11/my_reach.py
- uv run month-03/week-11/my_validity.py
- uv run month-03/week-11/make_map.py

## What I found

- The 32631 ESPG code was chosen because there was need to convert from a geographic coordinate system to a projected coordinate system to calculate area accurately in meters and not in degrees. Also, the estimate_utm_crs(), suggested it too
- There is at least one school in each ward.
- I chose a buffer of 500m since I wanted to know the population of primary school children that live within 500m of a school. Government officials can use this to quickly spot underserved neighborhoods that lack convenient walk-to-school access, helping them decide where public interventions, community school partnerships, or safe walking routes are needed most
- There was no invalid geometry

## Limitation of method

- Using a buffer of 500m nearly covered the whole study area. This will mean almost all wards are completely covered.
- I couldnt use make_valid as the geometry was already valid.