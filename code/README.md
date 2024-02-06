# Code
---

## Preprocessing
- extractUniqueTEKs.py is a script that unzips all of the all-zips folders and extracts the TEKs into one large file. Based of code from sftcd keys repo, uses tek_list.py and TemporaryExposureKeyExport.proto. Takes a few hours to run.
- deduplicates.sh remove the duplicates from the large combined file and stores the unique keys in another file. Before remvoing duplicates the size of the combined keys file was 59.5GB. After removing the duplicates the size is 4.09GB

--- 

## Tests
- spectralTest.R is an R script to perform spectral test for randomness, BROKEN, has issues with binary
- spectralTest.py is a python script to perform spectral test for randomness, works and does chi-squared and autocorrelation tests.

---

## Running
- pipeline.sh is a bash script that takes command line input:
    - the path to the data file you wish to use
    - the first bit you want to extract
    - the second bit you want to extract
    - 1 if you want to extract all the bits between them, or 0 if not

Example usage:
'''
bash pipeline.sh "D:\Dissertation\data_dest\uniques\snippetTeks" 1 5 1
'''

This script passes the parameters to the extractBits.py script. I will expand this script to pass the outputed file to the tests, etc.

- extractBits.py extracts the desired bits from the data. It takes startBit, endBit, runBool and file_path as parameters. The passed file should be in hexadecimal format. It converts each key in the file to binary and extracts the chosen bits. startBit is the first bit you want to extract and endBit is the last. runBool is used to choose whether you want all the bits inbetween startBit and endBit or just those bits themselves. It stores the bits in a temporary  named file. 

For example:
'''
key = 100110101
startBit = 1
endBit = 5
runBool = 1
extracted_bits = 00110

startBit = 1
endBit = 5
runBool = 0
extracted_bits = 00
'''