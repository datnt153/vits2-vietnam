**vits2-vietnam**

Follow like this:

# Install environment

```bash
conda create -y -n whisper python=3.8
conda activate whisper
conda install cudatoolkit=11.3.1 cudnn=8.2.1
pip install -r requirements.txt
```

# Process data

## Prepare dataset

- python Step0_merge_input.py (create each file <= 50k character )
- Upload text to vbee.vn => download
- python Step1_split_audio.py
- python Step2_transcription_whisper.py
- python Step2_transcription_wav2vec.py
- python Step3_map_file.py

## Create label

- map predict with ground truth => file map

- check file map with predict

- If use from raw audio from youtube use postprocess.ipynb and download in folder crawl youtube

- pyton Step4_create_label.py

## Trainning in vits

```python
python preprocess.py --text_index 1 --filelists filelists/infore_audio_text_train_filelist.txt filelists/infore_audio_text_val_filelist.txt filelists/infore_audio_text_test_filelist.txt --text_cleaners basic_cleaners
```

# Credits

- [ViSV2TTS](https://github.com/v-nhandt21/ViSV2TTS)
- [faster_whisper](https://github.com/guillaumekln/faster-whisper)
