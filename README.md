
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
source avpjp-transcribe-env/bin/activate
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

ChatGPT 4.5

prompt

```
以下のテキストはPodcastの書き起こしです。視聴者がアクセスしやすいように、全体をおよそ10個のチャプターに細かく分割し、YouTubeのチャプター形式（「分:秒 チャプタータイトル」）で整理して書き出してください。特に話題や内容が変わる部分を意識して、視聴者が興味のあるポイントに簡単にアクセスできるようにしてください。
特に後半部分も含めて全体を均等に細かく分割するように意識してください
```

# Environment & Performance

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
