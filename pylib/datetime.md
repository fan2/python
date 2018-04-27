
[datetime](https://docs.python.org/3/library/datetime.html)  

## strftime

datetime.**strftime**(*format*)

**strftime**: Return a string representing the date

```shell
>>> import datetime

>>> datetime_now = datetime.datetime.now()
>>> datetime_now
datetime.datetime(2018, 4, 24, 15, 51, 2, 399371)
>>> datetime_now.strftime('%Y-%m-%d %H:%M:%S')
'2018-04-24 15:51:02'
```

## strptime

*classmethod* datetime.**strptime**(*date_string*, *format*)

**strptime**: Return a datetime corresponding to date_string, parsed according to format.

```shell
>>> datetime_now = datetime.datetime.strptime('20180424', '%Y%m%d')
>>> datetime_begin = datetime.datetime.strptime('20180323', '%Y%m%d')
>>> datetime_count = datetime_now-datetime_begin
>>> datetime_count
datetime.timedelta(32)
>>> datetime_count.days
32
```

## type-specific formatting

```shell
>>> import datetime
>>> d=datetime.datetime(2018, 4, 25, 13, 0, 0)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2018-04-25 13:00:00'
```

## demos

```shell
>>> # 获取当前时间
>>> d0 = datetime.datetime.now()
>>> # 按格式输出字符串
>>> # 等效: str_now = '{:%Y-%m-%d %H:%M:%S}'.format(d0)
>>> str_now = d0.strftime('%Y-%m-%d %H:%M:%S')
>>> str_now
'2018-04-26 22:37:55'
>>> # 字符串格式化创建日期
>>> str_begin_date = '20180314'
>>> d1 = datetime.datetime.strptime(str_begin_date, '%Y%m%d')
>>> d2 = datetime.datetime(2018,2,2)
>>> # 计算日期相隔天数
>>> dd1=d0-d1
>>> dd1.days
43
>>> dd2=d1-d2
>>> dd2.days
40
>>> # 计算32天前的日期
>>> d3 = d0 - datetime.timedelta(days=32)
>>> d3
datetime.datetime(2018, 3, 25, 22, 37, 55, 465668)
```
