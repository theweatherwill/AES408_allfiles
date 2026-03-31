def convert_lon(lon):
    if lon <= 0:
        lon = lon + 180
    else:
        lon = lon + 180
    return lon

def test_convert_lon():
    lon_expected = {
        -180:0,
        0:180,
        180:360
    }
    lon_actual = {}

    for lon in lon_expected:
        actual_longitude = convert_lon(lon)
        lon_actual[lon] = actual_longitude

    print(lon_actual)
    print(lon_expected)
    assert lon_actual == lon_expected

test_convert_lon()

from shapely import Polygon
import geopandas as gpd

def area_poly(poly, crs):
    gdf = gpd.GeoDataFrame(geometry=[poly], crs="EPSG:32616")
    # Suggest by Google/Gemini after continous errors
    return gdf.geometry.area.iloc[0]

def test_area_poly():
    area_expected = {
        Polygon([(0,0), (1,0), (1,1), (0,1)]): 1*1,
        Polygon([(0,0), (50,0), (50,50), (0,50)]): 50*50,
        Polygon([(0,0), (0,0), (0,0), (0,0)]): 0,
    }
    area_actual = {}

    for poly in area_expected:
        actual_area = area_poly(poly, crs="EPSG:4326")
        area_actual[poly] = actual_area

    print(area_actual)
    print(area_expected)
    assert area_actual == area_expected

test_area_poly()