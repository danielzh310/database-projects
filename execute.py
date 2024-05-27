import asammdf
import utils
import slice_file_john
import tkinter as tk
from tkinter import filedialog
import quickplot_accel as QA
import quickplot_vd as QV
import gen_GG_plot as GG
import gen_understeer as US
import gen_var_vs_time as VAR
import gen_dampers as DP
import genRollPitchYaw as TRIO
import gen_loadcells as LC
import yawRate as YR
import gen_steering_angle_plot as SA
import gen_GPS as GPS

#ask for the file path from user (or set file name and path for development purposes)
#file_path = input("Please enter the path to the file for analysis")
root = tk.Tk()
root.withdraw()

#file_path = ''
#print('Please select a file to view.')
#while file_path == '':
#    file_path = filedialog.askopenfilename()#change this to a list of files, read from files folder?
#    #file_path = ("C:/Users/Aaron/Documents/Carnegie Mellon/CMR/autox/logfile_2023-06-16_15-36-31.mdf")

#load the file
[file, file_path] = slice_file_john.slice_file()
#file = utils.load_file(file_path)
print('file loaded: ' + file_path)

#ask the user what type of analysis they would like to conduct
analysis_ls = ["0) GG, AccX, AccY","1) GG-Plot", "2) Variable vs Time",
               "3) Understeer Gradient", "4) Damper Graphs", "5) Roll, Pitch, Yaw",
               "6) Loadcell Graphs", "7) Yaw Moment", "8) Driver Input Plot", "9) GPS Plot"] #update this list as new analysis functions are created

#enter into the associated fuction for the selected analysis method
while True:

    print("\nHere are the list of available analysis options:")
    for item in analysis_ls:
        print(item)

    analysis_meth = input("Enter the number of which analysis you would like to run:\n(To exit program, type 'exit')\n(To reset the testID, type 'restart')\n")

    if analysis_meth == '0':
        QA.gen_plot(file, file_path)
    elif analysis_meth == '1':
        #wrapper function for the GG plot
        GG.gen_GG_plot(file, file_path)
    elif analysis_meth == '2':
        VAR.gen_variable_plot(file, file_path)
    elif analysis_meth == '3':
        US.gen_understeer_plot(file, file_path)
    elif analysis_meth == '4':
        DP.gen_damper_plots(file, file_path)
    elif analysis_meth == "5":
        TRIO.genRollPitchYaw(file, file_path)
    elif analysis_meth == "6":
        LC.gen_loadcells(file, file_path)
    elif analysis_meth == "7":
        YR.yawRate(file, file_path)
    elif analysis_meth == "8":
        SA.gen_Steering_Angle_plot(file, file_path)
    elif analysis_meth == "9":
        GPS.gen_GPS_plot(file, file_path)
    elif analysis_meth == "restart":
        [file, file_path] = slice_file_john.slice_file()
    elif analysis_meth == "exit":
        break
    else:
        print("Input not understood, try again.")

#print out channels or variables available for plotting
#print_channels(file)

#request user input on the variables for the GG plot
#var_x = input("Please enter the x-axis channel for the GG plot: ")
#print("You entered: " + var_x)

#var_y = input("Please enter the y-axis channel for the GG plot: ")
#print("You entered: " + var_y)

#pull the data for GG plot (if the data was input incorrectly, then there will be an error in the file.get function)
#accel_x = file.get(var_x) #SBG_Accel_X
#accel_y = file.get(var_y) #SBG_Accel_Y

#plot the raw data and ask user to input a start and stop time for the relevant data
#print("The raw data will now be displayed.  Please review the figure and pick a start and stop window.")
#print("Then close the figure and follow the input prompt.")
#gen_lineplot(accel_x)
#start = input("Please enter the starting timestamp: ")
#stop = input("Please enter the stopping timestamp: ")

#subset data function

#TODO: plot just a line plot of the data to pick out the time of interest
#TODO: subset the data based on the start and stop time

#create the GG plot
#gen_GG_plot(accel_x, accel_y)





##
##print(accel_x)
###print(accel_x[1])
##print(accel_x.samples)
##print(type(accel_x.samples))
##print(len(accel_x))
###plot(accel_x)
##
##


