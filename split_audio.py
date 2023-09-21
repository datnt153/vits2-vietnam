import os
import librosa  # Optional. Use any library you like to read audio files.
import soundfile  # Optional. Use any library you like to write audio files.

from slicer2 import Slicer

def split_file(filename='HN-Ngoc_Lan/24.wav', output_path=""):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    audio, sr = librosa.load(filename, mono=False)  # Load an audio file with librosa.
    slicer = Slicer(
        sr=sr,
        threshold=-40,
        min_length=5000,
        min_interval=300,
        hop_size=10,
        max_sil_kept=500
    )
    chunks = slicer.slice(audio)
    for i, chunk in enumerate(chunks):
        if len(chunk.shape) > 1:
            chunk = chunk.T  # Swap axes if the audio is stereo.
        soundfile.write(f'{output_path}/example_{i}.mp3', chunk, sr)  # Save sliced audio files with soundfile.
    

number_file = len(os.listdir("HN-Ngoc_Lan"))
print(f"number file: {number_file}")


for i in range(57, 58):
    print(f"Handle file with index: {i}")
    filename = f"HN-Ngoc_Lan/{i}.wav"
    split_file(filename=filename, output_path=f"split_Ngoc_Lan/{i}")
