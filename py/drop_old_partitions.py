#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import platform
import datetime


def dump_platform_info():
    print('\n')
    print('platform.machine =', platform.machine())
    print('platform.processor =', platform.processor())
    print('platform.system =', platform.system())
    print('platform.python_implementation =', platform.python_implementation())
    print('platform.python_version =', platform.python_version())
    (major, minor, micro) = platform.python_version_tuple()
    print('(major, minor, micro) =', (major, minor, micro))
    print('\n')


# ------------------------------------------------------------------------------
# 批量老化删除32天之前的陈旧分区
# ------------------------------------------------------------------------------
def drop_old_partitions(str_begin_date, int_aging_days):
    datetime_now = datetime.datetime.now()
    if len(str_begin_date) > 0:
        datetime_now = datetime.datetime.strptime(str_begin_date, '%Y%m%d')

    # 推算32天之前的日期
    datetime_begin = datetime_now - datetime.timedelta(days=int_aging_days)
    # 初始创建的第一个分区的日期
    datetime_create = datetime.datetime.strptime('20180101', '%Y%m%d')

    # 计算总共有多少天的分区需要删除
    datetime_count = datetime_begin - datetime_create
    int_aging_count = datetime_count.days
    print('aging range is [%s, %s), count = %d\n' %
          (datetime_create.strftime('%Y%m%d'),
           datetime_begin.strftime('%Y%m%d'),
           int_aging_count))

    for date_index in range(0, int_aging_count):
        datetime_day = datetime_create + datetime.timedelta(days=date_index)
        str_day = datetime_day.strftime('%Y%m%d')
        # print('day[%d]=%s' % (date_index, str_day))
        tableName = 'db.table'
        str_sql = 'alter table %s truncate partition (p_%s)' % (
            tableName, str_day)
        print('running SQL: ' + str_sql)


def main(args):
    str_begin_date = ''

    # 参数1: 20180424
    if len(args) > 1:
        str_begin_date = args[1]

    # 参数2: 截至保留数据天数（默认一个月）
    int_aging_days = 32

    if len(args) > 2:
        str_aging_days = args[2]
        int_aging_days = int(str_aging_days)

    drop_old_partitions(str_begin_date, int_aging_days)


# main entry
if __name__ == '__main__':
    print('This program is being run by itself')
    dump_platform_info()
    main(sys.argv)
else:
    print('I am being imported from another module')
