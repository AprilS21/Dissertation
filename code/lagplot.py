# Import Libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats as sc

def main(path):
    """
    Creates lag plot for set of keys

    Parameters:
    path to file containing keys, binary format

    Returns:
    saves figure as lagplot.png
    """
    binary_keys = []

    with open(path, 'r') as file:
        # file in binary, strings of binary
        for line in file:
            line = line.strip()
            if line:
                binary_keys.append(int(line))


    data_series = pd.Series(binary_keys)
    #print(data_series.head()) 
    data=data_series.reset_index()
    #print(data.head()) 
    fig, ax = plt.subplots(1, 2, figsize=(12, 7)) 
    ax[0].plot(data['index'],data[0])
    pd.plotting.lag_plot(data,lag=1,ax =ax[1]) 
    plt.savefig('lagplot.png') 

if __name__ == "__main__":
    path = "//wsl.localhost//Ubuntu//tmp//chosenBitsjmqeohbo.tekBits"
    main(path)
