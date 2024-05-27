import asammdf
import utils
import tkinter as tk
from tkinter import filedialog




file_path = ("C:/Users/Aaron/Documents/Carnegie Mellon/CMR/autox/logfile_2023-06-16_15-36-31.mdf")

mdf = asammdf.MDF(file_path)

utils.print_channels(mdf)

accel_X = mdf.get('SBG_Accel_X')
print(accel_X.timestamps)
print(accel_X.samples)
x = accel_X.samples == 0
print(x)
y = accel_X.timestamps[x]
print(y)
print(len(accel_X))
print(len(y))

#ask for the file path from user (or set file name and path for development purposes)
#file_path = input("Please enter the path to the file for analysis")
#root = tk.Tk()
#root.withdraw()

#file_path = ''

#print('Please select a file to view.')

#while file_path == '':
#    file_path = filedialog.askopenfilename()#change this to a list of files, read from files folder?
#file_path = ("C:/Users/Aaron/Documents/Carnegie Mellon/CMR/autox/logfile_2023-06-16_15-36-31.mdf")

#load the file
#file = utils.load_file(file_path)
#print('file loaded: ' + str(file))

#print(type(file))


#file = asammdf.MDF(file_path)

#channels = file.search("*", mode = 'wildcard')
