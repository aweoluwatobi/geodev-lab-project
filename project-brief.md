# My Project Brief

## The Question

What percentage of primary school-aged children in each ward of Shomolu Local Government Area, Lagos State, live within 500 meters of a primary school?

## Why It Matters

Local government officials can use this to quickly spot underserved neighborhoods that lack convenient walk-to-school access, helping them decide where public interventions, community school partnerships, or safe walking routes are needed most.

## The Data I Need

- **Operational Ward Boundaries:** Vector polygon dataset of administrative wards in Shomolu LGA (`GeoPackage / .gpkg`). Size: 15.6 MB
- **Primary School Locations:** Vector point dataset containing spatial locations of primary schools (`GeoPackage / .gpkg`). Size: 30.8 MB
- **Gridded Population Estimates:** High-resolution 100m raster layers representing target age groups (e.g., female and male population age) (`GeoTIFF / .tif`). Size: 1.71 GB

## Where Each Dataset Comes From

- **GRID3 NGA - Operational Wards v1.0 (Data Updated: 2025):**
  [GRID3 NGA - Operational Wards v1.0 on GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about)
- **GRID3 NGA - Schools (Data updated: 2025):**
  [GRID3 NGA - Schools on GRID3 Data Hub](https://data.grid3.org/datasets/GRID3::grid3-nga-schools/about)
- **GRID3 NGA - Modelled gridded population estimates for Nigeria v3.0 (2025):**
  [GRID3 NGA - Population Estimate v3.0 on GRID3 Data Hub](https://data.grid3.org/maps/6966d625aea0488496d01debd3bb80f9/about)

## What I Would Build

A simple interactive web dashboard for Shomolu local government officers that displays a map alongside a summary chart. The map shows ward boundaries shaded from red to green based on their overall access level, with school location points and their 500m circular coverage areas layered on top. When an officer clicks on any ward on the map, the simple chart next to it updates to show the total number of children who live close enough to a school versus those who live too far.
