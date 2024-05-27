import matplotlib.pyplot as plt
import utils
from utils import len_match

def yawRate(file, file_path):
    yawAcc = file.get("SBG_Yaw_Acc")
    latAcc = file.get("SBG_Accel_Y")

    start, stop = utils.get_start_stop(latAcc)

    yawAccSub = yawAcc.cut(start, stop)
    latAccSub = latAcc.cut(start, stop)

    yawAccSubMatch = len_match(yawAccSub, latAccSub)

    plt.figure()
    plt.scatter(latAccSub.samples, yawAccSubMatch, marker='o', color='b')
    plt.xlabel('SBG_Accel_Y (m/s^2)')
    plt.ylabel('SBG_Yaw_Acc (m/s^2)')
    plt.title('Yaw Moment Diagram')
    plt.show()

    

