import os
import subprocess
import torch 

# the directory of your mp3 files
input_root_dir = "split_Ngoc_Lan"
output_root_dir = "split_Ngoc_Lan_22050"

# create the root directory for output if it doesn't exist
os.makedirs(output_root_dir, exist_ok=True)

# loop over all subdirectories
for dirpath, dirnames, filenames in os.walk(input_root_dir):
    # create equivalent directory under output directory
    output_dir = os.path.join(output_root_dir, os.path.relpath(dirpath, input_root_dir))
    print(f"output_dir: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)

    # loop over all mp3 files in the subdirectory
    for filename in filenames:
        if filename.endswith(".mp3"):
            print(f"filename: {filename}")
            # remove the .mp3 extension
            base = filename[:-4]

            print(f"base: {base}")
            # create output file path
            output_file = os.path.join(output_dir, base + ".wav")
            print(f"output_file: {output_file}")
            
            # convert to wav with 41kHz sample rate
            subprocess.run(["ffmpeg", "-i", os.path.join(dirpath, filename), "-ar", "22050", output_file])
