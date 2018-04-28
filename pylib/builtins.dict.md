# [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

## empty dict

1. `d=dict()`: 构造一个空字典对象。  
2. `d={}`：大括号定义空字典。  

字典的键值以冒号分隔，`d1={1:2}` 等效于 `d1=dict();d1[1]=2`。  
多对键值以逗号分隔，例如 `d1={1:2, 3:4}`。  

字典支持基于脚标键值访问值（access through subscripted index）。

## expressions

- `len(d)`: Return the number of elements in dict d.  
- `e in d`: Test e for membership in d.keys.  
- `e not in d`: Test e for non-membership in d.keys.  
- `for e in d`: enumerate elements in d.keys.  

```shell

>>> for k in dict1.keys():
...     print('dict1[{0}]={1}'.format(k, dict1[k]))
... 
dict1[k1]=1
dict1[k2]=2
dict1[k3]=3
dict1[k4]=4
dict1[k5]=5
dict1[k6]=6
dict1[k7]=7
>>>
>>> for key, value in dict1.items():
...     print('dict1[{0}]={1}'.format(key, value))
... 
dict1[k1]=1
dict1[k2]=2
dict1[k3]=3
dict1[k4]=4
dict1[k5]=5
dict1[k6]=6
dict1[k7]=7
```