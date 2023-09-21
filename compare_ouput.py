# Function to preprocess and compare two files line by line based on line length, first word, and last word
def compare_files(file1, file2):
    def preprocess_line(line):
        # Convert to lowercase and remove specified characters
        line = line.lower()
        line = line.translate(str.maketrans('', '', '.,?#!'))
        return line.strip()

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
                print(f"First difference found at line {line_number}:\n")
                print(f"File 1: {line1.strip()}")
                print(f"File 2: {line2.strip()}")
                break
        else:
            print("Files are identical")
# Specify the paths to the two files you want to compare
file1_path = 'predict/2.txt'
file2_path = 'output-map-folder/2.txt'

# Call the compare_files function
compare_files(file1_path, file2_path)
