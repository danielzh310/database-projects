import matplotlib.pyplot as plt
import asammdf
import numpy as np
import pandas as pd
#for checking skipselect
import slice_file_john as SFJ


def load_file(file_name):
    file = asammdf.MDF(file_name)

    return file


def print_channels(file):
    channels = file.search("*", mode = 'wildcard')
    
    with open(r'channels.txt', 'w') as fp:
        for item in channels:
            print(item)
            fp.write("%s\n" % item)

        print('Done: All available channels saved to "channels.txt"')
        print("There are " + str(len(channels)) + " channels in the datafile")
        
    return


def get_start_stop(var):
    
    start = var.timestamps[0]
    stop = var.timestamps[-1]
    
    if SFJ.skipselect == False:
        print("The raw data will now be displayed.  Please review the figure and pick a start and stop window.\n")
        print("Then close the figure and follow the input prompt.\n")
        gen_lineplot(var)

        start = 'a'
        stop = 'a'

        while (not start.isdigit()) or (not stop.isdigit()):
            print("\n## Please enter digits only. ##")
            start = input("Please enter the starting timestamp: \n")
            stop = input("Please enter the stopping timestamp: \n")

    return float(start), float(stop)


def gen_lineplot(var):

    plt.figure()

    varsamples = smooth([var])[0]

    plt.plot(var.timestamps, varsamples)
    plt.xlabel('Time (s)')
    plt.ylabel(var.name + ' (' + var.unit + ')')
    plt.suptitle(var.name + ' vs Time')
    plt.show()

    return


def len_match(var1, var2):
    var1_corrected = var1.samples
    if len(var1.samples) != len (var2.samples):
        array1 = np.array(range(0,len(var1.samples)))
        array2 = np.array(range(0,len(var2.samples)))
        var1_corrected = np.interp(array2, array1, np.array(var1.samples))

    return var1_corrected
    
def smooth(varlist):
    #var.samples is the array of sensor data
    
    window_size = 0
    
    while window_size == 0:
    
        smoothfactor = 'a'
        while not smoothfactor.isdigit():
            print("\n## Please enter digits only. ##")
            smoothfactor = input("Please enter the nonzero smoothing factor:\n(If unsure put 10 and adjust based on noise level. Enter 1 for no smoothing.)\n")

        window_size = int(smoothfactor)

    smoothed_varlist = []

    for var in varlist:
        series = pd.Series(var.samples)
        smoothed_series = series.rolling(window=window_size, min_periods=1).mean()
        smoothed_varlist.append(smoothed_series.tolist())

    return smoothed_varlist

def get_peak(file, var=[], start=None, stop=None):

    if start != None:
        file_cut = file.cut(start, stop)

    min_val_ls = []
    max_val_ls = []
    min_time_ls = []
    max_time_ls = []

    for v in var:
        signal = file_cut.get(v) #get the signal data for the current variable
        min_val = min(signal.samples)
        max_val = max(signal.samples)
        min_time = signal.timestamps[signal.samples == min_val]
        max_time = signal.timestamps[signal.samples == max_val]

        min_val_ls.append(min_val)
        max_val_ls.append(max_val)
        min_time_ls.append(min_time)
        max_time_ls.append(max_time)

    peak_dict = {'Variable':var, 'min val':min_val_ls, 'min time':min_time_ls,
                 'max val':max_val_ls, 'max time':max_time_ls}

    df = pd.DataFrame(peak_dict)
    for row in range(len(df)):
            print(df.iloc[row])
            print('\n')
    
    return peak_dict
        
