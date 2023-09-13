# Read the content from File 1 and File 2
with open('file1.txt', 'r') as file1:
    content_file1 = file1.read()

with open('file2.txt', 'r') as file2:
    content_file2 = file2.read()

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
    if index == 67:
        print("")
    words_file1 = line1.strip().split()
    mapped_line = []
    # Accumulate words from File 2 to match the number of words in File 1
    while words_file1:
        if j < len(lines_file2):
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

    # Append the mapped line to the result
    mapped_lines.append(' '.join(mapped_line))

# Join the mapped lines and write to a new file
with open('mapped_file.txt', 'w') as mapped_file:
    mapped_file.write('\n'.join(mapped_lines))

print("Mapped content written to 'mapped_file.txt'.")
