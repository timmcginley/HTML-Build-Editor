(SAME AS Changes.md)

We have made changes to the code that presents the cost of the floor when pressed, it also presents what this cost estimation is based on (how many beams etc.). 

This has been done by editing the html-build.js file and index_duplex.html files. The properties box has been edited by defining a value for Cost_estimate calculating a total cost for all the floors. We have also added abbreviations for columns, beams, walls and slabs as we ran out of space in the "plan box". The "plan box" has been edited to show cost of each floor, and what the cost is based on. The attributes has been defined in the index_duplex.html file and linked to the html-build.js file. 

We have tried to edit the floor_properties in the HTMLBuild.py file so when loading the duplex model we get the index.html file as output with cost_estimates, we could also have done this for the information about what the cost is based on, but for now we have focused on editing the index_duplex.html file. In the future the plan is to edit the code so it extracts the actual building information with the correct values for material quantities and assosiated costs.
