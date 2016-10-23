#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""utils.py"""

"""
This file is part of The Last Caturai.

    The Last Caturai is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The Last Caturai is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

"""Set of functions that will be needed more than one time."""

import base64
import zlib

# Function that obtains a decoded and decompressed chain of characters on base64
def decode(codedChar):
    # Decoding from base64
    decodedChar = base64.b64decode(codedChar)

    # Descompressing from zLib.
    finalChar = zlib.decompress(decodedChar)

    output = []
    for idx in range(0, len(finalChar), 4):
        val = ord(chr(finalChar[idx])) | (ord(chr(finalChar[idx + 1])) << 8) | \
        (ord(chr(finalChar[idx + 2])) << 16) | (ord(chr(finalChar[idx + 3])) << 24)
        output.append(val)

    return output
