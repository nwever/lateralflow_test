import numpy as np

# DEM grid parameters
ncols = 40
nrows = 40
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

# Grid center
cx = (ncols - 1) * cellsize / 2.0
cy = (nrows - 1) * cellsize / 2.0

# Distance squared from center
dist2 = (xx - cx)**2 + (yy - cy)**2

# Create DEM with Gaussian hill: H = H0 * exp( -r^2 / (2 * sigma^2) )
dem = min_height + (max_height - min_height) * np.exp(-dist2 / (2 * sigma**2))

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

