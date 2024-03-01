#!/bin/bash

# Get a large enough set of Mads' random number torrent files

for ((year = 2017; year <= 2023; year++))
do
    for ((month = 1; month <= 12; month++))
    do
        MONTH="`printf  "%02d" $((month))`"
        echo "Getting $year-$MONTH"
        wget https://archive.random.org/download?file=$year-$MONTH-bin.torrent
    done
done
