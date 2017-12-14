#coding=utf-8

#from platform import python_version
#print(python_version())

import platform
print(platform.python_version())
print('\n' * 1)

import sys
print(sys.version)

print('\n' * 1)

print(sys.version_info)
print("The Python version is %s.%s.%s" % sys.version_info[:3])
