import numpy as np

# DEM grid parameters
ncols = 20
nrows = 20
xllcorner = 781550.0
yllcorner = 175850.0
cellsize = 100.0
nodata = -9999

# Topography parameters for Gaussian
max_height = 2700.0   # height at the center
min_height = 1700.0   # miminum height

# Determine radius and sigma
radius = min(ncols, nrows) * cellsize / 2.0
sigma = radius / 2.0

# Setup grid
x = np.linspace(0, (ncols - 1) * cellsize, ncols)
y = np.linspace(0, (nrows - 1) * cellsize, nrows)
xx, yy = np.meshgrid(x, y)

# Create DEM with a plane
dem = min_height + (max_height - min_height) * (1 - yy / yy.max())

# Write DEM
out_file = "cone.asc"
with open(out_file, "w") as f:
    f.write(f"ncols         {ncols}\n")
    f.write(f"nrows         {nrows}\n")
    f.write(f"xllcorner     {xllcorner}\n")
    f.write(f"yllcorner     {yllcorner}\n")
    f.write(f"cellsize      {cellsize}\n")
    f.write(f"NODATA_value  {nodata}\n")

    for row in dem:
        f.write(" ".join(f"{val:.3f}" for val in row) + "\n")

# Write LUS
out_file = "cone.lus"
with open(out_file, "w") as f:
    f.write(f"ncols         {ncols}\n")
    f.write(f"nrows         {nrows}\n")
    f.write(f"xllcorner     {xllcorner}\n")
    f.write(f"yllcorner     {yllcorner}\n")
    f.write(f"cellsize      {cellsize}\n")
    f.write(f"NODATA_value  {nodata}\n")

    for row in dem:
        f.write(" ".join("12300" for val in row) + "\n")

