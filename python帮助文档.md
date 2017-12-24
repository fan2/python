## help
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

### roman
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

可输入 *`包名.类名.函数名`* 逐级查看帮助。

输入 `<C-c>` 或 `<C-d>` 均可退出 `help> ` 回到 Python 主控制台 `>>> `。
