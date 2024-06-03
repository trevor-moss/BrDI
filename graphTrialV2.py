import h5py
import matplotlib.pyplot as plt

# Path to the HDF5 file
hdf5_filename = 'output_data.h5'

# Open the HDF5 file
with h5py.File(hdf5_filename, 'r') as hdf5_file:
    # List all datasets in the file
    datasets = list(hdf5_file.keys())
    print("Datasets in the HDF5 file:", datasets)
    
    # Ask user which datasets to plot
    selected_datasets = input("Enter the names of datasets to plot, separated by commas: ").split(',')
    selected_datasets = [dataset.strip() for dataset in selected_datasets]
    
    # Ask user which columns to plot
    x_column = input("Enter the name of the column for the x-axis: ")
    y_column = input("Enter the name of the column for the y-axis: ")
    
    plt.figure(figsize=(10, 6))
    
    # Iterate over selected datasets and plot the specified columns
    for dataset_name in selected_datasets:
        if dataset_name in datasets:
            data = hdf5_file[dataset_name][:]
            
            # Extract specified columns
            x_data = data[x_column]
            y_data = data[y_column]
            
            # Plot the data
            plt.plot(x_data, y_data, label=dataset_name)
        else:
            print(f"Dataset {dataset_name} not found in the HDF5 file.")
    
    # Customize plot
    plt.xlabel(f'Column {x_column}')
    plt.ylabel(f'Column {y_column}')
    plt.title('Selected Datasets')
    plt.legend()
    plt.grid(True)
    
    # Show plot
    plt.show()