# Code

- extractUniqueTEKs.py is a script that unzips all of the all-zips folders and extracts the TEKs into one large file. Based of code from sftcd keys repo, uses tek_list.py and TemporaryExposureKeyExport.proto. Takes a few hours to run.
- deduplicates.sh remove the duplicates from the large combined file and stores the unique keys in another file. Before remvoing duplicates the size of the combined keys file was 59.5GB. After removing the duplicates the size is 4.09GB
- spectralTest.R is an R script to perform spectral test for randomness, BROKEN, has issues with binary
- spectralTest.py is a python script to perform spectral test for randomness, works and does chi-squared and autocorrelation tests.