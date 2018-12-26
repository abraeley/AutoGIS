#- Alan Braeley
#- Automating GIS
#- Tools

from shapely.geometry import Point, LineString, Polygon

def getCentroid(geoObj):
    return geoObj.centroid

def getArea(polyObj):
    return polyObj.area

def getLength(geoObj):
    if type(geoObj) is LineString:
        return geoObj.length
    elif type(geoObj) is Polygon:
        return geoObj.exterior.length
    else:
        return "Error: LineString or Polygon geometries required!"

def createPointGeom(x_coord, y_coord):
    return Point(x_coord, y_coord)    

def createLineGeom(pointList):
    '''
    This function takes a list of Point objects and returns themas a LineString object
    '''
    if all(isinstance(point, Point) for point in pointList):
        return LineString(pointList)

def createPolyGeom(ingredients):
    for x in ingredients:
        return Polygon([[p.x, p.y] for p in ingredients])
