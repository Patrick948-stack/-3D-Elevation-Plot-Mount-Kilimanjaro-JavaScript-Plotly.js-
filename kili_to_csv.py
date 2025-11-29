import rasterio
import csv

input_path = "SRTM.tif"          # your DEM file
output_path = "kili_elevations.csv"

with rasterio.open(input_path) as src:
    band = src.read(1)           # elevation values
    transform = src.transform

    rows, cols = band.shape

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["lat", "lon", "elevation"])

        for i in range(rows):
            for j in range(cols):
                lon, lat = rasterio.transform.xy(transform, i, j)
                elev = band[i, j]
                writer.writerow([lat, lon, int(elev)])
