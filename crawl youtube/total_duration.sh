#!/bin/bash

directory="blv AQ"
total_duration=0

# Iterate over files in the directory
for file in "$directory"/*.wav; do
    # Get the duration of the WAV file using soxi
    duration=$(soxi -D "$file")
    
    # Add the duration to the total
    total_duration=$(bc <<< "$total_duration + $duration")
done

# Print the total duration
echo "Total Duration: $total_duration seconds"
