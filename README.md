# BioreactorDataStorage
 
**dataProcessing.py:** \
Imports CSVs from an inbox repository "csvInbox"
Converts the first column from a datetime string to UNIX time
Adds the data as a database in the hdf5 file "bioreactorData.h5"

**graphTrialV2.py:** \
Opens "bioreactorData.h5" and asks the user to select a single database or multiple databases
Asks the user which column to plot against which column (multiple columns from a single database soon)
Plots with matplotlib

## Changelog
### Future Functionality:
* Ability to add external time series data to the CSV during the data import process
* Ability to add metadata to the HDF5 bioreactor dataset
  * Ex: Overall yield
* Additional column calculations
  * Ex: Oxygen uptake, ____

**June 7th, 2024**
* Added a searchbar to the GUI when selecting dataset

**June 5th, 2024**
* Adds a basic GUI to the graphing script
* Can now graph multiple columns from each dataset

**June 3rd, 2024**
* CSV to HDF5 import script with first column datatime to UNIX conversion
* Basic graphing functionality, specifying datasets and columns on the command line
