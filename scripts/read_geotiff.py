"""Inspect an annual soil-retention GeoTIFF without modifying it."""
import argparse
import rasterio

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("path", help="Path to China_Soil_Retention_Service_2023_1km.tif")
args = parser.parse_args()
with rasterio.open(args.path) as ds:
    values = ds.read(1, masked=True)
    print("CRS:", ds.crs)
    print("Resolution (m):", ds.res)
    print("Dimensions (columns, rows):", ds.width, ds.height)
    print("NoData:", ds.nodata)
    print("Unit (provider confirmed): t/(ha*a)")
    print("Valid cells:", values.count())
    if values.count():
        print("Valid range:", float(values.min()), float(values.max()))
