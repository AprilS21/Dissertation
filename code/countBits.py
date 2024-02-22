#!/bin/python
import sys
import matplotlib.pyplot as plt
import numpy as np

def main(path):
    """
    Counts frequencies of 1 and 0 in each bit position in set of keys. Plots
    results.

    Parameters:
    path to file containing keys, hexadecimal format

    Returns:
    saves figure as counts1v0.png
    """
        
    countZeros = [0]*128
    countOnes = [0]*128
    number_of_bits = 128
    line_count = 0
    f = open(path, "r")
    for line in f:
        if (len(line) != 33):
            line_count += 1
            print("Skipping bad length line at",line_count,"line:",line,file=sys.stderr)
            print("length",len(line),file=sys.stderr)
            continue
        try:
            binary = bin(int(line.strip(), 16))[2:]
            #adds leading 0s to make sure all keys are 128 bits in length
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
            line_count += 1
            if ((line_count % 10000) == 0):
                print("Processed",line_count,file=sys.stderr)
        except Exception as e:
            print("Exception",e,"at",line_count,"index",index,file=sys.stderr)
            print("Line:",line,file=sys.stderr)
    percentageZerosArray = [0]*128
    percentageOnesArray = [0]*128
    print("Bit,zeros,ones,total")
    for index,x in enumerate(zip(countZeros, countOnes)):
        #print("count zeros vs ones on bit ", index, " is: ", x)
        totalCount = x[0] + x[1]
        percentageZeros = x[0]/totalCount * 100
        percentageZerosArray[index] = percentageZeros
        percentageOnes = x[1]/totalCount * 100
        percentageOnesArray[index] = percentageOnes
        # print("Bit ", index, " percentage of zeros ", percentageZeros,
              # " and percentage ones ", percentageOnes)
        print(index, ",", percentageZeros, ",", percentageOnes,
              ",", totalCount)

    bit_positions = np.arange(128)

    #Plot bar chart
    plt.figure(figsize=(12, 8))
    plt.barh(bit_positions, percentageOnesArray, color='blue',
             label='Percentage of Ones')
    plt.barh(bit_positions, percentageZerosArray, left=percentageOnesArray,
             color='red', label='Percentage of Zeros')

    plt.xlabel('Percentage')
    plt.ylabel('Bit Position')
    plt.title('Percentage of Ones and Zeros in Each Bit Position')
    plt.yticks(bit_positions, [str(bit) for bit in bit_positions])
    plt.legend(loc='upper right')
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)

    plt.savefig('./counts1v0.png')



if __name__ == "__main__":
    path = str(sys.argv[1])
    #path = "sampleData/snippetTeks"
    #path = "sampleData/nonRandomLooksRandom"
    main(path)

