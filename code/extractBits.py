import sys
import pandas as pd
import tempfile

def main(startBit, endBit, runBool, path):
    number_of_bits = 128
    temp_file = tempfile.NamedTemporaryFile(prefix= "chosenBits", suffix=".tekBits", delete=False)
    tmpf = open(temp_file.name, 'w')

    f = open(path, "r")
    #print(f.readline())

    for line in f:
        binary = bin(int(line.strip(), 16))[2:]
        num_zeros_to_add = number_of_bits - len(binary)
        # adding leading 0s to keeps keys 128 bits long
        if num_zeros_to_add > 0:
            binary = '0' * num_zeros_to_add + binary
        #print(binary)
        if(runBool == 1):
            # extract k  bit sub-string
            kBitSubStr = binary[startBit : endBit]
        else:
            kBitSubStr = binary[startBit, endBit]

        #print(kBitSubStr)
        tmpf.write(kBitSubStr + '\n')

    print(temp_file.name)
    #f.close()
    #tmpf.close()



if __name__ == "__main__":
    startBit = int(sys.argv[1])
    endBit = int(sys.argv[2])
    runBool = int(sys.argv[3])
    path = str(sys.argv[4])
    main(startBit, endBit, runBool, path)
