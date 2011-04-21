#! /usr/bin/python

# parse the android location service cache file
# (c) 2011 magnus eriksson aka packetlss
# 
# cache.cell + cache.wifi files located in /data/data/com.google.android.location/files on android device 
# 
# file format
#
# header
# unsigned short      db version, should be 1
# unsigned short      number of records
#
# x bytes             UTF string (key)
# int                 accuracy
# int                 confidence
# double              latitude
# double              longitude
# long                reading time

# key format
# cell: mcc + ":" + mnc + ":" + lac + ":" + cid
# wifi: mac address of AP

import sys, struct
from datetime import datetime

gpx = False
if sys.argv[1] == '--gpx':
    gpx = True
    sys.argv = sys.argv[1:]

fh = open(sys.argv[1], 'rb')

db_version, db_total = struct.unpack('>hh', fh.read(4))

if gpx:
    print '<gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" creator="android-locdump">'
    print '<metadata><name>Android Location Cache</name>'
    print '<desc>db version: %d; total: %d</desc></metadata>' % (db_version, db_total)
    print '<trk><trkseg>'
else:
    print "db version:  %d" % db_version
    print "total:       %d" % db_total
    print 
    print '%25s %6s %6s %11s %11s %5s' % ('key','accuracy','conf.','latitude','longitude','time')

i = 0
while i < db_total:
    key = fh.read(struct.unpack('>h', fh.read(2))[0])
    (accuracy, confidence, latitude, longitude, readtime) = struct.unpack('>iiddQ', fh.read(32))
    
    #print key,accuracy,confidence,latitude,longitude,time.strftime("%x %X %z", time.localtime(readtime/1000))
    if gpx:
        if accuracy >= 0:
            print '<trkpt lat="%f" lon="%f"><time>%sZ</time><name>%s</name><desc>accuracy: %d, confidence: %d</desc></trkpt>' % (latitude, longitude, datetime.utcfromtimestamp(readtime/1000.0).isoformat(), key, accuracy, confidence)
    else:
        print '%25s  %7d  %5d  %10f  %10f  %s' % (key,accuracy,confidence,latitude,longitude,time.strftime("%x %X %z", time.localtime(readtime/1000)))
    i=i+1

fh.close()

if gpx:
    print '</trkseg></trk></gpx>'
