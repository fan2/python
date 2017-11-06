
# Python Packaging User Guide
[PyPA](https://pypa.io/) » [Python Packaging User Guide](https://packaging.python.org/) » [Guides](https://packaging.python.org/guides/) » [Tool recommendations](https://packaging.python.org/guides/tool-recommendations/)

- Installation Tool Recommendations  
	- Use **pip** to install Python [packages](https://packaging.python.org/glossary/#term-distribution-package) from [PyPI](https://packaging.python.org/glossary/#term-python-package-index-pypi).  
	- Use [**virtualenv**](https://packaging.python.org/key_projects/#virtualenv), or [venv](https://docs.python.org/3/library/venv.html) to isolate application specific dependencies from a shared Python installation.  
- Packaging Tool Recommendations  
	- Use [**setuptools**](https://packaging.python.org/key_projects/#setuptools) to define projects and create [Source Distributions](https://packaging.python.org/glossary/#term-source-distribution-or-sdist).  
	- Use the `bdist_wheel` [setuptools](https://packaging.python.org/key_projects/#setuptools) extension available from the [wheel project](https://packaging.python.org/key_projects/#wheel) to create [wheels](https://packaging.python.org/glossary/#term-wheel). This is especially beneficial, if your project contains binary extensions.  

## Packaging Tool
### setuptools
[Package Index](https://pypi.python.org/pypi) > [setuptools](https://pypi.python.org/pypi/setuptools)
Easily download, build, install, upgrade, and uninstall Python packages

Github Page: [pypa](https://github.com/pypa) / [setuptools](https://github.com/pypa/setuptools)

[setuptools](https://packaging.python.org/key_projects/#setuptools) (which includes `easy_install`) is a collection of enhancements to the Python distutils that allow you to more easily build and distribute Python distributions, especially ones that have dependencies on other packages.

macOS 下使用 brew 安装 python3 时，默认已安装 pip3 和 setuptools。

```Shell
faner@THOMASFAN-MB0:~|⇒  pip3 list
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
pip (9.0.1)
setuptools (36.5.0)
wheel (0.30.0)
```

可通过 `pip3 show setuptools` 命令查看 wheel 包信息。

```Shell
faner@THOMASFAN-MB0:~|⇒  pip3 show setuptools
Name: setuptools
Version: 36.5.0
Summary: Easily download, build, install, upgrade, and uninstall Python packages
Home-page: https://github.com/pypa/setuptools
Author: Python Packaging Authority
Author-email: distutils-sig@python.org
License: UNKNOWN
Location: /usr/local/lib/python3.6/site-packages
Requires:
```

### Wheel
[Docs](https://wheel.readthedocs.io/en/latest/#)  » [Wheel](https://wheel.readthedocs.io/en/latest/)

A built-package format for Python.  
A **wheel** is a ZIP-format archive with a specially formatted filename and the `.whl` extension.  

macOS 下使用 brew 安装 python3 时，默认已安装 pip3 和 wheel3。

```Shell
faner@THOMASFAN-MB0:~|⇒  wheel3 -V
usage: wheel3 [-h]
              {keygen,sign,unsign,verify,unpack,install,install-scripts,convert,version,help}
              ...
wheel3: error: unrecognized arguments: -V
```

可通过 `pip3 show wheel` 命令查看 wheel 包信息。

```Shell
faner@THOMASFAN-MB0:~|⇒  pip3 show wheel     
Name: wheel
Version: 0.30.0
Summary: A built-package format for Python.
Home-page: https://github.com/pypa/wheel
Author: Alex Grönholm
Author-email: alex.gronholm@nextday.fi
License: MIT
Location: /usr/local/lib/python3.6/site-packages
Requires: 
```

## Installation Tool
Python有两个著名的包管理工具 `easy_install.py` 和 `pip`。

在 Python2.7 的安装包中，`easy_install.py` 是默认安装的，而 `pip` 需要我们手动安装。  
在 python 2.7.9+ 及 python 3.4+ 的安装包中，默认已经自带 `pip` 包管理器。  

### [easy_install](https://pypi.python.org/pypi/easy_install)
[EasyInstall](https://wiki.python.org/moin/EasyInstall) (easy_install) gives you a quick and painless way to install packages remotely by connecting to the cheeseshop or even other websites via HTTP. It is somewhat analogous to the CPAN and PEAR tools for Perl and PHP, respectively.

[setuptools 36.6.0 documentation](http://setuptools.readthedocs.io/en/latest/index.html) » [Easy Install](http://setuptools.readthedocs.io/en/latest/easy_install.html#id8)  

Easy Install is a python module (`easy_install`) bundled with `setuptools` that lets you automatically download, build, install, and manage Python packages.

在 macOS/raspbian 终端输入 `easy_install` 再按下 tab 可查看所有版本的 `easy_install`；

- 输入 `easy_install --version` 命令可查看 Python 2.7 对应的 easy_install 的版本号；  
- 输入 `easy_install-3.6 --version`（`easy_install3 --version`）可查看 Python 3.* 对应的 easy_install 的版本号。  

```Shell
faner@THOMASFAN-MB0:~|⇒  easy_install
easy_install      easy_install-2.6  easy_install-2.7  easy_install-3.6

faner@THOMASFAN-MB0:~|⇒  easy_install --version
setuptools 18.5 from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python (Python 2.7)

faner@THOMASFAN-MB0:~|⇒  easy_install-3.6 --version
setuptools 36.5.0 from /usr/local/lib/python3.6/site-packages (Python 3.6)
```

```Shell
pi@raspberrypi:~ $ easy_install
easy_install   easy_install3

pi@raspberrypi:~ $ easy_install --version
setuptools 33.1.1 from /usr/lib/python2.7/dist-packages (Python 2.7)
pi@raspberrypi:~ $ easy_install3 --version
setuptools 33.1.1 from /usr/lib/python3/dist-packages (Python 3.5)
```

### [pip](https://pypi.python.org/pypi/pip)
Github Page: [pypa](https://github.com/pypa) / [pip](https://github.com/pypa/pip)  

The [PyPA recommended](https://packaging.python.org/en/latest/current/) tool for installing Python packages.  
pip works on Unix/Linux, macOS, and Windows.  

[Pip](https://wiki.python.org/moin/CheeseShopTutorial) is a modern, general purpose installation tool for python packages. Most often it is useful to install it in your system python.

[pip](https://zh.wikipedia.org/wiki/Pip_(%E8%BB%9F%E4%BB%B6%E5%8C%85%E7%AE%A1%E7%90%86%E7%B3%BB%E7%B5%B1)) 是一个以 Python 计算机程序语言写成的软件包管理系统，他可以安装和管理软件包。  
另外，不少的软件包也可以在 PyPI 中找到。  

#### [Installation](https://pip.pypa.io/en/stable/installing.html)
To install pip, securely download get-pip.py. [2]

Then run the following:

```Shell
python get-pip.py
```

> [Installing pip/setuptools/wheel with Linux Package Managers](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)  
> [怎么在windows下安装pip?](https://taizilongxu.gitbooks.io/stackoverflow-about-python/content/8/README.html)  
> [windows下面安装Python和pip终极教程](http://www.cnblogs.com/yuanzm/p/4089856.html)  

#### [pip2 & pip3](https://www.zhihu.com/question/21653286)
 `pip` comes with the official Python 2.7 and 3.4+ packages from python.org, and a `pip` bootstrap is included by **default** if you build from source.  
`pip` is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4 binaries downloaded from [python.org](https://www.python.org/), but you'll need to [upgrade pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip).  

输入 pip 默认运行 pip 2，输入 pip3 则指定运行版本3的 pip。  

```Shell
# macOS

faner@THOMASFAN-MB0:~|⇒  pip3 -V
pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)
faner@THOMASFAN-MB0:~|⇒  which pip3
/usr/local/bin/pip3
```

```Shell
# raspbian

pi@raspberrypi:~ $ pip -V
pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)
pi@raspberrypi:~ $ which pip
/usr/bin/pip
pi@raspberrypi:~ $ whereis pip
pip: /usr/bin/pip /etc/pip.conf /usr/share/man/man1/pip.1.gz

pi@raspberrypi:~ $ pip3 -V
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.5)
pi@raspberrypi:~ $ which pip3
/usr/bin/pip3
pi@raspberrypi:~ $ whereis pip3
pip3: /usr/bin/pip3 /usr/share/man/man1/pip3.1.gz
```

#### help
官方文档：[Docs](https://pip.pypa.io/en/stable/#) » [pip](https://pip.pypa.io/en/stable/)  

pip 和 pip3 带 `-h`(`--help`) 选项可查看帮助（Show help）。  

pip 的主要命令（Commands）如下：

```Shell
pi@raspberrypi:~ $ pip -h

Usage:   
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  help                        Show help for commands.

```

在终端输入 `pip3 help install` 可查看 pip install 命令的帮助说明。  

在 raspbian 下还可以输入 `man pip` / `man pip3` 查看 pip(3) 的 Manual Page：

- man pip：`/usr/share/man/man1/pip.1.gz`  
- man pip3：`/usr/share/man/man1/pip3.1.gz`  

> [Python的包管理工具pip的安装与使用](http://blog.csdn.net/liuchunming033/article/details/39578019)  
> [pip安装使用详解](http://www.ttlsa.com/python/how-to-install-and-use-pip-ttlsa/) / [python pip常用命令](http://www.cnblogs.com/xueweihan/p/4981704.html)  
> [常用的python模块及安装方法](http://blog.chinaunix.net/uid-24567872-id-3926986.html)  
> [不得不知的几个 python 开源项目](http://lukejin.iteye.com/blog/608230)  

#### [upgrade pip](https://pip.pypa.io/en/stable/installing/#upgrading-pip)
On Linux or macOS:

```Shell
pip install -U pip
```

```Shell
pi@raspberrypi:~ $ pip install -U pip
Collecting pip
  Downloading pip-9.0.1-py2.py3-none-any.whl (1.3MB)
    100% |████████████████████████████████| 1.3MB 13kB/s 
Installing collected packages: pip
Successfully installed pip-9.0.1
```

On Windows:

```Shell
python -m pip install -U pip
```

### pip over easy_install
[Installing Python Modules](https://docs.python.org/3/installing/index.html): pip is the **preferred** installer program. Starting with `Python 3.4`, it is included by ***default*** with the Python binary installers.

#### reason
> [pip vs easy_install](https://packaging.python.org/discussions/pip-vs-easy-install/)  
> [Why use pip over easy_install? ](https://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install)  
> [Pip Compared To easy_install](https://pip.readthedocs.io/en/1.1/other-tools.html#pip-compared-to-easy-install)  

1. pip provides an `uninstall` command  
2. if an installation fails in the middle, pip will leave you in a <u>clean</u> state.  
3. **Requirements files** allow you to create a snapshot of all packages that have been installed through `pip`.  

@img ![current-state-of-packaging](https://i.stack.imgur.com/2icn1.jpg)


 [Setuptools](http://pythonhosted.org/setuptools/) and easy_install will be replaced by the new hotness—distribute and pip. While pip is still the new hotness, Distribute merged with Setuptools in 2013 with the release of Setuptools v0.7.

@img ![friendly_python_packaging_hotness](https://i.stack.imgur.com/RdBpi.png)

#### UPDATE
`setuptools` has absorbed `distribute` as opposed to the other way around, as some thought. `setuptools` is up-to-date with the latest `distutils` changes and the wheel format.  
Hence, `easy_install` and `pip` are more or less on equal footing now.  

