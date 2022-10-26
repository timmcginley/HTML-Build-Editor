''' written by Tim McGinley 2022 '''

import ifcopenshell
import os.path
import time

def modelLoader(name):

    ''' 
        load the IFC file 
    '''
    model_url = r"C:\Users\loics\Documents\HTML-Build-IFC-Converter-main\model\duplex.ifc"
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
    parent_dir = "C:/Users/loics/Documents/HTML-Build-IFC-Converter-main/output"
    # create an HTML file to write to
    if (os.path.exists("C:/Users/loics/Documents/HTML-Build-IFC-Converter-main/output/"+name))==False:
        path = os.path.join(parent_dir, name)
        os.mkdir(path)
    
    f_loc="C:/Users/loics/Documents/HTML-Build-IFC-Converter-main/output/"+name+"/index.html"
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
    custom+= classifyFloors(floors,site_elev,model)
    
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
    custom+=3*"\t"+"<props-></props->\n"
    
    # ---- CLOSE VIEWS
    custom+=2*"\t"+"</view->\n"
    
    # ---- RETURN THE CUSTOM HTML
    return custom

def classifyFloors(floors,site_elev,model):

    '''
    another way after arranging them would be to split them into above and below ground floor sets.
    '''
    
    floor_entities = ''
    
    # these are interesting and probably should be output somwhere - maybe to the building data?
    lower_floors = sum(f.Elevation < 0.1 for f in floors)
    level = len(floors)-lower_floors+1
    for floor in floors:
        if level ==0:
            level = "T/FDN"
                  # check if floor is lower than elevation...
        FoundationW=[]    
        for w in model.by_type('IfcWall'):
            if "Foundation" in w.ObjectType:
                for relContainedInSpatialStructure in w.ContainedInStructure:
                     lvl = relContainedInSpatialStructure.RelatingStructure.Name
                if str(level) in lvl:
                    FoundationW.append(w)
        ExteriorW=[]
        for w in model.by_type('IfcWall'):
            if "Exterior" in w.ObjectType:
                for relContainedInSpatialStructure in w.ContainedInStructure:
                     lvl = relContainedInSpatialStructure.RelatingStructure.Name
                if str(level) in lvl:
                    ExteriorW.append(w)
        Party_walls=[]
        for w in model.by_type('IfcWall'):
            if "Party" in w.ObjectType:
                for relContainedInSpatialStructure in w.ContainedInStructure:
                     lvl = relContainedInSpatialStructure.RelatingStructure.Name
                if str(level) in lvl:
                    Party_walls.append(w)
        Roof=[]
        for s in model.by_type('IfcSlab'):
            if "Roof" in s.ObjectType:
                    Roof.append(s)
        FinishF=[]
        for s in model.by_type('IfcSlab'):
            if "Finish" in s.ObjectType:
                for relContainedInSpatialStructure in s.ContainedInStructure:
                    lvl = relContainedInSpatialStructure.RelatingStructure.Name
                if str(level) in lvl:
                    FinishF.append(s)
        ExteriorF=[]
        for s in model.by_type('IfcSlab'):
            if "Exterior" in s.ObjectType:
                for relContainedInSpatialStructure in s.ContainedInStructure:
                    lvl = relContainedInSpatialStructure.RelatingStructure.Name
                if str(level) in lvl:
                    ExteriorF.append(s)
        FBeams=[]
        for b in model.by_type('IfcBeam'):
            for relContainedInSpatialStructure in b.ContainedInStructure:
                lvl = relContainedInSpatialStructure.RelatingStructure.Name
            if str(level) in lvl:
                FBeams.append(b)
        se ="Walls:\n Foundation walls:"+str(len(FoundationW))+"\n Exterior walls:"+str(len(ExteriorW))+"\n Party walls:"+str(len(Party_walls))+"\n Slabs \n Roof:"+str(len(Roof))+"\n Finish floors:"+str(len(FinishF))+"\n Exterior Floors:"+str(len(ExteriorF))+"\n Beams:"+str(len(FBeams))
        type = "floor_upper"
        if ( site_elev-.1 <= floor.Elevation <= site_elev+.1):
            type = "floor_ground"
        elif (site_elev < floor.Elevation):
            type = "floor_upper"
        else:
            type = "floor_lower"

        # THE SPAN STUFF SHOULD BE DEALT WITH IN JS...
        if level =='T/FDN':
            level = 0
        floor_entities+=6*"\t"+"<floor- class=\""+type+"\" name='{}' struct='{}' level='{}' elev=\"{}\" >{}<span class=\"floor_stats\">{}</span> </floor->\n".format(floor.Name, se , level-1, floor.Elevation,floor.Name, round(float(floor.Elevation),3))     
        level-=1
        if (type == "floor_ground"):
            floor_entities+=6*"\t"+"<ground-></ground->\n"
           
    return floor_entities
print("done")