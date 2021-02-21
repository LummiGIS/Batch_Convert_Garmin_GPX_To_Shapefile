#!/usr/bin/env python3
__author__ = 'Gerry Gabrisch (geraldg@lummi-nsn.gov)'
__date__ = 'February 2021'

import sys
import traceback
import subprocess
import shutil
import os
from osgeo import ogr
from osgeo import gdal

try:
    
    #########       USER DEFINED PARAMETERS     ####################
    #This is the path to the folder that stores the Garmin GPX files.  This path can be the actural Garmin connected via mini-USB
    in_dir = r"E:\Garmin"
    #This is the directory to store the output shapefiles...
    out_dir = r"Z:\GISpublic\GerryG\Python3\Batch_Convert_Garmin_GPX_To_Shapefile\Shapefiles"
    #Mike MacKay gave each Garmin an ID letter.  Enter that here since files from two Garmins might have the same name. This avoids naming conventions and overwriting of files.
    garmin_ID = 'R'
    ################################################################
   
    print('Running GPX to SHP converte...')
    
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
    
    #confirm or build the output directory
    confirm_or_make_dir(out_dir)
    
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
                        
                        
                
    print('Finished without error')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
