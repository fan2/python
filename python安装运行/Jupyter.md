
## vscode

[Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/python/jupyter-support)

[Jupyter](https://jupyter.org/install) 插件已经 Deprecated，只需要安装 [Microsoft Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 插件即可，微软官方提供了 Python 插件已经内嵌打包了 Jupyter 插件。

1. `Python`: IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests, and more.

    - Extension Pack: `Pylance`, `Jupyter` and `isort`.

2. `Jupyter`: Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.

    - Extension Pack: `Jupyter Keymap`, `Jupyter Notebook Renderers`, `Jupyter Slide Show`, `Jupyter Cell Tags`.


[VSCode配置jupyter逐行语句运行python](https://blog.csdn.net/cowry5/article/details/79764954)  
[VSCode 编写 Python 支持 Jupyter notebook 了](https://blog.csdn.net/qq_20084101/article/details/84146676)  

Jupyter notebook是逐个cell依次执行，那在VS Code要怎么做到这点呢？  
很简单，在你每一个cell前加上一行：`#%%`  

```Python
#%%
msg = 'hello, world'
print(msg)
```

## Jupyter Notebook

`Jupyter Notebook`: The Classic Notebook Interface

> The Jupyter Notebook is the original web application for creating and sharing computational documents. It offers a simple, streamlined, document-centric experience.

[Python的做笔记神器](https://blog.csdn.net/weixin_38168620/article/details/79576970)

Jupyter Notebook 相当于在浏览器中完成python编程任务，不仅可以写代码、做笔记，而且还可以得到每一步的执行结果，效果非常好。

自从Jupyter Notebook 1.0发布以来，越来越多科学家、研究者、教师使用IPython Notebook处理数据、写研究报告、甚至编写书籍。

推荐使用 Anaconda，自带了 Numpy、Scipy、Matplotlib 等多种 python 开发包和 Jupyter Notebook！

[jupyter notebook安装与配置](https://blog.51cto.com/huangyg/2315382?cid=728374)  
[Python Jupyter Notebook各种使用方法记录](https://blog.csdn.net/qq_25148881/article/details/83004238)  
[python环境搭建以及jupyter notebook的安装和启动](https://www.cnblogs.com/jiangfengtomhuo/p/7987419.html)  

在 Anaconda IDE 中点击启动 Jupyter Notebook 会开一个终端Terminal并启动 python webServer，然后在浏览器中输入本地 localhost url 即可访问web界面。

```Shell
$ /usr/local/anaconda3/bin/jupyter_mac.command ; exit;
[I 2022-06-03 10:17:13.200 LabApp] JupyterLab extension loaded from /usr/local/anaconda3/lib/python3.9/site-packages/jupyterlab
[I 2022-06-03 10:17:13.200 LabApp] JupyterLab application directory is /usr/local/anaconda3/share/jupyter/lab
[I 10:17:13.206 NotebookApp] Serving notebooks from local directory: /Users/faner
[I 10:17:13.206 NotebookApp] Jupyter Notebook 6.4.5 is running at:
[I 10:17:13.206 NotebookApp] http://localhost:8888/?token=b4f7fcc120abf0c978c105a14aa675b4f9326000da7519f4
[I 10:17:13.206 NotebookApp]  or http://127.0.0.1:8888/?token=b4f7fcc120abf0c978c105a14aa675b4f9326000da7519f4
[I 10:17:13.207 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 10:17:13.220 NotebookApp] 
```

[Jupyter notebook 和 Jupyter lab 的区别](https://www.cnblogs.com/heenhui2016/p/10637746.html)  
[Jupyter Lab对比Jupyter Notebook有什么优点和不足？](https://www.zhihu.com/question/413049489)  
[What is the difference between Jupyter Notebook and JupyterLab?](https://stackoverflow.com/questions/50982686/what-is-the-difference-between-jupyter-notebook-and-jupyterlab)  

Jupyter Notebook 是一个款以网页为基础的交互计算环境，可以创建Jupyter的文档，支持多种语言，包括Python, Julia, R等等。广泛用于数据分析，数据可视化和其他的交互和探索性计算中。

JupyterLab 是包括了Notebook的下一代用户界面。有模块化的界面，可以在同一个窗口同时打开好几个notebook或文件（HTML, TXT, Markdown等等），都以标签的形式展示，于是就更像是一个IDE。

## JupyterLab

`JupyterLab`: A Next-Generation Notebook Interface

> JupyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionality.

### docs

[Jupyter Project Documentation](https://docs.jupyter.org/en/latest/)

- [Docs » JupyterLab Documentation](https://jupyterlab.readthedocs.io/en/stable/)
- [The Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/latest/)

[jupyterlab——下一代notebook](https://zhuanlan.zhihu.com/p/38612108)  
[JupyterLab——极其强大的下一代notebook！](https://zhuanlan.zhihu.com/p/87403131)  

### Starting

[Docs » Starting JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/starting.html)

JupyterLab sessions always reside in a workspace. 

The default workspace is the main `/lab` URL:

```
http(s)://<server:port>/<lab-location>/lab
```

### URLs

[Docs » JupyterLab URLs](https://jupyterlab.readthedocs.io/en/stable/user/urls.html)

#### File Navigation with `/tree`

JupyterLab’s file navigation URLs adopts the nomenclature of the classic notebook; these URLs are `/tree` URLs:

```
http(s)://<server:port>/<lab-location>/lab/tree/path/to/notebook.ipynb
```

By default, the file browser will navigate to the directory containing the requested file. This behavior can be changed with the optional `file-browser-path` query parameter:

```
http(s)://<server:port>/<lab-location>/lab/tree/path/to/notebook.ipynb?file-browser-path=/
```

Entering the above URL will show the workspace root directory instead of the `/path/to/` directory in the file browser.

#### Managing Workspaces (UI)

JupyterLab sessions always reside in a workspace. Workspaces contain the state of JupyterLab: the `files` that are currently open, the `layout` of the application areas and tabs, etc. When the page is refreshed, the workspace is restored.


The default workspace does not have a name and resides at the primary `/lab` URL:

```
http(s)://<server:port>/<lab-location>/lab
```

All other workspaces have a name that is part of the URL:

```
http(s)://<server:port>/<lab-location>/lab/workspaces/foo
```

Workspaces ++save their state++ on the server and can be shared between multiple users (or browsers) as long as they have access to the same server.

A workspace should only be open in a single browser tab at a time. If JupyterLab detects that a workspace is being opened multiple times simultaneously, it will prompt for a new workspace name.

#### Managing Workspaces (CLI)

JupyterLab provides a command-line interface for workspace `import` and `export`:

```
$ jupyter lab workspaces export
$ jupyter lab workspaces export > ~/Downloads/jupyter_workspaces.json
```
