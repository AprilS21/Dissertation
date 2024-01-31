# Load required library for Fourier transform
library(signal)

# Function to perform spectral test for randomness
spectral_test <- function(keys) {
  # Compute Fourier Transform
  keys_fft <- fft(keys)
  
  # Compute Power Spectral Density (PSD)
  psd <- abs(keys_fft)^2 / length(keys)
  
  # Plot the PSD
  plot(psd, type = "l", xlab = "Frequency", ylab = "Power Spectral Density", 
       main = "Power Spectral Density (PSD)")
  
  # Perform statistical tests
  # You can add your statistical tests here to quantify randomness
  
  # Example of statistical test: Chi-square test for uniform distribution
  chisq_test <- chisq.test(psd)$p.value
  cat("Chi-square test p-value:", chisq_test, "\n")
  
  # Example of statistical test: Kolmogorov-Smirnov test for uniform distribution
  ks_test <- ks.test(psd, "punif")$p.value
  cat("Kolmogorov-Smirnov test p-value:", ks_test, "\n")
}

# Example usage:
# Generate a set of keys (random numbers in this case)
set.seed(123) # for reproducibility
keys <- runif(1000)  # Generating 1000 random numbers
spectral_test(keys)
