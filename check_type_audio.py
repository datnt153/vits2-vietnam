from pydub import AudioSegment
import os

# Specify the parent directory containing folders 0 to 13
parent_directory = './'

# Iterate through folders from 0 to 13
for folder_number in range(14):  # 0 to 13
    folder_path = os.path.join(parent_directory, str(folder_number))

    if not os.path.exists(folder_path):
        print(f"Folder {folder_number} does not exist.")
        continue

    # Iterate through audio files in the current folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp3') or filename.endswith('.wav'):
            file_path = os.path.join(folder_path, filename)
            audio = AudioSegment.from_file(file_path)

            # Check if the audio is stereo (2 channels)
            if audio.channels == 2:
                print(f"Converting {filename} in folder {folder_number} to mono...")
                # Convert stereo audio to mono
                audio = audio.set_channels(1)
                # Save the mono audio back to the same file
                audio.export(file_path, format="wav")
                print(f"{filename} in folder {folder_number} has been converted to mono.")
            else:
                print(f"{filename} in folder {folder_number} is already mono and will not be converted.")

