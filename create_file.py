from pathlib import Path 

txt_files = sorted(Path("./infore").glob("*.txt"))

# write all word 
f = open("data.txt", "w", encoding="utf-8")
for txt_file in txt_files:
    wav_file = txt_file.with_suffix(".wav")
    if not wav_file.exists():
        continue
    line = open(txt_file, "r", encoding="utf-8").read()
    f.write(f"{wav_file}|{line}\n")
    # for word in line.strip().lower().split():
    #     f.write(word)
    #     f.write("\n")
f.close()



def write_file(filename, data):
    f = open(filename, "w", encoding="utf-8")
    for line in data:
        f.write(f"{line}\n")
    f.close()

data = open("data.txt", "r", encoding="utf-8").read().strip().split("\n")
train_data = data[:-600]
val_data = data[-600:-500]
test_data = data[-500:]

print(len(train_data))
print(len(val_data))
print(len(test_data))

write_file("infore_audio_text_train_filelist.txt", train_data)
write_file("infore_audio_text_val_filelist.txt", val_data)
write_file("infore_audio_text_test_filelist.txt", test_data)