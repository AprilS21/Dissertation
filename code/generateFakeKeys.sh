#!/bin/bash

output_file1="nonRandomLooksRandom"
output_file2="nonRandom"

# Function to generate MD5 hash
generate_md5() {
    echo -n "$1" | md5sum | awk '{print $1}'
}

# Initial key
current_key="0"

# Generate 1000 keys
for (( i=1; i<=1000; i++ )); do
    # Generate MD5 hash of the current key
    md5_hash=$(generate_md5 "$current_key")
    
    # Update the current key with the MD5 hash
    current_key="$md5_hash"
    echo "$current_key" >> "$output_file1"
    # Output the key
    echo "Key $i: $current_key"
done


# Function to generate keys based on a sequential pattern
generate_key() {
    local prefix="111111111111111111111111111111"
    local suffix=$(printf "%02d" "$1") # Zero padding for numbers less than 10
    echo "$prefix$suffix"
}

# Generate 1000 keys
for ((i=1; i<=1000; i++)); do
    key=$(generate_key "$i")
    echo "$key" >> "$output_file2"
done

echo "Keys generated and saved to $output_file2"
