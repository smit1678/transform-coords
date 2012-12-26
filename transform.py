from osgeo import gdal,osr

# Transform from Minna / Nigeria Mid Belt to WGS84
#   http://www.spatialreference.org/ref/epsg/26392/
#   Minna/Nigeria Mid Belt EPSG = 26392
#   WGS83 EPSG = 4326

inSRS = 26392
outSRS = 4326

def transformTo(easting, northing, inSRS, outSRS):

    inproj = osr.SpatialReference()
    outproj = osr.SpatialReference()

    inproj.ImportFromEPSG(inSRS)
    outproj.ImportFromEPSG(outSRS)

    transForm = osr.CoordinateTransformation(inproj, outproj)

    transformed = transForm.TransformPoint(easting,northing)

    return transformed 

# Print test point
print transformTo(401190, 72819, inSRS, outSRS)