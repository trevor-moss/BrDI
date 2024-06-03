### Partially generated with GPT-4o: "Using python, import a CSV file and add it to an hdf5 file"
### Further modified for use case

import pandas as pd

# Step 1: Read the CSV file into a DataFrame
csv_file_path = 'csvData/fDRB230328_B1.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)

print(df)

# Step 2: Create an HDF5 file and add the DataFrame to it
hdf5_file_path = 'bioreactorDataset.h5'  # Replace with your HDF5 file path
df.to_hdf(hdf5_file_path, key='dataset', format='t', mode='w')

pd.read_hdf('bioreactorDataset.h5', 'dataset', columns=['MCGS_Time', 'F1Time'])

# If you want to add another DataFrame to the same HDF5 file
# df_another = pd.read_csv('another_csv_file.csv')
# df_another.to_hdf(hdf5_file_path, key='another_dataset', mode='a')