#!/usr/bin/env python
# encoding: utf-8
class Widget:
    def __init__(self, size=(40, 40)):
        self._size = size

    def getSize(self):
        return self._size

    def resize(self, width, height):
        if width < 0 or height < 0:
            raise ValueError ("illegal size")
        self._size = (width, height)

    def dispose(self):
        pass