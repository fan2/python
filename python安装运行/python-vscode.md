
[TOC]

[Python in VS Code](https://code.visualstudio.com/docs/python/)

- Tutorial - [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)  
- Environments - [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)  

[Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

* [Editing Code](https://code.visualstudio.com/docs/python/editing)  
* [Linting](https://code.visualstudio.com/docs/python/linting)  
* [Debugging](https://code.visualstudio.com/docs/python/debugging)  

## vscode + python

[vscode-python](https://github.com/fan2/Text-Reader-Editor/blob/master/vscode/vscode-python.md)

微软官方提供了 Python 插件（内嵌 Jupyter 插件）：

1. `Python`: IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests, and more.

    - Extension Pack: `Pylance`, `Jupyter` and `isort`.

2. `Jupyter`: Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.

    - Extension Pack: `Jupyter Keymap`, `Jupyter Notebook Renderers`, `Jupyter Slide Show`, `Jupyter Cell Tags`.

[vscode上配置python的运行环境](https://www.cnblogs.com/EtoDemerzel/p/8083313.html)  
[那些使用VSCode写Python踩过的坑(Anaconda配置)](https://blog.csdn.net/weixin_30784501/article/details/95107106)  

### interpreter

[Select a Python interpreter](https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter)

![select-python-interpreter](./../images/python-select-interpreter.png)

1. `Recommended` 为 vscode settings 中配置的 defaultInterpreterPath。
2. 当在 vscode settings 中配置了 CondaPath，会在此处出现 `Conda` 子环境的解释器版本。
3. `Global` 为 homebrew 安装（/usr/local/bin/python3）和 macOS 自带的（usr/bin/python3）。

> Global 下可能出现 brew 安装的多个版本供选择。

### run debug

## vscode + conda

Anaconda 配合 VSCode 可以搭建一个适用于机器学习、AI、数据科学领域学习与开发的 Python 开发环境。

### condaPath

```
  // Path to the conda executable to use for activation (version 4.4+).
  "python.condaPath": "/usr/local/anaconda3/condabin/conda",
```

[Remove python.condaPath from workspace scope #17819](https://github.com/microsoft/vscode-python/issues/17819)
[python.condaPath not considered when calling conda #9154](https://github.com/microsoft/vscode-python/issues/9154)

配置了 `python.condaPath` 之后，运行命令 Python: Select Interpreter 下拉列表中将会显示 conda base 环境的 python。

### pythonPath

[Activating Anaconda Environment in VsCode](https://stackoverflow.com/questions/43351596/activating-anaconda-environment-in-vscode)

快捷键 `cmd+,` 打开 vscode 偏好设置，编辑修改（`~/Library/Application Support/Code/User/settings.json`），找到如下两个参数：

1. python.pythonPath（现已变更为 `defaultInterpreterPath`）；  
2. python.autoComplete.extraPaths；  

修改为 conda 子环境下对应的 bin/python 和 side-packages：

> [Finding your Anaconda Python interpreter path](https://docs.anaconda.com/anaconda/user-guide/tasks/integration/python-path/)

```
# 设置 base 环境
    "python.defaultInterpreterPath": "/usr/local/anaconda3/bin/python3",
    "python.autoComplete.extraPaths": ["/usr/local/anaconda3/lib/python3.9/site-packages"],
```

```
# 设置 Py376 环境
    "python.defaultInterpreterPath": "/usr/local/anaconda3/envs/Py376/bin/python3",
    "python.autoComplete.extraPaths": ["/usr/local/anaconda3/envs/Py376/lib/python3.7/site-packages"],
```

### refs

[搭建 Python 轻量级编写环境（Anaconda+VSCode）](https://zhuanlan.zhihu.com/p/147336202)  
[Working with Anaconda in Visual Studio Code](https://stackoverflow.com/questions/54828713/working-with-anaconda-in-visual-studio-code)  

[Anaconda+VSCode搭建python环境](https://www.jianshu.com/p/f10fb1a4cc87) - Windows  
[Anaconda＋VSCode搭建python开发环境](https://cloud.tencent.com/developer/news/313349) - Windows  
[windows10环境下用anaconda和VScode配置](https://blog.csdn.net/u011622208/article/details/79625908)  

[MacOS下如何配置Vscode+Anaconda呢？](https://www.zhihu.com/question/265853927)  
[mac vscode配置 anaconda 虚拟环境](https://blog.csdn.net/liubingjun07/article/details/88833885)  
[Mac+Anaconda+PyCharm+VSCode环境搭建](https://blog.csdn.net/qq_28863845/article/details/82589857)  

## python debug

在 vscode 中打开 Python 脚本文件(test.py)，在文本编辑区左侧 gutter 上点击下断点。
然后在右上角 ▶︎ 按钮，下拉选择 `Python Debugger: Debug Python File`，即可启动调试。
启动调试运行起来后，命中断点中断，右侧会有一个悬浮的调试工具条，支持 Continue、Step Over/Into/Out。
同时，左侧侧边拉会打开 Run and Debug，其中可以查看 Variables（Locals, Globals）、Watch 和 CallStack。

参考：

- Quick Start - [UI tour](https://code.visualstudio.com/docs/python/python-quick-start#_ui-tour)。
- Quick Start - [Run, debug, and test](https://code.visualstudio.com/docs/python/python-quick-start#_run-debug-and-test)

## python unittest

[unittest --- 单元测试框架 — Python 3.12.2 文档](https://docs.python.org/zh-cn/3/library/unittest.html#)

[用单元测试让你的python代码更靠谱测试函数单元测试和测试用例测试类-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1347180)

假设 name_function.py 文件中定义了 get_formatted_name 函数：

```Python
# coding:utf-8

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
```

test_name_function.py 单测 name_function 中的 get_formatted_name 函数：

```Python
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
```

以上代码 class NameTestCase 继承 unittest.TestCase 创建了一个测试样例。
通过 setUp() 和 tearDown() 方法，可以设置测试开始前与完成后需要执行的指令。
上述两个独立的测试方法的命名都以 test 开头，这个命名约定告诉测试运行者类的哪些方法表示测试。

每个测试的关键是使用断言来管理预期：

- 调用 assertEqual() 或 assertNotEqual() 来检查预期的输出；
- 调用 assertTrue() 或 assertFalse() 来验证一个条件；
- 调用 assertIn() 或 assertNotIn() 来验证包含情况；
- 调用 assertRaises() 来验证抛出了一个特定的异常。

使用这些方法而不是 `assert` 语句是为了让测试运行者能聚合所有的测试结果并产生结果报告。

**常用断言方法**：

方法                       | 用途
--------------------------|------
assertEqual(a, b)         | 核实 a == b
assertNotEqual(a, b)      | 核实 a != b
assertTrue(x)             | 核实 x为True
assertFalse(x)            | 核实 x为False
assertIn(item , list )    | 核实 item 在 list 中
assertNotIn(item , list ) | 核实 item 不在 list 中
