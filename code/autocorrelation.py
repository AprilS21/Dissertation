# Importing the libraries.
import matplotlib.pyplot as plt 
import numpy as np 

import numpy as np

def correlation_analysis(keys):
    """
    Perform correlation analysis on a set of cryptographic keys.

    Args:
    keys (list): List of cryptographic keys (e.g., bytes or integers).

    Returns:
    float: Pearson correlation coefficient between keys.
    """
    # Convert keys to numpy array for efficient computation
    keys_array = np.array(keys)

    # Compute the Pearson correlation coefficient
    correlation_coefficient = np.corrcoef(keys_array)

    return correlation_coefficient


file_path = "//wsl.localhost//Ubuntu//tmp//chosenBitscd6wlfz0.tekBits"
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

correlation_coefficient = correlation_analysis(binary_keys)
print("Pearson correlation coefficient between keys:", correlation_coefficient)
