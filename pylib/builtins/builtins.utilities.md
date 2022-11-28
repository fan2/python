
[Built-in Functions](https://docs.python.org/3/library/functions.html)

## len

```Shell
    len(obj, /)
        Return the number of items in a container.
```

对于字符串（str）、数组（array）、列表（list）、元组（tuple）、集合（set）、字典（dict）等常用序列或集合，均可调用 len 取其大小（本质上是调用类的 `__len__()` 方法）。

```Shell
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


## ascii

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

## str to int

字符串转换为整形、浮点型：

```Shell
>>> help(int)

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer

```

[Python 数字系列-数字格式化输出](https://www.cnblogs.com/crawer-1/p/8241882.html)

将字符串转换为整形：

```Shell
>>> int('32')
32
```

将字符串按base指定的进制转换为整形：

```Shell
# 输出16进制0x32的十进制值：
>>> int('32', base=16)
50
>>> int('0x32', base=16)
50
# 输出2进制0b1011的十进制值：
>>> int('1011', base=2)
11
>>> int('0b1011', base=2)
11
```

## Integer literals

[Integer literals](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals)

Python 下的整形字面量可以 `_` 串联，类似千位分隔符([thousands separator](https://en.wikipedia.org/wiki/Decimal_mark))：

```Shell
>>> 100_000_000
100000000
```

Using the comma as a thousands separator:

```Shell
>>> '{:,}'.format(1234567890)
'1,234,567,890'
>>> '{:,}'.format(100000000)
'100,000,000'
>>> '{:_}'.format(100000000)
'100_000_000'
```

311 的二进制字面量写法为 0b100110111：

```Shell
>>> bin(311)
'0b100110111'
>>> 0b100110111
311
>>> 0b_100110111
311
>>> 0b_1_0011_0111
311
```

## DecHexBin

### print format

通过 `print()` 函数的占位符 `%o`、`%x` 格式化输出十进制数对应的八进制和十六进制格式：

```Shell
>>> x=2017
>>> print('oct=%o' %(x))
oct=3741
>>> print('hex=%x' %(2017))
hex=7e1
```

基于 str.format 设置打印进制格式：

```Shell
>>> # format also supports binary numbers
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'

>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

```

### bin(), hex()

value representation：打印数值的二进制、八进制、十六进制表示（字符串）：

binary/octal/hexadecimal representation：

builtins.bin  # binary string prefixed with “0b”  
builtins.oct  # octal string prefixed with “0o”  
builtins.hex  # lowercase hexadecimal string prefixed with “0x”  

```Shell
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

311 的十六进制字面量写法为 0x137：

```Python
>>> hex(311)
'0x137'
>>> 0x137
311
```

### bit_length

int 模块，还提供了 `bit_length` 可获取某个整数的二进制位数：

```Shell
class int(object)

 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
```

```Shell
>>> bin(37)
'0b100101'
>>> (37).bit_length()
6
```

53191的十六进制是0xcfc7，占用2Byte的unsigned short类型即可存储。

```Shell
>>> hex(53191)
'0xcfc7'
>>> (53191).bit_length()
16
```

### Bitwise Operations

[Bitwise Operations on Integer Types](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)

## math

builtins.min  
builtins.max  

builtins.abs # math.fabs  
builtins.sum # math.fsum  

builtins.round # 四舍五入保留指定浮点数  

### floor & ceil

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

### divmod

builtins.divmod  

Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.

> divmod(a, b) 等效于 `(a // b, a % b)`，计算商（quotient）和余数（remainder）。

`math.fmod(x, y, /)`：求余，基本等效于 x % y = divmod(x,y)[1]。  

`math.modf(x, /)`: Return the fractional and integer parts of x，取浮点数的整数和小数部分。  

math.modf(math.pi) = (0.14159265358979312, 3.0)  
math.modf(-math.pi) = (-0.14159265358979312, -3.0)  

其他：math.remainder

### pow & log

builtins.pow # math.pow：幂运算  

`math.sqrt`：Return the square root of x.  

`math.log(x, [base=math.e])`：Return the logarithm of x to the given base.  
`math.log10` = math.log(x, 10), 10^y=x  
`math.log2`  = math.log(x, 2), 2^y=x  

### demo

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