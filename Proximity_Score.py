# Import arcpy module
import arcpy

#Inputs
SeptSales = arcpy.GetParameterAsText(0)
SeptReSales = arcpy.GetParameterAsText

# Local variables:
# Criteria Layers
ROW= "ROW - Acquired Grantee"
UltROW100Yr = "sde_ecd.SDE.UltROW100Yr"
BuyoutTargetAreas = "Buyout Target Areas"
ActConsP = "ActConsP"
ActConsL = "ActConsL"
ActConsA = "ActConsA"
ActNonconsP = "ActNonconsP"
ActNonconsL = "ActNonconsL"
ActNonconsA = "ActNonconsA"
FutConsP = "FutConsP"
FutConsL = "FutConsL"
FutConsA = "FutConsA"
FutNonConsP = "FutNonConsP"
FutNonConsL = "FutNonConsL"
FutNonConsA = "FutNonConsA"

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(BuyoutTargetAreas, "NEW_SELECTION", "\"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'Yes'")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", SeptReSales, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field Yes=5
arcpy.CalculateField_management(SeptReSales, "BuyoutTar", "5", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptResales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute 
arcpy.SelectLayerByAttribute_management(BuyoutTargetAreas, "NEW_SELECTION", "\"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" <> 'Yes'")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptResales, "INTERSECT", BuyoutTargetAreas, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field Other=3
arcpy.CalculateField_management(SeptReSales, "BuyoutTar", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute 
arcpy.SelectLayerByAttribute_management(BuyoutTargetAreas, "NEW_SELECTION", "\"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'Yes'")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", SeptReSales, "", "NEW_SELECTION")

# Process: Calculate Field Yes=12
arcpy.CalculateField_management(SeptReSales, "BuyoutTar", "12", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptResales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(BuyoutTargetAreas, "NEW_SELECTION", " \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'Away chan' OR \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'In Review' OR \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'No' OR \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'No Comment' OR \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'Small Area'")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptResales, "INTERSECT", BuyoutTargetAreas, "", "NEW_SELECTION")

# Process: Calculate Field Other=7
arcpy.CalculateField_management(SeptReSales, "BuyoutTar", "7", "VB", "")

# Process: Clear Selection
arcpy.SelectLayerByAttribute_management(SeptResales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(Sept_Resales, "INTERSECT", ActConsP, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptResales, "ActCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptResales, "INTERSECT", ActConsL, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptResales, "ActCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", ActConsA, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "ActCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", ActNonconsP, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "ActCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", ActNonconsL, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "ActCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location (26)
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", ActNonconsA, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field (26)
arcpy.CalculateField_management(SeptReSales, "ActCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", FutConsP, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "FutCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", FutConsL, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "FutCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", FutConsA, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "FutCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", FutNonConsP, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "FutCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", FutNonConsL, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "FutCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", FutNonConsA, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "FutCIP", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptReSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute 
arcpy.SelectLayerByAttribute_management(UltROW100Yr, "NEW_SELECTION", "MainStem_o = 'Main Stem' OR MainStem_o = 'MAIN STEM'")

# Process: intersecting with Sales/Resales 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", UltROW100Yr, "", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "UltR100y", "7", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptResales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute 
arcpy.SelectLayerByAttribute_management(UltROW100Yr, "NEW_SELECTION", "MainStem_o= 'TRB_Studied' OR MainStem_o = 'TRB_Unstudied' OR MainStem_o = 'TRIB-STUDIED' OR MainStem_o = 'TRIB-UNSTUDIED'")

# Process: intersecting with Sales/Resales 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", UltROW100Yr, "", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "UltR100y", "5", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptResales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", ROW, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "ROWA", "2.5", "PYTHON", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptResales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptReSales, "INTERSECT", ROW, "10 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "ROWA", "7", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptResales, "CLEAR_SELECTION", "")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "TotalScore", "[UltR100y] + [BuyoutTar] + [ROWA] + [ActCIP] + [FutCIP]", "VB", "")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "HCFCDDteRc", "Now (  )", "VB", "")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptReSales, "Sale_Resal", "\"Resale\"", "VB", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", ActConsP, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "ActCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", ActConsL, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "ActCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", ActConsA, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "ActCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", ActNonconsP, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "ActCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", ActNonconsL, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "ActCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", ActNonconsA, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "ActCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", FutConsP, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "FutCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", FutConsL, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "FutCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", FutConsA, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "FutCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", FutNonConsP, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "FutCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", FutNonConsL, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "FutCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", FutNonConsA, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "FutCIP", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute 
arcpy.SelectLayerByAttribute_management(BuyoutTargetAreas, "NEW_SELECTION", "\"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'Yes'")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", SeptReSales, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field Yes=3
arcpy.CalculateField_management(SeptSales, "BuyoutTar", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute 
arcpy.SelectLayerByAttribute_management(BuyoutTargetAreas, "NEW_SELECTION", "\"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" <> 'Yes'")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", SeptReSales, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field Other=1
arcpy.CalculateField_management(SeptSales, "BuyoutTar", "1", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(BuyoutTargetAreas, "NEW_SELECTION", "\"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'Yes'")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", SeptReSales, "", "NEW_SELECTION")

# Process: Calculate Field Yes=10
arcpy.CalculateField_management(SeptSales, "BuyoutTar", "10", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute 
arcpy.SelectLayerByAttribute_management(BuyoutTargetAreas, "NEW_SELECTION", " \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'Away chan' OR \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'In Review' OR \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'No' OR \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'No Comment' OR \"sde_is.SDE.BUYOUTTARGETAREAS.PLN_Aprvd\" = 'Small Area'")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", SeptSales, "", "NEW_SELECTION")

# Process: Calculate Field Other=5
arcpy.CalculateField_management(SeptSales, "BuyoutTar", "5", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", ROW, "100 Feet", "NEW_SELECTION")

# Process: Calculate Field
arcpy.CalculateField_management(SeptSales, "ROWA", "0.5", "PYTHON", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Location 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", ROW, "10 Feet", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "ROWA", "5", "VB", "")

# Process: Clear Selection
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute 
arcpy.SelectLayerByAttribute_management(UltROW100Yr, "NEW_SELECTION", "MainStem_o = 'Main Stem' OR MainStem_o = 'MAIN STEM'")

# Process: intersecting with Sales/Resales 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", UltROW100Yr, "", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "UltR100y", "5", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Select Layer By Attribute 
arcpy.SelectLayerByAttribute_management(UltROW100Yr, "NEW_SELECTION", "MainStem_o= 'TRB_Studied' OR MainStem_o = 'TRB_Unstudied' OR MainStem_o = 'TRIB-STUDIED' OR MainStem_o = 'TRIB-UNSTUDIED'")

# Process: intersecting with Sales/Resales 
arcpy.SelectLayerByLocation_management(SeptSales, "INTERSECT", UltROW100Yr, "", "NEW_SELECTION")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "UltR100y", "3", "VB", "")

# Process: Clear Selection 
arcpy.SelectLayerByAttribute_management(SeptSales, "CLEAR_SELECTION", "")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "TotalScore", "[UltR100y] + [BuyoutTar] + [ROWA] + [ActCIP] + [FutCIP]", "VB", "")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "HCFCDDteRc", "Now (  )", "VB", "")

# Process: Calculate Field 
arcpy.CalculateField_management(SeptSales, "Sale_Resal", "\"Sale\"", "VB", "")
