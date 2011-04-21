Following the latest days internet outrage/overreaction to the
revelation that iPhone has a cache for its location service, I decided
to have look what my Android devices caches for the same function.

This is a quick dumper I threw together to parse the files from the
Android location provider.

The files are named cache.cell & cache.wifi and is located in
`/data/data/com.google.android.location/files` on the Android device.

You will need root access to the device to read this directory.

Usage:

```console
parse.py <cache file>
```

Important note: looking at old android source (this code is no longer
open from Google it seems) it seems to be limited heavily.

However, data is only pruned when new info is added. There is no time
based pruning unless there is new data being added to the cache. This
could lead to old data being if there is limited movement of the
device.

```java
    // Maximum time (in millis) that a record is valid for, before it needs
    // to be refreshed from the server.
    private static final long MAX_CELL_REFRESH_RECORD_AGE = 12 * 60 * 60 * 1000; // 12 hours
    private static final long MAX_WIFI_REFRESH_RECORD_AGE = 48 * 60 * 60 * 1000; // 48 hours

    // Cache sizes
    private static final int MAX_CELL_RECORDS = 50;
    private static final int MAX_WIFI_RECORDS = 200;
```


Example output:

```console
$ ./parse.py cache.wifi 
db version:  1
total:       47

key                     accuracy  conf.   latitude    longitude  time
50:63:13:57:42:7e             80     92   57.689354   11.994763  04/11/11 10:03:51 +0200
e0:cb:4e:7e:cc:53             75     92   57.689340   11.994495  04/11/11 10:03:51 +0200
4c:54:99:14:47:68             57     92   57.708979   11.916581  04/11/11 01:14:53 +0200
00:26:18:0a:ad:cb             60     92   57.709699   11.917637  04/13/11 08:40:36 +0200
00:22:15:28:3f:7a             60     92   57.699467   11.979340  04/13/11 11:52:16 +0200
00:22:3f:a7:d9:fd             65     92   57.699442   11.979343  04/13/11 11:52:16 +0200


$ ./parse.py cache.cell 
db version:  1
total:       41

key                     accuracy  conf.   latitude    longitude  time
240:5:15:983885             1186     75   57.704031   11.910801  04/11/11 20:03:14 +0200
240:5:15:983882              883     75   57.706322   11.911692  04/13/11 01:41:29 +0200
240:5:75:4915956             678     75   57.700175   11.976824  04/13/11 11:52:16 +0200
240:5:75:4915953             678     75   57.700064   11.976629  04/13/11 11:53:09 +0200
240:7:61954:58929           1406     75   57.710205   11.921849  04/15/11 19:46:31 +0200
240:7:15:58929                -1      0    0.000000    0.000000  04/15/11 19:46:32 +0200
240:5:75:4915832             831     75   57.690024   11.998419  04/15/11 16:13:53 +0200
```

If you have any questions/info that you'd like to share, I can be
reached via @packetlss on Twitter or packetlss+android@gmail.com


  
