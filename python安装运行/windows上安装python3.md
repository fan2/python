
## [Using Python on Windows](https://docs.python.org/3/using/windows.html)

To make Python available, the CPython team has compiled Windows installers (MSI packages) with every [release](https://www.python.org/download/releases/) for many years. 
These installers are primarily intended to add a `per-user` installation of Python, with the core interpreter and library being used by a single user.

[The full installer](https://docs.python.org/3/using/windows.html#windows-full) contains all components and is the best option for developers using Python for any kind of project.

### Installation steps

[Python Releases for Windows](https://www.python.org/downloads/windows/)

`Install Now`: 

- Python will be installed into your user directory.  
- the install directory will be added to **your** PATH.  
- Shortcuts will only be visible for the **current** user.  

`Customize installation`: 

- Python will be installed into the Program Files directory.  
- The standard library can be pre-compiled to bytecode.  
- If selected, the install directory will be added to the **system** PATH  
- Shortcuts are available for **all** users  

## [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/)

[Python3入门笔记（1） —— windows安装与运行](https://www.cnblogs.com/weven/p/7252917.html)  
[windows如何下载安装Python](https://blog.csdn.net/culous/article/details/78604618)  

[windows下面安装Python和pip终极教程](http://www.cnblogs.com/yuanzm/p/4089856.html)  
[Python3.6 Windows的安装以及配置指南](http://blog.sciencenet.cn/blog-2577109-1025666.html)  
[Windows同时兼容Python 2.x和Python 3.x](http://blog.sciencenet.cn/blog-350278-1104735.html)  

- [Python Launcher](https://www.jianshu.com/p/987746d4c9e0): 通过 `py -version` 的方式启动 Python。

## [Python on Windows documentation](https://docs.microsoft.com/en-us/windows/python/)

[Windows 10 Linux subsystem for Python developers](https://www.betteridiot.tech/blog/pop/betterblog/2018/9/windows-10-linux-subsystem-for-python-developers)  
[Who put Python in the Windows 10 May 2019 Update?](https://devblogs.microsoft.com/python/python-in-the-windows-10-may-2019-update/)  

## [Python Launcher for Windows](https://docs.python.org/3/using/windows.html#launcher)

[PEP 397 -- Python launcher for Windows](https://www.python.org/dev/peps/pep-0397/)

[请问python中的python launcher是什么？](https://www.zhihu.com/question/264343132)

python launcher 是 python 3.3 为 windows 引入的。

- **py.exe**，console 程序，启动 python.exe，关联到 `*.py` 文件。  
- **pyw.exe**，非 console 程序，启动 pythonw.exe，关联到 `*.pyw` 文件。  

### vscode

[Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)  

- [Anaconda Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-python.anaconda-extension-pack)  

[Python - 使用 Visual Studio Code 作為開發環境](https://oranwind.org/python-vscode/)  
[用VScode配置Python开发环境](https://zhuanlan.zhihu.com/p/31417084)  

pip install flake8 + pip install yapf，配置flake8和yapf并关闭pylint工具。

[How to execute Python code from within Visual Studio Code](https://stackoverflow.com/questions/29987840/how-to-execute-python-code-from-within-visual-studio-code)

- launch.json
