import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)

shomolu_wards = gpd.read_file("data/processed/shomolu_wards.gpkg", layer="grid3_nga_boundary_vaccwards")
pry_schools = gpd.read_file("data/processed/Shomolu_primary_school.gpkg", layer="shomolu_pry_school")
print(shomolu_wards.head())

fig, ax = plt.subplots(figsize=(8, 7.5))
shomolu_wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
pry_schools.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("Primary schools in Shomolu Local Government")
ax.set_axis_off()

fig.savefig("month-03/week-10/my_map.png", dpi=150, bbox_inches="tight")
print("Map saved")


wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
pop = pd.read_csv("data/raw/ward_population.csv")

first_try = wards.merge(pop, left_on="ward_name", right_on="ward", how="left")
matched = first_try["population_2024"].notna().sum()
print("Matched on first try:", matched, "of", len(wards))

def clean_name(name):
    return name.strip().upper().replace("-", " ")

wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward"].apply(clean_name)

joined = wards.merge(pop, on="join_key", how="left")
matched = joined["population_2024"].notna().sum()
print("Matched after cleaning:", matched, "of", len(wards))
print(joined[["ward_name", "population_2024"]])

fig, ax = plt.subplots(figsize=(8, 7.5))

joined.plot(
    ax=ax, 
    column="population_2024", 
    edgecolor="#ffeeff", 
    cmap="Greens", 
    legend=True, 
    legend_kwds={"label": "Population 2024"}
    )

ax.set_title("Ibadan Wards Population Distribution")
ax.set_axis_off()

fig.savefig("month-03/week-10/population_map.png", dpi=150, bbox_inches="tight")
print("Map saved")