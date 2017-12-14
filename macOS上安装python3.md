## macOS/Xcode 自带的 Python.framework
macOS 的 Xcode 自带安装的 Python 在 `/System/Library/Frameworks/Python.framework/` 目录下：

```Shell
faner@THOMASFAN-MB0:~|⇒  cd /System/Library/Frameworks/Python.framework/Versions/
faner@THOMASFAN-MB0:/System/Library/Frameworks/Python.framework/Versions|
⇒  ls
2.3     2.5     2.6     2.7     Current
```

macOS 的 Current Python 版本为 2.7，终端输入 `Python` 启动的是 2.7 的交互环境。  

鉴于 Python3 和 Python2 语法并不向下兼容，如果覆盖安装升级 Python3，会导致原来依赖 Python2 的一些程序无法执行。  

## brew 安装 Python3

### brew search python3
在 macOS 终端输入 `brew search python3` 即可搜索 Python3 安装包：

```Shell
faner@THOMASFAN-MB0:~|⇒  brew search python3
==> Searching local taps...
python3 ✔
==> Searching taps on GitHub...
```

### brew info python3
在 macOS 终端输入 `brew info python3` 即可查询 Python3 安装包信息：

```Shell
faner@THOMASFAN-MB0:~|⇒  brew info python3
python3: stable 3.6.3 (bottled), devel 3.7.0a1, HEAD
Interpreted, interactive, object-oriented programming language
https://www.python.org/
Not installed
```

### brew install python3
在 macOS 终端输入 `brew install python3` 即可安装 Python3。

## 使用 python3

### python3 --version
执行 `python -V`（`python --version`）查看 macOS/Xcode 自带的 python2 的版本号。  
安装 python3 后，执行 `python3 -V`（`python3 --version`）可查看安装的 python3  的版本号。  

```Shell
faner@THOMASFAN-MB0:~|⇒  python -V
Python 2.7.10
faner@THOMASFAN-MB0:~|⇒  which python
/usr/bin/python
faner@THOMASFAN-MB0:~|⇒  whereis python
/usr/bin/python

faner@THOMASFAN-MB0:~|⇒  python3 --version
Python 3.6.3
faner@THOMASFAN-MB0:~|⇒  which python3
/usr/local/bin/python3
```

raspbian 默认已经安装了 python2 和 python3：

```Shell
pi@raspberrypi:~ $ python --version
Python 2.7.13
pi@raspberrypi:~ $ which python
/usr/bin/python

pi@raspberrypi:~ $ python3 -V
Python 3.5.3
pi@raspberrypi:~ $ which python3
/usr/bin/python3
```

