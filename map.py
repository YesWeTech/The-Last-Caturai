#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""map.py"""

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

"""Reads and processes the TMX file, which is an XML."""

from xml.dom import minidom, Node
from utils import *
import config

class Map:

    def __init__(self, name):
        self.name = name
        self.layers = []
        self.load_map()

    def load_map(self):
        xmlMap = minidom.parse("levels/"+self.name)
        mainNode = xmlMap.childNodes[0]

        # Map size
        self.width = int(mainNode.attributes.get("width").value)
        self.height = int(mainNode.attributes.get("height").value)

        # Rest of the file
        for i in range(len(mainNode.childNodes)):
            if mainNode.childNodes[i].nodeType == 1:
                if mainNode.childNodes[i].nodeName == "tileset":
                    if mainNode.childNodes[i].attributes.get("name").value != "config":
                        width = mainNode.childNodes[i].attributes.get("tilewidth").value
                        height = mainNode.childNodes[i].attributes.get("tileheight").value
                        path = mainNode.childNodes[i].childNodes[1].attributes.get("source").value
                        name = obtain_name(path)
                        self.tileset = name
                    self.tile_size = (int(width), int(height))
                if mainNode.childNodes[i].nodeName == "layer":
                    if  mainNode.childNodes[i].attributes.get("name").value != "collisions":
                        layer = mainNode.childNodes[i].childNodes[1].childNodes[0].data.replace("\n", "").replace(" ", "")
                        layer = decode(layer)
                        layer = toArray(layer, self.width)
                        self.layers.append(layer)
                if mainNode.childNodes[i].nodeName == "objectgroup":
                    x = mainNode.childNodes[i].childNodes[1].attributes.get("x").value
                    y = mainNode.childNodes[i].childNodes[1].attributes.get("y").value
                    self.start = (int(x), int(y))

def toArray(list, col):
    newList = []
    for i in range(0, len(list), col):
        newList.append(list[i:i+col])
    return newList

def obtain_name(path):
    a = -1
    for i in range(len(path)):
        if path[i] == "/" or path[i] == "\\":
            a = i
    if a == -1:
        return path
    return path[a+1:]

# ---------------------------------------------------------------------

def main():
    return 0

if __name__ == '__main__':
    main()
