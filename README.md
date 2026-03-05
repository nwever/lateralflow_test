# lateralflow_test

### Generating synthetic DEMs

There are 3 options for synthetic DEMs:

1. `synthetic_dem.py`: a single gaussian hill
2. `synthetic_dem_fourhills.py`: four gaussian hills
3. `synthetic_dem_plane.py`: a simple plane with constant angle

The python scripts write a file `cone.asc` that contains the DEM. To get the slope angles in `cone.slope`, run: `gdaldem slope -of AAIGrid cone.asc cone.slope`
