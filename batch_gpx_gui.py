#!/usr/bin/python3
'''This script is a graphic user interface for batch generating shapefiles files GPX files.'''

import sys
import traceback
#import Create_KML_CSV_From_Geotagged_Images
import batch_convert_GPX_to_Shapefile
try:
    
    from tkinter import filedialog
    from tkinter import *
    
    def get_dir():
        '''opens the browser window'''
        root.directory = filedialog.askdirectory()
        print(root.directory)
        tb_1.insert(END, root.directory)
        return root.directory    
    
    def create_files():
        #use get methods to get the values from the user input boxes etc....
        Create_KML_CSV_From_Geotagged_Images.make_files(tb_1.get("1.0", "end-1c"),tb_2.get("1.0", "end-1c"),'ff000000', kml_var.get(), csv_var.get())
    
    #This creates the main window adn the default text to be displayed...
    root = Tk()
    root.geometry('650x200')
    root.title("Batch Convert GPX files to Shapefiles")
 
    #This is the stuff to get the directory to the images...
    b1 = Button(root, text = "Click To Set Directory of Geotagged Images. ", command = get_dir)
    b1.place(x=300,y=200)
    tb_1 = Text(root, height=1, width=75)
    
    # Create text widget and specify size to hold the user-defined project name... 
    tb_2 = Text(root, height = 1, width = 50) 
    #And here is the default project name...
    default_label = """Enter Project Name Here."""
    #This allows the user to choose to output a CSV file...
    csv_var = IntVar()
    csv_check =  Checkbutton (root, text = 'Create CSV?',variable = csv_var, onvalue = 1, offvalue=0,height=1, width=10)
    #This allows the user to choose to output a KML file...
    kml_var = IntVar()
    kml_check =  Checkbutton (root, text = 'Create KML?',variable = kml_var, onvalue = 1, offvalue=0,height=1, width=10)
    
    #This button does the work...
    b3 = Button(root, text = "Create Files. ", command = create_files)
    b3.place(x=500,y=200)
    
    b1.pack()
    tb_1.pack()
    tb_2.pack()
    csv_check.pack()
    kml_check.pack()
    b3.pack()
    tb_2.insert(INSERT, default_label) 
    root.mainloop()

except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))