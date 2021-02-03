
from distutils.core import setup
import py2exe

import sys; sys.argv.append('py2exe')

py2exe_options = dict(   
                      excludes=['_ssl',  # Exclude _ssl
                                'pyreadline', 'doctest',
								'optparse', 'pickle', 'calendar',
								'pdb','inspect',"Tkconstants","Tkinter","tcl",'tk'],  # Exclude standard library
                      dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
                      compressed=True,  # Compress library.zip
                      )

setup(name='RobotTranslator',
      version='1.0',
      description='',
      author='Xabier Fernandez',

      windows=[{
            "script": "RobotTranslator.py"}],
      options={'py2exe': py2exe_options},
      )
