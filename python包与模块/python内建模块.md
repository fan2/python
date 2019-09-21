打印 `sys.builtin_module_names` 可查看 python 解释器自带的基础模块：

```shell
>>> import sys
>>> sys.builtin_module_names
('_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_signal', '_sre', '_stat', '_string', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time', 'xxsubtype', 'zipimport')
```

> A tuple of strings giving the names of all modules that are compiled into this Python interpreter.

# builtins

在 python help utility 交互控制台中，直接输入 builtins 可查看模块帮助。  
在 python 交互控制台中，则先执行 `import builtins` 导入 builtins 模块，再调用 `help(builtins)` 查看模块帮助。

```shell
>>> import builtins
>>> help(builtins)

Help on built-in module builtins:

NAME
    builtins - Built-in functions, exceptions, and other objects.

DESCRIPTION
    Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.

```

- 执行 `print(builtins.__doc__)` 查看模块概要：

```shell
>>> import builtins
>>> print(builtins.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
```

- 执行 `dir(builtins)` 查看模块：

```shell
>>> import builtins
>>> dir(builtins)
```

	> 也可执行 `print(builtins.__dict__)` 打印 builtins 模块的符号表。

## [FUNCTIONS](https://docs.python.org/3/library/functions.html)

builtins 模块提供了一些常用的内置函数，大概分为 vars、math、utility 三类：

### vars

```shell
    globals()
        Return the dictionary containing the current scope's global variables.

    locals()
        Return a dictionary containing the current scope's local variables.

    vars(...)
        vars([object]) -> dictionary
        
        Without arguments, equivalent to locals().
        With an argument, equivalent to object.__dict__.
```

### math

```
    abs(x, /)
        Return the absolute value of the argument.

    divmod(x, y, /)
        Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.

    max(...)

    min(...)

    pow(x, y, z=None, /)
        Equivalent to x**y (with two arguments) or x**y % z (with three arguments)

    round(...)
        round(number[, ndigits]) -> number

    sorted(iterable, /, *, key=None, reverse=False)
        Return a new list containing all items from the iterable in ascending order.

    sum(iterable, start=0, /)
        Return the sum of a 'start' value (default: 0) plus an iterable of numbers

```

