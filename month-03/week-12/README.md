# Week 11: CRS and Spatial Operations

## What this folder contains

- inspect.py: visualize various parameters of the raster image e.g. widht and height, bands, data type, CRS, Pixel size, Bounds, Nodata value and Transform.
- read_values.py: visualize the shape, minimum, maximum of a DEM before and after exempting the no data value.
- pixel_coords.py: discover the coordinates of the center of a cell and then the pixel position of a coordinate.
- sample_points.py: get sample elevation at each health facilities within the location.
- ndvi.py: computes NDVI from Landsat image and saves it.
- plot_raster.py: maps the ndvi value from the raster and export the ndvi map.
- clip_raster.py: clip the DEM to the study area
- zonal_stats.py: perform zonal statistics with focus on mean elevation per ward.
- reproject_raster.py: reproject the DEM raster from EPSG 32631 to EPSG 4326
- my_inspect.py: It inspects my Landsat raster downloaded from USGS Explorer.
- my_index.py: It computes NDVI from downloaded Landsat scene clipped to my study area, prints the range and mean and save the result.
- my_zonal.py: calcuated mean elevation per ward in my study area and save result to CSV named my_zonal_output.csv.
- my_map.py: plot of NDVI with a colour ramp of Greens
- my_map.png: Vegetation Index of Shomolu
- my_zonal_output.csv: contains mean NDVI per wards

## How to run it

From the repository root:

- uv run month-03/week-11/inspect.py
- uv run month-03/week-11/read_values.py
- uv run month-03/week-11/pixel_coords.py
- uv run month-03/week-11/sample_points.py
- uv run month-03/week-11/ndvi.py
- uv run month-03/week-11/plot_raster.py
- uv run month-03/week-11/clip_raster.py
- uv run month-03/week-11/zonal_stats.py
- uv run month-03/week-11/reproject_raster.py
- uv run month-03/week-11/my_inspect.py
- uv run month-03/week-11/my_index.py
- uv run month-03/week-11/my_zonal.py
- uv run month-03/week-11/my_map.py

## What I found

- The scene name is LC08_L2SP_191056_20251117_20251202_02_T1 which means Landsat 8, Level-2 science product, path 191 row 056, acquired 17th November 2025, processed 2nd December 2025, Collection 2, Tier 1. It was downloaded using Google Earth Engine.The area containing my study area was cloud free. I downloaded both Band 4(Red) and 5(NIR).

- I inspected band 4 The Width is 7443 and the Height is 7703.The left is 396570.0, bottom is 523590.0, right is 619860.0 and top is 754680.0. After checking the width times resolution of the raster, it equals the right minus left.

- For this independent challenge, I decided to calculate NDVI though it doesn't suit my main research question but it was good for independent challenge.
