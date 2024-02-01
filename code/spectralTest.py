import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

def hex_to_binary(file_name):
    with open(file_name, 'r') as file:
        hex_lines = file.readlines()
    
    # Convert hexadecimal values to binary and concatenate them
    binary_content = ''.join(bin(int(line.strip(), 16))[2:] for line in hex_lines)
    
    return binary_content

def spectral_test(binary_content):
    # Convert binary string to numpy array of integers
    binary_array = np.array(list(binary_content), dtype=int)
    
    # Perform FFT
    fft_result = np.fft.fft(binary_array)
    
    # Calculate power spectral density
    psd = np.abs(fft_result) ** 2
    
    # Plot power spectral density
    plt.plot(psd)
    plt.title('Power Spectral Density')
    plt.xlabel('Frequency')
    plt.ylabel('Power')
    plt.show()

def autocorrelation(binary_content):
    # Convert binary string to array of integers
    binary_array = np.array(list(binary_content), dtype=int)
    
    # Compute autocorrelation
    autocorr = np.correlate(binary_array, binary_array, mode='full')
    
    # Plot autocorrelation
    plt.plot(autocorr)
    plt.title('Autocorrelation')
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.show()

def chi_squared_test(binary_content):
    # Convert binary string to array of integers
    binary_array = np.array(list(binary_content), dtype=int)
    
    # Count zeros and ones
    count_zeros = np.count_nonzero(binary_array == 0)
    count_ones = np.count_nonzero(binary_array == 1)
    
    # Compute expected counts for uniform distribution
    total_count = len(binary_array)
    expected_count = total_count / 2
    
    # Compute chi-squared statistic
    chi_squared = ((count_zeros - expected_count)**2 / expected_count) + ((count_ones - expected_count)**2 / expected_count)
    
    # Compute degrees of freedom
    degrees_of_freedom = 1
    
    # Compute p-value
    p_value = 1 - chi2.cdf(chi_squared, degrees_of_freedom)
    
    # Print results
    print(f"Chi-squared statistic: {chi_squared}")
    print(f"P-value: {p_value}")

file_name = "D://Dissertation//data_dest//uniques//snippetTeks"
binary_content = hex_to_binary(file_name)
spectral_test(binary_content)
autocorrelation(binary_content)
chi_squared_test(binary_content)
