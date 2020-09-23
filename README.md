# mp3-wav-converter
convert wav to mp3 by the way of keeping metadata

Convert the wav files in the specified folder recursively.
Metadata is stored without corruption by changing the encoding to UTF-8.

# Requirements
- python3
- ffmpeg
- iconv

these are available in both windows and linux.

# Example
show help
```bash
python3 main.py -h
```
convert files, which metadata is encoded as sjis
```bash
python3 main.py "D:/CD" -d "D:/MP3CD" --encoding sjis
```

# TODO
現在、SJISのダメ文字はその文字の後ろに円記号がついた文字に変換されるというバグがある。ダメ文字を含むSJISを上手く処理する必要がある。