
def merge(index_name):
    # Read the content from File 1 and File 2
    with open(f'predict/{index_name}.txt', 'r') as file1:
        text = file1.read()
        text = text.replace("Ô tô", "ôtô")
        text = text.replace("moto", "mo to")
        text = text.replace("camera", "ca me ra")
        text = text.replace("vi vút", "virus")
        text = text.replace("ti vi", "tivi")
        text = text.replace("massage", "mass sage")
        text = text.replace("-", " ")
        text = text.replace("ca lo", "calo")
        text = text.replace("acid", "a cid")
        # text = text.replace("TV", "ti vi")
        text = text.replace("vitamin", "vi ta min")
        text = text.replace("TP", "Thành phố")
        text = text.replace("USD", "đô la mỹ")
        # text = text.replace("Việt An", "real")
                                
        content_file1  = text

    with open(f'ouput20K/{index_name}.txt', 'r') as file2:
        content_file2 = file2.read()
        content_file2 = content_file2.replace("hlv", "huấn luyện viên")
        content_file2 = content_file2.replace("đt", "đội tuyển")
        content_file2 = content_file2.replace("ts", "tiến sĩ")
        content_file2 = content_file2.replace("usd", "đô la mỹ")
        content_file2 = content_file2.replace("xhcn", "xã hội chủ nghĩa")


    # Split the content of File 1 into lines
    lines_file1 = content_file1.split('\n')
    lines_file2 = content_file2.split('\n')

    # Create a list to store the mapped lines
    mapped_lines = []

    # Iterate through the lines of File 1 and map to File 2
    j = 0  # Initialize the index for File 2
    index = 0
    cur_index_2 = 0
    for line1 in lines_file1:
        index += 1
        # if index == 67:
        #     print("")
        words_file1 = line1.strip().split()
        mapped_line = []
        # Accumulate words from File 2 to match the number of words in File 1
        while words_file1:
            if j < len(lines_file2):
                # print(index)
                # print(words_file1)
                
                words_file2 = lines_file2[j].strip().split()
                words_file2 = words_file2[cur_index_2:]
                len_words_file2 = len(words_file2)

                if len_words_file2 <= len(words_file1):
                    mapped_line.extend(words_file2)
                    words_file1 = words_file1[len(words_file2):]
                    cur_index_2 = 0
                    j += 1
                else:
                    mapped_line.extend(words_file2[:len(words_file1)])
                    words_file2 = words_file2[len(words_file1):]
                    cur_index_2 += len(words_file1)
                    words_file1 = []
            # print(index)
            # print(words_file1)
            if index == len(lines_file1)-1 and len(words_file1) < 10:
                break

        # Append the mapped line to the result
        mapped_lines.append(' '.join(mapped_line))

    # Join the mapped lines and write to a new file
    with open(f'output-map-folder/{index_name}.txt', 'w') as mapped_file:
        mapped_file.write('\n'.join(mapped_lines))

    print("Mapped content written to 'mapped_file.txt'.")




# Function to preprocess and compare two files line by line based on line length, first word, and last word
def compare_files(file1, file2):
    def preprocess_line(line):
        # Convert to lowercase and remove specified characters
        line = line.lower()
        line = line.replace(".", "")
        line = line.translate(str.maketrans('', '', '.,?#!'))
        return line.strip()

    prev_line1 = ""
    prev_line2 = ""
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line_number, (line1, line2) in enumerate(zip(f1, f2), start=1):
            # Preprocess both lines before comparison
            line1_processed = preprocess_line(line1)
            line2_processed = preprocess_line(line2)
            
            # Remove leading/trailing whitespace and split lines into words
            words1 = line1_processed.split()
            words2 = line2_processed.split()

            # Compare the number of words, first word, and last word
            if words1[0] != words2[0] and words1[-1] != words2[-1]:
                print(f"First difference found at previous line {line_number-1}:")
                print(f"Previous File 1: {prev_line1.strip()}")
                print(f"Previous File 2: {prev_line2.strip()}")
                print()
                print(f"First difference found at line {line_number}:")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")
                break
            prev_line1 = line1
            prev_line2 = line2
        else:
            print("Files are identical")


# index = 1


# merge(index)

# file1_path = f'predict/{index}.txt'
# file2_path = f'output-map-folder/{index}.txt'

# # Call the compare_files function
# compare_files(file1_path, file2_path)

for i in range(1, 68):
    index = i
    print("Handle file with index", index)
    # Specify the paths to the two files you want to compare
    file1_path = f'predict/{index}.txt'
    file2_path = f'output-map-folder/{index}.txt'

    # Call the compare_files function
    compare_files(file1_path, file2_path)
