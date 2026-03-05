import numpy as np

# DEM grid parameters
ncols = 40
nrows = 40
xllcorner = 781550.0
yllcorner = 175850.0
cellsize = 100.0
nodata = -9999

# Topography parameters for Gaussian hills
max_height = 2500.0   # height at the center of each hill
min_height = 1900.0   # minimum height

# Setup grid
x = np.linspace(0, (ncols - 1) * cellsize, ncols)
y = np.linspace(0, (nrows - 1) * cellsize, nrows)
xx, yy = np.meshgrid(x, y)

# Initialize DEM with minimum height
dem = np.full((nrows, ncols), min_height)

# Hill parameters
radius = min(ncols, nrows) * cellsize / 4.0  # Each hill covers a quarter of the grid
sigma = radius / 2.0

# Centers for the four hills (one in each quadrant)
centers = [
    (radius, radius),                     # Bottom-left
    (radius, (nrows - 1) * cellsize - radius),  # Top-left
    ((ncols - 1) * cellsize - radius, radius),  # Bottom-right
    ((ncols - 1) * cellsize - radius, (nrows - 1) * cellsize - radius)  # Top-right
]

# Add each hill to the DEM
for cx, cy in centers:
    dist2 = (xx - cx)**2 + (yy - cy)**2
    dem += (max_height - min_height) * np.exp(-dist2 / (2 * sigma**2))

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

