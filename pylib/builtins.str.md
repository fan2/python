# [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

[str tutorial](https://docs.python.org/3.6/tutorial/introduction.html#strings)  

字符串类 str 是 python 最常用的类，用来处理文本数据。

## empty string

1. `s=str()`: 构造一个空字符串对象。  
2. `s=''`：定义空字符串字面量。  

## definition

字符串有三种定义方式：

- Single quotes: `'allows embedded "double" quotes'`  
- Double quotes: `"allows embedded 'single' quotes"`  
- Triple quoted: `'''Three single quotes''', """Three double quotes"""`  

> **Triple quoted** strings may span multiple lines - all associated whitespace will be included in the string literal.

其中单引号定义的字符串中可携带双引号；双引号定义的字符串中可携带单引号。  
若想以跨行模式定义长字符串，则可考虑使用三引号，支持换行书写。  

### 单引号

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

### 双引号

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

### 三引号

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

# 模板实例化
>>> data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
>>> print(template.format_map(data))
<html>
<head><title>My Home Page</title></head>
<body>
<h1>My Home Page</h1>
<p>Welcome to my home page!</p>
</body>
```

### 原始字符串

用前缀r表示原始字符串。原始字符串不会对反斜杠做特殊处理，而是让 字符串包含的每个字符都保持原样。

```shell
>>> print(r'C:\nowhere')
C:\nowhere
```

一个例外是，引号需要像通常那样进行转义，但这意味着用于执行转义的反斜杠也将包含 在最终的字符串中。

```shell
>>> print(r'Let\'s go!')
Let\'s go!
```

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

## misc.etc
模块 string 定义了一些字符类型集常量：

```shell
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
