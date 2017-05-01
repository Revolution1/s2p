#!/usr/bin/env python
# coding=utf-8
import argparse
import math
import sys

from png import png

__version__ = '0.1.0'


def convert(data, f):
    if len(data) % 3:
        data = data + ' ' * (3 - len(data) % 3)
    w = int(math.sqrt(len(data) / 3))
    if w * w < len(data):
        w = w + 1
        data = data + ' ' * (w * w * 3 - len(data))
    writer = png.Writer(w, w)
    data = [ord(a) for a in data]
    p = [data[n * w * 3:n * w * 3 + w * 3] for n in range(w)]
    writer.write(f, p)


def decode(data, f):
    reader = png.Reader(data)
    p = reader.read()[2]
    s = ''.join(str(i) for i in p)
    f.write(s)
    f.flush()


def main():
    p = argparse.ArgumentParser(description="Convert string to png image, for lovely Cisy. <revol.cai@gmail.com> ")
    p.add_argument('input', metavar='input', type=str,
                   help="input file's filename, '-' means read from stdin")
    p.add_argument('-o', dest='output', default='-',
                   help="output filename (default: stdout), '-' means output to stdout")
    p.add_argument('-d', dest='decode', action='store_true', help="convert png to string")
    p.add_argument('-v', '--version', action='version', version=__version__)

    arg = p.parse_args()
    if arg.decode:
        if arg.input == '-':
            data = sys.stdin
        else:
            data = open(arg.input, 'rb')
        if arg.output == '-':
            decode(data, sys.stdout)
        else:
            with open(arg.output, 'wb') as f:
                decode(data, f)
        if data != sys.stdin:
            data.close()
    else:
        if arg.input == '-':
            data = sys.stdin.read()
        else:
            with open(arg.input, 'rb') as f:
                data = f.read()
        if arg.output == '-':
            convert(data, sys.stdout)
        else:
            with open(arg.output, 'wb') as f:
                convert(data, f)


if __name__ == '__main__':
    main()
