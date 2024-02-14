import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import scipy.special as spc

def spectral(bin_data: str):
    #From: https://gist.github.com/StuartGordonReid/54845bf66de7e195b335#file-spectral-py 
    """
    Note that this description is taken from the NIST documentation [1]
    [1] http://csrc.nist.gov/publications/nistpubs/800-22-rev1a/SP800-22rev1a.pdf
    The focus of this test is the peak heights in the Discrete Fourier Transform of the sequence. The purpose of
    this test is to detect periodic features (i.e., repetitive patterns that are near each other) in the tested
    sequence that would indicate a deviation from the assumption of randomness. The intention is to detect whether
    the number of peaks exceeding the 95 % threshold is significantly different than 5 %.
    :param bin_data: a binary string
    :return: the p-value from the test
    """
    n = len(bin_data)
    n = int(n)
    #print(n)
    plus_minus_one = []
    for char in bin_data:
        if char == '0':
            plus_minus_one.append(-1)
        elif char == '1':
            plus_minus_one.append(1)
    # Product discrete fourier transform of plus minus one
    s = np.fft.fft(plus_minus_one)
    modulus = np.abs(s[0:n // 2])
    tau = np.sqrt(np.log(1 / 0.05) * n)
    # Theoretical number of peaks
    count_n0 = 0.95 * (n / 2)
    # Count the number of actual peaks m > T
    count_n1 = len(np.where(modulus < tau)[0])
    # Calculate d and return the p value statistic
    d = (count_n1 - count_n0) / np.sqrt(n * 0.95 * 0.05 / 4)
    p_val = spc.erfc(abs(d) / np.sqrt(2))
    return p_val

def main():
    countKeys =0
    countSignificant =0
    with open(path, 'r') as file:
        # file in binary, strings of binary
        for line in file:
            line = line.strip()
            line = bin(int(line.strip(), 16))[2:]
            if line:
                countKeys += 1
                x = spectral(line)
                if(x < 0.05):
                    countSignificant += 1

    print("rejected", countSignificant, " out of ", countKeys, " result ", countSignificant/countKeys*100, "%")


if __name__ == "__main__":
    #path = str(sys.argv[1])
    #path = "sampleData/nonRandomLooksRandom"
    path = "sampleData/nonRandom"
    #path = "sampleData/snippetTeks"
    main()