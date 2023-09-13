from faster_whisper import WhisperModel
import os

model_size = "large-v2"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("audio1.mp3", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
#     with open(f"transcription.txt", "a", encoding="utf-8") as txt:
#         txt.write(f"{segment.text}\n")
#     # for word in segment.words:
#     #     print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))


for i in range(len(os.listdir("test"))):
    segments, info = model.transcribe(f"test/example_{i}.mp3", beam_size=5)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        with open(f"sub/transcription_{i}.txt", "a", encoding="utf-8") as txt:
            txt.write("[%.2fs -> %.2fs] %s \n" % (segment.start, segment.end, segment.text))
        # for word in segment.words:
        #     print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))
