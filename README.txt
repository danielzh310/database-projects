README

Thank you for your interest in developing and using our scripts for quick-turn vehicle analysis!  Please follow the below instructions to download python, setup a virtual environment, install the necessary packages and the execute the analysis files.


Instructions for first time setup
1) Make sure python is downloaded on you computer: https://www.python.org/downloads/

2) clone the github repository to this location, all files should be downloaded to your analysis folder (mine is located here: ...\Programs\Python\Python312\CMR_data_analysis\quick-turn-data-analysis)

3) Create a virtual environment (steps described below, documentation here: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
a) open up terminal
b) navigate to where you want the virtual environment, cd command, my path is ...\Python\Python312
c) enter into the terminal, py -m venv .venv

4) activate the virtual environment (documentation: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
a) .venv\Scripts\activate

5) install python packages for analysis (only needed once, can skip if already installed previously)
with .venv activated...
py -m pip install asammdf
py -m pip install matplotlib
py -m pip install tk
py -m pip install numpy

6) execute analysis, just type into the terminal
execute.py

7) after you are done with analysis, deactivate the virtual environment by typing "deactivate" into the terminal
deactivate
