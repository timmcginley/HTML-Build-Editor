# 41934 Advanced BIM, Assignment 2
## Group 16: Isabella Vad (s183616) and Amalie Hartvig Jensen (s183619)

**Process of Assignment 2**

First the zip-file was forked from Tim's github account. 
We ran the codes on our machines and tried to understand the different outputs and connections between the html script, java script and index.html file. 

Instead of making changes directly in the index.html file, we focused on making changes in the html-build python file so we could use the code later on in our use case project.

In regards to our chosen use case on the theme of LCA, the target was simply to calculate the number of windows on each level in the buiding.

**Changes made**

In the python file _HTMLBuild_ we added 2 elements:
1. A code in line 98-101 which calculates the total ammount of windows in the building by taking the length of rows in the duplex file.  
2. A function in line 173 called "ClassifiedWindows". Which calculates the ammount of window per level. 

In the javascript file _html-build_ we added 2 element:
1. A code to display the total ammount of windows from _HTMLBuild_, in the properties box in line 21.
2. We added windows per level to the existing code for floors in line 28-33 (note that this is work in progress:) ).

**Results**

We managed to get the correct output of windows per level in the HTMLBuild python code, but didn't manage to get the correct output displayed for all levels in the index.html file due to lack of correct code in the java script (html-build.js).
Notice that only the number of windows on Level 1 are displayed in the viewport when clicking on a floor in the index.html file.
This is subject for future work e.g. using a less hardcoded approach for count of windows in the *classifyWindows* function. 

**License**

The license *GNU General Public License v3.0* was chosen for the script and applied to the github code. 

**Link to Github:**

https://github.com/AmalieHJ/Advanced-BIM-A2.git
