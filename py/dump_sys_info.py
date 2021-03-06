#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import platform
import sys
import os
import sysconfig


def dump_platform_info():
    print('platform.machine =', platform.machine())
    print('platform.processor =', platform.processor())
    print('platform.system =', platform.system())
    print('platform.python_implementation =', platform.python_implementation())
    print('platform.python_version =', platform.python_version())
    (major, minor, micro) = platform.python_version_tuple()
    print('(major, minor, micro) =', (major, minor, micro))
    print('\n')


def dump_sys_info():
    print('sys.platform = ' + sys.platform)
    print('sys.version = ' + sys.version)
    print('sys.version_info = ' + repr(sys.version_info))
    print('sys.byteorder = ' + sys.byteorder)
    if sys.version_info.major > 2:
        print('sys.implementation = ' + repr(sys.implementation))
        print('sys.int_info = ' + repr(sys.int_info))
        print('sys.thread_info = ' + repr(sys.thread_info))
    print('\n')


def dump_os_info():
    print('os.name = %s' % os.name)
    print('os.sep = %s' % os.sep)
    print('os.extsep = %s' % os.extsep)
    print('os.pathsep = %s' % os.pathsep)
    print('os.linesep = %s' % repr(os.linesep))
    print('\n')


def dump_sysconfig_info():
    print('sysconfig.get_platform is', sysconfig.get_platform())
    print('sysconfig.get_python_version is', sysconfig.get_python_version())


def main(args):
    dump_platform_info()
    dump_sys_info()
    dump_os_info()
    dump_sysconfig_info()


# main entry
if __name__ == '__main__':
    print('This program is being run by itself')
    if len(sys.argv) < 2:
        # print('please input parameters:')
        main(None)
    else:
        main(sys.argv[1:])
else:
    print('I am being imported from another module')
