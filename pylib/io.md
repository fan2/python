
[open](https://docs.python.org/3/library/functions.html#open)  

[io — Core tools for working with streams](https://docs.python.org/3/library/io.html)

[7.2. Reading and Writing Files](https://docs.python.org/3.7/tutorial/inputoutput.html#reading-and-writing-files)

## help

要打开文件，可使用内置的函数 `open`，它实际位于自动导入的模块io中。
相当于 builtins 模块中执行了 `from io import open`。

```Shell
>>> help(open)

Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
```

也可以先导入 io 模块（`import io`），再 help(io) 或 help(io.open) 查看完整帮助。

```Shell
>>> import io
>>> help(io.open)
```

`open`() returns a file object, and is most commonly used with two positional arguments and one keyword argument:

> open(filename, mode, encoding=None)

## open

The first argument `file` is a string containing the filename.

函数 open 将文件名作为唯一必不可少的参数，并返回一个文件对象。
如果当前目录中有一个名为somefile.txt的文本文件（可能是使用文本编辑器创建的），则可像下面这样打开它：

>>> f = open('somefile.txt')

如果文件位于其他地方，可指定相对路径或完整的绝对路径。

```
>>> fp = open('test.py')
>>> # io manipulation
>>> fp.close()
```

最终文件不用时，需要显式调用 fp.`close`() 关闭文件。

### mode

The second argument `mode` is another string containing a few characters describing the way in which the file will be used.

The mode argument is optional; `'r'` will be assumed if it’s omitted.

```Shell
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
```

Normally, files are opened in text mode(`'t'`), that means, you read and write strings from and to the file, which are encoded in a specific encoding.

> 默认 mode='r'，即以只读、文本模式(`rt`)打开文件。

In text mode (the default, or when 't' is included in the mode argument), the contents of the file are returned as `str`, the bytes having been first *decoded* using a platform-dependent encoding or using the specified encoding if given.

Appending a `'b'` to the mode opens the file in binary mode. Binary mode data is read and written as bytes objects. You can not specify encoding when opening file in binary mode.

Files opened in binary mode (including 'b' in the mode argument) return contents as [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) objects without any decoding.

---

`mode`: Must have exactly one of create/read/write/append mode and at most one plus

1. 选定打开模式：`t` 和 `b` 二选一，以文本形式或二进制形式打开文件。
2. 选定读写模式：`r`、`x`、`w`、`a` 四选一，分别是 read/create/write/append，第一种为读，后三种都是写。
3. 最多可以包含一个加号：`+`。

模式位组合示例：

1. 如果打开的是 `tr`/`br`，如果还想写，可以追加一个加号：`tr+`/`br+`。
2. 如果打开的是 `ta`/`ba`，如果还想读，可以追加一个加号：`ta+`/`ba+`。

### with open

以下代码片段演示了打开文件（open），然后进行处理（manipulation），最后关闭文件（close）的流程。

无论 try 主处理模块中有无异常抛出，最终都会进入 finally 释放文件句柄资源。

```Python
debug = True
file = None # io.TextIOWrapper
shebang = ''

try:
    file = open('nosuchfile.md')
    shebang = file.readline()
    print(shebang)
    # manipulation
except Exception as exc:
    if (debug):
        print(exc)
        print(shebang)
    else:
        print('A exception flew by!')
        raise
finally:
    print('finally')
    if file:
        file.close()
```

It is good practice to use the `with` keyword when dealing with file objects.  
The advantage is that the file is properly **closed** after its suite finishes, even if an exception is raised at some point.  
Using with is also much shorter than writing equivalent `try-finally` blocks.  

建议采用 with...as 语句：`with open('test.py') as fp:`。

因为 with 区块销毁时会自动执行清理动作，从而无需显式调用 close。
即使读写文件中途遇到异常，也能安全回收文件资源。
另外，相比 try-finally 区块，可以简化代码。

If you’re not using the `with` keyword, then you should call f.`close`() to close the file and immediately free up any system resources used by it.

Warning Calling f.`write`() without using the `with` keyword or calling f.`close`() might result in the arguments of f.`write`() not being completely written to the disk, even if the program exits successfully.

### os.path

参考 [sysos](./sysos.md)，对于给定路径字符串，在尝试调用 open 之前，可调用 os.path 先行判断文件的存在性和相关属性。

1. 判断给定字符串是否为目录：os.path.isdir(path)
2. 判断给定字符串是否为文件：os.path.isfile(path)
3. 判断给定字符串（目录或文件）是否存在：os.path.exists(path)
4. 获取路径目录和文件部分：os.path.dirname, os.path.basename
5. 分离或组合路径字符串：os.path.split(drive, ext)，os.path.join

## Class hierarchy

可以 import io，然后执行 `help(io)` 一览 io 模块，涉及到的类如下：

```Shell
>>> help(io)

CLASSES
    _io._BufferedIOBase(_io._IOBase)
        _io.BufferedRWPair
        _io.BufferedRandom
        _io.BufferedReader
        _io.BufferedWriter
        _io.BytesIO
        BufferedIOBase(_io._BufferedIOBase, IOBase)
    _io._IOBase(builtins.object)
        IOBase
            BufferedIOBase(_io._BufferedIOBase, IOBase)
            RawIOBase(_io._RawIOBase, IOBase)
            TextIOBase(_io._TextIOBase, IOBase)
    _io._RawIOBase(_io._IOBase)
        _io.FileIO
        RawIOBase(_io._RawIOBase, IOBase)
    _io._TextIOBase(_io._IOBase)
        _io.StringIO
        _io.TextIOWrapper
        TextIOBase(_io._TextIOBase, IOBase)
```

在控制台 REPL 中，借助帮助 tab 自动补全，可以看看 io 模块向外提供的接口：

```Shell
>>> help(io.
io.abc                        io.DEFAULT_BUFFER_SIZE        io.SEEK_END
io.BlockingIOError(           io.FileIO(                    io.SEEK_SET
io.BufferedIOBase()           io.IncrementalNewlineDecoder( io.StringIO(
io.BufferedRandom(            io.IOBase()                   io.text_encoding(
io.BufferedReader(            io.open(                      io.TextIOBase()
io.BufferedRWPair(            io.open_code(                 io.TextIOWrapper(
io.BufferedWriter(            io.RawIOBase()                io.UnsupportedOperation(
io.BytesIO(                   io.SEEK_CUR
```

IOBase 为基类，BufferedIOBase 为二进制处理基类，TextIOBase 为文本处理基类。

1. 二进制相关处理：BufferedReader/BufferedWriter 和 BytesIO
2. 文件处理相关：FileIO
3. 文本相关处理：TextIOWrapper

- [io.IOBase](https://docs.python.org/3/library/io.html?highlight=textiowrapper#io.IOBase)  
- [io.TextIOBase](https://docs.python.org/3/library/io.html?highlight=textiowrapper#io.TextIOBase)  
- [io.TextIOWrapper](https://docs.python.org/3/library/io.html?highlight=textiowrapper#io.TextIOWrapper)  

执行 `type(fp)` 可以查看打开的文件句柄是 TextIOWrapper 对象：

```Shell
>>> type(fp)
<class '_io.TextIOWrapper'>

>>> isinstance(f, io.TextIOWrapper)
True
```

执行 `help(io.TextIOWrapper)` 查看文件句柄对象相关帮助。

```Shell
 |  Method resolution order:
 |      TextIOWrapper
 |      _TextIOBase
 |      _IOBase
 |      builtins.object
```

借助帮助 tab 自动补全，查看 TextIOWrapper 类向外提供的接口：

```Shell
>>> help(io.TextIOWrapper.
io.TextIOWrapper.buffer         io.TextIOWrapper.line_buffering io.TextIOWrapper.seek(
io.TextIOWrapper.close(         io.TextIOWrapper.mro()          io.TextIOWrapper.seekable(
io.TextIOWrapper.closed         io.TextIOWrapper.name           io.TextIOWrapper.tell(
io.TextIOWrapper.detach(        io.TextIOWrapper.newlines       io.TextIOWrapper.truncate(
io.TextIOWrapper.encoding       io.TextIOWrapper.read(          io.TextIOWrapper.writable(
io.TextIOWrapper.errors         io.TextIOWrapper.readable(      io.TextIOWrapper.write(
io.TextIOWrapper.fileno(        io.TextIOWrapper.readline(      io.TextIOWrapper.write_through
io.TextIOWrapper.flush(         io.TextIOWrapper.readlines(     io.TextIOWrapper.writelines(
io.TextIOWrapper.isatty(        io.TextIOWrapper.reconfigure(
```

对于打开的文件句柄（TextIOWrapper 对象实例），可查看相关属性：

```Shell
>>> fp.name
'test.py'
>>> fp.mode
'r'
>>> fp.encoding
'UTF-8'
>>> fp.newlines
'\n'
```

下面主要针对文本文件处理（TextIOWrapper）展开讨论，后面涉及到网络编程时再看看二进制处理。

## read

要使用文本文件中的信息，首先需要将信息读取到内存中。为此，你可以一次性读取文件的全部内容，也可以以每次一行的方式逐步读取。

`io.TextIOWrapper` 中读文件相关的接口如下：

```Shell
>>> help(io.TextIOWrapper)

 |  read(self, size=-1, /)
 |      Read at most size characters from stream.
 |
 |      Read from underlying buffer until we have size characters or we hit EOF.
 |      If size is negative or omitted, read until EOF.
 |
 |  readline(self, size=-1, /)
 |      Read until newline or EOF.
 |
 |      Return an empty string if EOF is hit immediately.
 |      If size is specified, at most size characters will be read.

 |  ----------------------------------------------------------------------
 |  Methods inherited from _IOBase:
 |
 |  readlines(self, hint=-1, /)
 |      Return a list of lines from the stream.
 |
 |      hint can be specified to control the number of lines read: no more
 |      lines will be read if the total size (in bytes/characters) of all
 |      lines so far exceeds hint.
```

### read

`read` 方法从文件最多（或者说尽量尝试）读取 size 指定数量的字符（字节）。
如果未指定size，则默认读至末尾（EOF, End Of File），即读取整个文件的内容。

> 对于文本模式，read 读取返回 `str` 对象（包含换行符的 repr）。

Python读文件和C语言中的文件操作类似，内部有游标（指针）跟踪读取位置，以支持迭代读取。
具体来说，每调用一次读操作（read, readline, readlines），都从当前游标开始读取。
每读取一个字节，游标后移一位，本次读完后，游标后移至下一个待读取点。

可以调用继承自 IOBase 的 `tell` 方法，获取当前游标位置（初始为0）。

```Shell
>>> help(io.TextIOWrapper)

 |  ----------------------------------------------------------------------
 |  Methods inherited from _IOBase:
 |
 |  tell(self, /)
 |      Return the stream position as an opaque number.
 |
 |      The return value of tell() can be given as input to seek(), to restore a
 |      previous stream position.
```

以下 read 和 tell 配合演示了读取文本文件一行的过程和机制：

```Shell
# 打开文件
>>> f = open('test.py')
# 初始游标位置为0：下一个待读初始位置
>>> f.tell()
0
# 读取2个字符（字节），游标自动后移2位
>>> f.read(2)
'#!'
>>> f.tell()
2
# 继续读取12个字符（字节），游标自动后移12位
>>> f.read(12)
'/usr/bin/env'
>>> f.tell()
14
# 继续读取1个字符（字节），游标自动后移1位
>>> f.read(1)
' '
# 继续读取7个字符（字节），游标自动后移7位
>>> f.read(7)
'python3'
>>> f.tell()
22
# 继续读取1个字符（字节），为第一行结尾换行符；游标自动后移1位至下一行开头
>>> f.read(1)
'\n'
# 继续读取1个字符（字节），为第二行第一个字符
>>> f.read(1)
'#'
```

### seek

如果中途想改变读取的游标位置，可以考虑调用 seek 方法。

```Shell
>>> help(io.TextIOWrapper)

 |  ----------------------------------------------------------------------
 |  Methods inherited from _IOBase:
 |
 |  seek(self, cookie, whence=0, /)
 |      Set the stream position, and return the new stream position.
 |
 |        cookie
 |          Zero or an opaque number returned by tell().
 |        whence
 |          The relative position to seek from.
 |
 |      Four operations are supported, given by the following argument
 |      combinations:
 |
 |      - seek(0, SEEK_SET): Rewind to the start of the stream.
 |      - seek(cookie, SEEK_SET): Restore a previous position;
 |        'cookie' must be a number returned by tell().
 |      - seek(0, SEEK_END): Fast-forward to the end of the stream.
 |      - seek(0, SEEK_CUR): Leave the current stream position unchanged.
 |
 |      Any other argument combinations are invalid,
 |      and may raise exceptions.
 |
 |  tell(self, /)
 |      Return the stream position as an opaque number.
 |
 |      The return value of tell() can be given as input to seek(), to restore a
 |      previous stream position.
```

其中 whence 参数可以取以下枚举值，代表文件开头、当前位置和结尾。

```Shell
>>> io.SEEK_SET
0
>>> io.SEEK_CUR
1
>>> io.SEEK_END
2
```

1. seek(0, io.SEEK_CUR)：保持当前游标。
2. seek(0, io.SEEK_END)：定位到文件结尾。

    - 这两种情况下，cookie 必须为零，否则报错：io.UnsupportedOperation: can't do nonzero cur-relative seeks。

3. seek(0, io.SEEK_SET)：定位到文件开头，可指定 cookie 偏移量。

    - f.seek(2, io.SEEK_SET)：返回新的位置，同 f.tell() = 2。

### readline

readline: Read until newline or EOF.

TextIOWrapper 的 `readline` 方法基于 newlines（默认为 `\n`）作为断行分割符。

> 对于文本模式，readline 读取返回`str` 对象，它是一行内容的字符串表示（包含换行符的 repr）。

readline 如果指定了 size，读取当前行的 size 个字符（字节）；否则，读取当前行（包括行尾部换行符），游标移动到下一行开头。

```Shell
>>> f.seek(0, io.SEEK_SET)
0
# 读取当前行（3个字符）
>>> f.readline(3)
'#!/'
# 继续读完该行
>>> f.readline()
'usr/bin/env python3\n'
# 继续读取第二行第一个字符
>>> f.read(1)
'#'
# 继续读完第二行
>>> f.readline()
' -*- coding: UTF-8 -*-\n'
# 继续读第三行（空行）
>>> f.readline()
'\n'
```

实际项目应用中，可在循环中调用 readline，实现逐行读取处理。
readline 带 size 相当于 read 读取指定字节，不带 size 读取到行尾。
这种特性适合解析基于行分割的 HTTP 报文：read 读取报文头，readline 读至结尾。

以下演示了循环调用 readline 逐行读取文本内容。

1. 由于事先不知道总行数，故用 while True 循环，待读到 EOF 返回 None 时 break 结束循环。
2. 由于每一行末尾自带换行符，print 默认会在末尾（end）插入换行符，因此应重设 end 为空，或对行内容执行 rstrip。

```Python
with open(filename) as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end='') # print(line.rstrip())
        # manipulation
```

以下代码 for 循环读取6行文本，打印每一行，给每一行冠以行号：

```Python
import string

MAX_LINES = 6

with open('test.py') as f:
    for i in range(MAX_LINES):
        line = f.readline()
        if (not line.startswith(tuple(string.whitespace))):
            print(f'{i+1}:', line, end='')
            # manipulation
        else:
            print(f'{i+1}: ')
```

### readlines

TextIOWrapper 的 `readline` 方法和继承自基类 IOBase 的 `readlines` 方法都是基于 newlines（默认为 `\n`）作为断行分割符。

- readline: Read until newline or EOF.
- readlines: Return a list of lines from the stream.

如果不指定参数（hint默认为-1 或 0），readlines 将逐行读取全文，返回字符串列表（list<str>）。
相当于循环调用 readline 再 append 到列表。

下面重点看看，当 hint 非零时，即在指定字符限定下，该方法是如何尽可能多地读取行。

假设 test.py 文件前四行的字符数如下（每行包含结尾换行符）：

1. 23
2. 24
3. 1
4. 11

以下代码片段演示了 readlines 的参数 hint 的限制逻辑。

```Shell
# hint少于1行，至少读取一行
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines(3)
['#!/usr/bin/env python3\n']
# hint刚好1行（不包括换行符），读取一行
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines(22)
['#!/usr/bin/env python3\n']
# hint刚好1行（包括换行符），读取一行，再读一行
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines(23)
['#!/usr/bin/env python3\n', '# -*- coding: UTF-8 -*-\n']
# hint刚好2行（不包括第二行的换行符），读取两行
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines(46)
['#!/usr/bin/env python3\n', '# -*- coding: UTF-8 -*-\n']
# hint刚好2行（包括第二行的换行符），读取两行，再读一行
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines(47)
['#!/usr/bin/env python3\n', '# -*- coding: UTF-8 -*-\n', '\n']
```

大部分情况下，调用 readlines 不传参数，读取整个文件内容。
当然也可直接将支持序列化的文件对象传给 list 直接构造，实现同等效果。

If you want to read all the lines of a file in a list you can also use `list(f)` or `f.readlines()`.

读取所有行到字符串列表（list of str），然后可以 for 循环逐行进行文本分析。

```Shell
>>> lines = fp.readlines() # list(fp)
>>> type(lines)
<class 'list'>
>>> type(lines[0])
<class 'str'>
```

`len(lines)` 计算文件包含的行数（包含空行）：

```Shell
>>> len(lines)
294637
```

对于小文件，一次性读取到内存，空间换取I/O时间，可以在内存中便捷存取。
但是，对于大文件，一次性读取到内存，比较消耗内存空间。
根据情况可折衷选择循环 readline，边读边处理。

### for loop

IOBase (and its subclasses) supports the iterator protocol, meaning that an IOBase object can be iterated over yielding the lines in a stream.

For reading lines from a file, you can **loop** over the file object. This is memory efficient, fast, and leads to simple code.

文件实际上是可迭代的，这意味着可在for循环中直接使用它们来迭代行。
建议采用 for...in （或 while readline）循环迭代逐行读取分析。

以下代码读取文件前10行并逐行分析（打印）：

```Python
with open('test.py') as f:
    line_count = 10
    line_index = 0
    for line in fp:
        if (line_index < line_count):
            print(line, end='') #print(line)
            line_index = line_index+1
        else:
            break
```

文件指针已经偏移到了第11行，如果再继续执行一遍以上代码，将会打印第11-20行。  
如果想重新打印前10行，则需要执行 `fp.seek(0, io.SEEK_SET)` 将游标移到开始位置。  

也可以先将文件对象传给 enumerate，再 for 循环迭代，析解行索引和内容。

```Python
import string

with open('test.py') as f:
    for index, line in enumerate(f):
        if (not line.startswith(tuple(string.whitespace))):
            print(f'{index+1}:', line, end='')
        else:
            print(f'{index+1}: ')
```

## write

要想写文件，打开文件时，要支持写模式。

第一种方式是，打开文件以读模式（`r`）打开，但是追加 `+` 支持写更新：`tr+`/`br+`。
第二种方式是，打开文件时，以写模式（`x`、`a`、`w`）打开。

关于 open 以写模式打开 mode 标记的注意事项：

- `x`: 如果指定路径的文件已经存在，会报错 FileExistsError: [Errno 17] File exists。
- `a`: 打开已经存在的文件，将游标移到文件末尾（下一个可写的位置），以便 write 追加内容。
- `w`: 打开已经存在的文件，并且清空文件（truncate first），千万要注意。

如果是以写模式打开还想读，可以追加一个加号：`tx+`/`bx+`、`ta+`/`ba+`。

与 `read` 方法相对应，TextIOWrapper 提供了 `write` 方法，支持写入字符串。
与 `readlines` 方法相对应，继承了基类 IOBase 的 `writelines` 方法支持写入多行（字符串列表：list<str>）。

**注意**：两个方法都需要自行在写入的字符串（text）末尾追加换行字符串（`\n`），否则多次write(lines)的内容会粘连在一起。

```Shell
>>> help(io.TextIOWrapper)

 |  write(self, text, /)
 |      Write string to stream.
 |      Returns the number of characters written (which is always equal to
 |      the length of the string).

 |  ----------------------------------------------------------------------
 |  Methods inherited from _IOBase:
 |
 |  writelines(self, lines, /)
 |      Write a list of lines to stream.
 |
 |      Line separators are not added, so it is usual for each of the
 |      lines provided to have a line separator at the end.
```

以下调用 write 插入两个字符串，由于行尾没有换行符，多次写入文件追加为一行。

```Shell
>>> f=open('test.log', 'tr+')
>>> f.tell()
0
>>> f.write('line 1')
6
>>> f.write('line 2')
6
# 游标在末尾，要想读取，需要复位
>>> f.readlines()
[]
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines()
['line 1line 2']
```

**注意**：write 总是在当前游标处开始写入，如果中途将游标回拨，可能会覆写掉原来的数据！

```Shell
>>> f.seek(0, io.SEEK_SET)
0
>>> f.write('line 3')
6
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines()
['line 3line 2']
```

以下演示废弃 test.log 中的内容，然后重新写入带换行符的字符串行：

```Shell
>>> f=open('test.log', 'tw+')
>>> f.readlines()
[]
>>> f.write('line 1\n')
7
>>> f.write('line 2\n')
7
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines()
['line 1\n', 'line 2\n']
```

下面演示 writelines 写入列表中的多行字符串：

```Shell
>>> line34=['line 3', 'line 4']
>>> f.tell()
14
>>> f.writelines(line34)
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines()
['line 1\n', 'line 2\n', 'line 3line 4']

>>> line56=['line 5\n' 'line 6\n']
>>> f.writelines(line56)
>>> f.seek(0, io.SEEK_SET)
0
>>> f.readlines()
['line 1\n', 'line 2\n', 'line 3line 4line 5\n', 'line 6\n']
```

## codecs

### BOM

可以用 hexdump 查看 UTF-8 with BOM（byte-order mark）开头的3个字节是 `0xEF 0xBB 0xBF`。

[Encoding declarations](https://docs.python.org/3/reference/lexical_analysis.html#encoding-declarations):

If no encoding declaration is found, the default encoding is UTF-8. In addition, if the first bytes of the file are the UTF-8 byte-order mark (`b'\xef\xbb\xbf'`), the declared file encoding is UTF-8 (this is supported, among others, by Microsoft’s **notepad**).

[Reading Unicode file data with BOM chars in Python](https://stackoverflow.com/questions/13590749/reading-unicode-file-data-with-bom-chars-in-python)  

Standard UTF-8 without BOM:

```
>>> b'hello'.decode('utf-8')
'hello'
>>> b'hello'.decode('utf-8-sig')
'hello'
```

BOM encoded UTF-8:

```
>>> b'\xef\xbb\xbfhello'.decode('utf-8')
'\ufeffhello'
>>> b'\xef\xbb\xbfhello'.decode('utf-8-sig')
'hello'
```

自动检测文件编码：

```Python
import codecs

def detect_by_bom(path,default):
    with open(path, 'rb') as f:
        raw = f.read(4)    #will read less if the file is smaller
    for enc,boms in \
            ('utf-8-sig',(codecs.BOM_UTF8,)),\
            ('utf-16',(codecs.BOM_UTF16_LE,codecs.BOM_UTF16_BE)),\
            ('utf-32',(codecs.BOM_UTF32_LE,codecs.BOM_UTF32_BE)):
        if any(raw.startswith(bom) for bom in boms): return enc
    return default
```

codecs 打印 BOM 头：

```
>>> codecs.BOM_UTF8
b'\xef\xbb\xbf'
>>> codecs.BOM_UTF16_LE
b'\xff\xfe'
>>> codecs.BOM_UTF16_BE
b'\xfe\xff'
>>> codecs.BOM_UTF32_LE
b'\xff\xfe\x00\x00'
>>> codecs.BOM_UTF32_BE
b'\x00\x00\xfe\xff'
```

---

[Convert UTF-8 with BOM to UTF-8 with no BOM in Python](https://stackoverflow.com/questions/8898294/convert-utf-8-with-bom-to-utf-8-with-no-bom-in-python)  

Sublime Text: File - Save with Encoding

```Python
import os

# absfilepath1, add BOM
s1 = open(absfilepath1, mode='r', encoding='utf-8').read()
(filepath1, filename1) = os.path.split(absfilepath1)
(relfilename1, fileext1) = os.path.splitext(filename1)
bom_filename = relfilename1+'_bom'+fileext1
bom_filepath = os.path.join(filepath1, bom_filename)
open(bom_filepath, mode='w', encoding='utf-8-sig').write(s1)

#rewrite without BOM
s = open(bom_file, mode='r', encoding='utf-8-sig').read()
open(bom_file, mode='w', encoding='utf-8').write(s)

# absfilepath2, remove BOM
s2 = open(absfilepath2, mode='r', encoding='utf-8-sig').read()
(filepath2, filename2) = os.path.split(absfilepath2)
(relfilename2, fileext2) = os.path.splitext(filename2)
nobom_filename = relfilename2+'_nobom'+fileext2
nobom_filepath = os.path.join(filepath2, nobom_filename)
open(nobom_filepath, mode='w', encoding='utf-8').write(s2)
```

### UnicodeDecodeError

```
>>> fp1 = open('2019-09-23-06.log')
>>> lines1 = fp1.readlines()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/Cellar/python/3.7.4_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb5 in position 7312: invalid start byte

>>> fp2 = open('2019-10-01-12.log')
>>> lines2 = fp2.readlines()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/Cellar/python/3.7.4_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8d in position 6873: invalid start byte
```

[UnicodeDecodeError: 'utf-8' codec can't decode byte](https://stackoverflow.com/questions/19699367/unicodedecodeerror-utf-8-codec-cant-decode-byte)  
[UnicodeDecodeError: 'utf8' codec can't decode byte 0x80 in position 3131: invalid start byte](https://stackoverflow.com/questions/38518023/unicodedecodeerror-utf8-codec-cant-decode-byte-0x80-in-position-3131-invali)  

The encoding was "**ISO-8859-1**", so replacing `open("u.item", encoding="utf-8")` with `open('u.item', encoding = "ISO-8859-1")` will solve the problem.

> The trick is that `ISO-8859-1` or `Latin_1` is 8 bit character sets, thus all garbage has a valid value. Perhaps not useable, but if you want to ignore!
