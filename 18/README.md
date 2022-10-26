''' Written by Emilie, Maria, Rikke og Helena 2022''''

--------------------------------------------- Goal ---------------------------------------------

The vision of the BIM project is to provide easy knowledge sharing between 
relevant stakeholders, when estimating the needed ventilation flow for a given 
building.  
 

Example of a use case situation: 
A building owner would like to get a quick overview of the estimated ventilation 
requirements for new buildings and for managing old buildings, when  these are renovated. 
Architects and engineers design the building layout and the building owner would like the 
communication between the construction site manager and the architects/engineers to run 
smoothly with a consistent workflow from project to project.  

So far, the project updates have been shared on a platform, where pdfs, drawings and models 
are uploaded, but it is always different formats and there is often need to install new 
software.   
With this BIM project the users can access the information on updates without downloading 
software or buying a new license. 
 

The vision is to make it possible for the engineers and architects to export their BIM model 
to an IFC file, run our script and freely share the air flow rate results to the rest of the 
team through a webpage link.  



 ------------------------------------ FEATURE AND REQUIREMENTS ----------------------------------

The features of the BIM tool are:
- Conversion from IFC to HTML enabling accessibility and easy to share ventilation requirements 
  between stakeholders 
- Shorten the time spent on calculating the total inlet and outlet air flow with instant 
  feedback 
- Provide a quick overview of the specific rooms (kitchen and toilets), which require an 
  outlet and their corresponding floor level 
 

The requirements of the BIM tool are:  
- The user must be able to export their BIM model in an IFC format 
- Room types must be defined as a property  
- The script will so far only work for residential buildings 


 
------------------------------- HOW WE ATTEMP TO MEET THE GOAL -------------------------------------

See picture "ProcessTree" in img folder: 
"HTML-Build-IFC-Converter-main\HTML-Build-IFC-Converter-main_Group18\img\ProcessTree.PNG"

------------------------------------ IDENTIFYING A LICENSE ------------------------------------------

When choosing a licence for our script, we should think of what is best for the user and future 
scenarios. At the moment, the script is super simple and can therefore easily be used by 
non-engineers. The scripts would benefit from other developers, that are able to construct and 
distribute new better versions based on the software. A collective quality guarantee can therefore 
be achieved from an open-source perspective. 

Furthermore, it is possible to expand with other 
calculations (other functions?) that can help the user. The concept of BIM is still in development 
and the evolution of the building industry has not yet embraced the scope of possibilities 
(maybe because some people find it unrealistic…). But we believe when developing new BIM software
(especially in the early stages) that the knowledge (the software) should be open and free for 
others to use. 
We are able to have this point of view because our software currently is not dependented on any 
economic factors. 

At the moment, we have chosen the MIT licence, because we think that is has the least conditions 
and therefore will be easily accessed for others.  




 

