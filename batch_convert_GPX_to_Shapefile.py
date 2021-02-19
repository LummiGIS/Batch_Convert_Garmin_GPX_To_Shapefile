#!/usr/bin/env python3
__author__ = 'Gerry Gabrisch (geraldg@lummi-nsn.gov)'
__date__ = 'February 2021'

import sys
import traceback
import subprocess
import shutil
import os

try:
    
    #########       USER DEFINED PARAMETERS     ####################
    #This is the path to the folder that stores the Garmin GPX files.  This path can be the actural Garmin connected via mini-USB
    in_dir = '/home/gerry/PythonScripts/Garmin/GARMIN'
    #This is the directory to store the output shapefiles...
    out_dir = '/home/gerry/PythonScripts/Garmin/shapefiles'
    #Mike MacKay gave each Garmin an ID letter.  Enter that here since files from two Garmins might have the same name. This avoids naming conventions and overwriting of files.
    garmin_ID = 'R'
    ################################################################
    
    
    def confirm_or_make_dir(out_dir):
        '''builds the output directory if it does not already exist'''
        if os.path.exists(out_dir):
            pass
        else:
            os.mkdir(out_dir)
    
    
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
                    #Build the file output paths as string
                    file_name_only = in_file.split('.')[0]
                    this_dir = out_dir  + '/Garmin_Unit_' + garmin_ID + '_' + file_name_only +'.shp'
                    #Build the ogr command...
                    cmd = 'ogr2ogr -f "ESRI Shapefile" '+ ' "' + this_dir  + '" "' + fullpath + '"'
                    print('running', cmd)
                    #Run the command from the command line.
                    subprocess.call(cmd, shell = 'True')                

except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
