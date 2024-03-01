#!/bin/bash

# check hashes match files after bittorrent downloads

for ((year = 2017; year <= 2023; year++))
do
    for ((month = 1; month <= 12; month++))
    do
        MONTH="`printf  "%02d" $((month))`"
        hashfile="download?file=$year-$MONTH-bin.md5"
        if [ ! -f $hashfile ]
        then
            echo "Can't find $hashfile - exiting"
            exit 1
        fi

        while read line
        do
            hash=`echo $line | awk '{print $1}'`
            hashin=`echo $line | awk '{print $2}'`
            hashcalc=`cat random.org-pregenerated-$year-$MONTH-bin/$hashin | openssl md5 | awk '{print $2}'`
            if [[ "$hash" != "$hashcalc" ]]
            then
                echo "Hash mismatch for $hashin - exiting"
                exit 2
            else
                echo "hash ok for $hashin"
            fi
        done < $hashfile
    done
done
