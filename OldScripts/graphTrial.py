import h5py
import matplotlib.pyplot as plt

# Path to the HDF5 file
hdf5_filename = 'output_data.h5'

# Open the HDF5 file
with h5py.File(hdf5_filename, 'r') as hdf5_file:
    # List all datasets in the file
    datasets = list(hdf5_file.keys())
    print("Datasets in the HDF5 file:", datasets)
    
    # Select one dataset to plot (assuming there is at least one dataset)
    if datasets:
        dataset_name = datasets[0]
        data = hdf5_file[dataset_name][:]
        
        # Extract the first column (Unix time) and the second column (assuming it's some numerical data)
        elapsed_time = data['F1Time']
        dissolvedOxygen = data['F1_DO']

        
        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(elapsed_time, dissolvedOxygen, label=dataset_name)
        plt.xlabel('Elapsed Time [hr]')
        plt.ylabel('Value')
        plt.title(f'Dataset: {dataset_name}')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("No datasets found in the HDF5 file.")
