# Import arcpy module
import arcpy
import arcgisscripting
import locale
import os
import sys

gp = arcgisscripting.create(10.1)

# Local variables:

Sales = gp.GetParameter (0)
Resales = gp.GetParameter (1)

# Process: Add Field Year, Month, UltROW,BuyoutTar,ROWA,ActCIP, FUTCIP for Sales
arcpy.AddField_management(Sales, "YEAR", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Sales, "MONTH", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Sales, "UltROW10", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Sales, "BuyoutTar", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Sales, "ROWA", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Sales, "ActCIP", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Sales, "FutCIP", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field Year, Month, UltROW,BuyoutTar,ROWA,ActCIP, FUTCIP for ReSales
arcpy.AddField_management(Resales, "YEAR", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Resales, "MONTH", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Resales, "UltROW10", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Resales, "BuyoutTar", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Resales, "ROWA", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management(Resales, "ActCIP", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field FutCIP 
arcpy.AddField_management(Resales, "FutCIP", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

