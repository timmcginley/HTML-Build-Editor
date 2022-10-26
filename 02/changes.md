# A2 - Future BIM
Group 2 - Anders Træland and Nicklas Mikkelsen 

## What do we want to achieve with this assignment? 

Seeing that we have Cost Estimation as our use case, we want to make changes in the script that helps to define the quantities of certain materials. By defining the height of each floor in the building, and assume the dimensions of slabs and walls (we assume that beams and columns are included these) we are able to calculate the total volum of concrete in each floor. Seeing as we have not yet received the Molio cost data, we will be making qualified assumptions on the price for each cubic meter. This price will invclude the cost of materials, the cost of labor and so on. The unit price can easily be changed at a later instance. 

## What changes have we made? 
- The first thing that we did was to increase the number of floors by editing in the "index.html" file. We copied the code in line 12-14 and added them to the script, in order to achieve the numbers of floors that we aimed for. We then changed the names of the floors and edited the properties, so that the height of each floor is set to 4 meters. We now have a relatively tall building consisting of two floors "below ground level" (Level -2 and Ground Floor) and 12 additional floors above ground level (Level 0 - level 11). 
- We assume that we have a building consisting of floors with dimensions width x length = 20m x 40m. We assume thickness of walls to be 20 cm and the thickness of the slab to be 25cm. This gives the following volumes:
1) Walls in each floor: Volume_wall = 4m*0.2m*20m + 4m*0.2m*40m = 16m^3 + 32m^3 = 48 m^3  
2) Slabs in each floor: Volume_slab = 40m*20m*0.25m = 200 m^3 
Total volume in each floor: Volume_tot = 48 m^2 + 200 m^3 = 248 m^3 

NOTE: For the ground floow the walls have a height of 6m, hence: 
3) The volume of the walls in this floor is: V_wall2 = 6m*0.2m*20m + 6m*0.2m*40m = 24 m^3 + 48 m^3 = 72 m^3. 
This gives a total volume of 272 m^3 for this floor. 
- First we edit the HTMLBuild.py file. We add and extra dictionary in line 156, called "Volume{}. Further right, in the same line, we add the volume in the same position. 
- The next thing we do is to go in the html-build.js file. On line 17 we add a statement that calculates the total amount of volume in the building. This is supposed to appear underneath the textbox on the website. 
- We also changed the text in the box from "Happy" to "This figure shows the volume of each floor" in line 25. 
- By editing in line 33 we make it possible to print the volume of each floor in the text box, by clicking on the specific floor. 
- We now have the total volume of the building. We assume a price of 1500 DKK per m^3. This is a rough estimate and can and will be edited when we dive deeper into the Molio Cost data. In order to get a more accurate cost, we should also distinguish between the price of slabs, walls etc. This will be done in Assignment 3. 

The total cost of the concrete in the building will therefore be: 

Cost = 3496 m^3 * 1500 DKK/m^3 = 5 244 000 DKK. 




