import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)
fc_facilities = arcpy.GetParameterAsText(1)
fc_zip = arcpy.GetParameterAsText(2)
arcpy.MakeFeatureLayer_management(fc_facilities, 'facilities_lyr')
arcpy.MakeFeatureLayer_management(fc_zip, 'zip_lyr')
arcpy.management.SelectLayerByLocation('facilities_lyr', 'WITHIN_A_DISTANCE', 'zip_lyr', '3000 Meters')
arcpy.AddMessage('select by location (method - within a distance)')
arcpy.management.SelectLayerByAttribute('facilities_lyr', 'SUBSET_SELECTION', "FACILITY = 'COLLEGE'")
arcpy.AddMessage('select by attribute')
out_path_copylayer = arcpy.GetParameterAsText(3)
arcpy.CopyFeatures_management('facilities_lyr', out_path_copylayer)
arcpy.AddMessage('create layer with selected features')
with arcpy.da.SearchCursor(out_path_copylayer, ["Shape", "ADDRESS", "NAME", "FACILITY"]) as cursor:
    for row in cursor:
        print('Geometry: {0}, Address: {1}, Name: {2}, Facility: {3}'.format(row[0], row[1], row[2], row[3]))
arcpy.AddMessage('get some atrribute data from objects in created layer')
#facilities_Distance_3000_lyr = r"E:\university\3 course\programming in gis\lections\pr6, lab 11\Programming_in_GIS_2024_L6_p11\Results\facilities_Distance_3000_lyr"
arcpy.AddField_management(out_path_copylayer, 'C_NAME', 'DOUBLE')
arcpy.AddMessage('add new field to created layer')
#arcpy.MakeFeatureLayer_management(out_path_copylayer, facilities_Distance_3000_lyr)
#arcpy.management.AddJoin(facilities_Distance_3000_lyr, "NAME", 'facilities_lyr', "NAME")
#arcpy.CalculateField_management(facilities_Distance_3000_lyr, "C_NAME", "!fc_facilities.FAC_ID!", "PYTHON_9.3")
with arcpy.da.UpdateCursor(out_path_copylayer, ["C_NAME", "FAC_ID"]) as cursor:
    for row in cursor:
        row[0] = row[1]
        cursor.updateRow(row)
arcpy.AddMessage('copy data from another field to new field')


