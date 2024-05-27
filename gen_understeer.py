import matplotlib.pyplot as plt
import numpy as np
import utils
import string

def gen_understeer_plot(file, file_path):
    # Pull the variables from the file
    str_deg = file.get('FSM_steeringWheelAngle')
    accel_Y = file.get('SBG_Accel_Y')

    # Get start and stop time from user
    start, stop = utils.get_start_stop(accel_Y)

    # Reduce the data to the timestamps of interest
    str_deg_sub = str_deg.cut(start, stop)
    accel_Y_sub = accel_Y.cut(start, stop)

    # Create the understeer plot
    plot_US(str_deg_sub, accel_Y_sub, file_path, start, stop)

    return

def plot_US(str_deg, accel_Y, file_path, start, stop):
    # Interpolation in case lengths don't match (will make into a util)
    if len(str_deg.samples) != len(accel_Y.samples):
        str_deg_corrected = utils.len_match(str_deg, accel_Y)

    filtered_indicies = []

    while True:
        beg, end = get_linear_portion(str_deg_corrected, accel_Y.samples)

        filtered_indices = (accel_Y.samples > beg) & (accel_Y.samples < end)

        if len(accel_Y.samples[filtered_indices]) > 0:
            break
        else:
            print("No data within that range, please try again.\n")

    line = np.polyfit(accel_Y.samples[filtered_indices], str_deg_corrected[filtered_indices], 1)
    p = np.polyfit(accel_Y.samples, str_deg_corrected, 10)

    # Evaluate the polynomial on a finer grid
    t = np.linspace(min(accel_Y.samples), max(accel_Y.samples), 200)
    fitted_curve = np.polyval(p, t)
    fitted_line = np.polyval(line,t)
    coeffs = np.poly1d(line)
    usgValue = str(coeffs.coefficients[0] * (np.pi / 180) * 9.81)

    # Plot the original data and the fitted curve
    plt.figure()
    plt.scatter(accel_Y.samples, str_deg_corrected, label='Original Data', marker='o', color='b')
    plt.plot(t, fitted_curve, '--', color='gray', label='Fitted Curve')
    plt.plot(t, fitted_line, '--', color='red', label = 'K = ' + usgValue + ' rad/g')
    plt.ylabel('FSM_steeringWheelAngle (deg)')
    plt.xlabel('SBG_Accel_Y (m/s^2)')
    plt.suptitle('Understeer gradient for file:\n' + file_path)
    plt.title('(timestamp: ' + str(start) + '-' + str(stop) + ')')
    plt.legend()
    plt.show()

    return

def get_linear_portion(var1, var2):

    start = 'a'
    stop = 'a'

    plt.figure()
    plt.scatter(var2, var1, marker='o', color='b')
    plt.ylabel('FSM_steeringWheelAngle (deg)')
    plt.xlabel('SBG_Accel_Y (m/s^2)')
    plt.title('Please Identify the Linear Region (Lateral Accel range)')
    plt.show()

    while (not start.replace('-', '').isdigit()) or (not stop.replace('-', '').isdigit()):
        print("\n## Please enter digits only. (note 2 - 8 m/s^2 seems to be a good range) ##")
        start = input("Please enter the start of the linear portion (lat accel): \n")
        stop = input("Please enter the end of the linear portion (lat accel): \n")

    return float(start), float(stop)