# [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

[str tutorial](https://docs.python.org/3.6/tutorial/introduction.html#strings)  

## empty string

1. `s=str()`: 构造一个空字符串对象。  
2. `s=''`：定义空字符串字面量。  

## expressions

- `len(s)`: Return the length of str(number of single character).  
- `c in s`: Test x for membership in s.  
- `c not in s`: Test x for non-membership in s.  
- `for c in s`: enumerate substring(character)  in s.  

## access through subscripted index

```shell
>>> word = 'Python'
>>> word[0]
'P'
>>> word[5]
'n'
>>> word[-1]
'n'
>>> word[-2]
'o'
>>> word[-6]
'P'
>>> word[0:2]
'Py'
>>> word[2:5]
'tho'
>>> word[2:]
'thon'
>>> word[4:]
'on'
>>> word[-2:]
'on'
```

## [String Methods](https://docs.python.org/3.6/library/stdtypes.html#string-methods)

```shell

# 基于占位符格式化创建字符串
str.format(*args, **kwargs)

# 判断是否以某个子串开头/结尾
str.startswith(prefix[, start[, end]])
str.endswith(suffix[, start[, end]])

# 计算子串的个数
str.count(sub[, start[, end]])
 
# 查找子串的位置索引，不存在则返回-1
str.find(sub[, start[, end]])
str.rfind(sub[, start[, end]])

# 查找子串的位置索引，找不到则抛 ValueError 异常
str.index(sub[, start[, end]]) 
str.rindex(sub[, start[, end]])

# 替换子串
str.replace(old, new[, count])

# 移除开头或结尾的空白
str.strip([chars])
str.lstrip([chars])
str.rstrip([chars])

# 分割三部分(head, sep, tail)
str.partition(sep)
str.rpartition(sep)

# 按照分隔符分割成子串
str.split(sep=None, maxsplit=-1)
str.rsplit(sep=None, maxsplit=-1)

str.splitlines([keepends])

```

## demos

```shell

>>> str1='py'
>>> str2='python'

>>> str1 in str2
True

>>> str2.find(str1)
0

>>> str2.count(str1)
1

>>> str2.startswith(str1) or str2.endswith(str1)
True
```
