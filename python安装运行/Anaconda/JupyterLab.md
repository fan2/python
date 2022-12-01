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

### launch

在 Anaconda Navigator 中点击启动 JupyterLab 会开一个终端Terminal并启动 python webServer。
将会在默认浏览器中打开 http://localhost:8888/lab 。

在 JupyterLab 中 New Launcher 支持创建 Notebook - Python 3 (ipykernel) 和 Console - Python 3 (ipykernel)。
还可创建 Other 文件类型。

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
