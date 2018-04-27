reference - [6. Expressions](https://docs.python.org/3/reference/expressions.html)  

```shell
>>> str1='1234567'
>>>
>>> range1=range(1,8)
>>> list(range1)
[1, 2, 3, 4, 5, 6, 7]
>>>
>>> tuple1=tuple(range1)
>>> tuple1
(1, 2, 3, 4, 5, 6, 7)
>>>
>>> list1=list(range1)
>>> list1
[1, 2, 3, 4, 5, 6, 7]
>>>
>>> dict1=dict() # dict1={}
>>> for i in range1:
...     k = 'k{}'.format(i)
...     dict1[k]=i
... 
>>> dict1
{'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4, 'k5': 5, 'k6': 6, 'k7': 7}
>>>
>>> set1=set(range1)
>>> set1
{1, 2, 3, 4, 5, 6, 7}
>>>
```

## ternary conditional operator

[Does Python have a ternary conditional operator?](https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator)

```shell
>>> print('yes') if True else print('no')
yes
>>> print('yes') if False else print('no')
no
```

## len(obj)

- `len(s)`: Return the length of str(number of single character).  

```shell
>>> help(len)

Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```

本质上是调用对象的 `__len__()` 方法，返回序列（包括字符串）、集合或字典等容器所包含元素的个数。

```shell
# 等效于 list1.__len__()
>>> len(list1)
7
```

## in, not in

- `c in s`: Test x for membership in s.  
- `c not in s`: Test x for non-membership in s.  

## for in

- `for c in s`: enumerate substring(character)  in s.  

```shell
>>> for e in list1:
...     print(e)
... 
1
2
3
4
5
6
7
```

**列表解析**将for循环和创建新元素的代码合并成一行，并自动附加新元素。

```shell
>>> squares = [value**2 for value in range(1,11)]
>>> print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## iter, next

```shell
>>> it=iter(list1)
>>> while True:
...     try:  
...         e = next(it)
...     except StopIteration:  
...         break
...     print(e)
... 
1
2
3
4
5
6
7
```

## enumerate

```shell
>>> import builtins
>>> help(builtins)

Help on built-in module builtins:

    class enumerate(object)
     |  enumerate(iterable[, start]) -> iterator for index, value of iterable
     |  
     |  Return an enumerate object.
```

```shell
>>> type(enumerate(list1))
<class 'enumerate'>
>>>
>>> tuple(enumerate(list1))  # pair(index, value)
((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7))
>>>
>>> list(enumerate(list1))  # pair(index, value)
[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
>>>
```

## multiple assignment 

```shell
# 等效于 first, *rest = list1
>>> first, rest = list1[0], list1[1:]
>>> first, rest
(1, [2, 3, 4, 5, 6, 7])

# 针对 list 的 iter, __next__
>>> it = iter(list1)
>>> first=it.__next__()
>>> rest=list(it)
>>> first, rest
(1, [2, 3, 4, 5, 6, 7])

# 针对 dict 的 iter, __next__
>>> it=iter(dict1)
>>> first=next(it)  # it.__next__()
>>> rest=list(it)
>>> first, rest
('k1', ['k2', 'k3', 'k4', 'k5', 'k6', 'k7'])

# 等效于 head, *body, tail = list1
>>> head, body, tail = list1[0], list1[1:-1], list1[-1]
>>> head, body, tail
(1, [2, 3, 4, 5, 6], 7)

>>> for first, *rest in [(1, 2, 3), (4, 5, 6, 7)]:
...     print(first, rest)
... 
1 [2, 3]
4 [5, 6, 7]
```

## starred expression

[PEP 448 -- Additional Unpacking Generalizations](https://www.python.org/dev/peps/pep-0448/)  
[PEP 3132 -- Extended Iterable Unpacking](https://www.python.org/dev/peps/pep-3132/)  

[starred_expression](https://docs.python.org/3/reference/expressions.html#grammar-token-starred_expression)  
[starred_list](https://docs.python.org/3/reference/expressions.html#grammar-token-starred_list)  

[Python 3: starred expression to unpack a list](https://stackoverflow.com/questions/12555627/python-3-starred-expression-to-unpack-a-list)  
[Star * operator on left vs right side of an assignment statement](https://stackoverflow.com/questions/35636785/star-operator-on-left-vs-right-side-of-an-assignment-statement)  

```shell
>>> '{0}, {1}, {2}'.format(*str1)
'1, 2, 3'
>>> '{0}, {1}, {2}'.format(*range1)
'1, 2, 3'
>>> '{0}, {1}, {2}'.format(*tuple1)
'1, 2, 3'
>>> '{0}, {1}, {2}'.format(*list1)
'1, 2, 3'
>>> '{0}, {1}, {2}'.format(*set1)
'1, 2, 3'
```

```shell
# position
>>> '{0}, {1}, {2}'.format(*dict1)
'k1, k2, k3'

# name
>>> '{k1}, {k2}, {k3}'.format(**dict1)
'1, 2, 3'
```

`*elements, = iterable`: elements is always going to be a list containing all the items in the iterable.  
`elements = *iterable,`: expands the contents of the iterable it is attached to.  

```shell
# *elements, = iterable 生成列表
# 等效于 parenth_form : list2 = [*set1]
>>> *list2, = set1
>>> list2
[1, 2, 3, 4, 5, 6, 7]

# elements = *iterable, 生成 tuple
>>> tuple2 = *set1,
>>> tuple2
(1, 2, 3, 4, 5, 6, 7)
```
