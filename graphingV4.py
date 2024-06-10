import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import MultiCursor
from tkinter import Tk, Label, Listbox, MULTIPLE, Button, END, Entry, Checkbutton, BooleanVar

# Load data from the HDF5 file
hdf5_filename = 'bioreactorData.h5'
with h5py.File(hdf5_filename, 'r') as hdf5_file:
    datasets = list(hdf5_file.keys())
    column_names = hdf5_file[datasets[0]].dtype.names if datasets else []
    data_dict = {dataset: hdf5_file[dataset][:] for dataset in datasets}

# Function to plot selected datasets and columns
def plot_data():
    selected_datasets = [dataset_listbox.get(i) for i in dataset_listbox.curselection()]
    selected_columns = [column_listbox.get(i) for i in column_listbox.curselection()]

    if not selected_datasets or not selected_columns:
        print("Please select at least one dataset and one column to plot.")
        return

    if plot_separately.get():
        fig, axs = plt.subplots(len(selected_columns), 1, figsize=(15, 4 * len(selected_columns)), sharex=True)
        if len(selected_columns) == 1:
            axs = [axs]
    else:
        fig, axs = plt.subplots(1, 1, figsize=(15, 6))
        axs = [axs]

    for dataset_name in selected_datasets:
        data = data_dict[dataset_name]

        if "F1Time" not in data.dtype.names:
            print(f"'F1Time' column not found in dataset {dataset_name}")
            continue

        x_data = data["F1Time"]

        for i, col in enumerate(selected_columns):
            if col in data.dtype.names:
                y_data = data[col]
                if plot_separately.get():
                    axs[i].plot(x_data, y_data, label=f"{dataset_name} - {col}")
                    axs[i].set_title(col)
                else:
                    axs[0].plot(x_data, y_data, label=f"{dataset_name} - {col}")
            else:
                print(f"Column '{col}' not found in dataset {dataset_name}")

    if plot_separately.get():
        for i, ax in enumerate(axs):
            if i < len(axs) - 1:
                ax.set_xlabel('')
            else:
                ax.set_xlabel('F1Time')
            ax.set_ylabel('Value')
            ax.legend()
            ax.grid(True)

        # Add a multi-cursor line that moves with the mouse if cursor_enabled is True
        if cursor_enabled.get():
            multi_cursor = MultiCursor(fig.canvas, axs, color='red', linewidth=1, horizOn=False, vertOn=True)
        plt.tight_layout(pad=2.0)
    else:
        axs[0].set_xlabel('F1Time')
        axs[0].set_ylabel('Value')
        axs[0].set_title('Selected Datasets and Columns')
        axs[0].legend()
        axs[0].grid(True)

    # Use Matplotlib's object-oriented interface to reuse figure and axes objects
    plt.show(block=False)


##### GUI Code #####

# Function to update the dataset listbox based on the search query
def update_listbox(*args):
    search_query = search_var.get().lower()
    current_selection = [dataset_listbox.get(i) for i in dataset_listbox.curselection()]
    dataset_listbox.delete(0, END)

    # Use NumPy for data manipulation
    selected_filtered_datasets = sorted(dataset for dataset in current_selection if search_query in dataset.lower())
    non_selected_filtered_datasets = sorted(dataset for dataset in datasets if search_query in dataset.lower() and dataset not in current_selection)

    for dataset in selected_filtered_datasets:
        dataset_listbox.insert(END, dataset)
        dataset_listbox.selection_set(END)

    for dataset in non_selected_filtered_datasets:
        dataset_listbox.insert(END, dataset)

# Create the main window
root = Tk()
root.title("HDF5 Data Plotter")

# Database search label
Label(root, text="Database Search").pack()

# Search bar
search_var = Entry(root)
search_var.pack()
search_var.bind('<KeyRelease>', update_listbox)

# Dataset listbox
Label(root, text="Select Datasets:").pack()
dataset_listbox = Listbox(root, selectmode=MULTIPLE, exportselection=0)
dataset_listbox.pack()
for dataset in datasets:
    dataset_listbox.insert(END, dataset)

# Column listbox
Label(root, text="Select Columns:").pack()
column_listbox = Listbox(root, selectmode=MULTIPLE, exportselection=0)
column_listbox.pack()

for col in column_names:
    column_listbox.insert(END, col)

# Plot separately checkbox (default to False)
plot_separately = BooleanVar(value=False)
Checkbutton(root, text="Plot columns separately", variable=plot_separately).pack()

# Cursor enabled checkbox (default to False)
cursor_enabled = BooleanVar(value=False)
Checkbutton(root, text="Enable cursor", variable=cursor_enabled).pack()

# Plot button
plot_button = Button(root, text="Plot", command=plot_data)
plot_button.pack()

# Run the main loop
root.mainloop()