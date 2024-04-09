#!/bin/bash

# Convert Windows path to wsl path
#input_file=$(wslpath -u "$1")
#echo "1st parameter = $input_file"

#the path is not empty
#if [ -z "$input_file" ]; then
#    echo "Error: Empty input file path."
#    exit 1
#fi

input_file=$1
startBits=$2
endBits=$3
runBool=$4

python3 countBits.py "$input_file"

python3 hilbertCurve.py "$input_file"

tmp_file=$(python3 extractBits.py "$startBits" "$endBits" "$runBool" "$input_file")

echo "temp file is $tmp_file"

#dieharder -a -f "$tmp_file"

python3 chisquared.py "$tmp_file"

python3 spectralTest.py "$tmp_file"

python3 autocorrelation.py "$tmp_file"

python3 lagplot.py "$tmp_file"
 
