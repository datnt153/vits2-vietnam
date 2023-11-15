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
- if download from youtube:  yt-dlp -x --audio-format wav --batch-file youtube_links.txt
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

* remember cover audio to mono: python check_type_audio.py

## Trainning in vits


```bash 
git clone https://github.com/p0p4k/vits2_pytorch.git 

cd vit2_pytorch

cd monotonic_align

python setup.py build_ext --inplace

cd ..
```

- add line "_letters  = '0123456789aáảàãạâấẩầẫậăắẳằẵặbcdđeéẻèẽẹêếểềễệfghiíỉìĩịjklmnoóỏòõọôốổồỗộơớởờỡợpqrstuúủùũụưứửừữựvwxyýỷỳỹỵz'" in text/symbols.py 

- add line "logging.getLogger('numba').setLevel(logging.WARNING)" in utils.py (ignore warning numba)
- copy file vits2_blv_AQ.json into config 

```bash
python preprocess.py --text_index 1 --filelists filelists/infore_audio_text_train_filelist.txt filelists/infore_audio_text_val_filelist.txt filelists/infore_audio_text_test_filelist.txt --text_cleaners basic_cleaners

python train.py -c config/vits2_blv_AQ -m blv_AQ
```

# Credits

- [ViSV2TTS](https://github.com/v-nhandt21/ViSV2TTS)
- [faster_whisper](https://github.com/guillaumekln/faster-whisper)
