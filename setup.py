"""
exec(open('util.py').read())
def cx(inp):	
inp = []
cx(inp)
"""
from distutils.core import setup
import py2exe

setup(console=["stock5.py"])