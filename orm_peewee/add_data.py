#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Album, Artist

new_artist = Artist.create(name="Newsboys")
album_one = Album(artist=new_artist,
                  title="Read All About It",
                  publisher="Refuge",
                  media_type="CD")
album_one.save()

albums = [{"artist": new_artist,
           "title": "Hell is for Wimps",
           "publisher": "Sparrow",
           "media_type": "CD"
           },
          {"artist": new_artist,
           "title": "Love Liberty Disco",
           "publisher": "Sparrow",
           "media_type": "CD"
           },
          {"artist": new_artist,
           "title": "Thrive",
           "publisher": "Sparrow",
           "media_type": "CD"}
          ]
'''
for album in albums:
    a = Album(**album)
    a.save()
'''

Album.insert_many(albums).execute()

bands = ["MXPX", "Kutless", "Thousand Foot Krutch"]
for band in bands:
    artist = Artist.create(name=band)
    artist.save()