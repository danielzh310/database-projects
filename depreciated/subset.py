import asammdf as mdf
from load_mdf import load_file
from print_channels import print_channels
from gen_GG_plot import gen_GG_plot
from gen_lineplot import gen_lineplot


#ask for the file path from user (or set file name and path for development purposes)
#file_path = input("Please enter the path to the file for analysis")
file_path = ("logfile_2023-06-17_10-35-49.mdf")
#file_path = ("C:/Users/Aaron/Documents/Carnegie Mellon/CMR/autox/logfile_2023-06-16_15-36-31.mdf")

#load the file
file = load_file(file_path)
print('file loaded: ' + str(file))


accel_x = file.get('SBG_Accel_X')

print(type(accel_x))
print(accel_x)

print(accel_x.cut(1,2))

mdf.plot(accel_x.cut(1,2).samples)
