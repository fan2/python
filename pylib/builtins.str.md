# [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

[str](https://docs.python.org/3/library/stdtypes.html#str)  
[str tutorial](https://docs.python.org/3.6/tutorial/introduction.html#strings)  

字符串类 str 是 python 最常用的类，用来处理字符序列和文本数据。

## empty string

1. `s=str()`: 构造一个空字符串对象。  
2. `s=''`：定义空字符串字面量。  

## Literals

参考 reference - [2.4. Literals](https://docs.python.org/3/reference/lexical_analysis.html#literals) - String and Bytes literals。

One syntactic restriction not indicated by these productions is that whitespace is not allowed between the `stringprefix` or `bytesprefix` and the rest of the literal.

String literals are described by the following lexical definitions:

```
stringliteral   ::=  [stringprefix](shortstring | longstring)
stringprefix    ::=  "r" | "u" | "R" | "U" | "f" | "F"
                     | "fr" | "Fr" | "fR" | "FR" | "rf" | "rF" | "Rf" | "RF"
```

Bytes literals are described by the following lexical definitions:

```
bytesliteral   ::=  bytesprefix(shortbytes | longbytes)
bytesprefix    ::=  "b" | "B" | "br" | "Br" | "bR" | "BR" | "rb" | "rB" | "Rb" | "RB"
```

### 原始字符串

Both string and bytes literals may optionally be prefixed with a letter `'r'` or `'R'`; such strings are called *raw* strings and treat backslashes as literal characters. As a result, in string literals, `'\U'` and `'\u'` escapes in raw strings are not treated specially.

用前缀r表示原始字符串。原始字符串不会对反斜杠做特殊处理，而是让字符串包含的每个字符都保持原样。

```shell
>>> print(r'C:\nowhere')
C:\nowhere
```

一个例外是，引号需要像通常那样进行转义，但这意味着用于执行转义的反斜杠也将包含在最终的字符串中。

```shell
>>> print(r'Let\'s go!')
Let\'s go!
```

### str

字符串有三种定义方式：

- Single quotes: `'allows embedded "double" quotes'`  
- Double quotes: `"allows embedded 'single' quotes"`  
- Triple quoted: `'''Three single quotes''', """Three double quotes"""`  

> **Triple quoted** strings may span multiple lines - all associated whitespace will be included in the string literal.

其中单引号定义的字符串中可携带双引号；双引号定义的字符串中可携带单引号。  
若想以跨行模式定义长字符串，则可考虑使用三引号，支持换行书写。  

#### 单引号

单引号定义的字符串中可包含双引号：

```shell
>>> 'allows embedded "double" quotes'
'allows embedded "double" quotes'

>>> '"Hello, world!" she said'
'"Hello, world!" she said'
```

单引号定义的字符串中不能包含撇号，否则解释器报错：

```shell
>>> 'Let's go!'
  File "<stdin>", line 1
    'Let's go!'
         ^
SyntaxError: invalid syntax
```

> 在这里，字符串为 'Let'，因此 Python 不知道如何处理 s 后面的内容。

可使用反斜杠（\\）对引号进行转义，示意中间的引号是字符串的一部分，而非字符串结束标志。

```
>>> 'Let\'s go!'
"Let's go!"
```

#### 双引号

双引号定义的字符串中可包含单引号：

```shell
>>> "allows embedded 'single' quotes"
"allows embedded 'single' quotes"

>>> "Let's go!"
"Let's go!"
```

双引号定义的字符串中不能包含双引号，否则解释器报错：

```shell
>>> ""Hello, world!" she said"
  File "<stdin>", line 1
    ""Hello, world!" she said"
          ^
SyntaxError: invalid syntax
```

此时，使用反斜杠（\\）对字符串中的双引号进行转义，示意中间的双引号为原义。

```shell
>>> "\"Hello, world!\" she said"
'"Hello, world!" she said'
```

#### 三引号

可使用三引号（三个单引号或三个双引号）来表示很长的字符串：

```shell
>>> '''Three single quotes''', """Three double quotes"""
('Three single quotes', 'Three double quotes')
```

三引号中可包含单引号和双引号：

```shell
>>> str1 = ''''single' quotes and "double" quotes in Three single quotes'''
# 相当于 print(repr(str1))
>>> str1
'\'single\' quotes and "double" quotes in Three single quotes'
# 相当于 print(str(str1))
>>> print(str1)
'single' quotes and "double" quotes in Three single quotes

# 注意中间包含撇号还是要转义！
>>> str2='''Let\'s say "Hello, world!"'''
# 相当于 print(repr(str2))
>>> str2
'Let\'s say "Hello, world!"'
# 相当于 print(str(str2))
>>> print(str2)
Let's say "Hello, world!"
```

### [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)

Only ASCII characters are permitted in bytes literals (regardless of the declared source code encoding).  
Any binary values over 127 must be entered into bytes literals using the appropriate escape sequence.

Bytes literals are always prefixed with `'b'` or `'B'`; they produce an instance of the `bytes` type instead of the `str` type.  
They may only contain ASCII characters; bytes with a numeric value of 128 or greater must be expressed with escapes.

```
>>> bs = b'ABC'
>>> type(bs)
<class 'bytes'>

>>> bs
b'ABC'
>>> bs[0]
65
>>> bs[1]
66
>>> bs[2]
67
```

Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal numbers are a commonly used format for describing binary data. Accordingly, the bytes type has an additional class method to read data in that format:

```
classmethod fromhex(string)
    This bytes class method returns a bytes object, decoding the given string object.  
    The string must contain two hexadecimal digits per byte, with ASCII whitespace being ignored.
```

```Python
>>> dot = b'\x2E'
>>> dot
b'.'

>>> bytes.fromhex('2Ef0 F1f2  ')
b'.\xf0\xf1\xf2'
```

其中 ASCII 字符 `.` 的编码为 0x2E(46)：

```
>>> chr(0x2E)
'.'
>>> int('2E', 16)
46
>>> ord('.')
46
>>> hex(46)
'0x2e'
```

A **reverse** conversion function exists to transform a bytes object into its hexadecimal representation.

```
hex()
    Return a string object containing two hexadecimal digits for each byte in the instance.
```

```
>>> b'\xf0\xf1\xf2'.hex()
'f0f1f2'

>>> bs.hex()
'414243'
```

## expressions

- `len(s)`: Return the length of str(number of single character).  
- `c in s`: Test x for membership in s.  
- `c not in s`: Test x for non-membership in s.  
- `for c in s`: enumerate substring(character)  in s.  

## sequential access

access through subscripted index

```shell
>>> word = 'Python'
```

顺序索引访问（从0开始）：

```
>>> #第一个字符
... word[0]
'P'

>>> #最后一个字符
... word[len(word)-1]
'n'
>>> word[5]
'n'
```

负数倒序索引访问（从-1开始）：

```
>>> #倒数第一个字符
... word[-1]
'n'

>>> #倒数第二个字符
... word[-2]
'o'

>>> #倒数第六个字符
... word[-6]
'P'
```

区间索引访问：

```
>>> word[0:2]
'Py'
>>> word[2:5]
'tho'
```

不指定起始索引，默认的起始索引为句首（0）:

```
>>> word[:2]
'Py'
```

不指定起始索引，默认的起始索引至末尾（len(s)-1,-1）:

```>>> word[2:]
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

## repr

```
>>> help(repr)

Help on built-in function repr in module builtins:

repr(obj, /)
    Return the canonical string representation of the object.
    
    For many object types, including most builtins, eval(repr(obj)) == obj.
```

repr 实际上调用的是 obj 的 `__repr__` 方法，获取该对象实例的描述信息。

`repr(obj) = obj.__repr__()`

## str.format

- reference - [2.4.3. Formatted string literals](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings) - New in version 3.6.  
- tutorial - [7.1. Fancier Output Formatting](https://docs.python.org/3.6/tutorial/inputoutput.html#fancier-output-formatting)  
- library - [str.format](https://docs.python.org/3/library/stdtypes.html#str.format)  
- library - [**6.1.3. Format String Syntax**](https://docs.python.org/3/library/string.html#formatstrings)  

The [string](https://docs.python.org/3.6/library/string.html#module-string) module contains a [Template](https://docs.python.org/3.6/library/string.html#string.Template) class which offers yet another way to **substitute** values into strings.

函数原型：str.**format**(\**args*, \*\**kwargs*)

```
Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument.
```

`format()` 函数把字符串当成一个模板，通过传入的参数进行格式化，并使用大括号 `{}` 作为特殊字符代替 % 占位格式符。

### positional argument

大括号中可指定参数索引（the numeric index of a positional argument）。  
从 Python 3.1 开始，占位序号也可以省略，`{} {}` 自动编号为 `{0} {1}`。  

Accessing arguments by position:

```shell
>>> print('{0} {1}'.format('hello','world'))
hello world
>>> print('{} {}'.format('hello','world'))
hello world
>>> print('{0} {1} {0}'.format('hello','world'))
hello world hello
```

### keyword argument

大括号中也可指定占位替换变量（the name of a keyword argument）。  

Accessing arguments by name:

```shell
>>> print('i love {you}'.format(you='python'))
i love python
>>>
>>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'
>>> 
>>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
>>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
'Coordinates: 37.24N, -115.81W'
```

位置占位和关键字占位可混合使用：

```shell
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
```

### demo

以下示例利用三引号跨行定义一个 HTML 模板：

```shell
>>> template='''<html>
... <head><title>{title}</title></head>
... <body>
... <h1>{title}</h1>
... <p>{text}</p>
... </body>'''

>>> template
'<html>\n<head><title>{title}</title></head>\n<body>\n<h1>{title}</h1>\n<p>{text}</p>\n</body>'

>>> print(template)
<html>
<head><title>{title}</title></head>
<body>
<h1>{title}</h1>
<p>{text}</p>
</body>
```

通过 format 传参替换占位变量对模板进行实例化：

```shell
>>> print(template.format(title='My Home Page', text='Welcome to my home page!'))
<html>
... <head><title>My Home Page</title></head>
... <body>
... <h1>My Home Page</h1>
... <p>Welcome to my home page!</p>
... </body>
```

Python 3.2 开始还提供了 str.**format_map()** 方法，支持传入字典作为参数键值对对模板进行实例化：

```shell
>>> data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
>>> print(template.format_map(data))
<html>
<head><title>My Home Page</title></head>
<body>
<h1>My Home Page</h1>
<p>Welcome to my home page!</p>
</body>
```

## [Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

A string literal with `'f'` or `'F'` in its prefix is a *formatted string literal*; see Formatted string literals.  
The `'f'` may be combined with `'r'`, but not with `'b'` or `'u'`, therefore raw formatted strings are possible, but formatted bytes literals are not.

```Python
>>> year = 2019
>>> f'year is {year!s}'
'year is 2019'

>>> number = 1024
>>> f"{number:#0x}"
'0x400'

>>> today = datetime.datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}"
'January 27, 2017'
```

## [string](https://docs.python.org/3/library/string.html)

模块 `string` 定义了一些字符类型集常量：

```shell
# 或直接输入 help('string')
>>> import string
>>> print(string.__doc__)
A collection of string constants.

Public module variables:

whitespace -- a string containing all ASCII whitespace
ascii_lowercase -- a string containing all ASCII lowercase letters
ascii_uppercase -- a string containing all ASCII uppercase letters
ascii_letters -- a string containing all ASCII letters
digits -- a string containing all ASCII decimal digits
hexdigits -- a string containing all ASCII hexadecimal digits
octdigits -- a string containing all ASCII octal digits
punctuation -- a string containing all ASCII punctuation characters
printable -- a string containing all ASCII characters considered printable

```

```shell
>>> string.digits
'0123456789'
>>> '5' in string.digits
True

>>> string.hexdigits
'0123456789abcdefABCDEF'
>>> 'f' in string.hexdigits
True
```

### Formatter

Custom String Formatting

The built-in string class provides the ability to do complex variable substitutions and value formatting via the [format()](https://docs.python.org/3/library/stdtypes.html#str.format) method described in [PEP 3101](https://www.python.org/dev/peps/pep-3101).  
The Formatter class in the string module allows you to create and **customize** your own string formatting behaviors using the same implementation as the built-in `format()` method.

```
class string.Formatter
The Formatter class has the following public methods:

format(format_string, *args, **kwargs)
    The primary API method. It takes a format string and an arbitrary set of positional and keyword arguments. It is just a wrapper that calls vformat().

vformat(format_string, args, kwargs)
    This function does the actual work of formatting. It is exposed as a separate function for cases where you want to pass in a predefined dictionary of arguments, rather than unpacking and repacking the dictionary as individual arguments using the *args and **kwargs syntax.
```

### Template

```
CLASSES
    builtins.object
        Formatter
        Template
```

The [string](https://docs.python.org/3/library/string.html#module-string) module provides a [Template](https://docs.python.org/3/library/string.html#string.Template) class that implements these rules. The methods of [Template](https://docs.python.org/3/library/string.html#string.Template) are:

*class* string.**Template**(*template*)

> The constructor takes a single argument which is the template string.

```shell
>>> from string import Template
>>> s = Template('$who likes $what')
>>> s.substitute(who='tim', what='kung pao')
'tim likes kung pao'
```

[TDW](http://code.tencent.com/tdw.html)（[腾讯的分布式数据仓库](https://blog.csdn.net/johnny_lee/article/details/26673829/)）  [HIVE SQL](http://data.qq.com/article?id=819) 使用了 python 作为流程控制语言，以下摘自某段格式化查询脚本：

```python
# 模板
sql_query_t = 'SELECT * FROM ${db}::${tbl} WHERE time=${date}'
# 格式化替换参数
sql_query = string.Template(sql_query_t).substitute(db='myDB', tbl='myTable', date='20180108')
# 执行 sql
tdwqe.execute(sql_query)
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
