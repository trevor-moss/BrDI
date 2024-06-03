import os
import pandas as pd

# h5 file to save CSVs to (set once)
hdf5_file_path = 'bioreactorDatasetMulti.h5'

# Defines csvProcessed and csvInbox as the csv inbox and storage folders
inboxDirectory = 'csvInbox'
processedDirectory = 'csvProcessed'

# Iterate the following for all files in the inbox
for filename in os.listdir(inboxDirectory):

    # Mac specific setting: Macs create this file that contains information on which view Finder uses to open the folder, etc.
    if filename != '.DS_Store':

        # Processes original filename into a key to be used in the h5 file
        f = os.path.join(inboxDirectory,filename)
        keyName = filename[:-4]

        # Opens the CSV, writes ('a') it to the h5 file in the format of a table ('t') with the key made earlier
        df = pd.read_csv(f)
        df.to_hdf(hdf5_file_path, key=keyName, format='t', mode='a')

        # Moves processed CSV file from the inbox folder to the processed folder
        os.rename(f, os.path.join(processedDirectory,filename))






