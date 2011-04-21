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

import sys, struct, time

fh = open(sys.argv[1], 'rb')

db_version, db_total = struct.unpack('>hh', fh.read(4))

print "db version:  %d" % db_version
print "total:       %d" % db_total
print 
print '{0:22s}  {1:6s}  {2:6s}  {3:10s}  {4:9s}  {5:s}'.format('key','accuracy','conf.','latitude','longitude','time')

i = 0
while i < db_total:
    key = fh.read(struct.unpack('>h', fh.read(2))[0])
    (accuracy, confidence, latitude, longitude, readtime) = struct.unpack('>iiddQ', fh.read(32))
    
    #print key,accuracy,confidence,latitude,longitude,time.strftime("%x %X %z", time.localtime(readtime/1000))
    print '{0:25s}  {1:5d}  {2:5d}  {3:10f}  {4:10f}  {5:s}'.format(key,accuracy,confidence,latitude,longitude,time.strftime("%x %X %z", time.localtime(readtime/1000)))
    i=i+1

fh.close()
