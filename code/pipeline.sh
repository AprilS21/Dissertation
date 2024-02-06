#!/bin/bash

input_file=$(wslpath -u "$1")
echo "1st parameter = $1 "
#input_file=$1
startBits=$2
endBits=$3
runBool=$4

tmp_file=$(python3 extractBits.py $startBits $endBits $runBool $input_file)

echo "temp file is $tmp_file "

