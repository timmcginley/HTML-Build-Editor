## Changes in the script

Since our focus area is indoor climate, we decided to look at the windows instead of the floors. Therefore we changed the script into counting the overall numbers of windows in the building instead. 

![Skærmbillede 2022-10-12 kl  17 28 59](https://user-images.githubusercontent.com/112402480/195385784-2f5bb635-0a8d-4021-99ef-145d61755aa3.jpeg)

To do the changes in the index file, we had to make change in the HTMLBuild.py file. Here we changed one of the custom HTML entitites. The first thing we added was defining the windows from the IFC model, so we later on was able to count them (line 98-99).
After this, we added the windows to the building custome entitity (line 102). 

The display of entities on the site is generated in the js file. We needed to add another property line for the window counting (line 20). In the js file we also played a bit with some of the other text fields on the site. 

In the css file the layout is done, by changing the color on the site.

The original plan was to count the number of windows on each storey instead of the total amount. But it was more complicated than expected. 
