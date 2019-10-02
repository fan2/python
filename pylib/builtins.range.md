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

可以将其转换为 tuple 或 list 打印出其值：

```
>>> tuple(r)
(1, 3, 5, 7, 9)

>>> list(r)
[1, 3, 5, 7, 9]
```

## access through subscripted index

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

## slice

slice命令用法:

```
slice(start, stop[, step])
```

创建一个slice类型. slice(None) 等价于冒号 `:`，表示从头到尾。

a = `[1,2,3,4,5,6,7]`，取切片 `a[1:3]` 索引范围 = [1,3)，取出的子集为 `[2, 3]`。

也可以用 slice 函数指定 start、stop 和 step，构造切片索引，对序列进行切片取值。

```
s = slice(1,3)
a[s] = [2,3]
```

这样使得切片范围可编程定制化，更灵活的截取子集。

### refs

[Python切片Slice](http://liao.cpython.org/07slice/)  
[python中切片（Slice）操作符](https://blog.csdn.net/xiaofeiyu321/article/details/82941765)  
[切片（Slice）在python中的运用](https://blog.csdn.net/dfshi198/article/details/80843175)  
[Python高级特性——切片（Slice）](https://www.cnblogs.com/hiwuchong/p/8052502.html)  
