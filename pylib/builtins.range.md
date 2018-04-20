# [range](https://docs.python.org/3/library/stdtypes.html#range)（区间范围）

```shell
>>> r=range(1,10,2)

>>> r.start
1
>>> r.stop
10
>>> r.step
2
```

range 支持下标索引访问：

```shell
>>> r[3]
7
>>> r[:3]
range(1, 7, 2)
>>> r[-1]
9
```

## expressions

- `len(r)`: Return the number of elements in range r.  
- `e in r`: Test e for membership in r.  
- `e not in r`: Test e for non-membership in r.  
- `for e in r`: enumerate elements in r.  

```shell
# 返回区间包含的元素个数
>>> len(r)
5

# 判断5是否在区间内
>>> 5 in r
True

# 判断6是否不在区间内
>>> 6 not in r
True

# for 循环遍历
>>> for i in r:
...     print(i)
... 
1
3
5
7
9
```

## Methods

```shell

 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 
```

`r.count(e)`：返回区间范围内元素e的个数：

```shell
>>> r.count(4)
0
>>> r.count(5)
1
```

`r.index(e)`：返回区间范围内元素e的索引，不存在抛异常：

```shell
>>> r.index(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 4 is not in range
>>> r.index(5)
2
```