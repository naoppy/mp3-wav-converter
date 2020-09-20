import argparse
import glob
import os

import ffmpeg

parser = argparse.ArgumentParser(description='指定したフォルダから再帰的にたどり、wavファイルをmp3ファイルに変換する')
parser.add_argument(
    'src',
    metavar='path_to_src',
    type=str,
    help='content root folder, both relative path and absolute path are OK.',
)

parser.add_argument(
    '-d',
    default=None,
    nargs='?',
    metavar='path_to_out',
    type=str,
    help='output folder, both relative path and absolute path are OK.',
)


# 参考：https://qiita.com/suzutsuki0220/items/43c87488b4684d3d15f6
# ffmpeg -i "input.wav" -vn -ac 2 -ar 44100 -ab 256k -acodec libmp3lame -f mp3 "output.mp3"
def convert(src, dst):
    ilist = glob.glob(src + '/**/*.wav', recursive=True)
    for filename in ilist:
        filename = os.path.abspath(filename)
        relative = os.path.relpath(filename, src)
        outpath = os.path.splitext(os.path.join(dst, relative))[0] + '.mp3'
        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        # print(filename)
        # print(relative)
        # print(outpath)
        input = ffmpeg.input(filename)
        out = ffmpeg.output(input, outpath,
                            # ac='2',
                            # ar='44100',
                            audio_bitrate='128k',
                            acodec='libmp3lame',
                            f='mp3')
        ffmpeg.run(out)


if __name__ == '__main__':
    args = parser.parse_args()
    src = args.src
    dst = args.d

    if not os.path.exists(src):
        print("broken src path")
        exit(1)

    if dst is not None:
        if not os.path.exists(dst):
            print("broken dst path")
            exit(1)
    else:
        dst = os.getcwd()

    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    print('src dir :' + src)
    print('dst dir :' + dst)
    convert(src, dst)
