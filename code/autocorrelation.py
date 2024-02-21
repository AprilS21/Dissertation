import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

def convert_ints(keys):
    return [int(x) for x in keys]

def calculate_autocorrelation(data):
    """
    Calculates autocorrelation on a set of  keys. Normalises the data

    Parameters:
    keys (list): List of keys, binary format
    """
    # normalize data to range [0,  1]
    normalized_data = (data - np.mean(data)) / np.std(data)
    autocorrelation_result = np.correlate(normalized_data, normalized_data, mode='full')
    
    # normalize result
    autocorrelation_result = autocorrelation_result / np.max(autocorrelation_result)
    return autocorrelation_result[autocorrelation_result.size //  2:]

def plot_autocorrelation_normalised(autocorrelation_result):
    plt.plot(autocorrelation_result)
    plt.title('Autocorrelation of Cryptographic Keys')
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.savefig("./normalisedAutocorrelation.png")

def plot_autocorrelation(data):
    """
    Plots autocorrelation. Uses different function that calculate_autocorrelation, doesn't normalise

    Parameters:
    keys (list): List of keys, binary format
    """
    plt.clf()
    plt.title("Autocorrelation Plot") 
    plt.xlabel("Lags") 
    #plot autocorrelation
    plt.acorr(data, maxlags = 10) 
    plt.grid(True)
    plt.savefig("./autocorrelation.png")

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


def main(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    int_keys = convert_ints(binary_data)

    autocorrelation_result = calculate_autocorrelation(int_keys)
    plot_autocorrelation_normalised(autocorrelation_result)

    plot_autocorrelation(int_keys)
    correlation_coefficient = correlation_analysis(int_keys)
    print("Pearson correlation coefficient between keys:", correlation_coefficient)
    


main(str(sys.argv[1]))
