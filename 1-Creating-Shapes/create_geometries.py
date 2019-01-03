
# coding: utf-8



from shapely.geometry import Point, LineString, Polygon
#- importing the shapely tools



def createPointGeom(x_coord, y_coord):
    '''
    This function takes two coordinates (an x and a y) and transforms them into a
    Point object.
    '''
    return Point(x_coord, y_coord)    


def createLineGeom(pointList):
    '''
    This function takes a list of Point objects and returns themas a LineString object
    '''
    if all(isinstance(point, Point) for point in pointList):
        return LineString(pointList)



def createPolyGeom(ingredients):
    '''
    This function takes a list of points and returns a Polygon object.
    '''
    for x in ingredients:
        return Polygon([[p.x, p.y] for p in ingredients])

