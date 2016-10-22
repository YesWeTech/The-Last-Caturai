#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""scene.py"""

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

"""Class Scene, from which the scene objects will inherit."""

class Scene:

    def __init__(self, director):
        self.director = director

    # Event methods on_update, on_event, and on_draw
    def on_update(self):
        raise NotImplemented("on_update method not implemented.")

    def on_event(self, event):
        raise NotImplemented("on_event method not implemented.")

    def on_draw(self, screen):
        raise NotImplemented("on_draw method not implemented.")

    def on_resize(self, screen, event):
        raise NotImplemented("on_resize method not implemented.")
