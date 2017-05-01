# s2p
convert text to png image

```
usage: s2p.py [-h] [-o OUTPUT] [-d] [-v] input

Convert string to png image, for lovely Cisy. <revol.cai@gmail.com>

positional arguments:
  input          input file's filename, '-' means read from stdin

optional arguments:
  -h, --help     show this help message and exit
  -o OUTPUT      output filename (default: stdout), '-' means output to stdout
  -d             convert png to string
  -v, --version  show program's version number and exit
```

# Quick Start

```sh
# encode
echo aaa|./s2p.py - >/tmp/a.png

# decode

cat /tmp/a.png|./s2p.py -d -
aaa
        %
```

# TODO

- [ ] Smarter padding
- [ ] Support Unicode
- [ ] Inject into other img
