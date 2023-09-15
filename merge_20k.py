import os

# Define the maximum character limit per merged file
max_chars_per_file = 49700

# Specify the directory containing your text files
input_directory = 'infore'

# Define the output directory and file name
output_directory = 'ouput50K'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to merge text files and split into multiple output files
def merge_and_split_text_files(input_directory, output_directory, max_chars_per_file):
    current_chars = 0
    output_file_number = 1
    merged_text = ''

    for filename in sorted(os.listdir(input_directory)):
        if filename.endswith('.txt'):
            with open(os.path.join(input_directory, filename), 'r') as file:
                file_text = file.read()
                if len(file_text) + current_chars > max_chars_per_file:
                    # Save the current merged text to a new output file
                    output_file_path = os.path.join(output_directory, f'merged_{output_file_number}.txt')
                    with open(output_file_path, 'w') as output_file:
                        output_file.write(merged_text + "\n")
                    output_file_number += 1
                    merged_text = ''
                    current_chars = 0

                merged_text += file_text 
                merged_text += '\n'
                current_chars += len(file_text)

    # Save any remaining merged text to the last output file
    if merged_text:
        output_file_path = os.path.join(output_directory, f'merged_{output_file_number}.txt')
        with open(output_file_path, 'w') as output_file:
            output_file.write(merged_text)

# Merge and split the text files
merge_and_split_text_files(input_directory, output_directory, max_chars_per_file)

print(f'Merged and split files in {input_directory} into {output_directory}')