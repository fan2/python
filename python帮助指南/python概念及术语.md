# Concepts

## [python](https://www.python.org/)

Once you have read a tutorial, you can browse through [Python's online documentation](http://docs.python.org/). It includes [a tutorial](http://docs.python.org/tut/) that might come in handy, [a Library Reference](http://docs.python.org//lib/) that lists all of the modules that come standard with Python, and [the Language Reference](http://docs.python.org/ref/) for a complete (if rather dry) explanation of Python's syntax.

## [PyPI](http://pypi.python.org/pypi)

The `Python Package Index`(PyPI) is a repository of software for the Python programming language.

## [PyPA](https://www.pypa.io/)

The `Python Packaging Authority` (PyPA) is a working group that **maintains** many of the relevant projects in Python packaging.

Github Page: <https://github.com/pypa>  

## PEP

[PEP 0 -- Index of Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/)  
[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)  

## Implementation

[The Python Language Reference](https://docs.python.org/3/reference/index.html) - [Alternate Implementations](https://docs.python.org/3/reference/introduction.html#alternate-implementations)  

```shell
>>> import sys
# Python 实现信息
>>> sys.implementation
namespace(_multiarch='darwin', cache_tag='cpython-36', hexversion=50726384, name='cpython', version=sys.version_info(major=3, minor=6, micro=5, releaselevel='final', serial=0))

>>> import platform
>>> platform.python_implementation()
'CPython'
>>> platform.python_version()
'3.6.5'

```

### [CPyhton](https://en.wikipedia.org/wiki/CPython)

This is the original and most-maintained implementation of Python, written in C. New language features generally appear here first.

---

[What is CPython?](https://www.quora.com/What-is-CPython)  

Written in ***C***, CPython is the **default** and most widely used implementation of the language.

Python Source code: [github](https://github.com/python/cpython) / [Mercurial](https://hg.python.org/cpython/)  

### [Jython](https://en.wikipedia.org/wiki/Jython)

Python implemented in Java. This implementation can be used as a scripting language for Java applications, or can be used to create applications using the Java class libraries. It is also often used to create tests for Java libraries. More information can be found at [the Jython website](http://www.jython.org/).

```shell
>>> import test
>>> test.support.is_jython
False
```

### Python for .NET

This implementation actually uses the CPython implementation, but is a managed .NET application and makes .NET libraries available. It was created by Brian Lloyd. For more information, see the [Python for .NET home page](https://pythonnet.github.io/).

### [IronPython](https://en.wikipedia.org/wiki/IronPython)

An alternate Python for .NET. Unlike Python.NET, this is a complete Python implementation that generates IL, and compiles Python code directly to .NET assemblies. It was created by Jim Hugunin, the original creator of Jython. For more information, see [the IronPython website](http://ironpython.net/).

### [PyPy](https://en.wikipedia.org/wiki/PyPy)

An implementation of Python written completely in Python. It supports several advanced features not found in other implementations like stackless support and a Just in Time compiler. One of the goals of the project is to encourage experimentation with the language itself by making it easier to modify the interpreter (since it is written in Python). Additional information is available on [the PyPy project’s home page](http://pypy.org/).

---

<http://pypy.org/>

[Docs](http://doc.pypy.org/en/latest/#) » [PyPy’s documentation](http://doc.pypy.org/en/latest/)

[introduction](http://doc.pypy.org/en/latest/introduction.html)

Historically, PyPy has been used to mean two things.   
The first is the [RPython translation toolchain](http://rpython.readthedocs.io/en/latest/index.html#index) for generating interpreters for dynamic programming languages.  
And the second is one particular implementation of [Python](http://python.org/) produced with it.  

---

Each of these implementations varies in some way from the language as documented in this manual, or introduces specific information beyond what’s covered in the standard Python documentation. Please refer to the implementation-specific documentation to determine what else you need to know about the specific implementation you’re using.
