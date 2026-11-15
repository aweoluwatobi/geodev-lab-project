# Week 10: GeoPandas, layers as tables

## What this folder contains

- explore_pandas.py: first look at the ward population table
- filter_sort.py: filter, sort and add population in thousand column to ward layer
- explore_layer.py: open a ward vector layer and explore CRS and bounds
- geom_props.py: focus on one ward geometry and print if the shape is well formed and the centroid
- csv_to_points.py: turn health facilities csv into points and export to geopackage format
- join_population.py: joins population to ward polygons after cleaning names
- make_map.py: draw health facilities point layer over wards polygon and export as an map image
- facilities_map.png : map of health facilities by ward
- save_outputs.py: save the outputs of wards to csv after dropping geometry column
- wards_table.csv: CSV Output from the save_outputs.py
- my_explore.py: load my ward data and explore CRS and bounds
- my_points.py: clean the type column of the health_facilities csv and print value_counts() of type before and after
- my_join.py: summarize school layer and join to ward table
- my_map.py: export map of ward and school layer
- my_map.png: map of primary school by wards in shomolu local government
- population_map.png: map of Ibadan wards coloured by population

## How to run it

From the repository root:
uv run month-03/week-10/explore_pandas.py
uv run month-03/week-10/filter_sort.py
uv run month-03/week-10/explore_layer.py
uv run month-03/week-10/geom_props.py
uv run month-03/week-10/csv_to_points.py
uv run month-03/week-10/join_population.py
uv run month-03/week-10/make_map.py
uv run month-03/week-10/save_outputs.py
uv run month-03/week-10/my_explore.py
uv run month-03/week-10/my_points.py
uv run month-03/week-10/my_join.py
uv run month-03/week-10/my_map.py

## What I found

- The Bounds puts my data where I expect. [3.36686455 6.52347934 3.40148813 6.55847896].
- In my_points.py script, after running value_counts() before cleanup of the type column in the health_facilities.csv, Primary Health Care had 9 records and PHC had 8 records. I ensured Primary Health Care is maintained as the naming convention. After cleanup, there was no more PHC and Primary Health Care was now 17 records.
- In my_join.py, i used the ward and school layer in my study and merged using the wardname column. On the first try without any cleaning, 16 out of 16 records matched. That shows the data was clean from download and prepared for any join operation.
- For my_map.png, I used the Shomolu Ward and the Primary School layer and then created the map covering the study area.

## What went wrong and how I fixed it

-In the my_points.py challenge, I did not have any CSV with coordinates as part of my project so I used the health_facilities.csv and cleaned up the type column so that PHC and Primary Health Centre becomes one value.

- In the my_join.py challenge, I didn't have any ward related data I could add to the ward layer so I decided to use the school layers. There are 149 schools for my study and there are schools in each ward after observation. Intially after join, I was getting 149 of 16 records match. I decided to first summarize the schools by wardname. The result is a new dataframe called school_counts with 16 records. After running join operation again, the 16 ward records matched.
