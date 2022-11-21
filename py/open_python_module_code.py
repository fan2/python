#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
运行示例：
$ python3 open_python_module_code.py string
$ python3 open_python_module_code.py datetime
"""

import os
import sys
import importlib


def open_module_source_code(str_module_name):
    try:
        dynamic_module = importlib.import_module(str_module_name)
        str_cmd = 'code '  # 'open ' # 'subl '
        # module_path = inspect.getsourcefile(str_module_name)
        str_file = dynamic_module.__file__  # 绝对路径
        if str_file is not None:
            (file_path, file_name) = os.path.split(str_file)
            # dot_idx = str_file.rindex(os.extsep)
            # file_ext = str_file[(dot_idx + 1):]
            (file_name_prefix, file_name_suffix) = os.path.splitext(file_name)
            if file_name_suffix == '.py':  # ext
                if file_name_prefix == '__init__':
                    print(str_cmd + file_path)
                    os.system(str_cmd + file_path)  # vscode打开目录
                else:
                    print(str_cmd + str_file)
                    os.system(str_cmd + str_file)  # vscode打开文件
            else:  # 'module.cpython*.so'
                # file_name_idx = str_file.rindex(os.sep)
                # file_name = str_file[file_name_idx+1:]
                print('module file: ', str_file)
        else:
            print('module file not exist!')
    except (ImportError, AttributeError, ValueError) as e:
        print(e)
        sys.exit()


def main(args):
    open_module_source_code(args[0])


# main entry
if __name__ == '__main__':
    print('This program is being run by itself')
    if len(sys.argv) < 2:
        print('please input module name')
    else:
        main(sys.argv[1:])
else:
    print('I am being imported from another module')
