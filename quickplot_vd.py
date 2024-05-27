import matplotlib.pyplot as plt
import numpy as np
import utils

def gen_plot(file, file_path):
    # Pull the variables from the file
    str_deg = file.get('FSM_steeringWheelAngle')
    accel_Y = file.get('SBG_Accel_Y')

    # Create the understeer plot
    plot_US(str_deg, accel_Y, file_path)

def plot_US(str_deg, accel_Y, file_path):
    # Interpolation in case lengths don't match (will make into a util)
    if len(str_deg.samples) != len(accel_Y.samples):
        str_deg_corrected = utils.len_match(str_deg, accel_Y)
    else:
        str_deg_corrected = str_deg.samples  # No correction needed

    # Fit a polynomial of degree 2
    coeffs = np.polyfit(accel_Y.samples, str_deg_corrected, 2)
    poly_fit = np.polyval(coeffs, accel_Y.samples)

    # Create the plot
    plt.figure(figsize=(10, 6))  # Adjust figsize as needed
    plt.plot(accel_Y.samples, str_deg_corrected, label='Data')
    plt.plot(accel_Y.samples, poly_fit, '--', color='gray', label='Polyfit (Degree 2)')
    plt.ylabel('FSM_steeringWheelAngle (deg)')
    plt.xlabel('SBG_Accel_Y (m/s²)')
    plt.suptitle('Understeer Gradient for File: ' + file_path)
    plt.title('(Entire Data Range)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return
