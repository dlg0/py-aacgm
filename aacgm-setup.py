from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sources = ["c-aacgm.pyx"]
extra_objects = ["libaacgmlib_v2.so"]

ext_modules = [Extension(
		name = "aacgm",
		sources = sources,
		extra_objects = extra_objects,
		include_dirs = ["./"]
	)]

setup(
	name = 'aacgm',
	cmdclass = {'build_ext': build_ext},
	ext_modules = ext_modules
)
	

