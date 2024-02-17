import sys
import matplotlib.pyplot as plt
import numpy as np

def main(path):
    countZeros = [0]*128
    countOnes = [0]*128
    number_of_bits = 128
    f = open(path, "r")
    for line in f:
        binary = bin(int(line.strip(), 16))[2:]
        # Ensure that the binary string has the desired number of bits by adding leading zeros if necessary
        num_zeros_to_add = number_of_bits - len(binary)
        if num_zeros_to_add > 0:
            binary = '0' * num_zeros_to_add + binary
        #print("binary ", binary)
        index =0
        for i in binary:
            #print(i)
            if(i == '0'):
                countZeros[index] += 1
                #print("added 0 at index ", index)
            else:
                if (i == '1'):
                    countOnes[index] += 1
                    #print("added 1 at index ", index)
            index += 1
    percentageZerosArray = [0]*128
    percentageOnesArray = [0]*128
    for index,x in enumerate(zip(countZeros, countOnes)):
        #print("count zeros vs ones on bit ", index, " is: ", x)
        totalCount = x[0] + x[1]
        percentageZeros = x[0]/totalCount * 100
        percentageZerosArray[index] = percentageZeros
        percentageOnes = x[1]/totalCount * 100
        percentageOnesArray[index] = percentageOnes
        print("Bit ", index, " percentage of zeros ", percentageZeros, " and percentage ones ", percentageOnes)

    # Sample data (percentage of ones and zeros for each bit position)
    # Replace this with your actual data
    bit_positions = np.arange(128)

        # Create stacked bar chart
    plt.figure(figsize=(12, 8))
    plt.barh(bit_positions, percentageOnesArray, color='blue', label='Percentage of Ones')
    plt.barh(bit_positions, percentageZerosArray, left=percentageOnesArray, color='red', label='Percentage of Zeros')

    plt.xlabel('Percentage')
    plt.ylabel('Bit Position')
    plt.title('Percentage of Ones and Zeros in Each Bit Position')
    plt.yticks(bit_positions, [str(bit) for bit in bit_positions])
    plt.legend(loc='upper right')
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)

    plt.savefig('counts1v0.png')



if __name__ == "__main__":
    #path = str(sys.argv[1])
    path = "sampleData/snippetTeks"
    #path = "sampleData/nonRandomLooksRandom"
    main(path)