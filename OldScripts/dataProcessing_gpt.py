import os
import shutil
import numpy as np
import h5py
from datetime import datetime
import time

# Define directories
source_dir = 'csvInbox'
processed_dir = 'csvProcessed'
hdf5_filename = 'output_data.h5'

# Create processed directory if it doesn't exist
if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

# Create function for converting Y-m-d H:M:S to unix timestamp: seconds since Jan 1 1970
def datetime_to_unix_timestamp(datetime_str, format_str='%Y-%m-%d %H:%M:%S'):
    dt = datetime.strptime(datetime_str, format_str)
    unix_timestamp = int(time.mktime(dt.timetuple()))
    return unix_timestamp

vectorized_datetimeUnix = np.vectorize(datetime_to_unix_timestamp)

# Example usage
datetime_str = "2023-3-29 3:37:52"
unix_timestamp = datetime_to_unix_timestamp(datetime_str)
print(unix_timestamp)

# Open HDF5 file
with h5py.File(hdf5_filename, 'w') as hdf5_file:
    # Iterate through each file in the source directory
    for csv_filename in os.listdir(source_dir):
        if csv_filename.endswith('.csv'):
            csv_path = os.path.join(source_dir, csv_filename)
            
            # Read CSV file using numpy
            data = np.genfromtxt(csv_path, delimiter=',', names=True, dtype=None, encoding='utf-8')


            
            # Create a dataset in the HDF5 file
            hdf5_file.create_dataset(csv_filename.replace('.csv', ''), data=data)
            
            # Move the processed CSV file to the processed directory
            shutil.move(csv_path, os.path.join(processed_dir, csv_filename))

print("All CSV files have been processed and moved to the processed directory.")