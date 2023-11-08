import os
import librosa  # Optional. Use any library you like to read audio files.
import soundfile  # Optional. Use any library you like to write audio files.

from slicer2 import Slicer

def split_file(filename='', output_path=""):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    audio, sr = librosa.load(filename, mono=False)  # Load an audio file with librosa.
    slicer = Slicer(
        sr=sr,
        threshold=-40,
        min_length=5000,
        max_length=20000,
        min_interval=300,
        hop_size=10,
        max_sil_kept=500
    )
    chunks = slicer.slice(audio)
    for i, chunk in enumerate(chunks):
        if len(chunk.shape) > 1:
            chunk = chunk.T  # Swap axes if the audio is stereo.
        soundfile.write(f'{output_path}/split_{i}.wav', chunk, sr)  # Save sliced audio files with soundfile.
    

folder_name = "blv AQ"
number_file = len(os.listdir(folder_name))
print(f"number file: {number_file}")

number_file = 1
for i in range(number_file):
    print(f"Handle file with index: {i}")
    filename = f"{folder_name}/{i}.wav"
    split_file(filename=filename, output_path=f"split_{folder_name}/{i}")
