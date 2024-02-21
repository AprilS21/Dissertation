import sys
from scipy.stats import chi2_contingency


def chi_squared_test_for_randomness(binary_keys:str):
    """
    Performs a chi-squared test for randomness on a set of binary keys.

    Args:
    binary_keys (list): List of binary keys (0s and 1s), strings.

    Returns:
    p_value (float): The p-value obtained from the chi-squared test.
    """

    zeros =0
    ones =0
    for x in binary_keys:
        zeros += x.count('0')
        ones += x.count('1')
    #print(binary_keys)
    print("Number of zeros:" , zeros)
    print("Number of ones: ", ones)
    # observed frequencies array
    observed_freq = [zeros, ones]

    # Expected frequencies, 50% chance of either
    total_count = zeros + ones
    expected_freq = [total_count / 2, total_count / 2]

    chi2, p_value, _, _ = chi2_contingency([observed_freq, expected_freq])

    return chi2, p_value, expected_freq


def main(path):
    binary_keys = []

    with open(path, 'r') as file:
        # file in binary, strings of binary
        for line in file:
            line = line.strip()
            if line:
               binary_keys.append(line)
    print(len(binary_keys))

    chi, pval, expected_freq = chi_squared_test_for_randomness(binary_keys)
    print("Chi-squared Statistic:", chi)
    print("P-value:", pval)
    print("Expected Frequencies:", expected_freq)

if __name__ == "__main__":
    #path = "//wsl.localhost//Ubuntu//tmp//chosenBitsr0lzrvxp.tekBits"
    path = str(sys.argv[1])
    #path = "sampleData/test"
    main(path)
