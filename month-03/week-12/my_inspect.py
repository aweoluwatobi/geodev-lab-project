import rasterio
folder = "data/raw/landsat/"
scene = "LC08_L2SP_191056_20251117_20251202_02_T1"

with rasterio.open(folder + scene + "_SR_B4.tif") as src:
  print("Width x height:", src.width, "x", src.height)
  print("Bands:", src.count)
  print("Data type:", src.dtypes)
  print("CRS", src.crs)
  print("Pixel size:", src.res)
  print("Bounds:", src.bounds)
  print("Nodata:", src.nodata)
  print("Transform:")
  print(src.transform)