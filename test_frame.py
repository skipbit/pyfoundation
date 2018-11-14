#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ff=unix ft=python
from frame import *

def test_point_equals():
    a = Point(10, 10)
    b = Point(10, 10)
    assert a == b

def test_point_not_equals():
    a = Point(10, 10)
    b = Point(11, 10)
    assert a != b

def test_point_less_than():
    a = Point(10, 10)
    b = Point(20, 20)
    assert a < b

def test_point_less_than_or_eauals():
    a = Point(10, 10)
    b = Point(20, 10)
    assert a <= b

def test_frame_union():
    a = Rect(0, 0, 100, 100)
    b = Rect(50, 50, 100, 100)
    c = a.union(b)
    assert (c.origin.x, c.origin.y, c.size.width, c.size.height) == (0, 0, 150, 150)

def test_equal_frame_union():
    a = Rect(50, 50, 100, 100)
    b = Rect(50, 50, 100, 100)
    c = a.union(b)
    assert (c.origin.x, c.origin.y, c.size.width, c.size.height) == (50, 50, 100, 100)

def test_non_overlap_frame_union():
    a = Rect(0, 0, 100, 100)
    b = Rect(100, 0, 100, 100)
    c = a.union(b)
    assert (c.origin.x, c.origin.y, c.size.width, c.size.height) == (0, 0, 200, 100)

def test_frame_intersect():
    a = Rect(0, 0, 100, 100)
    b = Rect(50, 50, 100, 100)
    c = a.intersect(b)
    assert (c.origin.x, c.origin.y, c.size.width, c.size.height) == (50, 50, 50, 50)

def test_equal_frame_intersect():
    a = Rect(50, 50, 100, 100)
    b = Rect(50, 50, 100, 100)
    c = a.intersect(b)
    assert (c.origin.x, c.origin.y, c.size.width, c.size.height) == (50, 50, 100, 100)

def test_non_overlap_frame_intersect():
    a = Rect(0, 0, 100, 100)
    b = Rect(100, 0, 100, 100)
    c = a.intersect(b)
    assert (c.origin.x, c.origin.y, c.size.width, c.size.height) == (0, 0, 0, 0)

