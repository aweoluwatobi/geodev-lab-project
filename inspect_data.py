import csv

def inspect_column(filename, column):
  with open(filename, encoding="utf=8-sig") as f:
    rows = list(csv.DictReader(f))

  values = []
  for row in rows:
    raw = row[column].strip()
    if raw == "":
      continue
    values.append(float(raw))

  return {
    "Smallest": min(values),
    "Largest": max(values),
    "Count": len(values),
  }

pct_within_500m = inspect_column("shomolu_wards.csv", "pct_within_500m")
served_pop = inspect_column("shomolu_wards.csv", "ward_buffer_dissolved_population_served_sum")

print("pct_within_500m:", pct_within_500m)
print("served_pop:", served_pop)