import os 
def create_label(index):
    with open(f'output-map-folder/{index}.txt', 'r') as file1:
        text = file1.read()

    lines = text.split('\n')

    with open(f"label.txt", "a") as f:

        for i, line in enumerate(lines):
            audio_path = f"split_Ngoc_Lan/{index}/example_{i}.mp3"
            if os.path.isfile(audio_path):
                f.write(f"{audio_path}|{line}\n")

 
for i in range(1, 68):
     create_label(i)
