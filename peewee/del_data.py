#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import Artist

band = Artist.get(Artist.name == "MXPX")
band.delete_instance()