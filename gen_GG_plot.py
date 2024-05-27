import matplotlib.pyplot as plt
import utils
import pandas as pd
#from gen_lineplot import gen_lineplot
#from get_start_stop import get_start_stop

def gen_GG_plot(file, file_path):
    #start for loop here for each file
    #pull the variables from the file
    accel_X = file.get('SBG_Accel_X')
    accel_Y = file.get('SBG_Accel_Y')

    #get start and stop time from user
    start, stop = utils.get_start_stop(accel_Y)

    #reduce the data to the timestamps of interest
    accel_X_sub = accel_X.cut(start, stop)
    accel_Y_sub = accel_Y.cut(start, stop)

    #Ask the user if they want to smooth the data
    accel_X_smoothed, accel_Y_smoothed = utils.smooth([accel_X_sub, accel_Y_sub])

    #Ask the user if they would like to include peak values
    go_peak = input("Would you like to display the RAW min and max peak values? (y/n)\n")
    if go_peak == 'y':
        peak_dict = utils.get_peak(file, ['SBG_Accel_X', 'SBG_Accel_Y'], start, stop)

    #create the GG plot
    plot_GG(accel_X_smoothed, accel_Y_smoothed, file_path, start, stop) 

    return



def plot_GG (accel_X, accel_Y, file_path, start, stop):

    plt.figure()
    plt.scatter(accel_Y, accel_X, marker='o', color='b')
    plt.xlabel('SBG_Accel_Y (m/s^2)')
    plt.ylabel('SBG_Accel_X (m/s^2)')
    plt.suptitle('GG Plot for file: ' + file_path)
    plt.title('(timestamp: ' + str(start) + '-' + str(stop) + ')')
    plt.show()

    return


