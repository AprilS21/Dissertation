#!/bin/bash

output_file1="nonRandomLooksRandom"
output_file2="nonRandom"

# Function to generate MD5 hash
generate_md5() {
    echo -n "$1" | md5sum | awk '{print $1}'
}

current_key="0"

for (( i=1; i<=1000; i++ )); do
    md5_hash=$(generate_md5 "$current_key")
    current_key="$md5_hash"
    echo "$current_key" >> "$output_file1"
    echo "Key $i: $current_key"
done

# Function to generate keys based on a sequential pattern
generate_key() {
    local prefix="111111111111111111111111111111"
    local suffix=$(printf "%02d" "$1") # Zero padding
    echo "$prefix$suffix"
}

for ((i=1; i<=1000; i++)); do
    key=$(generate_key "$i")
    echo "$key" >> "$output_file2"
done

echo "Keys generated and saved to $output_file2"
