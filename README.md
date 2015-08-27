# Proximity-Score
Customer - PAS

GOAL
PAS receives monthly files "Sales" and "Resales" from PID. Want to provide scoring to allow focus on more qualified properties.

Objective:
1) Apply a set of criteria and determine which criteria are met to facilitate evaluation by PAS.
2) Provide easy access to data (service / use of Geocortex), and 
3) provide a printing template for selected items.

Scoring Criteria

Take the 2 input files (provided monthly by James Wade, PAS), create field (columns in table) to track scoring for each criteria, apply criteria, and update the appropriate field.

Criteria
a) Within Buyout Target areas
a.	Approved - 10
b.	Other – 5
c.	Within 100’ buffer of approved - 3
d.	Within 100' buffer of Other– 1
e.	Outside 100’ buffer - 0
b) Proximity to Ultimate ROW
a.	Main channel - 5
b.	Tributary - 3
c.	Else - 0
c) Proximity to ROW Acquired Buffer
a.	Within 10’ of ROW acquired - 5
b.	Within 100' of ROW acquired - 0.5
c.	Outside 100’ of buffer - 0
d) Proximity to Active and Future CIP w/ 100' buffer – 0.5 
e) If RESALES, not equal to zero – then each score criteria gets additional 2 points
                
Note - scoring is only a PRELIMINARY ranking for providing a suggested sequence for viewing / evaluating.

