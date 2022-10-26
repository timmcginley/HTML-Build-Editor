''' written by Tim McGinley 2022 '''

import ifcopenshell
import os.path
import time

def modelLoader(name):

    ''' 
        load the IFC file 
    '''
    
    model_url = "model/"+name+".ifc"
    start_time = time.time()

    if (os.path.exists(model_url)):
        model = ifcopenshell.open(model_url)
        print("\n\tFile    : {}.ifc".format(name))
        print("\tLoad    : {:.2f}s".format(float(time.time() - start_time)))
        
        start_time = time.time()
        writeHTML(model,name)
        print("\tConvert : {:.4f}s".format(float(time.time() - start_time)))
        
    else:
        print("\nERROR: please check your model folder : " +model_url+" does not exist")

def writeHTML(model,name):

    ''' 
        write the HTML entities 
    '''
    
    # parent directory - put in setting file?
    parent_dir = "output/"
    # create an HTML file to write to
    if (os.path.exists("output/"+name))==False:
        path = os.path.join(parent_dir, name)
        os.mkdir(path)
    
    f_loc="output/"+name+"/index.html"
    f = open(f_loc, "w")
    cont=""
    
    # ---- START OF STANDARD HTML
    cont+=0*"\t"+"<html>\n"
    # ---- ADD HEAD
    cont+=1*"\t"+"<head>\n"
    # ---- ADD HTMLBUILD CSS - COULD ADD OTHERS HERE :)
    cont+=2*"\t"+"<link rel='stylesheet' href='../css/html-build.css'></link>\n"
    # ---- ADD HTMLBUILD JS - COULD ADD OTHERS HERE :)
    cont+=2*"\t"+"<script src='../js/html-build.js'></script>\n"
    # ---- JQUERY - IT WOULD BE CRAZY NOT TO
    cont+=2*"\t"+"<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.js'></script>\n"
    # ---- CLOSE HEAD
    cont+=1*"\t"+"</head>\n"
    # ---- ADD BODY
    cont+=1*"\t"+"<body onload=\"main()\">\n"  
    
    # ---- ADD CUSTOM HTML FOR THE BUILDING HERE
    cont+=writeCustomHTML(model)
    
    # ---- CLOSE BODY AND HTML ENTITIES
    cont+=1*"\t"+"</body>\n"   
    cont+=0*"\t"+"</html>\n"

    # ---- WRITE IT OUT
    f.write(cont)
    f.close()

    # ---- TELL EVERYONE ABOUT IT
    print("\tSave    : "+f_loc)

def writeCustomHTML(model):

    ''' 
        write the custom HTML entities 
    '''
    
    custom=""
    site_elev = 0 # variable for to store the elevation of the site
    
    # ---- DEFINE THE MODEL
    
    custom+=2*"\t"+"<model->\n"
    
    # ---- ADD PROJECT CUSTOM ENTITY
    project = model.by_type('IfcProject')[0]
    custom+=3*"\t"+"<project- name=\"{d}\">\n".format(d=project.LongName)
    # it looks like it would make sense to use the DOM here and append stuff to it...
    
    # ---- ADD SITE CUSTOM ENTITY
    site = model.by_type('IfcSite')[0]
    site_elev = site.RefElevation
    custom+=4*"\t"+"<site- lat=\"{}\" long=\"{}\" elev=\"{}\">\n".format(site.RefLatitude,site.RefLongitude,site_elev )

    # ---- ADD BUILDING CUSTOM ENTITY
    custom+=5*"\t"+"<building->\n"
    
   
    
    # ---- ADD FLOOR CUSTOM ENTITIES
    floors = model.by_type('IfcBuildingStorey')
    floors.sort(key=lambda x: x.Elevation, reverse=True)
   
    
    # ---- CLASSIFY THE FLOORS AS LOWER, GROUND OR UPPER AND WRITE TO CUSTOM ENTITIES
    custom+= classifyFloors(floors,site_elev, model) # G12: inserted model, which is used later in the outputVolumeArea function
    
    # ---- CLOSE BUILDING
    custom+=5*"\t"+"</building->\n"
    
    # ---- CLOSE SITE AND PROJECT
    custom+=4*"\t"+"</site->\n"
    custom+=3*"\t"+"</project->\n"
    
    # ---- END OF MODEL ENTITY
    custom+=2*"\t"+"</model->\n"
    
    # ---- ADD VIEWS.
    custom+=2*"\t"+"<view->\n"
    
    # ---- ADD PLAN.
    custom+=3*"\t"+"<plan-></plan->\n"
    
    # ---- ADD PROPERTIES ETC.
    custom+=3*"\t"+"<props-> </props->\n"
    
    # ---- CLOSE VIEWS
    custom+=2*"\t"+"</view->\n"
    
    # ---- RETURN THE CUSTOM HTML
    return custom

