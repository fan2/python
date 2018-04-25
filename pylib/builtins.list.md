# [list](https://docs.python.org/3/library/stdtypes.html#list)（有序列表）

```shell
>>> type(sys.argv)
<class 'list'>
```

## empty list

1. `l=list()`: 构造一个空列表对象。  
2. `l=[]`：中括号定义空列表。  

多个元素之间以逗号分隔，例如 `l1=[1,2,3,4]`。  

列表支持基于脚标索引访问元素（access through subscripted index）。

## expressions

- `len(l)`: Return the number of elements in list l.  
- `e in l`: Test e for membership in l.  
- `e not in l`: Test e for non-membership in l.  
- `for e in l`: enumerate elements in l.  

## demos

```shell
# 判断模块名称中是否包含 '__doc__' 和 '__file__'
>>> import builtins
>>> '__doc__' in dir(builtins)
True
>>> '__file__' in dir(builtins)
False

>>> import os
>>> '__doc__' in dir(os)
True
>>> '__file__' in dir(os)
True
```