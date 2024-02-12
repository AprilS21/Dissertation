from scipy.stats import chi2_contingency

def chi_squared_test_for_randomness(binary_keys):
    """
    Perform the chi-squared test for randomness on a set of binary keys.

    Parameters:
    binary_keys (list): A list of binary keys (0 or 1).

    Returns:
    tuple: A tuple containing the test statistic, p-value, degrees of freedom,
           and the expected frequencies array.
    """
    observed_frequencies = [binary_keys.count(0), binary_keys.count(1)]
    total_keys = sum(observed_frequencies)
    expected_frequency = total_keys / 2  # Since we have 2 categories (0 and 1)

    # Perform the chi-squared test
    chi2_stat, p_val = chi2_contingency([observed_frequencies])[0:2]

    return chi2_stat, p_val, 1, [[expected_frequency, expected_frequency]]


def chi_squared_test_for_randomness_from_file(file_path):
    """
    Perform the chi-squared test for randomness on a set of binary keys read from a file.

    Parameters:
    file_path (str): The path to the file containing binary keys, one key per line.

    Returns:
    tuple: A tuple containing the test statistic, p-value, degrees of freedom,
           and the expected frequencies array.
    """
    # Read binary keys from file
    binary_keys = []

    with open(file_path, 'r') as file:
        # file in binary, strings of binary
        for line in file:
            line = line.strip()
            if line:
               binary_keys.append(int(line))
    print(len(binary_keys))
    print(binary_keys[0])
    return chi_squared_test_for_randomness(binary_keys)

file_path = "//wsl.localhost//Ubuntu//tmp//chosenBitsjmqeohbo.tekBits" 
chi2_stat, p_val, dof, expected_freq = chi_squared_test_for_randomness_from_file(file_path)
print("Chi-squared Statistic:", chi2_stat)
print("P-value:", p_val)
print("Degrees of Freedom:", dof)
print("Expected Frequencies:", expected_freq)
