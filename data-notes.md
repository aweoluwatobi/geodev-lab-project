# Data Notes

## GRID3 NGA - Operational Wards v1.0 (Data Updated: 2025)

- **Source:** https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about
- **Downloaded:** 5th September, 2026
- 9,410 features, polygons
- **Columns:**
  - **FID** (integer)
  - **globalid** (text)
  - **uniq_id** (integer)
  - **timestamp** (datetime)
  - **editor** (text)
  - **wardname** (text)
  - **wardcode** (text)
  - **lganame** (text)
  - **lgacode** (text)
  - **statename** (text)
  - **statecode** (text)
  - **amapcode** (text)
  - **status** (text)
  - **source** (text)
  - **urban** (text)

- No nulls in wardname
- Covers Shomolu LGA fully

- COMPLETENESS: good as it is complete for my study area.
- CURRENCY: It was published in 2021 but updated in 2025.
- POSITIONAL: Ward boundary aligns well with google basemap to a good extent.
- ATTRIBUTE: Attribute is reliable.
- FITNESS: adequate for clipping other layers to boundary.

## GRID3 NGA - Schools (Data updated: 2025)

- **Source:** https://data.grid3.org/datasets/GRID3::grid3-nga-schools/about
- **Downloaded:** 5th September, 2026
- 107,670 features, points
- **Columns:**
  - **FID** (integer)
  - **globalid** (text)
  - **uniq_id** (integer)
  - **timestamp** (datetime)
  - **editor** (text)
  - **wardname** (text)
  - **wardcode** (text)
  - **lganame** (text)
  - **lgacode** (text)
  - **statename** (text)
  - **statecode** (text)
  - **secondary** (text)
  - **student_ct** (text)
  - **teacher_ct** (text)
  - **poi_type** (text)
  - **education** (text)
  - **management** (text)
  - **subtype** (text)
  - **category** (text)
  - **name** (text)
  - **source** (text)

- No nulls in subtype
- Coverage looks good but data not fully updated as some primary schools are missing based on my knowledge of the environment.

- COMPLETENESS: few new unregistered primary schools not available in the data so it is not complete.
- CURRENCY: It was published in 2020 but updated in 2025.
- POSITIONAL: School point aligns.
- ATTRIBUTE: Attribute is reliable.
- FITNESS: fit for purpose

## **GRID3 NGA - Modelled gridded population estimates for Nigeria v3.0 (2025)**

- **Source:** https://data.grid3.org/maps/6966d625aea0488496d01debd3bb80f9/about
- **Downloaded:** 5th September, 2026
- Raster Layers
- COMPLETENESS: good
- CURRENCY: It is a 2025 population estimate.
- POSITIONAL: Good.
- ATTRIBUTE: No attribute
- FITNESS: fit for purpose

## CRS and preparation

- All source layers arrived in EPSG: 4326
- Study area: Shomolu, extracted from GRID3 wards
- All layers clipped to study area, then reprojected to EPSG: 32631 (UTM 31N)
- Area check: Not done
- Working files in data/processed/, raw files untouched
