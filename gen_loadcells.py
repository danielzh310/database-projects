import matplotlib.pyplot as plt
import numpy as np
import utils

def gen_loadcells(file, file_path):
    #start for loop here for each file
    #pull the variables from the file
    yaw = file.get('SBG_Yaw')
    yawrate = file.get('SBG_Yaw_Acc')
    roll = file.get('SBG_Roll')
    pitch = file.get('SBG_Pitch')
    fll = file.get('NAU7802_FORCE_3')
    frl = file.get('NAU7802_FORCE_0')
    rll = file.get('NAU7802_FORCE_2')
    rrl = file.get('NAU7802_FORCE_1')
    time = file.get('SBG_Accel_X')


    #get start and stop time from user
    start, stop = utils.get_start_stop(time)


    #reduce the data to the timestamps of interest
    flt = fll.cut(start, stop)
    frt = frl.cut(start, stop)
    rlt = rll.cut(start, stop)
    rrt = rrl.cut(start, stop)
    yt = yaw.cut(start, stop)
    yrt = yawrate.cut(start, stop)
    rt = roll.cut(start, stop)
    pt = pitch.cut(start, stop)

    #allow the samples to have the same sample size
    fll_corrected = utils.len_match(flt, flt)
    frl_corrected = utils.len_match(frt, flt)
    rll_corrected = utils.len_match(rlt, flt)
    rrl_corrected = utils.len_match(rrt, flt)
    yaw_corrected = utils.len_match(yt, flt)
    yawrate_corrected = utils.len_match(yrt, flt)
    roll_corrected = utils.len_match(rt, flt)
    pitch_corrected = utils.len_match(pt, flt)


    # Initialise the subplot function using number of rows and columns
    figure, axis = plt.subplots(3, 3)

    axis[0, 0].plot(flt.timestamps, fll_corrected)
    axis[0, 0].set_title("Front Left Load")

    axis[0, 1].plot(flt.timestamps, roll_corrected)
    axis[0, 1].set_title("Roll")

    axis[0, 2].plot(flt.timestamps, frl_corrected)
    axis[0, 2].set_title("Front Right Load")

    axis[1, 0].plot(flt.timestamps, pitch_corrected)
    axis[1, 0].set_title("Pitch")

    axis[1, 1].plot(flt.timestamps, yaw_corrected)
    axis[1, 1].set_title("Yaw")

    axis[2, 1].plot(flt.timestamps, yawrate_corrected)
    axis[2, 1].set_title("Yaw Rate")

    axis[2, 0].plot(flt.timestamps, rll_corrected)
    axis[2, 0].set_title("Rear Left Load")

    axis[2, 2].plot(flt.timestamps, rrl_corrected)
    axis[2, 2].set_title("Rear Right Load")

    # Combine all the operations and display
    plt.show()
