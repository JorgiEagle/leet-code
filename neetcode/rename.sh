#!/bin/bash

# Loop through all files in the current directory
for file in *.py; do
  # Extract the base name without the extension
  base=$(basename "$file" .py)
  # Use regex to match the pattern and extract parts
  if [[ $base =~ ^(.*)_([0-9]+)$ ]]; then
    prefix=${BASH_REMATCH[1]}
    number=${BASH_REMATCH[2]}
    # Construct the new file name
    newname="${number}_${prefix}.py"
    # Rename the file
    mv "$file" "$newname"
  fi
done
