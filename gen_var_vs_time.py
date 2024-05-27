import matplotlib.pyplot as plt
import utils
from utils import gen_lineplot
from utils import get_start_stop

def gen_variable_plot(file, file_path):
    #pull the variables from the file

    while True:
        variableY = input("Please enter the name of your variable: ")
        try:
            y_var = file.get(variableY)
            break
        except:
            print("Variable name not found! Please try again.")

    #get start and stop time from user
    start, stop = utils.get_start_stop(y_var)

    #reduce the data to the timestamps of interest
    y_var_sub = y_var.cut(start, stop)

    
    #create the plot
    gen_lineplot(y_var_sub)

    return