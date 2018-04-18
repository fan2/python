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
