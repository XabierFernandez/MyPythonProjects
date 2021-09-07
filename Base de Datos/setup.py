
from distutils.core import setup
import py2exe

import sys; sys.argv.append('py2exe')

py2exe_options = dict(   
                      excludes=['_ssl',  # Exclude _ssl
                                'pyreadline', 'difflib', 'doctest', 
                                'optparse', 'pickle', 'calendar'],  # Exclude standard library
                      dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
                      compressed=True,  # Compress library.zip
                      )

setup(name='BDP',
      version='1.0',
      description='',
      author='Xabier Fernandez',

      windows=[{
            "script": "BDP.pyw",
            "icon_resources": [(1, "BDP.ico")]}],
      options={'py2exe': py2exe_options},
      )
