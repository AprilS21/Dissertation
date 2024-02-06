import sys
import pandas as pd
import tempfile

def main(startBit, endBit, runBool, path):
    temp_file = tempfile.NamedTemporaryFile(prefix= "chosenBits", suffix=".tekBits", delete=False)
    tmpf = open(temp_file.name, 'w')

    f = open(path, "r")
    #print(f.readline())

    for line in f:
        binary = bin(int(line.strip(), 16))[2:]
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
