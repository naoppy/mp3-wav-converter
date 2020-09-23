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
```python3
python3 main.py "D:/CD" -d "D:/MP3CD"
```

# TODO
It now support only sjis-metadata to utf-8 metadata, so it will suppport other encode-specify options in future version.
