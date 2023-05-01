from functools import lru_cache
from constants import Constants
import geopandas as gpd
import pandas as pd




@lru_cache(maxsize=1280)
def open_shp(shp_name: str):
    shp = gpd.read_file(shp_name)
    return shp


async def distance(data: dict) -> dict:
    df = pd.DataFrame(data={'lat': [data.lat], 'lon': [data.lon]})

    geodf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df['lon'], df['lat'], crs="EPSG:4326"))
    geodf = geodf.to_crs(Constants._CRS_)
    dict_return = {}

    for (index, shp) in (Constants._SHP_).items():
        track_line = open_shp(shp)
        track_line.crs = "+proj=utm +zone=23 +south +ellps=intl +units=m +no_defs"
        track_line = track_line.to_crs(Constants._CRS_)
        single_track_line = track_line.unary_union
        dict_return[index +
                    '_km'] = round((geodf.distance(single_track_line) / 1000).loc[0], 2)

    return dict_return

