
dir(builtins) 分类梳理一览

[Built-in Functions](https://docs.python.org/3/library/functions.html)

## id

builtins.dir  

builtins.id  
builtins.hash  
builtins.type  

builtins.isinstance  
builtins.issubclass  

## vars

builtins.vars  
builtins.locals  
builtins.globals  

argparse 解析参数 `args = argparser.parse_args()`，调用 print(args) 打印出来的是 Namespace：

```
Namespace(debug=False, logpath='logs/19.09.30.14-MBR.log', platform=1)
```

调用 print(vars(args)) 以字典形式打印 `object.__dict__`：

```
{'platform': 1, 'logpath': 'logs/19.09.30.14-MBR.log', 'debug': False}
```

## print

builtins.repr  
builtins.print  

交互输入：

builtins.input

## types

### None

builtins.None  
builtins.Ellipsis # 省略号  

### bool

builtins.bool  
builtins.False  
builtins.True  

builtins.any # 一组值中只要有一个为 True。

- bool(x) 传入数值 0 为 False，传入非 0 值为 True。  
- bool(x) 传入空对象 None 为 False，传入非空对象为 True。  

### Sequence Types

builtins.str - Text Sequence  

builtins.list # array  
builtins.tuple  
builtins.range  

builtins.slice  

### Mapping Types

builtins.dict  
builtins.map  

### Set Types

builtins.set  
builtins.frozenset  

### Binary Sequence Types

builtins.bytes  
builtins.bytearray  
builtins.memoryview  

## len & filter

builtins.len # 对字符串、列表等序列化数据集合求取长度（size）。

builtins.reversed  
builtins.filter  
builtins.sorted  

builtins.zip  

## enum & iter

### enumerate

builtins.enumerate  

help(enumerate) 查看相关帮助：

```
class enumerate(object)
 |  enumerate(iterable, start=0)
 |
 |  Return an enumerate object.
 |
 |    iterable
 |      an object supporting iteration
 |
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
```

枚举列表的索引与值。

对 enumerate 返回的对象转换为list，可知其内为 (index, value) 的 tuple 数组。

```
>>> l = [1,2,3,4]
>>> el = enumerate(l)
>>> list(el)
[(0, 1), (1, 2), (2, 3), (3, 4)]
```

for 循环遍历取 tuple 二维元素值：

```
>>> for i,e in enumerate(l):
...     print('l[%d] = %d' % (i, e))
...
l[0] = 1
l[1] = 2
l[2] = 3
l[3] = 4
```

### iter & next

builtins.iter  
builtins.next  

```
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit)) #StopIteration Exception!!!
```

## utilities

### string to value

字符串转换为整形、浮点型：

builtins.int  
builtins.float  

### value representation

打印数值的二进制、八进制、十六进制表示（字符串）：

binary/octal/hexadecimal representation：

builtins.bin  # binary string prefixed with “0b”  
builtins.oct  # octal string prefixed with “0o”  
builtins.hex  # lowercase hexadecimal string prefixed with “0x”  

[Python 数字系列-数字格式化输出](https://www.cnblogs.com/crawer-1/p/8241882.html)

#### [Integer literals](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals)

Python 下的整形字面量可以 `_` 串联，类似千位分隔符([thousands separator](https://en.wikipedia.org/wiki/Decimal_mark))：

```Python
>>> 100_000_000
100000000
```

311 的十六进制字面量写法为 0x137：

```Python
>>> hex(311)
'0x137'
>>> 0x137
311
```

311 的二进制字面量写法为 0b100110111：

```Python
>>> bin(311)
'0b100110111'
>>> 0b100110111
311
>>> 0b_100110111
311
>>> 0b_1_0011_0111
311
```

#### format()

builtins.format # help('FORMATTING')  

可参考 [builtins.format](https://docs.python.org/3/library/functions.html#format) 函数，可输入 `help('FORMATTING')` 查看字符串格式化相关议题。

format 函数将值类型按照指定格式转换为字符串表示：

```
format(value[, format_spec])

Convert a value to a “formatted” representation, as controlled by *format_spec*. 
```

The default `format_spec` is an empty string which usually gives the same effect as calling `str(value)`.

str(255) 将值字符串化为 '255'，hex(255) 将值字符串化为带 0x 前缀的十六进制表示 '0xff'。
除此之外，可以通过 format 函数指定更详细的表示格式，例如不带 0x 前缀、十六进制大小写等。

```
>>> '%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
>>> format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
>>> f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')
```

### ascii

builtins.ascii  
builtins.ord # 返回 Unicode 编码  
builtins.chr # 返回 Unicode 编码对应的字符  

`ord(c)`: Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.

```
>>> ord('a')
97
>>> ord('A')
65
```

`chr(i)`: Return the string representing a character whose Unicode code point is the integer i.

```
>>> chr(97)
'a'
>>> chr(65)
'A'
```

### math

builtins.min  
builtins.max  

builtins.abs # math.fabs  
builtins.sum # math.fsum  

builtins.round # 四舍五入保留指定浮点数  

#### floor & ceil

math.floor：向下取整  
math.ceil：向上取整  

```
>>> length = 4788224
>>> math.log(length, 1024)
2.2191059214531657
>>> math.floor(math.log(length, 1024))
2
>>> math.ceil(math.log(length, 1024))
3
```

#### divmod

builtins.divmod  

Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.

> divmod(a, b) 等效于 `(a // b, a % b)`，计算商（quotient）和余数（remainder）。

`math.fmod(x, y, /)`：求余，基本等效于 x % y = divmod(x,y)[1]。  

`math.modf(x, /)`: Return the fractional and integer parts of x，取浮点数的整数和小数部分。  

math.modf(math.pi) = (0.14159265358979312, 3.0)  
math.modf(-math.pi) = (-0.14159265358979312, -3.0)  

其他：math.remainder

#### pow & log

builtins.pow # math.pow：幂运算  

`math.sqrt`：Return the square root of x.  

`math.log(x, [base=math.e])`：Return the logarithm of x to the given base.  
`math.log10` = math.log(x, 10), 10^y=x  
`math.log2`  = math.log(x, 2), 2^y=x  

#### demo

[Better way to convert file sizes in Python](https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python)

https://pypi.org/project/hurry.filesize/

```py
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = math.floor(math.log(size_bytes, 1024))
   p = pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
```

math.log(size_bytes, 1024))：计算真数 size_bytes 以 1024 为底的对数。math.floor 向下取指数的整数部分。

> 如果指数是2，则对应数量单位为 p=pow(1024, 2)=1048576，表示单位为 MB。

将 size_bytes 除以 1048576 得到 MB 计量数量，然后 round 四舍五入取整，最后格式化打印出 `mm.nn MB`。

测试示例：

```
>>> length = 4788224
>>> convert_size(length)
'4.57 MB'
```

## open

builtins.open  

builtins.eval  
builtins.exec  

## warning/error

builtins.Warning  
builtins.UserWarning  

builtins.IndexError  
builtins.FileExistsError  
builtins.FileNotFoundError  

builtins.TypeError  
builtins.ValueError  

[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)  
[warnings — Warning control](https://docs.python.org/3/library/warnings.html?highlight=warning#module-warnings)  

## refs

[30段极简Python代码](http://www.raincent.com/content-85-14066-1.html)
