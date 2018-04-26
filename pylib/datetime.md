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
