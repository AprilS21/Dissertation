import sys

def main(path):
    countZeros = [0]*12
    countOnes = [0]*12
    number_of_bits = 12
    f = open(path, "r")
    for line in f:
        binary = bin(int(line.strip(), 16))[2:]
        # Ensure that the binary string has the desired number of bits by adding leading zeros if necessary
        num_zeros_to_add = number_of_bits - len(binary)
        if num_zeros_to_add > 0:
            binary = '0' * num_zeros_to_add + binary
        print("binary ", binary)
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
    for index,x in enumerate(countZeros):
        print("count zero on bit ", index, " is: ", x)
    for index,x in enumerate(countOnes):
        print("count ones on bit ", index, " is: ", x)


if __name__ == "__main__":
    #path = str(sys.argv[1])
    path = "sampleData/test"
    main(path)