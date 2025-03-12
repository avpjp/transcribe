
# Requirements

Python 3.3+
ffmpeg

```
brew install ffmpeg
```

# Steps

Make environment and install packages.

```
python3 -m venv avpjp-transcribe-env
source bin/activate
pip install -r requirements.txt
```

Run transcribe.py.

```
python3 transcribe.py video.mp4 > output.txt
```

Clean up environment.

```
deactivate
rm -rf avpjp-transcribe-env
```

# Make chapters

prompt

```
This is podcast transcribe. Please make youtube format chapter.
```

![](https://github.com/avpjp/transcribe/blob/main/.github/screenshot.png)

# Environment & Performance

ChatGPT Plus

```
Hardware:
    Hardware Overview:
      Model Name: MacBook Pro
      Model Identifier: MacBookPro18,4
      Model Number: MKH53J/A
      Chip: Apple M1 Max
      Total Number of Cores: 10 (8 performance and 2 efficiency)
      Memory: 64 GB
      System Firmware Version: 11881.81.4
      OS Loader Version: 11881.81.4
```

| Duration | Size | Transcribe Time | Output file size |
| --- | --- | --- | --- |
| 1:02:29 | 2.8GB | 403.14s | 107KB |

# See also

[venv: Python 仮想環境管理](https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e)

[MacBook ProでWhisper large-v3-turboをMLXと共に試してみる](https://note.com/ngc_shj/n/n4b197c67a8d9)
