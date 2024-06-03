import h5py
import numpy as np

# data2 = np.genfromtxt("csvData/fDRB230328_B1.csv", delimiter=",")
data = np.genfromtxt("csvData/fDRB230328_B1.csv", dtype=None, skip_header=1, delimiter=",")


print(data[:5])