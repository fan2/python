#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import importlib


def open_module_source_code(str_module_name):
    try:
        dynamic_module = importlib.import_module(str_module_name)
        str_cmd = 'subl '  # 'open '
        str_file = dynamic_module.__file__
        dot_idx = str_file.rindex(os.extsep)
        file_ext = str_file[(dot_idx + 1):]
        if file_ext == 'py':
            print('execute system command: ', str_cmd + str_file)
            os.system(str_cmd + str_file)
        else:  # 'module.cpython*.so'
            # file_name_idx = str_file.rindex(os.sep)
            # file_name = str_file[file_name_idx+1:]
            print('module file: ', str_file)
    except (ImportError, AttributeError, ValueError) as e:
        print(e)
        sys.exit()
    pass


def main(args):
    open_module_source_code(args[0])
    pass


# main entry
if __name__ == '__main__':
    print('This program is being run by itself')
    if len(sys.argv) < 2:
        print('please input module name')
    else:
        main(sys.argv[1:])
else:
    print('I am being imported from another module')
