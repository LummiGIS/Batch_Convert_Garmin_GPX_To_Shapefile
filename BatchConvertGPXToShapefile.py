#!/usr/bin/python3
'''This script is a graphic user interface for batch generating shapefiles files GPX files.'''

import sys
import os
import traceback
import batch_convert_GPX_to_Shapefile
import subprocess
import shutil

from osgeo import ogr
from osgeo import gdal
try:
    
    from tkinter import filedialog
    from tkinter import *
  
    
    def get_dir():
        '''opens the browser window'''
        root.directory = filedialog.askdirectory()
        print(root.directory)
        tb_1.insert(END, root.directory)
        return root.directory 
    def get_dir2():
        '''opens the browser window'''
        root.directory = filedialog.askdirectory()
        print(root.directory)
        tb_3.insert(END, root.directory)
        return root.directory       
    
    def create_files():
        #use get methods to get the values from the user input boxes etc....
        make_files(tb_1.get("1.0", "end-1c"),tb_3.get("1.0", "end-1c"),tb_2.get("1.0", "end-1c"))
        os.open(file, flags)
    def get_help():
        #use get methods to get the values from the user input boxes etc....
       os.startfile('Read_Me.md')   
   
    def confirm_or_make_dir(out_dir):
        '''builds the output directory if it does not already exist'''
        if os.path.exists(out_dir):
            pass
        else:
            os.mkdir(out_dir)
            
    def count_shapefile_records(in_shapefile):
        '''counts the total number of records in the shapefile...'''
        #in_shapefile = r"C:\gTemp\CAD_Extents.shp"
        driver = ogr.GetDriverByName('ESRI Shapefile')
        dataSource = driver.Open(in_shapefile, 0) # 0 means read-only. 1 means writeable.
        # Check to see if shapefile is found.
        if dataSource is None:
            print('Could not open %s' % (in_shapefile))
        else:
            layer = dataSource.GetLayer()
            featureCount = layer.GetFeatureCount()
            return featureCount  
        
    def delete_empty_shapfile(in_shapefile):
        driver = ogr.GetDriverByName("ESRI Shapefile")
        if os.path.exists(in_shapefile):
            driver.DeleteDataSource(in_shapefile)
    
   
    
    def make_files(in_dir,out_dir, garmin_ID):
       #Sift through every file in every folder in the input directory...
        for (dirpath, dirnames, filenames) in os.walk(in_dir):
            for in_file in filenames:
                if in_file.endswith('.gpx') or in_file.endswith('.GPX'):
                    if dirpath == in_dir:
                        fullpath = os.path.join(dirpath,in_file)
                    else:
                        fullpath = os.path.join(dirpath,in_file)    
    
                    #I am unsure of what .Position.gpx is but that period before the file name messes with the damn path names...SKIP IT FOR NOW
                    if in_file == '.Position.gpx':
                        pass
                    else:
                        #make a backup of the gpx files
                        
                        #Build the file output paths as string
                        file_name_only = in_file.split('.')[0]
                        #this_dir = out_dir  + '/Garmin_Unit_' + garmin_ID + '_' + file_name_only +'.shp'
                        this_dir = out_dir  + '/Garmin_Unit_' + garmin_ID + '_' + file_name_only 
                        gdal.VectorTranslate(this_dir, fullpath)
                        shutil.move(fullpath, out_dir)
        #Garmin GPX converts to at least five files, many of which are empty. If so, purge them.                
        for (dirpath, dirnames, filenames) in os.walk(out_dir):
            for in_file in filenames:
                if in_file.endswith('.shp') or in_file.endswith('.SHP'):
                    if dirpath == in_dir:
                        fullpath = os.path.join(dirpath,in_file)
                    else:
                        fullpath = os.path.join(dirpath,in_file)                        
                        record_count = count_shapefile_records(fullpath)
                        if record_count == 0:
                            delete_empty_shapfile(fullpath)
   
        os.startfile(out_dir)
   
    
    
    
    #This creates the main window adn the default text to be displayed...
    root = Tk()
    root.geometry('850x200')
    root.title("Batch Convert GPX files to Shapefiles")
   
    lbl = Label(root, text = "\nConverts all GPX files from the input directory to ESRI Shapefiles in the output directory.\nAll GPX files are removed from the input directory and copied to the output directory.\nCreated by G. Gabrisch (geraldg@lummi-nsn.gov)\n", justify= LEFT )
     
 
    #This is the stuff to get the directory to the images...
    b1 = Button(root, text = "Click to set input directory. ", command = get_dir)
    
    tb_1 = Text(root, height=1, width=75)
    
    # Create text widget and specify size to hold the user-defined project name... 
    tb_2 = Text(root, height = 1, width = 29) 
    
    #And here is the default project name...
    default_label = """Enter Unique ID Here."""
    #This allows the user to choose to output a CSV file...
    
    

    
    #This is the stuff to get output...
    b2 = Button(root, text = "Click to set output directory. ", command = get_dir2)
    
    tb_3 = Text(root, height=1, width=75)
    
    # Create text widget and specify size to hold the user-defined project name... 
    tb_4 = Text(root, height = 1, width = 50) 
    #And here is the default project name...
    default_label = """unique ID"""
    #This allows the user to choose to output a CSV file...
    
    #This button does the work...
    b3 = Button(root, text = "Create Files. ", command = create_files)
    
    
    
    lbl.place(x=0, y=0)
    
    b1.place(x=10, y=65)
    tb_1.place(x=200, y=70)
    
   
    b2.place(x=10, y=105)
    
    tb_3.place(x=200, y=110)
    
    tb_2.place(x=10, y=145)
    
    
    b3.place(x=10, y=170) 
  

    tb_2.insert(INSERT, default_label) 
    root.mainloop()
    print('Finished without errors.')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))