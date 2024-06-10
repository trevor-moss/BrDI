# BrDI (Bioreactor Data Insights)
 
**dataProcessing.py:** \
Imports CSVs from an inbox repository "csvInbox"
Converts the first column from a datetime string to UNIX time
Adds the data as a database in the hdf5 file "bioreactorData.h5"

**graphingV4.py:** \
Opens "bioreactorData.h5" and asks the user to select a single database or multiple databases
Asks the user which column(s) to plot
Plots with matplotlib

### Future Functionality:
* Ability to add external time series data to the CSV during the data import process
* Ability to add metadata to the HDF5 bioreactor dataset
  * Ex: Overall yield, specific productivity, volumetric productivity
* Additional column calculations
  * Ex: Oxygen uptake, ____
 * Adding databases to folders within the HDF5 file
 * Ability to specify regions along the x-axis to highlight

## Changelog
**June 10th, 2024**
* Added graphingV4.py
  * Option to plot columns independent of each other as vertically-stacked subplots
    * Option to show a vertical line that follows the cursor across subplots
  * Error messages
  * Reworked some sections to make code faster, can still be improved


**June 7th, 2024**
* Added a searchbar to the GUI when selecting dataset(s)

**June 5th, 2024**
* Adds a basic GUI to the graphing script
* Can now graph multiple columns from each dataset

**June 3rd, 2024**
* CSV to HDF5 import script with first column datatime to UNIX conversion
* Basic graphing functionality, specifying datasets and columns on the command line
