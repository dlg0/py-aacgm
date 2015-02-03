# py-aacgm
AACGM V2 Library in Python

First step is to build the libaacgmlib_v2.so from the aacgmlib_v2 files, i.e., 
```
gcc -c -o libaacgmlib_v2.so aacgmlib_v2.c
```
Then build the python extension ...

```
./clean
./make
```

See test-aacgm.py for example usage, running it gives the following output ...

```
dlg-air:py-aacgm dg6$ python test-aacgm.py 

Set date and time
SUCCESS

Get date and time
AACGM Time (status, year, month, day, hr, mn, sc, doy):  (0, 2011, 10, 3, 5, 2, 0, 276)

dayno
dayno output (doy, diy):  (276, 365)
SUCCESS

Convert GEO to AACGM with convert_geo_coord
GEO (Lat,Lon):  80 170
AACGM Output (status,lat,lon)  (0, 76.06491401789191, -141.177224200949)
SUCCESS

Convert GEO to AACGM with AACGM_v2_Convert
GEO (Lat,Lon):  80 170
AACGM Output (status,lat,lon,r)  (0, 76.06491401789191, -141.177224200949, 1.0)
SUCCESS

Testing CGM2Alt
CGM2Alt output (status, lat_adj):  (0, 75.95375301316209)
SUCCESS

Testing Alt2CGM
Alt2CGM output (lat_adj):  (0, 75.95375301316209)

Test LoadCoefs
Load year:  1980
SUCCESS

Test LoadCoef
Load file:  coeffs/aacgm_coeffs-11-2010.asc
SUCCESS

Set date and time to NOW using AACGM_v2_SetNow()

AACGM-v2: No date/time specified, using current time: 20150203 1057:27

SUCCESS

Get date and time
AACGM Time (status, year, month, day, hr, mn, sc, doy):  (0, 2015, 2, 3, 10, 57, 27, 34)
SUCCESS
```
