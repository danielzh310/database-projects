import matplotlib.pyplot as plt
import utils
import numpy as np

def gen_GPS_plot(file, file_path):
    # Pull the variables from the file
    lat = file.get('SBG_Latitude')
    long = file.get('SBG_Longitude')
    throttle = file.get('FSM_throttlePos')
    brake = file.get('FSM_brakePressureFront')

    # Get start and stop time from user
    start, stop = utils.get_start_stop(lat)  # Assuming you have a function called get_start_stop

    # Reduce the data to the timestamps of interest
    lat_sub = lat.cut(start, stop)
    long_sub = long.cut(start, stop)
    throttle_sub = throttle.cut(start, stop)
    brake_sub = brake.cut(start, stop)

    # Calculate the average latitude and longitude
    average_lat = np.median(lat_sub.samples)
    average_long = np.median(long_sub.samples)

    # Calculate distance from the average point (assuming Earth is flat for simplicity)
    lat_diff_avg = lat_sub.samples - average_lat
    long_diff_avg = long_sub.samples - average_long
    distance_avg = np.sqrt(lat_diff_avg**2 + long_diff_avg**2) * 111.32  # Approximate km per degree

    # Filter out data points more than 1 km away from the average point
    valid_indices_avg = np.where(distance_avg <= 1.0)
    print(valid_indices_avg)
    lat_valid_avg = lat_sub.samples[valid_indices_avg]
    long_valid_avg = long_sub.samples[valid_indices_avg]
    throttle_valid_avg = throttle_sub.samples[valid_indices_avg]
    brake_valid_avg = brake_sub.samples[valid_indices_avg]

    # Create the scatter plot with colors based on throttle and brake values
    plt.figure()
    plt.scatter(long_valid_avg, lat_valid_avg, c=throttle_valid_avg, cmap='Greens', marker='o', label='Throttle')
    plt.scatter(long_valid_avg, lat_valid_avg, c=brake_valid_avg, cmap='Reds', marker='X', label='Brake')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('GPS Map')
    plt.colorbar(label='Throttle/Brake Value')
    plt.legend()
    plt.show()

    return
