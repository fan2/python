## sys

### doc

```shell
>>> print(sys.__doc__)
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

```

- Dynamic objects  
- Static objects  
- Functions  

**argv** 为脚本运行参数列表(str list)。  
`argv[0]` 为脚本名称，从 `argv[1]` 开始为用户参数。  

### test

```shell
>>> import sys

# 平台类型标识
>>> sys.platform
'darwin'

# 版本信息（string格式）
>>> sys.version
'3.6.5 (default, Apr 14 2018, 06:59:43) \n[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)]'

>>> print(sys.version)
3.6.5 (default, Apr 14 2018, 06:59:43) 
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)]

# 版本信息（tuple格式）
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=5, releaselevel='final', serial=0)

# Python 实现信息
>>> sys.implementation
namespace(_multiarch='darwin', cache_tag='cpython-36', hexversion=50726384, name='cpython', version=sys.version_info(major=3, minor=6, micro=5, releaselevel='final', serial=0))

# 字节序
>>> sys.byteorder
'little'

# 线程模型
>>> sys.thread_info
sys.thread_info(name='pthread', lock='mutex+cond', version=None)

```

## os

```shell
>>> import os

>>> os.path
<module 'posixpath' from '/usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/posixpath.py'>

>>> os.name
'posix'

>>> os.uname()
posix.uname_result(sysname='Darwin', nodename='MBP-FAN', release='17.6.0', version='Darwin Kernel Version 17.6.0: Fri Apr 13 19:57:44 PDT 2018; root:xnu-4570.60.17.0.1~3/RELEASE_X86_64', machine='x86_64')

# 路径分隔符（pathname separator）
>>> os.sep
'/'

# 文件后缀分隔符（extension separator）
>>> os.extsep
'.'

# 环境变量 PATH 分隔符（component separator used in $PATH）
>>> os.pathsep
':'

# 换行符（line separator），nt 下为 '\r\n'
>>> os.linesep
'\n'

```

## platform

```shell
>>> import platform

>>> platform.platform()
'Darwin-17.6.0-x86_64-i386-64bit'

>>> platform.version()
'Darwin Kernel Version 17.6.0: Fri Apr 13 19:57:44 PDT 2018; root:xnu-4570.60.17.0.1~3/RELEASE_X86_64'

>>> platform.uname()
uname_result(system='Darwin', node='MBP-FAN', release='17.6.0', version='Darwin Kernel Version 17.6.0: Fri Apr 13 19:57:44 PDT 2018; root:xnu-4570.60.17.0.1~3/RELEASE_X86_64', machine='x86_64', processor='i386')

# 体系架构
>>> platform.machine()
'x86_64'

# 处理器
>>> platform.processor()
'i386'

# 系统
>>> platform.system()
'Darwin'

>>> platform.python_implementation()
'CPython'

>>> platform.python_version()
'3.6.5'

>>> platform.python_version_tuple()
('3', '6', '5')
```

## sysconfig

```shell
>>> import sysconfig

>>> sysconfig.get_platform()
'macosx-10.13-x86_64'

>>> sysconfig.get_python_version()
'3.6'
```
