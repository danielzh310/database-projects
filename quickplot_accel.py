import matplotlib.pyplot as plt
import utils
from matplotlib.patches import Ellipse

def gen_plot(file, file_path):
    accel_X = file.get('SBG_Accel_X')
    accel_Y = file.get('SBG_Accel_Y')

    accel_X_smoothed, accel_Y_smoothed = utils.smooth([accel_X, accel_Y])

    maxX, minX = max(accel_X_smoothed), min(accel_X_smoothed)
    maxY, minY = max(accel_Y_smoothed), min(accel_Y_smoothed)

    maxX_index = accel_X_smoothed.index(maxX)
    minX_index = accel_X_smoothed.index(minX)
    maxY_index = accel_Y_smoothed.index(maxY)
    minY_index = accel_Y_smoothed.index(minY)

    maxXtime = accel_X.timestamps[maxX_index]
    minXtime = accel_X.timestamps[minX_index]
    maxYtime = accel_Y.timestamps[maxY_index]
    minYtime = accel_Y.timestamps[minY_index]

    print("Max X Accel: {:.2f} m/s² @ t={:.2f} seconds".format(maxX, maxXtime))
    print("Min X Accel: {:.2f} m/s² @ t={:.2f} seconds".format(minX, minXtime))
    print("\nMax Y Accel: {:.2f} m/s² @ t={:.2f} seconds".format(maxY, maxYtime))
    print("Min Y Accel: {:.2f} m/s² @ t={:.2f} seconds".format(minY, minYtime))

    # Create the g-g plot
    figure, axis = plt.subplots(3, 1, figsize=(15, 5))  # Adjust figsize as needed

    # Plot Y vs X acceleration (g-g diagram)
    axis[0].scatter(accel_Y_smoothed, accel_X_smoothed, marker='o', color='b')
    axis[0].set_xlabel('Y Acceleration (m/s²)')
    axis[0].set_ylabel('X Acceleration (m/s²)')
    axis[0].set_title('g-g Diagram')

    # Add an ellipse around the maximum values
    ellipse = Ellipse((0,0), width=2*max(abs(maxY),abs(minY)), height=2*max(abs(maxX),abs(minX)), color='gray', fill=False, linestyle='--')
    axis[0].add_patch(ellipse)

    # Plot X acceleration vs time
    axis[1].plot(accel_X.timestamps, accel_X_smoothed, color='r')
    axis[1].set_xlabel('Time (seconds)')
    axis[1].set_ylabel('X Acceleration (m/s²)')
    axis[1].set_title('X Acceleration vs Time')

    # Add a dotted line at the maximum X acceleration
    axis[1].axhline(y=maxX, color='gray', linestyle='--')

    # Plot Y acceleration vs time
    axis[2].plot(accel_Y.timestamps, accel_Y_smoothed, color='g')
    axis[2].set_xlabel('Time (seconds)')
    axis[2].set_ylabel('Y Acceleration (m/s²)')
    axis[2].set_title('Y Acceleration vs Time')

    # Add a dotted line at the maximum Y acceleration
    axis[2].axhline(y=maxY, color='gray', linestyle='--')

    plt.tight_layout()
    plt.show()

    return
