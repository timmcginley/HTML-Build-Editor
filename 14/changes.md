
Group 14


Aim of the HTML
- The aim is to give information of the structural elements in the
  building with an interactive menu, focusing on the beam properties.


1. Changes to HTMLBuild.py

- Beam entity loader in 'writeCustomHTML' function, and a 
  structural subfolder to withhold information on structural '
  elements (114-126). 
	- Made customs (folders) to sort elements loaded from Ifc 
	  store. Make a list of customs that opens the folders and
	  and closes the folders.


- 'ClassifyBeams' function to load in beam entities (192-237).
	- Made a for loop to get information, such as materials.
	  Done by sorting through the Ifc store and selecting
	  wanted properties.
	- Gathering the beam's position in the building, by taking
	  every x, y, z coordinate and putting it into a string.
	- At the end of every loop all the wanted properties are
	  formatted into names, such as "class", "beam name", 
	  "material", etc.


2. Changes to html-build.js
- Calculate num. beams and columns for structural building 
  entities, adding them to properties box (17-38)

	Line 17-25:
	- Putting all information about beams into "beams".
	- Finding the number of beams by finding the length
	  of the "beams" vector.
	- Adding the number of the beams to the console
	- The same is done for columns.
	
	Line 28-38:
	- Putting the property information into the property box
	- Making a box where the possibilities of the program
	  are described.
	
	Line 52-67
	- Making the list of the beams interactable in that it
	  shows the wanted properties when clicking on the given
	  beam.
	

3. Changes to html-build.css
- Structural and beam blocks to model (100-126) 
	- Making a design for the list of beams.


Future work
- We had a desire to include a drawn cross section of the 
  chosen beam along with properties concerning the cross section.
  (see picture in the IMG folder).
  
