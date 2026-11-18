import geopandas as gpd

wards = gpd.read_file("data/processed/shomolu_wards.gpkg", layer="grid3_nga_boundary_vaccwards")
pry_schools = gpd.read_file("data/processed/Shomolu_primary_school.gpkg", layer="shomolu_pry_school")

print("Ward CRS", wards.crs)
print("School CRS", pry_schools.crs)

print("Suggested CRS", wards.estimate_utm_crs())

wards_utm = wards.to_crs(epsg=32631)
schools_utm = pry_schools.to_crs(epsg=32631)

wards_utm["area_km2"] = wards_utm.area / 1_000_000

print(wards_utm[["wardname", "area_km2"]])

wards_utm.to_file("data/processed/shomolu_wards_utm.gpkg", layer="shomolu_ward_utm")
schools_utm.to_file("data/processed/shomolu_pry_school_utm.gpkg", layer="shomolu_pry_school_utm")