[What is the difference between venv, pyvenv, pyenv, virtualenv, virtualenvwrapper, pipenv, etc?](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)  

# [pyenv](https://github.com/pyenv/pyenv)
github: [pyenv](https://github.com/pyenv) / [pyenv](https://github.com/pyenv/pyenv)

Simple Python Version Management: pyenv

pyenv lets you easily switch between multiple versions of Python.  
It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.  

> [Multiple Python installations on OS X](https://gist.github.com/Bouke/11261620)  
> [python 环境管理器pyenv 命令](http://blog.csdn.net/sentimental_dog/article/details/52718398)  
> [使用 pyenv 可以在一个系统中安装多个python版本](http://www.jianshu.com/p/a23448208d9a)  
> [在 Mac OS X 10.10 安装 pyenv 的一个小坑](http://blog.csdn.net/gzlaiyonghao/article/details/46343913)  
> [Python多版本管理软件pyenv的安装应用及pip的使用讲解](http://blog.csdn.net/magedu_linux/article/details/48528257)  

# [virtualenv](https://pypi.python.org/pypi/virtualenv)
virtualenv is a tool to create isolated Python environments.

[Docs](https://virtualenv.pypa.io/en/stable/#) » [Virtualenv](https://virtualenv.pypa.io/en/stable/)  

> [用pyenv 和 virtualenv 搭建单机多版本python 虚拟开发环境](http://www.cnblogs.com/npumenglei/p/3719412.html)  
> [使用 pyenv + virtualenv 打造多版本 Python 开发环境](http://python.jobbole.com/85587/)  

# [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
github: [pyenv](https://github.com/pyenv) / [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

pyenv 是一个 Python 多版本环境管理工具, 这个是和我们常用的 virtualenv 有所不同。  

1. 前者是对 Python 的版本进行管理, 实现不同版本的切换和使用；  
2. 后者测试创建一个虚拟环境, 与系统环境以及其他 Python 环境隔离，避免干扰。  

**pyenv-virtualenv** is a [pyenv](https://github.com/pyenv/pyenv) plugin that provides features to manage virtualenvs and conda environments for Python on UNIX-like systems.

# [six](http://pypi.python.org/pypi/six/)
[docs](http://six.rtfd.org/)  

```Shell
pi@raspberrypi:~ $ pip3 show six
Name: six
Version: 1.10.0
Summary: Python 2 and 3 compatibility utilities
Home-page: http://pypi.python.org/pypi/six/
Author: Benjamin Peterson
Author-email: benjamin@python.org
License: MIT
Location: /usr/lib/python3/dist-packages
Requires: 
```

# references

> [用了pyenv-virtualenv, 天黑都不怕](https://www.darkof.com/2014/10/17/pyenv-virtualenv/) - 简介  
> [Python多版本管理器pyenv和虚拟环境pyenv-virtualenv的安装设置](http://www.jianshu.com/p/1842a363257c)  

> [mac下使用pyenv,pyenv-virtualenv管理python的多个版本](http://blog.csdn.net/angel22xu/article/details/45443019)  
> [Mac OS 上用pyenv和pyenv-virtualenv管理多个Python多版本及虚拟环境](http://blog.csdn.net/liuchunming033/article/details/78345286)  
> [Python版本管理：pyenv和pyenv-virtualenv(MAC、Linux)、virtualenv和virtualenvwrapper(windows)](http://www.jianshu.com/p/60f361822a7e)  

> [mac下使用pyenv,pyenv-virtualenv管理python的多个版本](http://blog.csdn.net/angel22xu/article/details/45443019) - homebrew - 图文详细  
> [Mac OS 上用pyenv和pyenv-virtualenv管理多个Python多版本及虚拟环境](http://blog.csdn.net/liuchunming033/article/details/78345286) - homebrew  
> [pyenv简介——Debian/Ubuntu中管理多版本Python](http://www.malike.net.cn/blog/2016/05/21/pyenv-tutorial/) - git clone  
> [Python版本管理：pyenv和pyenv-virtualenv(MAC、Linux)、virtualenv和virtualenvwrapper(windows)](http://www.jianshu.com/p/60f361822a7e) - git clone  