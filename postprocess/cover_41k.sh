#!/bin/bash

# the directory of your mp3 files
input_root_dir="split_Ngoc_Lan"
output_root_dir="split_Ngoc_Lan_41k"

# create the root directory for output if it doesn't exist
mkdir -p ${output_root_dir}

# loop over all subdirectories
for dir in $(find ${input_root_dir} -type d)
do
  # create equivalent directory under output directory
  output_dir=${output_root_dir}/${dir#*/}
  mkdir -p "${output_dir}"

  # loop over all mp3 files in the subdirectory
  for file in $(find "${dir}" -name "*.mp3")
  do
    # remove the .mp3 extension
    base=${file%.mp3}

    # create output file path
    output_file=${output_dir}/${base#*/}.wav
    
    # convert to wav with 41kHz sample rate
    ffmpeg -i "${file}" -ar 44100 "${output_file}"
  done
done
