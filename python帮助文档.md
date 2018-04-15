## Docs

[Documentation](https://www.python.org/doc/) » [Python 3.x Docs](http://docs.python.org/3/)  

[Glossary](https://docs.python.org/3/glossary.html)  

[The Python Language Reference](https://docs.python.org/3/reference/index.html)  
[The Python Standard Library](https://docs.python.org/3/library/index.html)  
[The Python Tutorial](https://docs.python.org/3.6/tutorial/)  

[Python Developer’s Guide](https://devguide.python.org/)  

[查看python的模块和函数帮助文档方法](http://blog.csdn.net/u013810296/article/details/55509284)  

## `__doc__`

> python 中每个 module，每个 class，每个 def 都留有写 doc 的地方。

- `print(module.__doc__)`：查看模块概述。

```shell
>>> import builtins
>>> print(builtins.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.

>>> import array
# 同 help(array) 的 DESCRIPTION
>>> print(array.__doc__)
This module defines an object type which can efficiently represent
an array of basic values: characters, integers, floating point
numbers.  Arrays are sequence types and behave very much like lists,
except that the type of objects stored in them is constrained.
```

> 注意：先要 import module！

- `print(class.__doc__)`（或 `print(object.__doc__)`）：查看类说明。  

```shell
>>> print(str.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
```

- `print(class.method.__doc__)`（或 `print(object.method.__doc__)`）：查看类成员函数说明。  

```shell
>>> print(str.format.__doc__)
S.format(*args, **kwargs) -> str

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').
```

## help

```shell
>>> help
Type help() for interactive help, or help(object) for help about object.
```

### help(object)

调用 `import(module)` 导入模块后，可调用 `help(module)` 查看模块帮助：

1. 调用  `help(module.function)` 查看静态函数 function 帮助。  
2. 调用  `help(module.class)` 查看类 class 帮助。  
3. 调用  `help(module.class.method)` 查看类成员函数 function 帮助。  

对于内置的 builtins 模块，以上三步可省掉 module 前缀：

```shell
# 查看 builtins 内建的 print 函数帮助
>>> help(print)

Help on built-in function print in module builtins:

# 查看 builtins 内建的 len 函数帮助
>>> help(len)

Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

# 查看 builtins 内建的 str 类帮助
>>> help(str)

Help on class str in module builtins:

# 查看 builtins 内建的 int 类帮助
>>> help(int)

Help on class int in module builtins:

class int(object)

# 查看 builtins 内建的 list 类帮助
>>> help(list)

Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  

# 查看 builtins 内建的 set 类帮助
>>> help(set)

Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.

# 查看 builtins 内建的 set 类帮助
>>> help(dict)

Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
```

但是想调用 `help(module)` 查看 builtins 模块或其他模块帮助及说明，还得先显式 import，否则报错。  

```shell
>>> help(builtins)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'builtins' is not defined

>>> help(array)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'array' is not defined
```

#### quit

> `help(object)` 以 less/vi 模式打开帮助 manual page，底行输入 `q` 即可退出返回控制台。  
> 输入 `h` 可查看 less 命令帮助；输入 `?pattern` 或 `/pattern` 可执行前向/后向搜索。  

### help()

在 python 控制台中输入 `help()` 可打开交互式帮助系统（help utility）。

```shell
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 

```

从中我们可以获取到 Python 官方教程（The Python Tutorial）的网址为 <https://docs.python.org/3.6/tutorial/> 。

光标停留在 `help> ` 之后，可以输入 any module（name）、keywords 或 topics 查看模块、关键字、话题等相关帮助主题。

- `modules`：列出所有已安装模块  
- `keywords`：列出语言内置关键字  
- `symbols`：列出语言内置符号  
- `topics`：列出相关帮助主题  

#### keywords

输入 `keywords` 可以列出 Python 语言的内置关键字：

```shell
help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not                 
class               from                or                  
continue            global              pass                
```

#### symbols

输入 `symbols` 可以列出 Python 语言的内置符号：

```shell
help> symbols

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  *=                  <<                  ^
"                   +                   <<=                 ^=
"""                 +=                  <=                  _
%                   ,                   <>                  __
%=                  -                   ==                  `
&                   -=                  >                   b"
&=                  .                   >=                  b'
'                   ...                 >>                  j
'''                 /                   >>=                 r"
(                   //                  @                   r'
)                   //=                 J                   |
*                   /=                  [                   |=
**                  :                   \                   ~
**=                 <                   ]                   
```

#### [modules](https://docs.python.org/3.6/tutorial/modules.html)

输入 `modules` 可以列出当前所有已安装的模块：

```Shell
help> modules

Please wait a moment while I gather a list of all available modules...
```

除此之外，还可以调用 `modules time` 查看所有名称或概要信息中包含 time 的模块。

```shell
help> modules time

Here is a list of modules whose name or summary contains 'time'.
If there are any, enter a module name to get more help.

time - This module provides various functions to manipulate time values.
_strptime - Strptime-related classes and functions.
datetime - Concrete date/time and related types.
test.ann_module3 - Correct syntax for variable annotation that should fail at runtime
test.datetimetester - Test date/time type.
test.test_datetime 
test.test_strftime - Unittest for time.strftime
test.test_strptime - PyUnit testing against strptime
test.test_time 
test.test_timeit 
test.test_timeout - Unit tests for socket timeout feature.
test.time_hashlib 
timeit - Tool for measuring execution time of small code snippets.
_datetime 
pip._vendor.urllib3.util.timeout 

```

> 在处理某一特定领域问题，想要看看现有的模块库支持时，基于关键字进行模糊匹配相当实用。

##### src

[How do I find the location of Python module sources?](https://stackoverflow.com/questions/269795/how-do-i-find-the-location-of-python-module-sources)

在终端执行 python(3) 启动时，可携带 `-v` 选项，将输出详细的模块加载信息：

```shell
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
```

另外，也可以打印查看模块的 `__file__` 属性。

```shell
# builtins 模块未定义该属性
>>> import builtins
>>> builtins.__file__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'builtins' has no attribute '__file__'

# array 模块对应 cpython 实现动态库
>>> import array
>>> array.__file__
'/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload/array.cpython-36m-darwin.so'

# datetime 模块对应的 python 实现源码
>>> import datetime
>>> datetime.__file__
'/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/datetime.py'
```

#### quit

通过快捷键 `<C-c>` / `<C-d>` 或 `quit` 可退出 help utility 命令行 `help> ` 回到 Python 主控制台 `>>> `。

```shell
help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
```

`help>` 输入 `module`（无需先 imprt）, `module.function`, `module.class`, `module.class.method` 可查看相关帮助。

退回到 `>>>` 中输入`help(module)`、`help(module.function)`、`help(module.class)`、`help(module.class.method)` 可查看等效帮助。  

## [dir()](https://docs.python.org/3/library/functions.html#dir)

The built-in function [dir()](https://docs.python.org/3.6/tutorial/modules.html#the-dir-function) is used to find out which names a module defines. It returns a sorted list of strings:

> Note that it lists all types of names: variables, modules, functions, etc.  
> [dir()](https://docs.python.org/3.6/library/functions.html#dir) does not list the names of built-in functions and variables.  

内置模块 builtins 提供的 `dir()` 方法用于列举类或实例的属性方法。

可导入 builtins 模块，然后调用 `help(builtins.dir)` 查看帮助：

```
>>> import builtins
>>> help(builtins.dir)
```

由于 builtins 模块已经内置到解释器，因此对于其中的类或函数，可省去 import，直接调用 help 或访问其 `__doc__` 查看 `dir()` 函数的说明。

```shell
# 也可执行 print(dir.__doc__) 查看概要

>>> help(dir)

Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.
```

例如执行 `dir(builtins)` 可查看模块 builtins 提供的所有属性及方法：

```shell
>>> import builtins
>>> dir(builtins)
```

	> 也可执行 `print(builtins.__dict__)` 打印 builtins 模块的符号表。

## direct input

在 python 主控制台中直接输入 `module`、`module.function`、` module.class`、` module.class.method` 也会显示其类型信息：

```
>>> builtins
<module 'builtins' (built-in)>

>>> builtins.print
<built-in function print>

>>> builtins.str
<class 'str'>

>>> builtins.str.format
<method 'format' of 'str' objects>

>>> array
<module 'array' from '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload/array.cpython-36m-darwin.so'>
```

## autocompletion

在 python3 控制台中，对于明确类型的对象，输入引用符点号（`.`）后，再按下 tab 会列举所有可能的成员函数或属性：

```shell
>>> str1='hello'
>>> str1.
str1.capitalize(    str1.isalnum(       str1.join(          str1.rsplit(
str1.casefold(      str1.isalpha(       str1.ljust(         str1.rstrip(
str1.center(        str1.isdecimal(     str1.lower(         str1.split(
str1.count(         str1.isdigit(       str1.lstrip(        str1.splitlines(
str1.encode(        str1.isidentifier(  str1.maketrans(     str1.startswith(
str1.endswith(      str1.islower(       str1.partition(     str1.strip(
str1.expandtabs(    str1.isnumeric(     str1.replace(       str1.swapcase(
str1.find(          str1.isprintable(   str1.rfind(         str1.title(
str1.format(        str1.isspace(       str1.rindex(        str1.translate(
str1.format_map(    str1.istitle(       str1.rjust(         str1.upper(
str1.index(         str1.isupper(       str1.rpartition(    str1.zfill(
```

借此特性，在编码过程中，可一览某一类别实例的可用属性、方法。

对于 Sublime Text 等文本编辑器，需要借助 [Anaconda](https://www.anaconda.com/) 或 [SublimeLinter-pycodestyle](https://github.com/SublimeLinter/SublimeLinter-pycodestyle) 等插件来实现自动完成智能提示。
