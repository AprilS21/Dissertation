#!/bin/bash

# Convert Windows path to wsl path
input_file=$(wslpath -u "$1")
echo "1st parameter = $input_file"

#the path is not empty
if [ -z "$input_file" ]; then
    echo "Error: Empty input file path."
    exit 1
fi

startBits=$2
endBits=$3
runBool=$4

python3 ./code/countBits.py "$input_file"

python3 ./code/hilbertCurve.py "$input_file"

tmp_file=$(python3 ./code/extractBits.py "$startBits" "$endBits" "$runBool" "$input_file")

echo "temp file is $tmp_file"

#dieharder -a -f "$tmp_file"

python3 ./code/chisquared.py "$tmp_file"

python3 ./code/spectralTest.py "$tmp_file"

python3 ./code/autocorrelation.py "$tmp_file"

python3 ./code/lagplot.py "$tmp_file"
 