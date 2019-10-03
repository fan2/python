#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
import os
import enum


class PLATFORM(enum.Enum):
    ios = 0
    android = 1
    windows = 2


def main(platform: int, logpath: str, debug: bool):
    (filepath, filename) = os.path.split(logpath)
    print('parse {} log: {}\n'.format(PLATFORM(platform).name, filename))


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
    argparser = argparse.ArgumentParser(description='MBR_Client log analyzer',
                                        formatter_class=argparse.RawTextHelpFormatter,
                                        epilog='fan@qq.com')
    argparser.version = '1.0'
    argparser.add_argument('-V', '--version', action='version')
    argparser.add_argument('-p', '--platform', type=int,
                           choices=[0, 1, 2],
                           help='0 for ios,\n'
                                '1 for android,\n'
                                '2 for windows.\n'
                                '> guess from first line if miss.')
    # positional or -f
    # argsgroup = argparser.add_mutually_exclusive_group()
    # argsgroup.add_argument('logpath', type=str,
    #                        nargs='*', default=None,
    #                        help='path of log file')
    # argsgroup.add_argument('-f', '--filepath',
    #                        type=str, dest='logpath',
    #                        help='path of log file')
    argparser.add_argument('logpath', type=str, help='path of log file')
    argparser.add_argument('-v', '--verbose', dest='debug',
                           action='store_true', help='print debug verbose')
    args_namespace = argparser.parse_args()
    # print(vars(args_namespace))

    if not os.path.isfile(args_namespace.logpath):
        print('please input valid logpath')
    elif args_namespace.platform not in (PLATFORM.ios.value,
                                         PLATFORM.android.value,
                                         PLATFORM.windows.value):
        with open(args_namespace.logpath, encoding='ISO-8859-1') as mbr_log_file:
            first_log_line = mbr_log_file.readline()  # skip tlg first line
            second_log_line = mbr_log_file.readline()
            # guess_platform = try_to_guess_platform(second_log_line)
    else:
        main(args_namespace.platform,
             args_namespace.logpath,
             args_namespace.debug)

else:
    # print('I am being imported from another module')
    pass
