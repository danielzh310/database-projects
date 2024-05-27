
def get_start_stop(var):
    print("The raw data will now be displayed.  Please review the figure and pick a start and stop window.")
    print("Then close the figure and follow the input prompt.")
    gen_lineplot(var)
    start = input("Please enter the starting timestamp: ")
    stop = input("Please enter the stopping timestamp: ")

    return float(start), float(stop)
