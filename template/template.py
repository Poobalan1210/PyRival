#!/usr/bin/env python
from __future__ import division, print_function

import io
import os
import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

#region py3k
if sys.version_info[0] < 3:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange

#endregion

#region fastio
if sys.version_info[0] < 3:
    from cStringIO import StringIO
else:
    from io import BytesIO as StringIO

input = StringIO(os.read(0, os.fstat(0).st_size)).readline

sys.stdout, stream = io.IOBase(), StringIO()
sys.stdout.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
sys.stdout.write = stream.write if sys.version_info[0] < 3 else lambda s: stream.write(s.encode())

#endregion


def main():
    pass


if __name__ == '__main__':
    main()
