import asammdf
import utils
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog

#important for skipping "select start stop" function
global skipselect
skipselect = True

def slice_file():

    #VERY IMPORTANT:
    flagchannelname = 'TEST_FLAG'

    #ask for the file path from user (or set file name and path for development purposes)
    #file_path = input("Please enter the path to the file for analysis")
    root = tk.Tk()
    root.withdraw()
    
    time_range = []

    while len(time_range) == 0:

        #Ask the user to provide the random identifiers associated with the desired start and stop
        testID = input("To analyze a single file, type manual. Otherwise, please enter the testID:\n")

        if testID == 'manual':
            file_path = ''
            print('Please select a file to view.')
            while file_path == '':
                file_path = filedialog.askopenfilename()
            if file_path.endswith('.mdf'):
                file = utils.load_file(file_path)
                global skipselect
                skipselect = False
                utils.print_channels(file)
                return [file, file_path]
            else:
                print("Please try again and select a .mdf file.")
        else:
            print('Please select a folder of .mdf files.')

            folder_path = ''

            while folder_path == '':
                folder_path = filedialog.askdirectory()#change this to a list of files, read from files folder?
                #file_path = ("C:/Users/Aaron/Documents/Carnegie Mellon/CMR/autox/logfile_2023-06-16_15-36-31.mdf")
            
            for filename in os.listdir(folder_path):
                if filename.endswith('.mdf'):
                    file_path = os.path.join(folder_path,filename)
                    OG_file = utils.load_file(file_path)
                    #get the channel associated with the random flags
                    flags_chan = OG_file.get(flagchannelname)
                    #Determine the timestamp associated with the random variable ID (will need to debug with actual .mdf file w/ random IDs)
                    #note: testID is entered in hexidecimal (as displayed on DIM)
                    time_range = flags_chan.timestamps[flags_chan.samples.astype(int) == int(testID, 16)]
                    if len(time_range) > 0:
                        skipselect = True
                        break
            if len(time_range) == 0:
                print("The specified testID could not be found in these files. The following testIDs were found:")
                allflags = []
                for filename in os.listdir(folder_path):
                    if filename.endswith('.mdf'):
                        file_path = os.path.join(folder_path,filename)
                        OG_file = utils.load_file(file_path)
                        flags_chan = OG_file.get(flagchannelname)
                        allflags = allflags + list(np.unique(flags_chan.samples))
                for item in list(np.unique(allflags)):
                    print(str(hex(item)))


    #Cut the file of interest at these timesteps
    new_file = OG_file.cut(time_range[0], time_range[-1], whence=0) #not sure if OG_file.cut will work, .cut does work on individual variables though

    #write the new file to a location
    #new_file.save() #dst allows you to specify a destination

    #return the shortened file of interest #may not need to return anything, just save the sliced mdf file
    return [new_file, file_path]
