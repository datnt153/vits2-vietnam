import os 
from vinorm import TTSnorm
import re 
from num2words import num2words




def vi_num2words(num):
    # print(num)
    return num2words(num, lang='vi')


def replace_number(text):
   return re.sub('(?P<id>\d+)', lambda m: vi_num2words(int(m.group('id'))), text)


def merge(index_name):
    # Read the content from File 1 and File 2
    with open(f'predict_{sub}_{folder_name}/{index_name}.txt', 'r') as file1:
        text = file1.read()
                                
        text = text.replace("Dô bết", "dobet")
        text = text.replace("ô lưu", "oliu")
 
        content_file1  = text

    with open(f'output50K_VBSF001/merged_{index_name}.txt', 'r') as file2:
        content_file2 = file2.read() 


        content_file2 = content_file2.replace("mocjian", "moc jian")
        content_file2 = content_file2.replace("xalômông", "xa lo mong")
        content_file2 = content_file2.replace("\"", "")
        content_file2 = content_file2.replace("-", " ")
        content_file2 = content_file2.replace(".", " ")


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
        line1 = replace_number(line1)
        # print(f"line1: {line1}")
        
        words_file1 = line1.strip().split()
        mapped_line = []

        # Accumulate words from File 2 to match the number of words in File 1
        while words_file1:
            if j < len(lines_file2):
                # print(words_file1)
            
                line_file2 = lines_file2[j] 
                    
                if len(line_file2) == 0: 
                    j += 1
                    continue

                line_file2 = line_file2.strip()

                # add . in lastest line to break sentence 
                if line_file2[-1] not in [".", ","]:
                    line_file2 += "."

                words_file2 = line_file2.strip().split()
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
            
            # print(words_file1)
            
            # print(len(lines_file1))
            # print(f"index: {index}")
            if j == len(lines_file2):
                break
            # if index == len(lines_file1)-2 and len(words_file1) < 30:
            #     break

        # Append the mapped line to the result
        mapped_lines.append(' '.join(mapped_line))

    # Join the mapped lines and write to a new file
    with open(f'{output_dir}/{index_name}.txt', 'w') as mapped_file:
        mapped_file.write('\n'.join(mapped_lines))

    print("Mapped content written to 'mapped_file.txt'.")




# Function to preprocess and compare two files line by line based on line length, first word, and last word
def compare_files(file1, file2):
    def preprocess_line(line):
        # Convert to lowercase and remove specified characters
        line = line.lower()
        line = line.replace(".", "")
        line = line.replace(":", "")
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


# index = 15

# print("Handle file with index", index)

# merge(index)
# file1_path = f'predict/{index}.txt'
# file2_path = f'{output_dir}/{index}.txt'

# # Call the compare_files function
# compare_files(file1_path, file2_path)


start = 11
end = start + 1
folder_name = "VBSFOO1 anh khoi"

# sub = "wav2vec"
sub = "whisper"

output_dir = f"map file {folder_name}"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(start, end):
    index = i
    print("Handle file with index", index)
    merge(index)
    # Specify the paths to the two files you want to compare
    file1_path = f'predict_{sub}_{folder_name}/{index}.txt'
    file2_path = f'{output_dir}/{index}.txt'

    # Call the compare_files function
    compare_files(file1_path, file2_path)
    print("-" * 40)
