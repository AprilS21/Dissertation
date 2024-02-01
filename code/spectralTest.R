# Load required library for Fourier transform
library(signal)

spectral_test <- function(filename) {
 # Read the keys from the file
 keys <- readLines(filename)
  
 # Convert the keys to numeric values
 keys <- strtoi(keys, base = 16)
 print(head(keys))
  # Remove NA values
 keys <- keys[!is.na(keys)]
 print(keys)
 # Compute Fourier Transform
 keys_fft <- abs(fft(keys)) / length(keys)
  
 # Compute Power Spectral Density (PSD)
 psd <- abs(keys_fft)^2 / length(keys)
  # Remove NA values
 psd <- psd[!is.na(psd)]
 # Plot the PSD
 plot(psd, type = "l", xlab = "Frequency", ylab = "Power Spectral Density", 
       main = "Power Spectral Density (PSD)")
  
 # Perform statistical tests
 # Chi-square test
 chisq_test <- chisq.test(psd)$p.value
 cat("Chi-square test p-value:", chisq_test, "\n")
  
 # Kolmogorov-Smirnov test
 ks_test <- ks.test(psd, "punif")$p.value
 cat("Kolmogorov-Smirnov test p-value:", ks_test, "\n")
  
 # Anderson-Darling test
 #library(nortest)
 #ad_test <- ad.test(psd)$p.value
 #cat("Anderson-Darling test p-value:", ad_test, "\n")
}


# CommandArgs picks up the variables you pass from the command line
args <- commandArgs(trailingOnly = TRUE)
print(args[1])

# Read data from file and convert to ASCII values
#data <- read.table(args[1], header = TRUE, sep = "\n")
#head(data)

# Example usage:
# spectral_test function call
spectral_test(args[1])
