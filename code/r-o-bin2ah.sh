#!/bin/bash

# Convert random binary files from random.org into the
# ascii-hex format we have for TEKs (1 key/line)

# you can set this in the environment
: ${OUTPUT:=""}

if [[ "$OUTPUT" == "" ]]
then
    OUTPUT=`mktemp`
fi

echo "Adding TEK formatted randoms to $OUTPUT"

for file in $*
do
    echo "Doing $file"
    cat $file | xxd -c 16  -p >>$OUTPUT
done

echo "TEK formatted randoms added to $OUTPUT"
