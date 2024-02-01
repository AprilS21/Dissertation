import sys
import pandas as pd
import tempfile

def main(startBit, endBit, runBool, path):
    temp_file = tempfile.NamedTemporaryFile(suffix=".tekBits", dir="D:\\Dissertation\\data_dest\\uniques", delete=False)
    tmpf = temp_file.name

    f = open(path, "r")
    print(f.readline())

    for line in f:
        binary = bin(int(line.strip(), 16))[2:]
        #print(binary)
        if(runBool == 1):
            # extract k  bit sub-string
            kBitSubStr = binary[startBit : endBit]
        else:
            kBitSubStr = binary[startBit, endBit]
        print(kBitSubStr)



if __name__ == "__main__":
    startBit = int(sys.argv[1])
    endBit = int(sys.argv[2])
    runBool = int(sys.argv[3])
    path = str(sys.argv[4])
    main(startBit, endBit, runBool, path)
