# Last updated: Trevor Moss, June 3rd, 2024
# Imports csv files from an inbox folder, processes the first column datetime string into UNIX, adds the database to an HDF5 file, moves CSVs to a processed folder

import os
import h5py
import pandas as pd
import numpy as np

# Define directories, place CSVs in the csvInbox folder
source_dir = 'csvInbox'
processed_dir = 'csvProcessed'
hdf5_filename = 'bioreactorData.h5'

# Create processed directory if it doesn't exist
if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

# Open HDF5 file
with h5py.File(hdf5_filename, 'a') as hdf5_file:
    # Iterate through each file in the source directory
    for csv_filename in os.listdir(source_dir):
        if csv_filename.endswith('.csv'):
            csv_path = os.path.join(source_dir, csv_filename)
            
            # Read CSV file using pandas
            df = pd.read_csv(csv_path)
            
            # Convert the first column to Unix time
            df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0]).astype(int) / 10**9

            # Some datatype shenanigans, HDF5 didn't like the object formatting of the MCGS_Time column
            df['MCGS_Time'] = df['MCGS_Time'].astype(int)
            
            # Convert the dataframe to a numpy structured array
            data = df.to_records(index=False)
            
            # Create a dataset in the HDF5 file
            hdf5_file.create_dataset(csv_filename.replace('.csv', ''), data=data)
            
            # Move the processed CSV file to the processed directory
            os.rename(csv_path, os.path.join(processed_dir, csv_filename))

print("All CSV files have been processed, converted, and moved to the processed directory.")