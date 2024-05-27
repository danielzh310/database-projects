import matplotlib.pyplot as plt
import utils

def genRollPitchYaw(file, filePath):
    roll = file.get("SBG_Roll")
    pitch = file.get("SBG_Pitch")
    yaw = file.get("SBG_Yaw")

    start, stop = utils.get_start_stop(roll)

    roll = roll.cut(start, stop)
    pitch = pitch.cut(start, stop)
    yaw = yaw.cut(start, stop)

    lineplot(roll, pitch, yaw)

def lineplot(R, P, Y):
    figure, axis = plt.subplots(3, 1) 
    #plt.ylabel(var)
    #plt.figure()
    axis[0].plot(R.timestamps, R.samples) 
    axis[0].set_title("Roll") 
    axis[0].set_ylabel("Degrees")
    axis[1].plot(P.timestamps, P.samples) 
    axis[1].set_title("Pitch") 
    axis[1].set_ylabel("Degrees")
    axis[2].plot(Y.timestamps, Y.samples) 
    axis[2].set_title("Yaw") 
    axis[2].set_ylabel("Degrees")
    plt.show()
