import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/shomolu_wards.gpkg", layer="shomolu_wards")
facilities = gpd.read_file("data/processed/Shomolu_primary_school.gpkg", layer="Shomolu_primary_school")

fig, ax = plt.subplots(figsize=(7, 8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
facilities.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("Primary schools in Shomolu")
ax.set_axis_off()

fig.savefig("month-03/week-10/schools_map.png", dpi=150, bbox_inches="tight")
print("Map saved")