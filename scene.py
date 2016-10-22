#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""scene.py"""

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
