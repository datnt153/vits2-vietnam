import os 
def create_label(index):
    with open(f'output_25_09/{index}.txt', 'r') as file1:
        text = file1.read()

    lines = text.split('\n')

    with open(f"label.txt", "a") as f:

        for i, line in enumerate(lines):
            audio_path = f"split_Ngoc_Lan/{index}/example_{i}.mp3"
            if os.path.isfile(audio_path):
                f.write(f"{audio_path}|{line}\n")

 
for i in range(1, 68):
     create_label(i)



def split_text_file(input_file, train_file, test_file, val_file):
    # Read the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Calculate the indices for splitting
    total_lines = len(lines)
    test_lines = 100
    val_lines = 50

    # Split the lines into train, test, and val
    train_lines = lines[:total_lines - test_lines - val_lines]
    test_lines = lines[total_lines - test_lines - val_lines:total_lines - val_lines]
    val_lines = lines[total_lines - val_lines:]

    # Write the lines to respective files
    with open(train_file, 'w') as file:
        file.writelines(train_lines)

    with open(test_file, 'w') as file:
        file.writelines(test_lines)

    with open(val_file, 'w') as file:
        file.writelines(val_lines)

# Example usage
split_text_file("label.txt", "train.txt", "test.txt", "val.txt")
