#!/bin/bash

# Input file from which content will be copied
input_file="./sampleData/snippetTeks"

# CSV file to create
output_csv="hexKeys.csv"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file '$input_file' not found."
    exit 1
fi

# Copy contents from input file to CSV file
cp "$input_file" "$output_csv"

echo "Contents copied from '$input_file' to '$output_csv'."
