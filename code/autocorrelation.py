# Importing the libraries.
import matplotlib.pyplot as plt 
import numpy as np 

file_path = "//wsl.localhost//Ubuntu//tmp//chosenBitsjmqeohbo.tekBits"
# Read binary keys from file
binary_keys = []

with open(file_path, 'r') as file:
     # file in binary, strings of binary
    for line in file:
        line = line.strip()
        if line:
            binary_keys.append(int(line))

# Adding plot title.
plt.title("Autocorrelation Plot") 

# Providing x-axis name.
plt.xlabel("Lags") 

# Plotting the Autocorrelation plot.
plt.acorr(binary_keys, maxlags = 10) 

# Displaying the plot.
print("The Autocorrelation plot for the data is:")
plt.grid(True)

plt.savefig('autocorrelation.png')
