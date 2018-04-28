[PEP 0 -- Index of Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/)  

This PEP contains the index of all Python Enhancement Proposals, known as PEPs.

## [PEP8](https://www.python.org/dev/peps/pep-0008/)

[PEP 8 — the Style Guide for Python Code](https://pep8.org/)  

- [PEP8 Error codes](http://pep8.readthedocs.io/en/latest/intro.html#error-codes)  
- [Flake8 Rules](https://lintlyci.github.io/Flake8Rules/)  

```shell
faner@MBP-FAN:~|⇒  pip3 search pep8
autopep8 (1.3.4)                  - A tool that automatically formats Python code to conform
                                    to the PEP 8 style guide

pep8-naming (0.5.0)               - Check PEP-8 naming conventions, plugin for flake8
ulint-pep8 (0.2)                  - PEP8 linter for ulint
pytest-pep8 (1.0.6)               - pytest plugin to check PEP8 requirements
pep8 (1.7.1)                      - Python style guide checker
pepper8 (1.1.1)                   - Transforms pep8 or flake8 output into an HTML report.

```

[autopep8](https://github.com/hhatto/autopep8)  
[PEP8 online check](http://pep8online.com/)  
[Python PEP8 Autoformat](https://packagecontrol.io/packages/Python%20PEP8%20Autoformat)  

[PEP8 Python 编码规范](https://www.jianshu.com/p/52f4416c267d)  
[PEP 8——Python编码风格指南](https://lizhe2004.gitbooks.io/code-style-guideline-cn/content/python/python-pep8.html)  

## Anaconda

- `Anaconda: Disable linting on this file`，选中后将不再进行 PEP8 错误标识。  

	> 选中 **Disable** 禁止 PEP8 错误提示后，将多出相应的 **Enable** 项可恢复提示。  

- `Anaconda: Show error list`：浮窗列出 PEP8 错误列表。  
- `Anaconda: Next/Previous lint error`：查看下/上 PEP8 错误。  

- `Anaconda: Autoformat PEP8 Errors`：按PEP8风格自动排版代码。

### anaconda_linting

Anaconda 默认开启了 anaconda_linting。

`Anaconda.sublime-settings` 中 **use_pylint** 设置为 false，默认禁用 PyLint，基于 pep8 和 PyFlakes。

> [Sublime Text 3 - Disable Python Checker warning “indentation contains tabs”](https://stackoverflow.com/questions/23383699/sublime-text-3-disable-python-checker-warning-indentation-contains-tabs)  

### common PEP8 errors

1. [W] PEP8 (E265): block comment should start with ‘#’

	> 独行顶格注释：`#` 后需要一个（或以上）空格和注释文字隔开。

2. E261 & E262

	- [W] PEP8 (E261): at least two spaces before inline comment
	- [W] PEP8 (E262): inline comment should start with ‘#’

	> 行末跟随注释：`#` 前距离代码结尾两个（或以上）空格，  
	> `#` 后需要一个（或以上）空格和注释文字隔开。

3. [W] PEP8 (E703): statement ends with a semicolon

	> 从 C++ 等其他编程语言转过来，习惯在代码行末增加分号以示结束。  
	> 但 python 代码是以自然行作为组织单元，末尾无需添加分号。  

4. [W] PEP8 (E225): missing whitespace around operator

	> 逻辑运算符（`==`, `!=`）和算数运算符（`+`,`*`）前后都要留空格。

5. [W] PEP8 (E302): expected 2 blank lines, found 1

	> 函数定义（`def function():`）上面应预留两空行，当前只有一个空行。

6. [W] PEP8 (E305): expected 2 blank lines after class or function definition, found 1

	> 类或函数定义下面应预留两空行，当前只有一个空行。

7. [W] PEP8 (E303): too many blank lines(N)

	> E302/E305，补充空行数 N 超过两行，不能少也不能多。

## flake suites

> [About style guide of python and linter](https://blog.sideci.com/about-style-guide-of-python-and-linter-tool-pep8-pyflakes-flake8-haking-pyling-7fdbe163079d) : pep8, pyflakes, flake8, Pylint  

### pycodestyle

pycodestyle (formerly called pep8) - Python style guide checker

<http://pycodestyle.pycqa.org/>  
<https://pycodestyle.readthedocs.io/>  

<https://github.com/PyCQA/pycodestyle>  
<https://pypi.org/project/pycodestyle/>  

pycodestyle is a tool to check your Python code against some of the style conventions in [PEP 8](http://www.python.org/dev/peps/pep-0008/).

This package used to be called `pep8` but was **renamed** to `pycodestyle` to reduce confusion.

> **pycodestyle**(pep8): 静态检查 PEP 8 编码风格的工具。  

#### version information

执行 `pip3 install pycodestyle` 安装 pycodestyle。

查看帮助和版本信息：

```shell
faner@MBP-FAN:~|⇒  pycodestyle -h
Usage: pycodestyle [options] input ...

Options:
  --version            show program's version number and exit
  -h, --help           show this help message and exit
  -v, --verbose        print status messages, or debug with -vv

faner@MBP-FAN:~|⇒  pycodestyle --version
2.3.1
```

查看已安装的包信息：

```shell
faner@MBP-FAN:~|⇒  pip3 show pycodestyle
Name: pycodestyle
Version: 2.3.1
Summary: Python style guide checker
Home-page: https://pycodestyle.readthedocs.io/
Author: Ian Lee
Author-email: IanLee1521@gmail.com
License: Expat license
Location: /usr/local/lib/python3.6/site-packages
Requires: 
Required-by: flake8
```

#### [usage](https://pycodestyle.readthedocs.io/en/latest/intro.html#example-usage-and-output)

调用 pycodestyle 进行代码风格检查使用示例：

```shell
pycodestyle /usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/optparse.py
```

### pyflakes

A simple program which checks Python source files for errors.

<https://github.com/PyCQA/pyflakes>  
<https://pypi.org/project/pyflakes>  

Pyflakes is also faster than [Pylint](http://www.pylint.org/) or [Pychecker](http://pychecker.sourceforge.net/). This is largely because Pyflakes only examines the syntax tree of each file individually. As a consequence, Pyflakes is more limited in the types of things it can check.

If you require more options and more flexibility, you could give a look to [Flake8](https://pypi.python.org/pypi/flake8) too.  
If you like Pyflakes but also want stylistic checks, you want [flake8](https://pypi.python.org/pypi/flake8), which combines Pyflakes with style checks against [PEP 8](http://legacy.python.org/dev/peps/pep-0008/) and adds per-project configuration ability.  

> **pyflakes**: 静态检查 Python 代码逻辑错误的工具。  

#### version information

执行 `pip3 install pyflakes` 安装 pyflakes。

查看帮助和版本信息：

```shell
faner@MBP-FAN:~|⇒  pyflakes -h
Usage: pyflakes [options]

Options:
  --version   show program's version number and exit
  -h, --help  show this help message and exit
faner@MBP-FAN:~|⇒  pyflakes --version
1.6.0
```

查看已安装的包信息：

```shell
faner@MBP-FAN:~|⇒  pip3 show pyflakes
Name: pyflakes
Version: 1.6.0
Summary: passive checker of Python programs
Home-page: https://github.com/PyCQA/pyflakes
Author: A lot of people
Author-email: code-quality@python.org
License: MIT
Location: /usr/local/lib/python3.6/site-packages
Requires: 
Required-by: flake8
```

#### usage

调用 pyflakes 进行逻辑错误检查使用示例：

```
pyflakes /usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/optparse.py
```

### flake8

Your Tool For Style Guide Enforcement

<http://flake8.pycqa.org/>  
<http://flake8.readthedocs.io/en/latest/>  

<https://github.com/PyCQA/flake8>  
<https://pypi.python.org/pypi/flake8>  

Flake8 is a wrapper around these tools:

- PyFlakes  
- pycodestyle  
- Ned Batchelder’s McCabe script  

Flake8 runs all the tools by launching the single flake8 command. It displays the warnings in a per-file, merged output.

> [pyflakes vs flake8](https://python-forum.io/Thread-pyflakes-vs-flake8): Flake8 bring together pycodestyle(pep8) and pyflakes.

> [Configuring Flake8](http://flake8.pycqa.org/en/latest/user/configuration.html#configuration-locations)

- [Flake8简介](http://www.malike.net.cn/blog/2013/10/23/flake8-tutorial/)  
- [Vim插件之vim-flake8](https://blog.csdn.net/demorngel/article/details/69053321)  

#### version information

执行 `pip3 install flake8` 安装 flake8。

查看帮助和版本信息：

```shell
faner@MBP-FAN:~|⇒  flake8 -h
Usage: flake8 [options] file file ...

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose         Print more information about what is happening in
                        flake8. This option is repeatable and will increase
                        verbosity each time it is repeated.

Installed plugins: mccabe: 0.6.1, pycodestyle: 2.3.1, pyflakes: 1.6.0

faner@MBP-FAN:~|⇒  flake8 --version
3.5.0 (mccabe: 0.6.1, pycodestyle: 2.3.1, pyflakes: 1.6.0) CPython 3.6.5 on Darwin
```

查看已安装的包信息：

```shell
faner@MBP-FAN:~|⇒  pip show flake8
Name: flake8
Version: 3.5.0
Summary: the modular source code checker: pep8, pyflakes and co
Home-page: https://gitlab.com/pycqa/flake8
Author: Ian Stapleton Cordasco
Author-email: graffatcolmingov@gmail.com
License: MIT
Location: /usr/local/lib/python3.6/site-packages
Requires: pyflakes, pycodestyle, mccabe
Required-by: 
```

#### usage

flake8 同时调用 pycodestyle 和 pyflakes 分别进行代码风格检查和逻辑错误检查，使用示例：

```shell
flake8 path/to/code/to/check.py
# or
flake8 path/to/code/
```

```shell
flake8 /usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/lib/python3.6/optparse.py
```

flake8 相比 pycodestyle 多了一些 F 开头的错误码（pyflakes logic errors），例如：

```
optparse.py:1387:13: F841 local variable 'stop' is assigned to but never used
```

## SublimeLinter

[SublimeLinter](https://github.com/SublimeLinter) - The code linting framework for Sublime Text 3  
[SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) Framework  

- [SublimeLinter-pycodestyle](https://github.com/SublimeLinter/SublimeLinter-pycodestyle)：需先 pip 安装 pycodestyle  
- [SublimeLinter-pyflakes](https://github.com/SublimeLinter/SublimeLinter-pyflakes)：需先 pip 安装 pyflakes  
- [**SublimeLinter-flake8**](https://github.com/SublimeLinter/SublimeLinter-flake8)：需先 pip 安装 flake8  

### anaconda_linting - default

Anaconda 默认开启了 anaconda_linting。

> `Anaconda.sublime-settings` 中 **use_pylint** 设置为 false，默认禁用 PyLint，基于 pep8 和 PyFlakes。

### SublimeLinter-flake8 - recommended

建议采用 SublimeLinter-flake8 插件（基于 pycodestyle,pyflakes,mccabe），无需额外安装 SublimeLinter-pycodestyle 或 SublimeLinter-pyflakes 插件。

首先，在 `Sublime > Preferences > Package Settings > Anaconda > Settings - User` 中禁用  Anaconda 的 anaconda_linting：

```json
{
    "anaconda_linting": false,
}
```

其次，按照 [Three steps to lint Python 3.6 in Sublime Text](https://janikarhunen.fi/three-steps-to-lint-python-3-6-in-sublime-text.html) 以下步骤安装 SublimeLinter-flake8 插件：

1. macOS 终端执行 `pip3 install flake8` 安装 flake8，自动检测按需安装 pyflakes, pycodestyle, mccabe 等其他依赖包；  
2. 在 Sublime Text 中 PCI（Package Control: Install Package）安装 `SublimeLinter-flake8` 插件；  

SublimeLinter-flake8 自动检测 python 代码风格和逻辑错误，Sublime Text 底部状态栏左侧会实时显示鼠标聚焦当前行的检测结果（包括 annotations 和 flake8）。

出错时对应行号左侧边列（gutter）中将会出现红点，对应代码处将以红框标出（outine）。

- warning：橙色；  
- error：红色；  

当鼠标悬浮在 gutter 或 outine 上时，将会浮出错误提示框（tooltips），显示具体的错误码和错误提示信息。

### [Python Flake 8 Lint](https://packagecontrol.io/packages/Python%20Flake8%20Lint) - deprecated

<https://github.com/dreadatour/Flake8Lint>

[Flake8](http://pypi.python.org/pypi/flake8) (used in “Python Flake8 Lint”) is a wrapper around these tools:

- [pep8](http://pypi.python.org/pypi/pep8) is a tool to check your Python code against some of the **style** conventions in PEP8.  
- [PyFlakes](https://pypi.org/project/pyflakes/) checks only for **logical errors** in programs; it does not perform any check on style.  
- [mccabe](https://pypi.org/project/mccabe/) is a code **complexity checker**. It is quite useful to detect over-complex code. According to McCabe, anything that goes beyond 10 is too complex. See [Cyclomatic_complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity).  

There are additional tools used to lint Python files:

- [pydocstyle](https://pypi.org/project/pydocstyle/) is a static analysis tool for checking compliance with Python PEP257.  
- [pep8-naming](https://pypi.org/project/pep8-naming/) is a naming convention checker for Python.  
- [flake8-debugger](https://pypi.org/project/flake8-debugger/) is a flake8 debug statement checker.  
- [flake8-import-order](https://pypi.org/project/flake8-import-order/) is a flake8 plugin that checks import order in the fashion of the Google Python Style Guide (turned off by default).  
