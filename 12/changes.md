# Group 12: 
## Christina Kjær and Julie Bech Liengaard
### Use Case - Acoustics

This document describes the changes made in the HTML-Build-IFC-Converter-main folder/scripts.
Our use case focuses on acoustics, therefore the necessary extractions from the .ifc file are amongst other spaces, areas, volumes and material properties (such as absorption coefficients). 
In this assignment the learning objectives is to develop the python code, we have so far, and implement it in an .html file. 
This is beneficial because .html is an easy way to communicate information about the BIM model without the end user having to have any other software than simply a browser. 
If our implementations are done correctly it should not be necessary for the user to have any prior knowledge about BIM or the building model that is used/displayed.

## Descriptions of changes made
In the scripts HTMLBuild.py, html-build.js and index.html the changes will have a comment after saying "G12: " and a short explanation (usefuld for ctrl+f). 

HTMLBuild.py
All changes are made after line 108 in the original code.
- Line 108 in the custom, added model: custom+= classifyFloors(floors,site_elev, model)
- Around line 135: Inserted outputVolumeArea(model) function to return space_entities (code from blender Assingment 1).
- Inserted space_entities = outputVolumeArea(model) line in the function classifyFloors inside the for loop and stored in floor_entities. 
- From line 185 room numbers and roomnames for each floor are called from object attributes in the IfcBuildingStorey directory. 

html-build.js
Text is changed from "happy" to print something else. 
From the floor entities room and roomnames are called and stored in a roomList. 
Text is displayed in >view< >plan< in a scroll bar. 
After click we added $('props-').prepend('The area of ' +$(this).attr('name') +' is ' +$(this).attr('area') +'<br>'); to insert string with area information. 
The actual area output is coming from the space_entities which is now also embedded in floor_entities. This should be called in the .js file.

index.html (in /output/duplex folder)
space_entities needs to be called in the index.html file where it is inserted in the floor- lines, for example: 
	<floor- class="floor_upper" name='Roof'  level='3' area="Area 4" elev="6.00000000000039" >Roof<span class="floor_stats">6.0</span> </floor->
So far it is printing a string (area = "Area #"), but it should extract the data from the floor_entities (and hence space_entities) which we will work on. 


The code changes so far are helpful to identify spaces in the building on the floors which was the first point in our necessary extractions. 

 
## Future work
In the future new developments and implementations should be able to identify rooms and extract their area and volume. 
It could be useful to get an idea of the geometry shape (rectangular vs non-rectangular) based on number of walls in the space. Acoustics will, however, also be affected based on whether the walls are parallel or not, but this will not be considered at this level.
The idea is to be able to extract material and a suggested absorption coefficients.  
These values are used to calculate the reverberation time  
