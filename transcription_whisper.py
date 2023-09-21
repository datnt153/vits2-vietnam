from faster_whisper import WhisperModel
import os

model_size = "large-v2"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

# segments, info = model.transcribe("audio1.mp3", beam_size=5)

# print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
#     with open(f"transcription.txt", "a", encoding="utf-8") as txt:
#         txt.write(f"{segment.text}\n")
#     # for word in segment.words:
#     #     print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))

def transciption(folder_name, output_path, index):
    if not os.path.exists(f"{output_path}/{index}"):
        os.makedirs(f"{output_path}/{index}")
    
    f = open(f"predict/{index}.txt", "a", encoding="utf-8")
    for i in range(len(os.listdir(folder_name))):
        segments, info = model.transcribe(f"{folder_name}/example_{i}.mp3", beam_size=5, without_timestamps=True )

        # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

        for segment in segments:
            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
            with open(f"{output_path}/{index}/trans_{i}.txt", "a", encoding="utf-8") as txt:
                txt.write(f" {segment.text} \n" )
            f.write(f" {segment.text} \n" )
            # for word in segment.words:
            #     print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))
    f.close()


number_file = len(os.listdir("HN-Ngoc_Lan"))
print(f"number file: {number_file}")

for i in range(57, 58):
    print(f"In handle file with index: {i}")
    transciption(folder_name=f"split_Ngoc_Lan/{i}", output_path="sub_Ngoc_Lan", index=i)