> [python和numpy的版本、安装位置](http://www.cnblogs.com/klchang/p/4543032.html)  

### python3 Orignial
macOS 通过 brew 安装的 python3 默认在 `/usr/local/Cellar/python3/` 目录下，然后软链（symlink）到 `/usr/local/bin/` 目录下。

```Shell
faner@THOMASFAN-MB0:~|⇒  echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin
```

通过 `ls -l` 命令可显示 python3 的原身：

```Shell
faner@THOMASFAN-MB0:~|⇒  ls -al /usr/local/bin/python3
lrwxr-xr-x  1 faner  admin  35 Nov  3 08:09 /usr/local/bin/python3 -> ../Cellar/python3/3.6.3/bin/python3
```

进一步通过 `ls -l` 命令查找  python3  的终极原身：

```Shell
faner@THOMASFAN-MB0:~|⇒  ls -al /usr/local/Cellar/python3/3.6.3/bin/python3 
lrwxr-xr-x  1 faner  admin  55 Nov  3 08:09 /usr/local/Cellar/python3/3.6.3/bin/python3 -> ../Frameworks/Python.framework/Versions/3.6/bin/python3
```

### Hello World from Python3
新安装的 Python3 与系统自带的旧版 Python2 并存，使用时指明版本号即可。

在安装并配置好环境变量的系统终端中输入 `python` 默认进入 python2 的命令行编辑交互控制台。若显式指定 `python3`（或 python3.6），则可启动运行版本 3。

> The interpreter’s line-editing features include interactive editing, history substitution and code completion on systems that support readline.  

> The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a *script* from that file.  

python shell 前导符（primary prompt）为3个大于号 `>>>`（类似 bash shell 的 <kbd>$</kbd>），等待输入 python 命令。  

在 python(2) 下输入 `>>> print "Hello World from Python2"`，在 python3 下输入 `>>> print("Hello World from Python3")` 可打印 `Hello World from Python*`。

```Shell
faner@THOMASFAN-MB0:~|⇒  python
Python 2.7.10 (default, Feb  7 2017, 00:08:15) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print "Hello World from Python2"
Hello World from Python2
>>> ^D

faner@THOMASFAN-MB0:~|⇒  python3
Python 3.6.3 (default, Nov  3 2017, 08:08:42) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.35)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print "Hello World from Python3"
  File "<stdin>", line 1
    print "Hello World from Python3"
                                   ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World from Python3")?
>>> print ("Hello World from Python3")
Hello World from Python3
>>>  
```

> python3 XXX.py 指定 python3 执行 py 脚本文件。

### multi line input
如果一行输入不下，可以输入反斜杠 <kbd>\\</kbd>，新起续航书写。

```Shell
>>> hello = 'Hello World \
... from Python3'
>>> print(hello)
Hello World from Python3
>>> 
```

三引号（`'''`）开头结尾的输入，中间支持换行输入：

```Shell
>>> hello = '''Hello
... World
... from
... Python3'''
>>> print(hello)
Hello
World
from
Python3
```

以上每行尾部加反斜杠 <kbd>\\</kbd> 示意续行，防止分行：

```Shell
>>> hello = '''Hello \
... World \
... from \
... Python3'''
>>> print(hello)
Hello World from Python3
```

### quit/exit
按下 `<C-d>`（windows 下为 `<C-z>`）或输入 `quit()`/`exit()` 即可退出 python shell，退回到系统 shell。

> Typing an end-of-file character (`Control-D` on Unix, `Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: `quit()`.

### default python3

如果想输入 python 默认启动 python3，可以在 bash 配置文件中 `~/.bash_profile` 或 `~/.bashrc` 增加 alias 将 python 指向 Python3：

```Shell
alias python="/usr/local/Cellar/python3/3.6.3/Frameworks/Python.framework/Versions/3.6/bin/python3.6"
```

或

```Shell
alias python="python3.6"
```

### help
[Documentation](https://www.python.org/doc/) » [Python 3.x Docs](http://docs.python.org/3/)

在 python 的控制台中输入 `help()` 可打开交互式帮助系统。

```Shell
pi@raspberrypi:~ $ python3
Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.5's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.5/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 
```

输入 `help> modules` 可以列出当前所有已安装的模块：

```Shell
help> modules

Please wait a moment while I gather a list of all available modules...
```

输入 `help> roman` 可查看 roman 模块的帮助：

```Shell
help> roman

Help on module roman:

NAME
    roman - Convert to and from Roman numerals

```

输入 `help> roman.toRoman` 可查看 roman 模块的 toRoman 函数的帮助：

```Shell
help> roman.toRoman

Help on function toRoman in roman:

roman.toRoman = toRoman(n)
    convert integer to Roman numeral
```

可输入 `包名.类名.函数名` 逐级查看帮助。

输入 `<C-c>` 或 `<C-d>` 均可退出 `help> ` 回到 Python 主控制台 `>>> `。

## 参考

> [macOS 上如何切换默认的 Python 版本？](https://www.zhihu.com/question/30941329)  
> [macOS 上最简单配置python3开发环境](https://segmentfault.com/a/1190000006118856)  
> [macOS 上不卸载自带的 Python2 如何使用 Python3](http://www.jianshu.com/p/2c83363fa623)  
> [macOS 正确地同时安装Python 2.7 和 Python3](http://www.jianshu.com/p/51811fa24752/)  

> [macOS 上安装python环境](http://blog.csdn.net/powerlly/article/details/8879341)  
> macOS 安装 [Python3](http://blog.csdn.net/u010828718/article/details/70257622) 及 [初体验](http://www.cnblogs.com/leov1/p/5426191.html)  
> macOS 安装 Python3 以及问题总结：[Python3](http://blog.csdn.net/blue_zy/article/details/69568240) / [Python3.5](http://blog.csdn.net/s154421897/article/details/52687992)  
> [macOS下安装Python3.4和PyQt5](http://blog.csdn.net/lakerszhy/article/details/50636969)  

### 2.x 升级为 3.x

> [如何将 Mac OS X 10.9 下的Python 2.7升级到最新版的 Python 3.3](http://www.cnblogs.com/nokiaguy/p/3456590.html)  
> [升级MAC OS X 上的 Python 到最新版 3.4](http://blog.csdn.net/wirelessqa/article/details/23261723)  
> [macOS 上 Python 从2.x升级到3.x的艰苦历程](http://blog.csdn.net/ssgx1989/article/details/50603801)  

> [Mac下自带Python安装Tensorflow的问题](http://blog.csdn.net/quincuntial/article/details/52792429)
