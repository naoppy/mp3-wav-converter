import argparse
import glob
import os
import subprocess

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
    help='output folder, both relative path and absolute path are OK.'
         ' default is current directory.',
)

parser.add_argument(
    '--encoding',
    default='UTF-8',
    metavar='encoding',
    type=str,
    help='encoding name of metadata. just type `iconv -l` to see available name list.'
         ' default is UTF-8.'
)


# 参考：https://qiita.com/suzutsuki0220/items/43c87488b4684d3d15f6
# https://trac.ffmpeg.org/ticket/8510
#
# ffmpeg -i "input.wav" -vn -ac 2 -ar 44100 -ab 256k -acodec libmp3lame -f mp3 "output.mp3"
# ffmpeg -i `input.wav` -f ffmetadata - | iconv -f `encoding` -t utf8 | ffmpeg -i `input.wav` -i - -map_metadata 1 -b:a 256k -c:a libmp3lame sample.mp3
def convert(src, dst, encoding):
    ilist = glob.glob(src + '/**/*.wav', recursive=True)
    for filename in ilist:
        filename = os.path.abspath(filename)
        relative = os.path.relpath(filename, src)
        outpath = os.path.splitext(os.path.join(dst, relative))[0] + '.mp3'
        # print(filename)
        # print(relative)
        # print(outpath)

        os.makedirs(os.path.dirname(outpath), exist_ok=True)
        command = f'ffmpeg -i "{filename}" -f ffmetadata - | iconv -f {encoding} -t UTF-8 | ffmpeg -i "{filename}" -i - ' \
                  f'-map_metadata 1 -b:a 256k -c:a libmp3lame "{outpath}"'
        # print(command + '\n')
        subprocess.call(command, shell=True)


if __name__ == '__main__':
    args = parser.parse_args()
    src = args.src
    dst = args.d
    encoding = args.encoding

    if not os.path.exists(src):
        print("broken src path")
        exit(1)

    if dst is None:
        dst = os.getcwd()

    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    print('src dir :' + src)
    print('dst dir :' + dst)
    convert(src, dst, encoding)
