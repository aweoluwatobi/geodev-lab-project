import geopandas as gpd

wards = gpd.read_file("data/processed/shomolu_wards.gpkg", layer="grid3_nga_boundary_vaccwards")
schools = gpd.read_file("data/processed/Shomolu_primary_school.gpkg", layer="shomolu_pry_school")

# I summarized all 149 school records since from the data, there are 149 schools in Shomolu LGA and there are schools in each ward. 
# I grouped them by wardname and counted the number of schools in each ward. The result is a new dataframe called school_counts with 16 records.
school_counts = schools.groupby("wardname").size().reset_index(name="school_count")

first_try = wards.merge(school_counts, left_on="wardname", right_on="wardname", how="left")
matched = first_try["wardname"].notna().sum()
print("Matched on first try:", matched, "of", len(wards))