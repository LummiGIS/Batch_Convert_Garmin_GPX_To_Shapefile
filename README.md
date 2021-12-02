# Batch_Convert_Garmin_GPX_To_Shapefile

Batch converts all of the GPX files stored on a Garmin to ESRI Shapefile.


After making a USB connection from the Garmin to the computer run batch_gpx_gui.py.  A GUI will allow you to set the path to the Garmin and the path to the output directory.  Lummi Garmin units are assigned a letter identifier.  The letter identifier will append to the output shapefiles the letter identifier.  

Best to send the files to a new and clean directory.  This directory will contain a folder for each output shapefile.  All of the original GPX files are moved to this directory.  All GPX files are removed from the Garmin directory.

Tested and working on: 


      ETrex 20x (via mini USB connection)
      GPSmap 60Cx (by first removing the micoSD card)
