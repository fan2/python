# [Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

## help

```Shell
>>> help(set)

Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |
 |  Build an unordered collection of unique elements.
```

## empty set

`st=set()`: 构造一个空集合对象。  

> 注意： `st={}` 定义的是空字典。  

`st={1,2}` 相当于 `st=set();st.add(1);st.add(2)`。

集合不支持基于脚标索引访问元素（access through subscripted index）。

## expressions

- `len(st)`: Return the number of elements in set st.  
- `e in st`: Test e for membership in st.  
- `e not in st`: Test e for non-membership in st.  
- `for e in st`: enumerate elements in st.  
