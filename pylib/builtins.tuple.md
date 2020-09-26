# [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)（元组）

列表是可以修改的，非常适合用于存储在程序运行期间可能变化的数据集。  
然而，有时候你需要创建一系列不可修改的元素， 元组可以满足这种需求。  
Python将不能修改的值称为`不可变的`，而不可变的列表被称为**元组**。  

```shell
>>> range1=range(1,8)
>>> tuple1=tuple(range1)
>>> tuple1
(1, 2, 3, 4, 5, 6, 7)
>>> tuple1[-1]
7
>>> tuple1[-1]=8
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

## empty tuple

元组看起来犹如列表，但使用圆括号而不是方括号来标识。

1. `t=tuple()`: 构造一个空元组对象。  
2. `t=()`：小括号定义空元组。  

多个元素之间以逗号分隔，例如 `t1=(1,2,3,4)`。  

元组支持基于脚标索引访问元素（access through subscripted index）。

## expressions

- `len(t)`: Return the number of elements in tuple t.  
- `e in t`: Test e for membership in t.  
- `e not in t`: Test e for non-membership in t.  
- `for e in t`: enumerate elements in t.  
