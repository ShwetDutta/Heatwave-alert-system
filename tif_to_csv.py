# scripts/tif_to_csv.py

import rasterio
import pandas as pd
import numpy as np
import os

# Path to input TIF file
TIF_PATH = os.path.join("..", "data", "raw", "ehf_eobs_e19HOM_1950-2018_reference_1961-1990_ann_hws.tif")
# Output CSV path
CSV_PATH = os.path.join("..", "data", "processed", "ehf_hws.csv")

def convert_tif_to_csv(tif_path, csv_path):
    with rasterio.open(tif_path) as src:
        band = src.read(1)  # Read first band
        transform = src.transform

        rows, cols = band.shape
        data = []

        for row in range(rows):
            for col in range(cols):
                value = band[row, col]
                lon, lat = transform * (col, row)  # pixel to geographic coords
                data.append([lat, lon, value])

        df = pd.DataFrame(data, columns=["Latitude", "Longitude", "Value"])
        df.to_csv(csv_path, index=False)
        print(f"✅ Data saved to {csv_path}")


if __name__ == "__main__":
    convert_tif_to_csv(TIF_PATH, CSV_PATH)
