#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Album

datas = Album.select().limit(5)

for data in datas:
    print('title:', data.title, 'publisher:', data.publisher)

    data.media_type = 'DVD'
    data.save()

