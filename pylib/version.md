[TOC]

## python version

假设我们的python项目基于某一版本发行，若客户python运行时低于此版本，则某些功能特性可能不支持。
此时，我们可能需要检测客户是否安装了python，并且版本是否满足最低要求，否则提示用户安装或升级python。

### sh检测是否安装了python

未安装python时，执行 `python -V` 提示命令找不到：

```bash
$ python -V
zsh: command not found: python
$ echo $?
127
```

已安装python时，执行 `python -V` 正常返回版本：

```bash
$ python -V
Python 3.9.6
$ echo $?
0
```

以下定义了 shell 函数 check_python_version 用于检测本地是否安装了 python 运行时：

```bash
check_python_version()
{
    python -V &>/dev/null && {
        python_version=$(python -V 2>&1) 1>/dev/null
        echo "python installed: $python_version"
        return 0
    } || {
        echo "python uninstalled!"
        return 1
    }
}
```

### python检测当前安装版本

通过上文，我们知道，可以通过 sys、sysconfig 和 platform 相关接口检测当前 python 版本。

1. sys.version_info 返回 version_info 对象。

```bash
>>> sys.version_info
sys.version_info(major=3, minor=9, micro=6, releaselevel='final', serial=0)
>>> tuple(sys.version_info)
(3, 9, 6, 'final', 0)
>>> sys.version_info[:3]
(3, 9, 6)
>>> ".".join(map(str, sys.version_info[:3]))
'3.9.6'
```

2. sysconfig.get_python_version() 返回字符串，例如 '3.9'；

```bash
>>> sysconfig.get_python_version()
'3.9'
```

3. platform.python_version() 返回字符串，或调用 platform.python_version_tuple() 返回字符串元组。

```bash
>>> platform.python_version()
'3.9.6'
>>> platform.python_version_tuple()
('3', '9', '6')
>>> ".".join(platform.python_version_tuple())
'3.9.6'
```

### python对比安装版本

[How do I compare version numbers in Python? - Stack Overflow](https://stackoverflow.com/questions/11887762/how-do-i-compare-version-numbers-in-python)

以下用四种方式判断 python 版本是否大于 3.8/3.9.6。

```Python
import platform, sys, sysconfig

def version_str2tuple(vs:str):
    return tuple(map(int, vs.split(".")))

def version_tuple_str2int(vst:tuple):
    return tuple(map(int, vst))

# '3.12'
version_str2tuple(sysconfig.get_python_version()) > (3, 8)

# '3.12.2'
version_str2tuple(platform.python_version()) > (3, 9, 6)

# ('3', '12', '2')
version_tuple_str2int(platform.python_version_tuple()) > (3, 9, 6)

# (3, 12, 2, 'final', 0)
tuple(sys.version_info) > (3, 9, 6) # sys.version_info > (3, 9, 6)
```
