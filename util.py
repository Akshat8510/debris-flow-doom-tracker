# utils.py
import rasterio
import numpy as np
import pandas as pd

def load_raster(path):
    with rasterio.open(path) as src:
        return src.read(1), src.transform
