
from distutils.core import setup
import py2exe

import sys; sys.argv.append('py2exe')

py2exe_options = dict(   
                      excludes=['_ssl',  # Exclude _ssl
                                'pyreadline', 'difflib', 'doctest', 'locale', 
                                'optparse', 'pickle', 'calendar'],  # Exclude standard library
                      dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
                      compressed=True,  # Compress library.zip
                      )

setup(name='KRC2_Exporter',
      version='1.0',
      description='Exporter',
      author='Xabier Fernandez',

      console=['krc2_exporter.py'],
      options={'py2exe': py2exe_options},
      )