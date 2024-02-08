#!/bin/bash

# Convert Windows path to Unix-style path
input_file=$(wslpath -u "$1")
echo "1st parameter = $input_file"

# Ensure the path is not empty
if [ -z "$input_file" ]; then
    echo "Error: Empty input file path."
    exit 1
fi

# Now, continue with the script execution
startBits=$2
endBits=$3
runBool=$4

tmp_file=$(python3 extractBits.py "$startBits" "$endBits" "$runBool" "$input_file")

echo "temp file is $tmp_file"

python3 spectralTest.py "$tmp_file"