# G12: Function inserted from blender script, which extracts and prints name of room, area and volume (in that order) in a list
# output is stored in space_entities used in function classifyFloors.
def outputVolumeArea(model):   
    spaces = model.by_type("IfcSpace")
    space_entities = []
    for space in spaces: 
        for definition in space.IsDefinedBy: #Find in Excel in column N in IfcSpace 

            if definition.is_a("IfcRelDefinesByProperties"): # filter results
                property_set = definition.RelatingPropertyDefinition

                ## Sort by the name of the propertySet
                if property_set.Name == "PSet_Revit_Dimensions": #PSet_Revit_Dimensions
                    if property_set.HasProperties:
                        for property in property_set.HasProperties:

                        ## sort by the name of the property
                            if property.Name == "Volume":
                                print("Volume = ",property.NominalValue.wrappedValue)

                            if property.Name == "Area":
                                print("Area = ",property.NominalValue.wrappedValue)
                                space_entities.append(property.NominalValue.wrappedValue)
                                
    return space_entities

def classifyFloors(floors,site_elev, model): # G12: model added as input

    '''
    another way after arranging them would be to split them into above and below ground floor sets.
    '''
    
    floor_entities = ''
    
    # these are interesting and probably should be output somwhere - maybe to the building data?
    lower_floors = sum(f.Elevation < 0.1 for f in floors)
    level = len(floors)-lower_floors
    
    for floor in floors:
        # check if floor is lower than elevation...
        type = "floor_upper"
        if ( site_elev-.1 <= floor.Elevation <= site_elev+.1):
            type = "floor_ground"
        elif (site_elev < floor.Elevation):
            type = "floor_upper"
        else:
            type = "floor_lower"
           
        # THE SPAN STUFF SHOULD BE DEALT WITH IN JS...

        # G12: Code for extracting rooms on each floor and their names. 
        if (len(floor.IsDecomposedBy)!=0): # floor.IsDecomposedBy just gives us a tuple with one object in it if there are any rooms on the floor
            rooms = len(floor.IsDecomposedBy[0].RelatedObjects) # the object inside the tuple can be accessed by floor.IsDecomposedBy[0] and with .RelatedObjects we get a tuple over all the rooms on the floor - taking the length of the tuple gives us the amount of rooms
            roomNames = [i.LongName for i in floor.IsDecomposedBy[0].RelatedObjects] # Make a list over all the names of the rooms on the specific floor
            
            print(dir(floor.IsDecomposedBy[0].RelatedObjects[0].BoundedBy[0]))
        else: # if there are no rooms, the tuple of objects will have no elements
            rooms = 0
            roomNames = ['None']

        
        space_entities = outputVolumeArea(model) # G12: space entities are called 
        # G12: in floor_entities extra inouts are added: area, rooms and roomnames. 
        floor_entities+=6*"\t"+"<floor- class=\""+type+"\" name='{}'  level='{}' area = '{}' elev=\"{}\" rooms=\"{}\" roomnames=\"{}\" >{}<span class=\"floor_stats\">{}</span> </floor->\n".format(floor.Name, level, space_entities[0], floor.Elevation, floor.Name, round(float(floor.Elevation),3))     
        level-=1
        if (type == "floor_ground"):
            floor_entities+=6*"\t"+"<ground-></ground->\n"
            
    return floor_entities





