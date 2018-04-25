# print

在 Python 2 中，print 为关键字；在 Python 3 中，print 为内置函数（builtins.print）。

在 Python 3 中可执行 `help(print)` 查看 print 函数说明：

```shell
>>> help(print)

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
```

Python3 已经不支持 print 的非函数格式了，必须使用 `print()` 函数调用格式。

```shell
>>> print 'hello,world!'
  File "<stdin>", line 1
    print 'hello,world!'
                       ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello,world!')?
```

> [Python print函数用法](http://blog.csdn.net/zanfeng/article/details/52164124)  
> [python格式化输出](http://blog.csdn.net/wchoclate/article/details/42297173)  
> [python2与python3的print](https://blog.csdn.net/freestyle4568world/article/details/48369057)  

---

对很多应用程序来说，使用模块 logging 来写入日志比使用 print 更合适。

> 相关模块参考：syslog, logging。

## expr

`print(object)` 输出类型或描述信息。

```shell
#######################################
# 打印模块信息
#######################################
# python3
>>> print(builtins)
<module 'builtins' (built-in)>

>>> print(array)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'array' is not defined
>>> import array

# python2
>>> print(array)
<module 'array' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/array.so'>

# python3
>>> print(array)
<module 'array' from '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload/array.cpython-36m-darwin.so'>

#######################################
# 打印模块类型信息
#######################################

# python2
>>> print(list)
<type 'list'>

# python3
>>> print(list)
<class 'list'>

>>> print(len)
<built-in function len>

>>> print(hex)
<built-in function hex>

#######################################
# 打印对象实例描述（__repr__）
#######################################

>>> print(sys.version_info)
sys.version_info(major=3, minor=6, micro=5, releaselevel='final', serial=0)

>>> print(sys.thread_info)
sys.thread_info(name='pthread', lock='mutex+cond', version=None)
```

`print(var)` 或 `print(expr)` 打印变量或表达式的值。

```shell
>>> start=1
>>> stop=10
>>> step=2

>>> print(start)
1

>>> print(start+step)
3

>>> r=range(1,10,2)
# python2
>>> print(r)
[1, 3, 5, 7, 9]
# python3
>>> print(r)
range(1, 10, 2)

>>> l1=[1,2,3,4]
>>> print(l1)
[1, 2, 3, 4]

```

## list vars

逗号后直接接变量，Python 2 下输出 tuple；Python 3 将自动拼接前半句字面量和后面的变量，以空格（space-separated with `sep=' '`）隔开。

```shell
>>> start=0
>>> stop=30
>>> step=5

# python2 下的输出 tuple
>>> print('start is', start)
('start is', 0)
>>> print('start, stop is', start, stop)
('start, stop is', 0, 30)

# python3 下的输出
>>> print('start is', start)
start is 0
>>> print('start, stop is', start, stop)
start, stop is 0 30
```

## [printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)

C printf 风格，使用 `%` 格式符标识占位，

```shell
# start 可加括号
>>> print('start is %d' % start)
start is 0

>>> print('start,stop is %d, %d' % (start, stop))
start,stop is 0, 30

```

## format

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
从 Python 3.1 开始，占位序号也可以省略，`{} {}` 等效于 `{0} {1}`。  

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

```shell
>>> print('i love {you}'.format(you='python'))
i love python
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

Python 3.2 开始还提供了 **`format_map()`** 方法，支持传入字典作为参数键值对对模板进行实例化：

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

位置占位和关键字占位可混合使用：

```shell
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
```

### format specifier

An optional '`:`' and format specifier can follow the field name. This allows greater control over how the value is formatted.

1. 设置打印进制格式

```shell
>>> # format also supports binary numbers
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'

>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

```

Passing an integer after the '`:`' will cause that field to be a minimum number of characters wide. This is useful for making tables pretty.

2. 设置浮点数位数

```shell
>>> import math
>>> print('The value of PI is approximately {0:.3f}.'.format(math.pi))
The value of PI is approximately 3.142.

>>> '{0:6.2f}'.format(math.pi)
'  3.14'
>>> '{0:>6.2f}'.format(math.pi)
'  3.14'
>>> '{0:<6.2f}'.format(math.pi)
'3.14  '
```

3. 字符串截断输出

```shell
>>> 'i love %s' % 'python'
'i love python'
>>> 'i love %.2s' % 'python'
'i love py'

# 截取两位，总共三位，默认右对齐
>>> 'i love %3.2s' % 'python'
'i love  py'

# 截取两位，总共十位，默认右对齐
>>> 'i love %10.2s' % 'python'
'i love         py'

# 截取两位，总共十位，设置左对齐
>>> 'i love %-10.2s' % 'python'
'i love py        '

# 截取两位，总共十位，设置左对齐
>>> 'i love %-10.2s !' % 'python'
'i love py         !'
```

4. 设置输出宽度及填充格式

	> Aligning the text and specifying a width

```shell
# default align left, fill right with spaces
>>> '{:30}'.format('left aligned')
'left aligned                  '
>>> '{:<30}'.format('left aligned')
'left aligned                  '
>>> '{:>30}'.format('right aligned')
'                 right aligned'
>>> '{:^30}'.format('centered')
'           centered           '
>>> '{:*^30}'.format('centered')  # use '*' as a fill char
'***********centered***********'
>>> '{:-^30}'.format('centered')  # use '-' as a fill char
'-----------centered-----------'
```

```shell
# position:{width}{base}
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print('{0:10} ==> {1:10d}'.format(name, phone))
... 
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```
