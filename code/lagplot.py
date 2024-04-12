import sys
import matplotlib.pyplot as plt
import numpy as np

def read_hex_keys(filename):
    with open(filename, 'r') as file:
        keys = file.readlines()
    return [int(key.strip(), 16) for key in keys]

def calculate_differences(keys):
    return [keys[i] - keys[i-1] for i in range(1, len(keys))]

def plot_lagplot(differences):
    plt.figure(figsize=(12, 12))
    plt.scatter(differences[:-1], differences[1:], alpha=0.5)
    plt.xlabel('Difference i')
    plt.ylabel('Difference i+1')
    plt.title('Lagplot')
    plt.grid(True)
    #plt.show()
    plt.savefig('./lagplot.png')
    plt.close()

def main():
    filename = sys.argv[1] 
    keys = read_hex_keys(filename)
    differences = calculate_differences(keys)
    plot_lagplot(differences)

if __name__ == "__main__":
    main()
