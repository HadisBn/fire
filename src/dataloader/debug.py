import os

data_dir = "/Users/hbanafsh/Downloads/WildfireSpreadTS_HDF5"
for root, dirs, files in os.walk(data_dir):
    print(f"Directory: {root}")
    for file in files:
        print(f"  File: {file}")
