import geopandas as gpd

wards = gpd.read_file("data/processed/shomolu_wards.gpkg", layer="grid3_nga_boundary_vaccwards").to_crs(epsg=32631)
pry_schools = gpd.read_file("data/processed/Shomolu_primary_school.gpkg", layer="shomolu_pry_school").to_crs(epsg=32631)

# perform spatial join to determine schools in wards layer
joined = gpd.sjoin(pry_schools, wards[["wardname", "geometry"]], how="inner", predicate="within")
# groupby wardname to get how many schools is in each ward
count = joined.groupby(["wardname_right"]).size().rename("school_count").reset_index()

# join back to the ward layer and ensure any NA field becomes zero
wards = wards.merge(count, how="left", left_on="wardname", right_on="wardname_right")
wards["school_count"] = wards["school_count"].fillna(0).astype(int)
print(wards[["wardname", "school_count"]])

# print total-counted check
school_count_total = wards["school_count"].sum()
print(school_count_total, "of", len(pry_schools), "primary schools")