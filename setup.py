'''
  For building a Windows executable
  Usage: python make_exe.py py2exe
'''

from distutils.core import setup
import py2exe

setup(console=['emailsfromfile.py'])