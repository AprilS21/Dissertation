# Importing the libraries.
import matplotlib.pyplot as plt 
import numpy as np 

import numpy as np

def correlation_analysis(keys):
    """
    Perform correlation analysis on a set of  keys.

    Parameters:
    keys (list): List of keys, binary format

    Returns:
    float: Pearson correlation coefficient between keys.
    """
    keys_array = np.array(keys)
    # get Pearson correlation coefficient
    correlation_coefficient = np.corrcoef(keys_array)
    return correlation_coefficient

def main(path):
    """
    Plot autocorrelation of a set of keys

    Parameters:
    path to file containing keys, binary format

    Returns:
    saves plot as autocorrelation.png
    prints correlation coefficient
    """
    binary_keys = []

    with open(path, 'r') as file:
        # file in binary, strings of binary
        for line in file:
            line = line.strip()
            if line:
                binary_keys.append(int(line))

    plt.title("Autocorrelation Plot") 
    plt.xlabel("Lags") 
    #plot autocorrelation
    plt.acorr(binary_keys, maxlags = 10) 
    print("The Autocorrelation plot for the data is:")
    plt.grid(True)
    plt.savefig('autocorrelation.png')

    correlation_coefficient = correlation_analysis(binary_keys)
    print("Pearson correlation coefficient between keys:", correlation_coefficient)

if __name__ == "__main__":
    #path = str(sys.argv[1])
    #path = "sampleData/nonRandomLooksRandom"
    #path = "sampleData/nonRandom"
    #path = "sampleData/snippetTeks"
    path = "//wsl.localhost//Ubuntu//tmp//chosenBitscd6wlfz0.tekBits"
    main(path)
