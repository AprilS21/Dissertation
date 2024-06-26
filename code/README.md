# Code
---

## Preprocessing
- extractUniqueTEKs.py is a script that unzips all of the all-zips folders and extracts the TEKs into one large file. Based of code from sftcd keys repo, uses tek_list.py and TemporaryExposureKeyExport.proto. Takes a few hours to run.
- deduplicates.sh remove the duplicates from the large combined file and stores the unique keys in another file. Before remvoing duplicates the size of the combined keys file was 59.5GB. After removing the duplicates the size is 4.09GB

--- 

## Tests
- spectralTest.py is a python script to perform spectral test for randomness, the method returns a p-value. Prints the number of significant p-values out of all the keys.
- hilbertCurve.py, python script to plot a hilbert curve of the keys, hexadecimal format.
- countBits.py counts the number of 1s and 0s at each bit position of the given file. It plots the results.
- chisquared.py runs chi squared test on given binary file. Returns chi squared test statistic and p value.
- autocorrelation.py performs autocorrelation analysis. Does it twice using two methods to compare. The data is normalised in one of the methods. Plots the results.
- lagplot.py produces lagplot for the given binary data.

---

## Running
- pipeline.sh is a bash script that takes command line input:
    - the path to the data file you wish to use
    - the first bit you want to extract
    - the second bit you want to extract
    - 1 if you want to extract all the bits between them, or 0 if not

Example usage:
```
bash pipeline.sh "D:\Dissertation\data_dest\uniques\snippetTeks" 1 56 1
```

This script passes the parameters to the extractBits.py script and the tests mentioned above. Calls dieharder but is commented out for the moment. 

- extractBits.py extracts the desired bits from the data. It takes startBit, endBit, runBool and file_path as parameters. The passed file should be in hexadecimal format. It converts each key in the file to binary and extracts the chosen bits. startBit is the first bit you want to extract and endBit is the last. runBool is used to choose whether you want all the bits inbetween startBit and endBit or just those bits themselves. It stores the bits in a temporary  named file. 

For example:
```
key = 100110101
startBit = 1
endBit = 5
runBool = 1
extracted_bits = 00110

startBit = 1
endBit = 5
runBool = 0
extracted_bits = 00
```
