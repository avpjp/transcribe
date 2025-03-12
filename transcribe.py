import mlx_whisper
import sys

# コマンドライン引数からファイル名を取得（指定がなければデフォルト値を使用）
audio_file = sys.argv[1] if len(sys.argv) > 1 else "output_audio.mp3"

# 完全な結果オブジェクトを取得（["text"]で取り出さない）
result = mlx_whisper.transcribe(
    audio_file,
    path_or_hf_repo="mlx-community/whisper-large-v3-mlx",
    word_timestamps=True,
    language="ja",
)

# 発話セグメントごとにタイムスタンプと一緒に表示
for segment in result["segments"]:
    start_time = segment["start"]
    end_time = segment["end"]
    text = segment["text"]
    
    print(f"[{start_time:.2f}s - {end_time:.2f}s] {text}")