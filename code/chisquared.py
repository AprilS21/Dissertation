import sys
from scipy.stats import chi2_contingency

def chi_squared_test_for_randomness(zeros, ones):
    """
    Performs a chi-squared test for randomness on counts of zeros and ones.

    Args:
    zeros (int): Count of zeros.
    ones (int): Count of ones.

    Returns:
    p_value (float): The p-value obtained from the chi-squared test.
    """

    # Observed frequencies array
    observed_freq = [zeros, ones]

    # Expected frequencies, 50% chance of either
    total_count = zeros + ones
    expected_freq = [total_count / 2, total_count / 2]

    chi2, p_value, _, _ = chi2_contingency([observed_freq, expected_freq])

    return chi2, p_value, expected_freq

def main(path):
    zeros = 0
    ones = 0
    with open(path, 'r') as file:
        for line_count, line in enumerate(file, start=1):
            line = line.strip()
            if line:
                zeros += line.count('0')
                ones += line.count('1')
    print("Total number of keys:", line_count)

    chi, pval, expected_freq = chi_squared_test_for_randomness(zeros, ones)

    print("Chi-squared Statistic:", chi)
    print("P-value:", pval)
    print("Expected Frequencies:", expected_freq)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file_path")
        sys.exit(1)
    path = sys.argv[1]
    main(path)
