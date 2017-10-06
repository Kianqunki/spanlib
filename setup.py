######################################################################
## SpanLib, Raynaud 2006-2016
######################################################################

import os
import sys
import re
try:
    from configparser import SafeConfigParser
except:
    from ConfigParser import SafeConfigParser
from numpy.distutils.core import setup, Extension
from numpy.f2py import crackfortran

# Revision number
rootdir = os.path.dirname(__file__)
f = open(os.path.join(rootdir, 'lib/spanlib/__init__.py'))
for line in f:
    line = line[:-1].strip()
    if line.startswith('__version__'):
        exec(line)
        release = __version__
        break
f.close()
version_sphinx = release
release_sphinx = release

# Some info
version = release
description='Python extension to the spanlib fortran library'
author = 'Stephane Raynaud and Charles Doutriaux'
author_email = 'stephane.raynaud@gmail.com'
url = "http://spanlib.sf.net"

# From files
base = os.path.dirname(__file__)
with open(os.path.join(base, 'requirements.txt')) as f:
    requires = filter(None, f.read().split('\n'))


# Gather up all the files we need
spanlib_files = ['lib/spanlib/spanlib.pyf', 'lib/spanlib/spanlib_pywrap.f90',
    'lib/spanlib/spanlib.f90',  'lib/spanlib/anaxv.f90']
anaxv_files = ['lib/spanlib/anaxv.pyf', 'lib/spanlib/anaxv.f90']


# Paths for libs
# - standard and detected
libs = ['lapack', 'blas']
libdirs = []
uvcdat_extlibdir = os.path.join(sys.prefix, 'Externals', 'lib')
if os.path.exists(uvcdat_extlibdir):
    libdirs.append(uvcdat_extlibdir)
libdirs += os.environ.get('LD_LIBRARY_PATH', '').split(':')
libdirs += ['/usr/lib','/usr/local/lib']
# - user specified
cfg = SafeConfigParser()
cfg.read('setup.cfg')
site_libs = []
site_libdirs = []
for libname in libs:
    lib = libdir =  ''

    # - Libraries
    if os.getenv(libname.upper()) is not None:
        lib = os.getenv(libname.upper())
    elif cfg.has_option('blaslapack', libname):
        lib = cfg.get('blaslapack', libname)
    local_dir = None
    m = re.match('(.*%s)?lib%s.a'%(os.path.sep, libname), lib)
    if m:
        lib = libname
        local_dir = m.group(1)
    elif lib.startswith('-l'): lib = lib[2:]
    if lib: site_libs.append(lib)

    # - Library dirs
    if os.getenv(libname.upper()+'_LIB') is not None:
        libdir = os.getenv(libname.upper()+'_LIB')
    elif cfg.has_option('blaslapack', libname+'_lib'):
        libdir = cfg.get('blaslapack', libname+'_lib')
    if libdir.startswith('-L'): libdir = libdir[2:]
    if libdir: site_libdirs.append(libdir)
    if local_dir: site_libdirs.append(local_dir)

# - final setup
if len(site_libs): libs = site_libs
if len(site_libdirs): libdirs.extend(site_libdirs)


# Special setups
extra_link_args=[]
if sys.platform=='darwin':
    extra_link_args += ['-bundle','-bundle_loader '+sys.prefix+'/bin/python']
kwext = dict(libraries=libs, library_dirs=libdirs, extra_link_args=extra_link_args)

if __name__=='__main__':

    # Generate pyf files
    crackfortran.f77modulename = '_core'
    pyfcode = crackfortran.crack2fortran(crackfortran.crackfortran(['lib/spanlib/spanlib_pywrap.f90']))
    f = open('lib/spanlib/spanlib.pyf', 'w')
    f.write(pyfcode)
    f.close()
    crackfortran.f77modulename = 'anaxv'
    pyfcode = crackfortran.crack2fortran(crackfortran.crackfortran(['lib/spanlib/anaxv.f90']))
    f = open('lib/spanlib/anaxv.pyf', 'w')
    f.write(pyfcode)
    f.close()

    # Setup the python module
    s = setup(name="spanlib",
        version=version,
        description=description,
        author=author,
        author_email=author_email,
        maintainer=author,
        maintainer_email=author_email,
        license="GNU LGPL",
        install_requires=requires,

        # Fortran wrapper
        ext_modules = [
            Extension('spanlib._core', spanlib_files, **kwext),
            Extension('spanlib.anaxv', anaxv_files, **kwext),
        ],

        # Install these to their own directory
        package_dir={'spanlib':'lib/spanlib'},
        packages = ["spanlib"],

    )



