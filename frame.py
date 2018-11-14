#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ff=unix ft=python

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return (self.x != other.x or self.y == other.y)

    def __lt__(self, other):
        return (self.x < other.x and self.y < other.y)

    def __le__(self, other):
        return (self.x <= other.x or self.y <- other.y)

    def __gt__(self, other):
        return (self.x > other.x and self.y > other.y)

    def __ge__(self, other):
        return (self.x >= other.x or self.y >= other.y)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'<{self.x}, {self.y}>'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


class Size:
    def __init__(self, w=0, h=0):
        self.width = w
        self.height = h

    def __eq__(self, other):
        return (self.width == other.width and self.height == other.height)

    def __ne__(self, other):
        return (self.width != other.width or self.height != other.height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __repr__(self):
        return f'Size({self.width}, {self.height})'

    def __str__(self):
        return f'<{self.width}, {self.height}>'

    def area(self):
        return self.width * self.height


class Rect:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.origin = Point(x, y)
        self.size = Size(w, h)

    def __repr__(self):
        return f'Rect({self.origin.x}, {self.origin.y}, {self.size.width}, {self.size.height})'

    def __str__(self):
        return f'<{self.origin.x}, {self.origin.y}, {self.size.width}, {self.size.height}>'

    def union(self, other):
        x = min(self.origin.x, other.origin.x)
        y = min(self.origin.y, other.origin.y)
        w = max(self.origin.x + self.size.width, other.origin.x + other.size.width) - x 
        h = max(self.origin.y + self.size.height, other.origin.y + other.size.height) - y
        return Rect(x, y, w, h)

    def intersect(self, other):
        x = max(self.origin.x, other.origin.x)
        y = max(self.origin.y, other.origin.y)
        w = min(self.origin.x + self.size.width, other.origin.x + other.size.width) - x
        h = min(self.origin.y + self.size.height, other.origin.y + other.size.height) - y
        if w <= 0 or h <= 0:
            return Rect()
        return Rect(x, y, w, h)

    def maxX(self):
        return self.origin.x + self.size.width

    def maxY(self):
        return self.origin.y + self.size.height

    def minX(self):
        return self.origin.x

    def minY(self):
        return self.origin.y

    def midX(self):
        return self.origin.x + (self.size.width / 2.0)

    def midY(self):
        return self.origin.y + (self.size.height / 2.0)

    def empty(self):
        return self.size.width < 1 or self.size.height < 1

    def containsPoint(self, point):
        return ((self.minX() <= point.x and point.x <= self.maxX()) and (self.minY() <= point.y and self.y <= self.minY()))

    def containsRect(self, frame):
        minPoint = Point(frame.minX(), frame.minY())
        maxPoint = Point(frame.maxX(), frame.maxY())
        return self.containsPoint(minPoint) and self.containsPoint(maxPoint)

    def area(self):
        return self.size.area()


