[Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)  
[Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)  

[Visual Studio Code 在 python 中的使用](https://www.jianshu.com/p/0743ad5774dc)  

[**vs code上配置python的运行环境**](https://www.cnblogs.com/EtoDemerzel/p/8083313.html)  

## Jupyter

[VSCode配置jupyter逐行语句运行python](https://blog.csdn.net/cowry5/article/details/79764954)  

[Jupyter](https://jupyter.org/install) 插件已经 Deprecated，只需要安装 [Microsoft Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 插件即可。

### Jupyter Notebook

[Python的做笔记神器](https://blog.csdn.net/weixin_38168620/article/details/79576970)

自从Jupyter Notebook 1.0发布以来，越来越多科学家、研究者、教师使用IPython Notebook处理数据、写研究报告、甚至编写书籍。

推荐使用 Anaconda，自带了 Numpy、Scipy、Matplotlib 等多种 python 开发包和 Jupyter Notebook！

[jupyter notebook安装与配置](https://blog.51cto.com/huangyg/2315382?cid=728374)  
[python环境搭建以及jupyter notebook的安装和启动](https://www.cnblogs.com/jiangfengtomhuo/p/7987419.html)  
[Python Jupyter Notebook各种使用方法记录](https://blog.csdn.net/qq_25148881/article/details/83004238)  

### [VSCode 编写 Python 支持 Jupyter notebook 了](https://blog.csdn.net/qq_20084101/article/details/84146676)  

[Working with Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)

Jupyter notebook是一个cell一个cell依次执行，那在VS Code要怎么做到这点呢？
很简单，在你每一个cell前加上一行：`#%%`

```Python
#%%
msg = 'hello, world'
print(msg)
```

## [Anaconda](https://www.anaconda.com/distribution/)

The World's Most Popular Python/R Data Science Platform

The open-source Anaconda Distribution is the easiest way to perform Python/R data science and machine learning on Linux, Windows, and Mac OS X.

### python3 & pip3

[macOS 安装 Anaconda 后无法在终端使用 conda 命令怎么办？](https://zhuanlan.zhihu.com/p/144550389)

macOS 通过 brew 安装的 python3 目前的版本为 3.9.0：

```
$ python3 -V
Python 3.9.0

$ pip3 -V
pip 20.2.4 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)
```

---

cd 进入 anaconda3 命令行工具包目录下，执行 `./python3 -V` 可知，anaconda3 内置的 python3 版本为 3.7.6：

```
$ cd /usr/local/anaconda3/bin
$ ./python3 -V
Python 3.7.6

$ ./pip -V
pip 20.0.2 from /usr/local/anaconda3/lib/python3.7/site-packages/pip (python 3.7)
```

执行 `./pip list` 可以查看安装的第三方包：

```
$ ./pip list | more
Package                            Version
---------------------------------- -------------------
alabaster                          0.7.12
anaconda-client                    1.7.2
anaconda-navigator                 1.9.12
anaconda-project                   0.8.3

$ ./pip list | grep 'pandas'
pandas                             1.0.1
```

### conda

查看 conda 版本：

```
$ ./conda -V
conda 4.8.2
```

#### help

查看 conda 帮助：

```
$ ./conda -h
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

positional arguments:
  command
    clean        Remove unused packages and caches.
    config       Modify configuration values in .condarc. This is modeled
                 after the git config command. Writes to the user .condarc
                 file (/Users/faner/.condarc) by default.
    create       Create a new conda environment from a list of specified
                 packages.
    help         Displays a list of available conda commands and their help
                 strings.
    info         Display information about current conda install.
    init         Initialize conda for shell interaction. [Experimental]
    install      Installs a list of packages into a specified conda
                 environment.
    list         List linked packages in a conda environment.
    package      Low-level conda package utility. (EXPERIMENTAL)
    remove       Remove a list of packages from a specified conda environment.
    uninstall    Alias for conda remove.
    run          Run an executable in a conda environment. [Experimental]
    search       Search for packages and display associated information. The
                 input is a MatchSpec, a query language for conda packages.
                 See examples below.
    update       Updates conda packages to the latest compatible version.
    upgrade      Alias for conda update.

```

#### info

查看 conda 信息：

```
./conda info

     active environment : base
    active env location : /usr/local/anaconda3
            shell level : 1
       user config file : /Users/faner/.condarc
 populated config files : /Users/faner/.condarc
          conda version : 4.8.2
    conda-build version : 3.18.11
         python version : 3.7.6.final.0
       virtual packages : __osx=10.16
       base environment : /usr/local/anaconda3  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/osx-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/osx-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /usr/local/anaconda3/pkgs
                          /Users/faner/.conda/pkgs
       envs directories : /usr/local/anaconda3/envs
                          /Users/faner/.conda/envs
               platform : osx-64
             user-agent : conda/4.8.2 requests/2.22.0 CPython/3.7.6 Darwin/20.1.0 OSX/10.16
                UID:GID : 501:20
             netrc file : None
           offline mode : False
```

#### list

列举 conda 环境集成的工具包：

```
$ ./conda list | wc -l
     305

$ ./conda list | more
# packages in environment at /usr/local/anaconda3:
#
# Name                    Version                   Build  Channel
_ipyw_jlab_nb_ext_conf    0.1.0                    py37_0
alabaster                 0.7.12                   py37_0
anaconda                  2020.02                  py37_0
anaconda-client           1.7.2                    py37_0
anaconda-navigator        1.9.12                   py37_0
anaconda-project          0.8.4                      py_0

$ ./conda list | grep 'pandas'
pandas                    1.0.1            py37h6c726b0_0
```

### Toolset Suite

![Anaconda-Suite](https://www.anaconda.com/wp-content/uploads/2018/11/distro-01-1.png)

- [Jupyter](https://jupyter.org/): *Jupyter* is a non-profit, open-source project, born out of the [IPython Project](https://ipython.org/) in 2014 as it evolved to support interactive data science and scientific computing across all programming languages.  

Analyze data with scalability and performance:

- [NumPy](https://numpy.org/): *NumPy* is the fundamental package for scientific computing with Python.  
- [SciPy](https://www.scipy.org/): *SciPy* is a Python-based ecosystem of open-source software for mathematics, science, and engineering.  
- [Numba](https://numba.pydata.org/): *Numba* is an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code.  
- [pandas](http://pandas.pydata.org/): *pandas* is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.  
- [Dask](https://dask.org/): *Dask* provides advanced parallelism for analytics, enabling performance at scale for the tools you love. It is developed in coordination with other community projects like Numpy, Pandas, and Scikit-Learn.  

Visualize Toolset:

- [Matplotlib](https://matplotlib.org/): *Matplotlib* is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.  
- [Bokeh](https://bokeh.pydata.org/en/latest/): *Bokeh* is an interactive visualization library that targets modern web browsers for presentation.  
- [Datashader](http://datashader.org/): *Datashader* is a graphics pipeline system for creating meaningful representations of large datasets quickly and flexibly.  
- [Holoviews](http://holoviews.org/): *HoloViews* is an open-source Python library designed to make data analysis and visualization seamless and simple.  

### conda envs

[Anaconda介绍、安装及使用教程](https://zhuanlan.zhihu.com/p/32925500)  

#### init base

```
$ ./conda activate

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.
```

根据提示执行 `./conda init zsh`，`vim ~/.zshrc` 可看到 ZSH 配置文件末尾添加了 conda initialize，主要是将 conda bin 添加到环境变量：

```
export PATH="/usr/local/anaconda3/bin:$PATH"
```

执行 `. ~/.zshrc` 或 `source ~/.zshrc` 或重开一个新的 zsh 终端窗口，即可进入 conda base 环境，可直接运行 conda 系列命令。

```
$ conda -V
conda 4.8.2
(base)

$ python3 -V
Python 3.7.6
(base)
```

默认的 conda base 环境携带了所有集成的组件库（Toolset Suite），可以直接导入引用，新建的子环境则需要自行按需安装。  
如无环境隔离需求，普通简单的需求直接在 base 环境运行调试即可。  

##### uninit

在 conda base 环境下，执行 `conda deactivate` 可退出 base 环境，回到系统默认的 zsh-python 环境。

```
$ conda deactivate

faner at THOMASFAN-MB1 in ~
$ python3 -V
Python 3.9.0
```

由于执行 `./conda init zsh` 时改动了 ZSH 配置文件（`~/.zshrc`），导致每次启动 zsh 终端窗口，都会自动进入 conda base 环境。

---

[怎样取消每次自动进入 conda base 环境呢](https://blog.csdn.net/u014734886/article/details/90718719)？
可通过以下三种方式：

**方法一**：注释掉 ZSH 配置文件（`~/.zshrc`）中的 conda initialize 相关脚本；  
**方法二**：每次在命令行通过 `conda deactivate` 退出 base 环境；  

**方法三**：推荐方式

1. 通过将 `auto_activate_base` 参数设置为 false 实现：

```
conda config --set auto_activate_base false
```

2. 如果要进入的话通过 `conda activate base`

3. 如果反悔了，可以恢复 `auto_activate_base` 参数值：

```
conda config --set auto_activate_base true
```

#### create

```
# 创建
conda create -n [env_name]
# 删除
conda env remove -n [env_name]
```

输入 `conda create -n Py376 python=3.7.6`，创建一个名为 Py376 的 python 3.7.6 子环境。

> 由于需要下砸很多依赖包，可能耗时较长。

```
Preparing transaction: done
Verifying transaction: \ WARNING conda.core.path_actions:verify(963): Unable to create environments file. Path not writable.
  environment location: /Users/faner/.conda/environments.txt

done
Executing transaction: / WARNING conda.core.envs_manager:register_env(52): Unable to register environment. Path not writable or missing.
  environment location: /usr/local/anaconda3/envs/Py376
  registry file: /Users/faner/.conda/environments.txt
done
#
# To activate this environment, use
#
#     $ conda activate Py376
#
# To deactivate an active environment, use
#
#     $ conda deactivate

# 中间省略

Preparing transaction: done
Verifying transaction: \ WARNING conda.core.path_actions:verify(963): Unable to create environments file. Path not writable.
  environment location: /Users/faner/.conda/environments.txt

done
Executing transaction: / WARNING conda.core.envs_manager:register_env(52): Unable to register environment. Path not writable or missing.
  environment location: /usr/local/anaconda3/envs/Py376
  registry file: /Users/faner/.conda/environments.txt
done
#
# To activate this environment, use
#
#     $ conda activate Py376
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

提示 WARNING - Unable to register environment，可以重新执行一遍 `sudo ./conda create -n Py376 python=3.7.6`。

Anaconda 的 Python 子环境都被安装在 `/usr/local/anaconda3/envs` 目录下。

#### activate

创建好子环境之后，按照提示执行 `conda activate Py376`，激活名为 Py376 的子环境。

> 必须执行过 `conda init`，否则执行 activate 时提示报错 `CommandNotFoundError`！

此时执行 `conda activate Py376` 切换到 Py376 子环境，用完之后执行 `conda deactivate` 退回 base 环境。

```
$ conda activate Py376
(Py376)

$ conda deactivate
(base)
```

#### env list

执行 `conda env list` 可以查看所有的环境列表：

```
$ conda env list
# conda environments:
#
base                  *  /usr/local/anaconda3
Py376                    /usr/local/anaconda3/envs/Py376

(base)
```

#### + vscode

[搭建 Python 轻量级编写环境（Anaconda+VSCode）](https://zhuanlan.zhihu.com/p/147336202)  

创建Anaconda的Python子环境 - [Activating Anaconda Environment in VsCode](https://stackoverflow.com/questions/43351596/activating-anaconda-environment-in-vscode)

[Anaconda+VSCode搭建python环境](https://www.jianshu.com/p/f10fb1a4cc87) - Windows  
[Anaconda＋VSCode搭建python开发环境](https://cloud.tencent.com/developer/news/313349)  
[windows10环境下用anaconda和VScode配置](https://blog.csdn.net/u011622208/article/details/79625908)  

[vscode设置python3.7调试环境（已更新）](https://www.cnblogs.com/dotnetcrazy/p/9095793.html)  
[那些使用VSCode写Python踩过的坑(Anaconda配置)](https://www.cnblogs.com/chaoswr/p/10148142.html)  

[MacOS下如何配置Vscode+Anaconda呢？](https://www.zhihu.com/question/265853927)  
[mac vscode配置 anaconda 虚拟环境](https://blog.csdn.net/liubingjun07/article/details/88833885)  
[Mac+Anaconda+PyCharm+VSCode环境搭建](https://blog.csdn.net/qq_28863845/article/details/82589857)  

快捷键 `cmd+,` 打开 vscode 偏好设置，编辑修改（`~/Library/Application Support/Code/User/settings.json`），找到如下两个参数：

1. python.pythonPath；  
2. python.autoComplete.extraPaths；  

修改为 conda 子环境下对应的 bin/python 和 side-packages：

```
    "python.pythonPath": "/usr/local/anaconda3/envs/Py376/bin/python3",
    "python.autoComplete.extraPaths": ["/usr/local/anaconda3/envs/Py376/lib/python3.7/site-packages"],
```
