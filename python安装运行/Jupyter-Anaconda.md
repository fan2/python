
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

### Anaconda＋VSCode

[Anaconda+VSCode搭建python环境](https://www.jianshu.com/p/f10fb1a4cc87)  

创建Anaconda的Python子环境 - [Activating Anaconda Environment in VsCode](https://stackoverflow.com/questions/43351596/activating-anaconda-environment-in-vscode)

[windows10环境下用anaconda和VScode配置](https://blog.csdn.net/u011622208/article/details/79625908)  
[Anaconda＋VSCode搭建python开发环境](https://cloud.tencent.com/developer/news/313349)  

[那些使用VSCode写Python踩过的坑(Anaconda配置)](https://www.cnblogs.com/chaoswr/p/10148142.html)  
[vscode设置python3.7调试环境（已更新）](https://www.cnblogs.com/dotnetcrazy/p/9095793.html)  
