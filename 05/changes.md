# A2-Future-BIM

In our work we get inside of HTML-Build-IFC-Converter. How structural use case could be applied to it? – that’s the question worth considering. Used example file was  sufficient for this topic but in general they are built for bigger repetitive buildings. From IFC we would like to get information about beams that are in building. We try to find out their coordinates in space but we will do it in further investigation. Now we get number of beams on each building floor. When end user will need some kind of guidance. It may be hard for him to feel confident in program because some staff could be done in different parts of software environment. Some basic analysis can be performed with already held info. For example calculations of loads that each building part can carry out.

We modified code in main() function inside .js file that now it is possible to find beams that are in uploaded file
 
picture1



With some graphical improvements results could be seen on .html file: 
 
picture2
Getting beam coordinates demand importing correct library that is: ifcopenshell.util.placement in .py file:
picture3
And our fundaments for future code are below:
picture4
