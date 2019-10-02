
[open](https://docs.python.org/3/library/functions.html#open)  

[io — Core tools for working with streams](https://docs.python.org/3/library/io.html)

[7.2. Reading and Writing Files](https://docs.python.org/3.7/tutorial/inputoutput.html#reading-and-writing-files)

```
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
```

```Python
import io
io.open(filename)
```

## open

`open` 打开文件：

```
>>> fp = open('QQ2019-09-22-21-MBR.log')
>>> fp.close()
```

最终文件不用时，需要显式调用 fp.close() 关闭文件。

建议采用 with...as 语句：`with open('QQ2019-09-22-21-MBR.log') as fp:`。
因为 with 区块执行完毕会自动执行清理，从而无需显式调用 close。

It is good practice to use the with keyword when dealing with file objects.  
The advantage is that the file is properly **closed** after its suite finishes, even if an exception is raised at some point.  

### mode

```
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

Files opened in binary mode (including 'b' in the mode argument) return contents as [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) objects without any decoding.  
In text mode (the default, or when 't' is included in the mode argument), the contents of the file are returned as `str`, the bytes having been first *decoded* using a platform-dependent encoding or using the specified encoding if given.

默认 mode='r'，即以只读、文本模式(`rt`)打开文件。

## io.TextIOWrapper

执行 `type(fp)` 可以查看打开的文件句柄的对象类型：

```
>>> type(fp)
<class '_io.TextIOWrapper'>
```

可以 import io，然后 `help(io.TextIOWrapper)` 查看文件句柄对象相关帮助。

```
 |  Method resolution order:
 |      TextIOWrapper
 |      _TextIOBase
 |      _IOBase
 |      builtins.object
```

[io.IOBase](https://docs.python.org/3/library/io.html?highlight=textiowrapper#io.IOBase)  
[io.TextIOBase](https://docs.python.org/3/library/io.html?highlight=textiowrapper#io.TextIOBase)  
[io.TextIOWrapper](https://docs.python.org/3/library/io.html?highlight=textiowrapper#io.TextIOWrapper)  

### properties

```
>>> fp.name
'QQ2019-09-22-21-MBR.log'
>>> fp.mode
'r'
>>> fp.encoding
'UTF-8'
>>> fp.newlines
'\n'
```

### read

`io.TextIOBase` 中的 read 和 readline 说明：

```
read(size=-1)
Read and return at most size characters from the stream as a single str. If size is negative or None, reads until EOF.

readline(size=-1)
Read until newline or EOF and return a single str. If the stream is already at EOF, an empty string is returned.

If size is specified, at most size characters will be read.
```

### readline

基于 newlines（默认为 `\n`）作为断行分割符。

`io.IOBase` 中的 readline 和 readlines 说明：

```
# 读取1行
readline(size=-1)
Read and return one line from the stream. If size is specified, at most size bytes will be read.

The line terminator is always b'\n' for binary files; for text files, the newline argument to open() can be used to select the line terminator(s) recognized.

# 读取所有行
readlines(hint=-1)
Read and return a list of lines from the stream. hint can be specified to control the number of lines read: no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds hint.

Note that it’s already possible to iterate on file objects using for line in file: ... without calling file.readlines().
```

## Text Parsing

### readlines

If you want to read all the lines of a file in a list you can also use `list(f)` or `f.readlines()`.

读取所有行到字符串列表（list of str）：

```
>>> lines = fp.readlines() # list(fp)
>>> type(lines)
<class 'list'>
>>> type(lines[0])
<class 'str'>
```

`len(lines)` 计算文件包含的行数：

```
>>> len(lines)
294637
```

然后可以 for 循环逐行进行文本分析。

### foreach

readlines 将文本文件全部读出解析为字符串，比较耗内存。建议采用 for...in 循环逐行读取分析。

For reading lines from a file, you can **loop** over the file object. This is memory efficient, fast,

以下代码读取文件前10行并逐行分析（打印）：

```Python
line_count = 10
line_index = 0;
for line in fp:
    if (line_index < line_count):
        print(line, end='') #print(line)
        line_index = line_index+1
    else:
        break
```

文件指针已经偏移到了第11行，如果再继续执行一遍以上代码，将会打印第11-20行。  
如果想重新打印第10行，则需要执行 `fp.seek(0, io.SEEK_SET)` 将游标移到开始位置。  
