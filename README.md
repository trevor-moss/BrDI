# BioreactorDataStorage
 
**dataProcessing.py:** \
Imports CSVs from an inbox repository "csvInbox"
Converts the first column from a datetime string to UNIX time
Adds the data as a database in the hdf5 file "bioreactorData.h5"

**graphTrialV2.py:** \
Opens "bioreactorData.h5" and asks the user to select a single database or multiple databases
Asks the user which column to plot against which column (multiple columns from a single database soon)
Plots with matplotlib