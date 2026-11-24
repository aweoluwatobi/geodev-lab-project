import matplotlib.pyplot as plt
import rasterio

with rasterio.open("data/processed/shomolu_ndvi.tif") as src:
  ndvi = src.read(1, masked=True)
fig, ax = plt.subplots(figsize=(7,8))
image = ax.imshow(ndvi, cmap="RdYlGn", vmin=-0.1, vmax=0.8)
fig.colorbar(image, ax=ax, label="NDVI")
ax.set_title("Vegetation index, Shomolu")
ax.set_axis_off()
fig.savefig("month-03/week-12/my_map.png", dpi=150, bbox_inches="tight")
print("Saved my_map.png")
