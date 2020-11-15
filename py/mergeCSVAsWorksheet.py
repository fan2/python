#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
将指定目录下的 csv 文件合并成一个 excel 文件，每个 csv 文件对应一个 worksheet。

# python3 运行该脚本，指定 csv 文件所在目录（dirpath）:
python3 mergeCSVAsWorksheet.py dirpath
# 添加 -v 选项，可查看调试输出：
python3 mergeCSVAsWorksheet.py -v dirpath

# dirpath 为位置参数，可拖入绝对路径或手动输入相对路径：
python3 mergeCSVAsWorksheet.py -v /Users/faner/Projects/IWYU/IWYUPlugin/logs/FileAssist
python3 mergeCSVAsWorksheet.py -v ~/Projects/IWYU/IWYUPlugin/logs/FileAssist
python3 mergeCSVAsWorksheet.py -v FileAssist # 相对 pwd 的路径

# 输出合并的 excel 文件到 dirpath：
FileAssist/merged-20201111_111111.xlsx
"""

import os, sys, glob
import datetime
import argparse
import pandas

def main(dirpath: str, debug: bool = False):
    if debug:
        print('csvDirPath =', dirpath)
        print('----------------------------------------')

    # 在 dirpath 下创建输出 excel，命名引入时间戳，规避多次执行的重名冲突
    mergedFilePrefix = 'merged'  # os.path.split(dirpath)[-1] + '-merged'
    curDateTime = datetime.datetime.now()
    strCurTime = curDateTime.strftime('%Y%m%d_%H%M%S')
    mergedFileSuffix = '.xlsx'
    mergedFilename = mergedFilePrefix + '-' + strCurTime + mergedFileSuffix
    mergedFilepath = os.path.join(dirpath, mergedFilename)
    mergedExcelWriter = pandas.ExcelWriter(mergedFilepath)

    # glob 通配指定目录下的 csv 文件
    allCSVFiles = glob.glob(os.path.join(dirpath, "*.csv"))
    for csvFilePath in allCSVFiles:
        csvFileName = os.path.split(csvFilePath)[-1]      # 带后缀的文件名
        workSheetName = os.path.splitext(csvFileName)[0]  # 去除后缀的纯文件名
        # 读取 csv 内容并保存为 excel 的 worksheet
        csvDataFrame = pandas.read_csv(csvFilePath, sep=',')
        csvDataFrame.to_excel(mergedExcelWriter, sheet_name=workSheetName)
        if debug:
            print('csvFilePath =', csvFilePath)
            print('workSheetName =', workSheetName)
    mergedExcelWriter.save()

    if debug:
        print('----------------------------------------')
        print('mergedFilepath =', mergedFilepath)



# main entry
if __name__ == '__main__':
    # print('This program is being run by itself')
    # if len(sys.argv) < 2:
    #     print('please input args as dirpath')
    # else:
    #     argv1 = sys.argv[1]
    #     if os.path.isdir(argv1): #检查输入的参数为文件路径
    #         main(argv1)
    #     else:
    #         print('please input valid dirpath')
    argparser = argparse.ArgumentParser(description='merge csv files in folder',
                                        formatter_class=argparse.
                                        RawTextHelpFormatter,
                                        epilog='fan@qq.com')
    argparser.version = '1.0'
    argparser.add_argument('-V', '--version', action='version')
    argparser.add_argument('dirpath', type=str, help='dir of csv files')
    argparser.add_argument('-v', '--verbose', dest='debug',
                           action='store_true', help='print debug verbose')
    args_namespace = argparser.parse_args()
    # print(vars(args_namespace))
    if not os.path.isdir(args_namespace.dirpath):
        print('please input valid dirpath')
    else:
        main(args_namespace.dirpath, args_namespace.debug)
else:
    # print('I am being imported from another module')
    pass
