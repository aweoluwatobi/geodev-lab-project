import geopandas as gpd

wards = gpd.read_file("data/processed/shomolu_wards.gpkg", layer="grid3_nga_boundary_vaccwards").to_crs(epsg=32631)
pry_schools = gpd.read_file("data/processed/Shomolu_primary_school.gpkg", layer="shomolu_pry_school").to_crs(epsg=32631)

print((~wards.is_valid).sum(), "invalid")
