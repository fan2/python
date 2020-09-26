#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
import os
# import string

"""
过滤出文本文件中重复的行

# 在工程根目录下运行以下命令，检查符号表中重复的符号（文本行）：
# python3 rm-dup-sym.py ./Classes/module/TlibDy/TlibDy/sym_export.def
"""

"""
# TlibDy - Build Settings - Exported Symbols File

################################################################################
# Debug
################################################################################
## Any iOS Simulator SDK
# "./Classes/module/TlibDy/TlibDy/sym_export.def"
## Any macOS SDK, arm64 architecture
# "./Classes/module/TlibDy/TlibDy/sym_device_export.def"
## armv7 architecture
# "./Classes/module/TlibDy/TlibDy/sym_device_export_armv7.def"

################################################################################
# DailyBuild & Release
################################################################################
## Any iOS Simulator SDK, Any macOS SDK, arm64 architecture
# "./Classes/module/TlibDy/TlibDy/sym_release_export.def"
## armv7 architecture
# "./Classes/module/TlibDy/TlibDy/sym_release_export_armv7.def"

################################################################################
# 以下未配置?
################################################################################
# "./Classes/module/TlibDy/TlibDy/sym_dailybuild_export.def"
# "./Classes/module/TlibDy/TlibDy/sym_localrelease_export.def"
"""

def main(filepath: str, analyze: int, debug: bool = False):
    print('filepath =', filepath)
    (filePath, fileName) = os.path.split(filepath)
    # print('relative  path = {}'.format(filePath))
    # print('pure file name = {}'.format(fileName))

    outfile = None
    if analyze == 1:
        filename = os.path.splitext(filepath)[0]
        fileext = os.path.splitext(filepath)[1]
        outpath = ''
        i = 1
        while True:
            outpath = filename + '(' + str(i) + ')' + fileext
            if not os.path.isfile(outpath):  # 尚未占用
                print('outpath = {}\n'.format(outpath))
                break
            else:
                i += 1  # try next

        outfile = open(outpath, "w")

    with open(filepath, encoding='ISO-8859-1') as src_file:
        ########################################################################
        # 简单方案：集合去重
        # 需要 pip3 install orderedset，然后 import orderedset
        # 问题：空白行也被集合精简掉了！
        # lines = src_file.readlines()
        # uniq_lines = orderedset.OrderedSet(lines)
        # for uniline in uniq_lines:
        #     outfile.write(uniline)
        # return

        ########################################################################
        # 完整方案：逐行遍历
        unique_line_set = set()  # unique unordered collection
        dup_count_dict = dict()  # duplicate line counter map
        dup_lines_dict = dict()  # duplicate lines number map

        line_no = 0
        for line in src_file:
            line_no += 1
            line = line.strip()  # lstrip('#')
            if len(line):  # 非空白行: not line.isspace()
                if line not in unique_line_set:
                    # dst_file.write(line+ '\n')
                    if not line.startswith('#') \
                       or line.startswith('#_') \
                       or line.startswith('##_'):
                        unique_line_set.add(line)
                        dup_count_dict[line] = 1
                        dup_lines_dict[line] = [line_no]
                    else:
                        if analyze == 0 or debug:
                            print('comment line {} : \033[0;32;47m{}\033[0m'.
                                  format(line_no, line))

                    if analyze == 1:
                        outfile.write(line + '\n')
                else:
                    # if line in dup_count_dict:
                    dup_count_dict[line] += 1
                    # if line in dup_lines_dict:
                    dup_lines_dict[line].append(line_no)

        if analyze == 0 or debug:
            for dupline in dup_count_dict:
                if dup_count_dict[dupline] > 1:
                    print('\033[0;31;47m{0}\033[0m : dupCount = {1}, '
                          'dupLines = {2}'.format(dupline,
                                                  dup_count_dict[dupline],
                                                  dup_lines_dict[dupline]))


# main entry
if __name__ == '__main__':
    # print('This program is being run by itself')
    # if len(sys.argv) < 2:
    #     print('please input args as filepath')
    # else:
    #     argv1 = sys.argv[1]
    #     if os.path.isfile(argv1): #检查输入的参数为文件路径
    #         main(argv1)
    #     else:
    #         print('please input valid filepath')
    argparser = argparse.ArgumentParser(description='duplicate lines detector',
                                        formatter_class=argparse.
                                        RawTextHelpFormatter,
                                        epilog='fan@qq.com')
    argparser.version = '1.0'
    argparser.add_argument('-V', '--version', action='version')

    # positional or -f
    # argsgroup = argparser.add_mutually_exclusive_group()
    # argsgroup.add_argument('filepath', type=str,
    #                        nargs='*', default=None,
    #                        help='path of text-plain file')
    # argsgroup.add_argument('-f', '--filepath',
    #                        type=str, dest='filepath',
    #                        help='path of text-plain file')
    argparser.add_argument('filepath', type=str,
                           help='path of text-plain file')
    argparser.add_argument('-a', '--analyze', type=int,
                           choices=[0, 1], default=0,
                           help='0 for detect duplicate lines,\n'
                                '1 for remove duplicate lines')
    argparser.add_argument('-v', '--verbose', dest='debug',
                           action='store_true', help='print debug verbose')
    args_namespace = argparser.parse_args()
    # print(vars(args_namespace))
    if not os.path.isfile(args_namespace.filepath):
        print('please input valid filepath')
    else:
        main(args_namespace.filepath,
             args_namespace.analyze,
             args_namespace.debug)
else:
    # print('I am being imported from another module')
    pass
