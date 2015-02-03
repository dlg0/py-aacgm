from libc.stdio cimport FILE
#import numpy as np
#cimport numpy as np

cdef extern from "aacgmlib_v2.h":
	int AACGM_v2_Rylm(double colat, double lon, int order, double *ylmval)
	void AACGM_v2_Alt2CGM(double r_height_in, double r_lat_alt, double *r_lat_adj)
	int AACGM_v2_CGM2Alt(double r_height_in, double r_lat_in, double *r_lat_adj)
	double AACGM_v2_Sgn(double a, double b)
	int convert_geo_coord(double lat_in, double lon_in, double height_in, double *lat_out, double *lon_out, int flag, int order)
	int dayno(int year, int month, int day, int *diy)
	int AACGM_v2_LoadCoefFP(FILE *fp, int code)
	int AACGM_v2_LoadCoef(char *fname, int code)
	int AACGM_v2_LoadCoefs(int year)
	void msg_notime()
	int AACGM_v2_Convert(double in_lat, double in_lon, double height, double *out_lat, double *out_lon, double *r, int flag)
	int AACGM_v2_SetDateTime(int year, int month, int day, int hour, int minute, int second)
	int AACGM_v2_GetDateTime(int *year, int *month, int *day, int *hour, int *minute, int *second, int *dayno)
	int AACGM_v2_SetNow()

#def Rylm(colat, lon, order):
#	_ylmval = np.ndarray[np.double_t,ndim=1]
#	ret = AACGM_v2_Rylm(colat, lon, order, <double*> _ylmval.data)
#	return (ret, _ylmval)

def Alt2CGM(r_height_in, r_lat_alt):
	cdef double _r_lat_adj
	AACGM_v2_Alt2CGM(r_height_in, r_lat_alt, &_r_lat_adj)
	return _r_lat_adj

def CGM2Alt(r_height_in, r_lat_in):
	cdef double _r_lat_adj
	ret = AACGM_v2_CGM2Alt(r_height_in, r_lat_in, &_r_lat_adj)
	return (ret, _r_lat_adj)

def dayno_py(year, month, day):
	cdef int _diy
	doy = dayno(year, month, day, &_diy)
	return (doy, _diy)

def LoadCoef(fName, code):
	cdef char* c_fName = fName 
	ret = AACGM_v2_LoadCoef(c_fName, code)
	return ret

def LoadCoefs(year):
	ret = AACGM_v2_LoadCoefs(year)
	return ret

def SetDateTime(year, month, day, hour, minute, second):
	ret = AACGM_v2_SetDateTime(year, month, day, hour, minute, second)
	return ret

def SetNow():
	ret = AACGM_v2_SetNow()
	return ret

def GetDateTime():
	cdef int year, month, day, hour, minute, second, dayno
	ret = AACGM_v2_GetDateTime(&year, &month, &day, &hour, &minute, &second, &dayno)
	return (ret,year,month,day,hour,minute,second,dayno)

def convert_geo_coord_py(lat_in, lon_in, height_in, flag, order):
	cdef double lat_out
	cdef double lon_out
	ret = convert_geo_coord(lat_in, lon_in, height_in, &lat_out, &lon_out, flag, order) 
	return (ret,lat_out,lon_out)

def Convert(lat_in, lon_in, height_in, flag):
	cdef double lat_out 
	cdef double lon_out
	cdef double r_out
	ret = AACGM_v2_Convert(lat_in, lon_in, height_in, &lat_out, &lon_out, &r_out, flag) 
	return (ret,lat_out,lon_out,r_out)



