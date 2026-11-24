import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

with rasterio.open("data/processed/shomolu_ndvi.tif") as src:
  wards = gpd.read_file("data/processed/shomolu_wards.gpkg", layer="grid3_nga_boundary_vaccwards").to_crs(src.crs)
  means = []
  for geom in wards.geometry:
    cells, _ = mask(src, [geom], crop=True, filled=False)
    means.append(float(cells.mean()))

wards["mean_ndvi"] = np.round(means, 1)
wards.to_csv("month-03/week-12/my_zonal_output.csv", columns=["wardname", "mean_ndvi"], index=False)
