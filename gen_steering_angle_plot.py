import matplotlib.pyplot as plt
import utils
import pandas as pd
import numpy as np

def gen_Steering_Angle_plot(file, file_path):
    #pull the variables from the file
    steering_angle = file.get('FSM_steeringWheelAngle')
    throttle = file.get('FSM_throttlePos')
    brake = file.get('FSM_brakePressureFront')

    #get start and stop time from user
    start, stop = utils.get_start_stop(steering_angle)

    #reduce the data to the timestamps of interest
    steering_angle_sub = steering_angle.cut(start, stop)
    throttle_sub = throttle.cut(start, stop)
    brake_sub = brake.cut(start, stop)
   
    #create the plot
    plot_SA(steering_angle_sub, throttle_sub, brake_sub, file_path, start, stop)

    return


def plot_SA (SA, TR, BR, file_path, start, stop):

    figure, axis = plt.subplots(3, 1, figsize=(15, 5))  # Adjust figsize as needed

    axis[0].plot(SA.timestamps, SA.samples) 
    axis[0].set_title("Steering Angle") 
    axis[0].set_ylabel("Degrees")
    axis[1].plot(TR.timestamps, TR.samples) 
    axis[1].set_title("Throttle") 
    axis[2].plot(BR.timestamps, BR.samples) 
    axis[2].set_title("Brake") 
    plt.show()

    return
