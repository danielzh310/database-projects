import matplotlib.pyplot as plt
import numpy as np
import utils

def gen_damper_plots(file, file_path):
    #start for loop here for each file
    #pull the variables from the file
    fld = file.get('FL_DAMPER_MM')
    frd = file.get('FR_DAMPER_MM')
    rld = file.get('RL_DAMPER_MM')
    rrd = file.get('RR_DAMPER_MM')
    time = file.get('SBG_Accel_X')

    
    #get start and stop time from user
    start, stop = utils.get_start_stop(time)


    #reduce the data to the timestamps of interest
    flt = fld.cut(start, stop)
    frt = frd.cut(start, stop)
    rlt = rld.cut(start, stop)
    rrt = rrd.cut(start, stop)
    
    #allow the samples to have the same sample size
    flc = utils.len_match(flt, flt)
    frc = utils.len_match(frt, flt)
    rlc = utils.len_match(rlt, flt)
    rrc = utils.len_match(rrt, flt)
    
      
    # Initialise the subplot function using number of rows and columns 
    figure, axis = plt.subplots(3, 3) 
    
    axis[0, 0].plot(flt.timestamps, flc) 
    axis[0, 0].set_title("Front Left Damper") 
    
    axis[0, 1].plot(flt.timestamps, flc-frc) 
    axis[0, 1].set_title("Front Roll") 
    
    axis[0, 2].plot(flt.timestamps, frc) 
    axis[0, 2].set_title("Front Right Damper") 
    
    axis[1, 0].plot(flt.timestamps, flc-rlc) 
    axis[1, 0].set_title("Left Pitch")
    
    axis[1, 1].plot(flt.timestamps, (flc+rlc+frc+rrc)/4) 
    axis[1, 1].set_title("Heave")
    
    axis[1, 2].plot(flt.timestamps, frc-rrc) 
    axis[1, 2].set_title("Right Pitch")
    
    axis[2, 1].plot(flt.timestamps, rlc-rrc) 
    axis[2, 1].set_title("Rear Roll")
      
    axis[2, 0].plot(flt.timestamps, rlc) 
    axis[2, 0].set_title("Rear Left Damper") 
      
    axis[2, 2].plot(flt.timestamps, rrc) 
    axis[2, 2].set_title("Rear Right Damper") 
      
    # Combine all the operations and display 
    plt.show() 
