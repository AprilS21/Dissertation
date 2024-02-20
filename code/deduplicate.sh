#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <input_file>"
  exit 1
fi

input_file=$(wslpath -u "$1")
output_file="${input_file}_unique"

if [ ! -f "$input_file" ]; then
  echo "Error: Input file '$input_file' not found."
  exit 1
fi

temp_dir=$(mktemp -d)

# Split the large file into smaller chunks
split -l 100000 "$input_file" "$temp_dir/chunk_"

for chunk_file in "$temp_dir"/*; do
  sort -u "$chunk_file" >> "$temp_dir/unique_chunks"
done

sort -u "$temp_dir/unique_chunks" > "$output_file"

rm -rf "$temp_dir"

echo "Duplicate rows removed. Unique data saved to '$output_file'."

