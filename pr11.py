import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"E:\university\3 course\programming in gis\lections\pr6, lab 11\Programming_in_GIS_2024_L6_p11"
fc_facilities = "facilities.shp"
fc_zip = "zip.shp"
arcpy.MakeFeatureLayer_management(fc_facilities, 'facilities_lyr')
arcpy.MakeFeatureLayer_management(fc_zip, 'zip_lyr')