更多可参考 [math](https://docs.python.org/3/library/math.html)、[cmath](https://docs.python.org/3/library/cmath.html#module-cmath) 等 C 标准的数学库模块，或安装更专业的第三方科学计算库 [SciPy](https://www.scipy.org/) 组织提供的 SciPy 和 NumPy。  

### utility

#### print

在 Python 2 中，print 为关键字；在 Python 3 中，print 为内置函数（builtins.print）。

builtins 的 print() 函数：

```shell
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

> [Python print函数用法](http://blog.csdn.net/zanfeng/article/details/52164124)  
> [python格式化输出](http://blog.csdn.net/wchoclate/article/details/42297173)  

---

对很多应用程序来说，使用模块 logging 来写入日志比使用 print 更合适。

> 相关模块参考：syslog, logging。

#### bin(), hex()

```shell
    bin(number, /)
        Return the binary representation of an integer.

    hex(number, /)
        Return the hexadecimal representation of an integer.

    oct(number, /)
        Return the octal representation of an integer.
```

python 内置的 `bin()`、`oct()`、`hex()` 函数支持将十进制数转换为对应的二进制、八进制、十六进制字符串。

```Shell
>>> bin(2017)
'0b11111100001'
>>> oct(2017)
'0o3741'
>>> print(hex(2017))
0x7e1
>>> print(0x7e1)
2017
```

或者通过 `print()` 函数的占位符 `%o`、`%x` 格式化输出十进制数对应的八进制和十六进制格式：

```Shell
>>> x=2017
>>> print('oct=%o' %(x))
oct=3741
>>> print('hex=%x' %(2017))
hex=7e1
```

#### len

```shell
    len(obj, /)
        Return the number of items in a container.
```

对于字符串（str）、数组（array）、列表（list）、元组（tuple）、集合（set）、字典（dict）等常用序列或集合，均可调用 len 取其大小（本质上是调用类的 `__len__()` 方法）。

```shell
# len(str)：返回字符串中的字符个数。等效于调用 str.__len__()
>>> str1='hello,world!'
>>> len(str1)
12

>>> str2='"Isn\'t," she said.'
>>> print(str2)
"Isn't," she said.
>>> len(str2)
18

# len(array)：返回数组中的元素个数。等效于调用 array.__len__()
>>> a=array.array('i', [2018,5,4])
>>> len(a)
3

# len(list)：返回列表中的元素个数（以逗号分隔）。等效于调用 list.__len__()
>>> squares = [1, 4, 9, 16, 25]
>>> len(squares)
5

>>> len(dir(builtins))
152
>>> len(dir(str))
77

# len(tuple)：返回元组中的元素个数（以逗号分隔）。等效于调用 tuple.__len__()
>>> t = 12345, 54321, 'hello!'
>>> print(t)
(12345, 54321, 'hello!')
>>> len(t)
3

>>> v = ([1, 2, 3], [3, 2, 1])
>>> len(v)
2

# len(set)：返回集合中的元素个数（以逗号分隔，自动去重）。等效于调用 set.__len__()
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> len(basket)
4

# len(dict)：返回字典中的元素个数（以逗号分隔，键值对数）。等效于调用 dict.__len__()
>>> tel={'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> len(tel)
3

>>> len(builtins.__dict__)
152
>>> len(str.__dict__)
68

```

### inspect.isbuiltin

通过 `inspect.isbuiltin(object)` 可判断 object 是否为内置函数：

```shell
inspect.isbuiltin(object)
Return true if the object is a built-in function or a bound built-in method.
```

示例如下：

```shell
>>> inspect.isbuiltin(print)
True
>>> inspect.isbuiltin(len)
True
>>> inspect.isbuiltin(hex)
True
>>> inspect.isbuiltin(str)
False
>>> inspect.isbuiltin(string)
False
```

## [CLASSES](https://docs.python.org/3/library/stdtypes.html#)

builtins 模块还提供了一些常用的基础类：

```shell

CLASSES
    object
        BaseException

        bytearray
        bytes
        classmethod
        complex
        dict
        enumerate
        filter
        float
        frozenset
        int
            bool
        list
        map
        memoryview
        property
        range
        reversed
        set
        slice
        staticmethod
        str
        super
        tuple
        type
        zip
```

> [How do I check whether a module is installed or not in Python?](https://askubuntu.com/questions/588390/how-do-i-check-whether-a-module-is-installed-or-not-in-python)  

> [How to Check if a List, Tuple or Dictionary is Empty in Python](https://www.pythoncentral.io/how-to-check-if-a-list-tuple-or-dictionary-is-empty-in-python/)  

### [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

> Textual data in Python is handled with **str** objects.

字符串类 str 是 python 最常用的类，用来处理文本数据。

字符串有三种定义方式：

- Single quotes: `'allows embedded "double" quotes'`  
- Double quotes: `"allows embedded 'single' quotes"`  
- Triple quoted: `'''Three single quotes''', """Three double quotes"""`  

> **Triple quoted** strings may span multiple lines - all associated whitespace will be included in the string literal.

其中单引号定义的字符串中可携带双引号；双引号定义的字符串中可携带单引号。  
若想以跨行模式定义长字符串，则可考虑使用三引号，支持换行书写。  

---

两个相邻的字符串字面量会自动连接：

```shell
>>> str1='Py' 'thon'
>>> str1
'Python'

>>> prefix='Py'
>>> prefix+'thon'
'Python'
```

---

当书写长字符串时，使用 `()` 定义多个字面量部分，换行时自动跨行续接，直到反括号结束：

```shell
# 小括号定义多个字面量拼接
>>> text=('Put several strings within parentheses '
... 'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'

# 三引号跨行书写长字符串
>>> text='''Put several strings within parentheses 
... to have them joined together.'''
>>> text
'Put several strings within parentheses \nto have them joined together.'
```

`str[subscripted_index]`：基于脚标索引访问指定位置的字符（位置对应长度为1的子串）。

> Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

`str[start:stop]`：访问索引区间为 `[start, stop)` 对应的子字符串。

> subscripted_index、start、stop 均可为负数，其中 -1 索引最后一个元素，依次类推。

### [Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

- [int](https://docs.python.org/3/library/functions.html#int)：整形  
- [float](https://docs.python.org/3/library/functions.html#float)：浮点型  
- [complex](https://docs.python.org/3/library/functions.html#complex)：复数  

### Binary Sequence Types

- [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) objects are immutable sequences of single bytes.  
- [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray) objects are a mutable counterpart to bytes objects.  

[String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#strings)  
[Bytes and Bytearray Operations](https://docs.python.org/3/library/stdtypes.html#bytes-methods)  

### [Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

#### [list](https://docs.python.org/3/library/stdtypes.html#list)（有序列表）

列表定义格式为：[e1, e2, e3, ...]  

> 其中 e 可以为基本类型或 tuple、list、set、dict 等复合类型

```shell
# [整形,字符串,元组,列表,集合,字典]
>>> list1=[1,'2',(3,4),[5,6],{7,8},{'a':9,'b':10}]
>>> len(list1)
6
```

针对标量数值类型，可使用比 list 更高效的 [array](https://docs.python.org/3/library/array.html) 类型（Efficient arrays of numeric values）。

> Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained.

#### [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)（元组）

> Tuples are immutable sequences, typically used to store collections of heterogeneous data.

元组定义格式为：(e1, e2, e3, ...)  

> 其中 e 可以为基本类型或 tuple、list、set、dict 等复合类型

```shell
# (整形,字符串,元组,列表,集合,字典)
>>> tuple1=(1,'2',(3,4),[5,6],{7,8},{'a':9,'b':10})
>>> len(tuple1)
6
```

内置函数 [enumerate()](https://docs.python.org/3/library/functions.html#enumerate) 产生的结果为 `list<tuple>`，每个列表元素为 `(index, value)` 二元组（2-tuples）。

```shell
>>> help(enumerate)

Help on class enumerate in module builtins:

class enumerate(object)
 |  enumerate(iterable[, start]) -> iterator for index, value of iterable
 |  
 |  Return an enumerate object.  iterable must be another object that supports iteration.  The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
```

以下为具体示例：

```shell
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
```

#### [range](https://docs.python.org/3/library/stdtypes.html#range)（区间范围）

> The arguments to the range constructor must be **integers** (either built-in `int` or any object that implements the `__index__` special method).

- class range(stop)  
- class range(start, stop[, step])  

定义前开后闭区间 start ≤ e ＜ stop，步进为 step。

> start 默认为0；step 默认为1。

```shell
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
```

`range(start,stop,step)` 可用 while 循环等效实现：

```shell
>>> start=0
>>> stop=30
>>> step=5

>>> r=range(start,stop,step)
>>> list(r)
[0, 5, 10, 15, 20, 25]

# range 的等效定义
>>> i=0
>>> v=0
>>> while True:
...     v = start+i*step
...     if v >= stop:
...         break
...     else:
...         print('v[%d] = %d' % (i, v))
...         i += 1
... 
v[0] = 0
v[1] = 5
v[2] = 10
v[3] = 15
v[4] = 20
v[5] = 25
```

典型应用是 stop 取 len(list)，基于索引循环遍历列表：

```shell
>>> for i in range(len(list1)):\
...     print(list1[i])
... 
1
2
(3, 4)
[5, 6]
{8, 7}
{'a': 9, 'b': 10}
```

### [Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

- set：无序集合  

> A **set** object is an *unordered* collection of distinct [hashable](https://docs.python.org/3/glossary.html#term-hashable) objects.

集合定义格式为：{e1, e2, e3, ...}  

> 其中 e 可以为基本类型或 tuple 类型

```shell
>>> set1={1,'2',(3,4)}
>>> len(set1)
3
```

set 中的元素必须提供 `__hash__()` 方法，为 hashable（has a hash value），否则报错 `TypeError: unhashable type:`

```shell
>>> set2={1,'2',(3,4),[5,6]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> set3={1,'2',(3,4),{7,8}}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> set4={1,'2',(3,4),{'a':9,'b':10}}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
```

更多容器相关的类型，可参考 [collections](https://docs.python.org/3/library/collections.html#module-collections)。

### [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

- dict：无序字典(键值对映射)  

> A mapping object maps **hashable** values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary.  
> A dictionary’s keys are almost arbitrary values. Values that are **not hashable**, that is, values containing lists, dictionaries or other mutable types may not be used as keys.  

- key 必须为 arbitrary（hashable），list、set、dict 等 unhashable 类型不能作为键；  
- value 可为 not hashable 或 hashable。  

```shell
>>> dict1[squares]=3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> dict1[3]=squares
>>> dict1
{3: [1, 4, 9, 16, 25]}
```