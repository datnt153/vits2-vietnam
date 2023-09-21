# vits2-vietnam
Follow like this: 
## Prepare dataset 
- conda activate whisper
- python merge_20k.py (create each file <= 20k character )
- Upload text to vbee.vn => download 
- python split_audio.py 
- python transcription_whisper.py 
- python map_file.py

## Trainning 
python preprocess.py --text_index 1 --filelists filelists/infore_audio_text_train_filelist.txt filelists/infore_audio_text_val_filelist.txt filelists/infore_audio_text_test_filelist.txt --text_cleaners basic_cleaners
