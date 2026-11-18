import geopandas as gpd

wards = gpd.read_file("data/processed/shomolu_wards.gpkg", layer="grid3_nga_boundary_vaccwards").to_crs(epsg=32631)
pry_schools = gpd.read_file("data/processed/Shomolu_primary_school.gpkg", layer="shomolu_pry_school").to_crs(epsg=32631)

# Calculate area of each ward
wards["area_km2"] = wards.area / 1_000_000

# create a 500m buffer reach around schools and dissolve it to get one polygon
reach = pry_schools[["geometry"]].copy()
reach["geometry"] = reach.geometry.buffer(500)
reach = reach.dissolve()

# Overlay buffer and wards layer and get the ward areas that are uncovered
uncovered = gpd.overlay(wards, reach, how="difference")
uncovered["uncovered_km2"] = uncovered.area / 1_000_000
gaps = uncovered[["wardname","uncovered_km2"]]
# Merge back to ward layer and then ensure NA fields become Zero.
result = wards.merge(gaps, how="left", on="wardname")
result["uncovered_km2"] = result["uncovered_km2"].fillna(0)
# Calculate percentage of uncovered area and round off to 1 decimal place
result["uncovered_pct"] = round(result["uncovered_km2"] / result["area_km2"] * 100, 1)
# print out the ward name, ward area, uncovered area, percentage of uncovered area

print(result[["wardname", "area_km2", "uncovered_km2", "uncovered_pct"]])

uncovered_total = result["uncovered_km2"].sum()

uncovered.to_file("data/processed/shomolu_ward_uncovered.gpkg", layer="shomolu_ward_uncovered")
