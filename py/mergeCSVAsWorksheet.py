#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
将指定目录下的 csv 文件合并成一个 excel 文件，每个 csv 文件对应一个 worksheet。

# 在脚本目录下运行以下命令，拖入位置参数（dirpath）:
python3 mergeCSVAsWorksheet.py /Users/faner/Projects/IWYU/logs/FileAssist
# 加 -v 选项，可查看调试输出：
python3 mergeCSVAsWorksheet.py -v /Users/faner/Projects/IWYU/logs/FileAssist

# 输出合并的 excel 文件：
/Users/faner/Projects/IWYU/logs/FileAssist/FileAssist--merged.xlsx
"""

import os, sys, glob
import argparse
import pandas

def main(dirpath: str, debug: bool = False):
    mergedFilename = dirpath.split(os.sep)[-1] + '-merged.xlsx'
    mergedFilepath = os.path.join(dirpath, mergedFilename)
    excelWriter = pandas.ExcelWriter(mergedFilepath) # Arbitrary output name

    if debug:
        print('csvDirPath =', dirpath)
        print('mergedFilepath =', mergedFilepath)
        print('----------------------------------------')

    allCSVFiles = glob.glob(os.path.join(dirpath, "*.csv"))
    for csvFilePath in allCSVFiles:
        csvDataFrame = pandas.read_csv(csvFilePath, sep=',')
        csvNamePrefix = os.path.splitext(csvFilePath)[0]
        workSheetName = csvNamePrefix.split(os.sep)[-1]
        if debug:
            print('csvFilePath =', csvFilePath)
            print('workSheetName =', workSheetName)
        csvDataFrame.to_excel(excelWriter, sheet_name=workSheetName)
    excelWriter.save()



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
