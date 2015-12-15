#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Jack'

from collections import namedtuple

nt = namedtuple('NT', 'a b')
aNt = nt('c', 'd')
print(aNt)

print(aNt.a)
print(aNt.b)