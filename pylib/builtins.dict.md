# [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

在Python中，字典是一系列 `键—值对`。

每个键都与一个值相关联，你可以使用键来访问与之相关联的值。  
与键相关联的值可以是数字、字符串、列表乃至字典。  
事实上，可将任何Python对象用作字典中的值。  

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

## enumerate

```
>>> favorite_languages.keys()
dict_keys(['jen', 'sarah', 'edward', 'phil'])
>>> favorite_languages.values()
dict_values(['python', 'c', 'ruby', 'python'])
```

### keys

在不需要使用字典中的值时，方法 `keys()` 很有用，它返回键列表。

遍历字典时，会默认遍历所有的键。如果显式地使用方法 `keys()` 可让代码更容易理解。  

在这种循环中，可使用当前键来访问与之相关联的值。

```
>>> # 等效于 for k in dict1.keys()
>>> for k in dict1:
...     print('dict1[{0}]={1}'.format(k, dict1[k]))
... 
dict1[k1]=1
dict1[k2]=2
dict1[k3]=3
dict1[k4]=4
dict1[k5]=5
dict1[k6]=6
dict1[k7]=7
```

### values

如果你感兴趣的主要是字典包含的值，可使用方法 `values()`，它返回一个值列表，而不包含任何键。
可基于 `values()` 返回的列表构造集合(set)来剔除重复项。

```
>>> favorite_languages = {
...     'jen': 'python',
...     'sarah': 'c',
...     'edward': 'ruby',
...     'phil': 'python',
... }
>>> print("The following languages have been mentioned:")
The following languages have been mentioned:
>>> for language in set(favorite_languages.values()):
...     print(language.title())
...
Ruby
C
Python
```

### items

要编写用于遍历字典的for循环，可声明两个变量，用于存储键—值对中的键和值。对于这两个变量，可使用任何名称。

```
for k, v in user_0.items()
```

for语句的第二部分包含字典名和方法items()，它返回一个键—值对列表。for循环依次将每个键—值对存储到指定的两个变量中。

```shell
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