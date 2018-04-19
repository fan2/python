# [range](https://docs.python.org/3/library/stdtypes.html#range)（区间范围）

## Methods

```shell

 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 
```

## demos

```shell

>>> r=range(1,10,2)

>>> print(r)
range(1, 10, 2)

>>> for i in r:
...     print(i)
... 
1
3
5
7
9

>>> r.start
1
>>> r.stop
10
>>> r.step
2

>>> r.count(4)
0
>>> r.count(5)
1

>>> r.index(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 4 is not in range
>>> r.index(5)
2

```