import asammdf
import utils
import tkinter as tk
from tkinter import filedialog

def slice_file():

    #ask for the file path from user (or set file name and path for development purposes)
    #file_path = input("Please enter the path to the file for analysis")
    root = tk.Tk()
    root.withdraw()

    file_path = ''

    print('Please select a file to view.')

    while file_path == '':
        file_path = filedialog.askopenfilename()#change this to a list of files, read from files folder?
        #file_path = ("C:/Users/Aaron/Documents/Carnegie Mellon/CMR/autox/logfile_2023-06-16_15-36-31.mdf")

    #load the file
    OG_file = utils.load_file(file_path)
    print('file loaded: ' + str(OG_file))

    #Ask the user to provide the random identifiers associated with the desired start and stop
    start_id = input("Please enter the starting random identifier: ")
    stop_id = input("Please enter the ending random identifier: ")

    #get the channel associated with the random flags
    flags_chan = OG_file.get('insert name of channel with flags')

    #Determine the timestamp associated with the random variable ID (will need to debug with actual .mdf file w/ random IDs)
    start_time = flags_chan.timestamps[flags_chan.samples == start_id]
    stop_time = flags_chan.timestamps[flags_chan.samples == stop_id]

    #Cut the file of interest at these timesteps
    new_file = OG_file.cut(start_time, stop_time, whence=0) #not sure if OG_file.cut will work, .cut does work on individual variables though

    #write the new file to a location
    new_file.save() #dst allows you to specify a destination

    #return the shortened file of interest #may not need to return anything, just save the sliced mdf file
    return #OG_file, new_file
