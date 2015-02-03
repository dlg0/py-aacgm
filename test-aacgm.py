import aacgm

year=2011
month=10
day=3
hour=5
minute=2
second=0

lat_geo = 80
lon_geo = 170
height = 100 # km above the Earth surface
flag = 0 # 0: GEO -> AACGM , 1: AACGM -> GEO
order = 10

print ''
print 'Set date and time'
ret = aacgm.SetDateTime(year, month, day, hour, minute, second)
if ret==0 :
	print 'SUCCESS'
else:
	print 'FAIL'

print ''
print 'Get date and time'
ret = aacgm.GetDateTime()
print 'AACGM Time (status, year, month, day, hr, mn, sc, doy): ', ret

print ''
print 'dayno'
ret = aacgm.dayno_py(year,month,day)
print 'dayno output (doy, diy): ', ret
if (ret[0]>0) or (ret[0]<365):
	print 'SUCCESS'
else:
	print 'FAIL'

print ''
print 'Convert GEO to AACGM with convert_geo_coord'
print 'GEO (Lat,Lon): ', lat_geo,lon_geo
ret = aacgm.convert_geo_coord_py(lat_geo, lon_geo, height, flag, order)
print 'AACGM Output (status,lat,lon) ', ret
if ret[0]==0:
	print 'SUCCESS'
else:
	print 'FAIL'


print ''
print 'Convert GEO to AACGM with AACGM_v2_Convert'
print 'GEO (Lat,Lon): ', lat_geo,lon_geo
ret = aacgm.Convert(lat_geo, lon_geo, height, flag)
lat_aacgm = ret[1]
print 'AACGM Output (status,lat,lon,r) ', ret
if ret[0]==0:
	print 'SUCCESS'
else:
	print 'FAIL'


print ''
print 'Testing CGM2Alt'
ret = aacgm.CGM2Alt(height, lat_aacgm)
print 'CGM2Alt output (status, lat_adj): ',  ret
if ret[0]==0:
	print 'SUCCESS'
else:
	print 'FAIL'


print ''
print 'Testing Alt2CGM'
aacgm.Alt2CGM(height, lat_aacgm)
print 'Alt2CGM output (lat_adj): ',  ret


print ''
print 'Test LoadCoefs'
load_year = 1980
print 'Load year: ', load_year
ret = aacgm.LoadCoefs(load_year)
if ret==0:
	print 'SUCCESS'
else:
	print 'FAIL'


print ''
print 'Test LoadCoef'
load_file = 'coeffs/aacgm_coeffs-11-2010.asc' 
print 'Load file: ', load_file
code = 0; # 0 -> first set, 1 -> second set
ret = aacgm.LoadCoef(load_file,code)
if ret==0:
	print 'SUCCESS'
else:
	print 'FAIL'



print ''
print 'Set date and time to NOW using AACGM_v2_SetNow()'
ret = aacgm.SetNow()
if ret==0:
	print 'SUCCESS'
else:
	print 'FAIL'


print ''
print 'Get date and time'
ret = aacgm.GetDateTime()
print 'AACGM Time (status, year, month, day, hr, mn, sc, doy): ', ret
if ret[0]==0:
	print 'SUCCESS'
else:
	print 'FAIL'



