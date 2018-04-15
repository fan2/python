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

### [CPyhton](https://en.wikipedia.org/wiki/CPython)
[What is CPython?](https://www.quora.com/What-is-CPython)  

CPython is the reference implementation of the [Python programming language](https://en.wikipedia.org/wiki/Python_programming_language).  
Written in ***C***, CPython is the **default** and most widely used implementation of the language.

Python Source code: [github](https://github.com/python/cpython) / [Mercurial](https://hg.python.org/cpython/)  

### [Jython](https://en.wikipedia.org/wiki/Jython)

> <http://www.jython.org/>

Jython is an implementation of the Python programming language designed to run on the ***Java*** platform.  
It is the successor of JPython

```shell
>>> import test
>>> test.support.is_jython
False
```

### [IronPython](https://en.wikipedia.org/wiki/IronPython)

>  <http://ironpython.net/>

IronPython is an implementation of the Python programming language targeting the .NET Framework and Mono. Jim Hugunin created the project.

### [PyPy](http://pypy.org/)
[Docs](http://doc.pypy.org/en/latest/#) » [PyPy’s documentation](http://doc.pypy.org/en/latest/)

#### [wiki](https://en.wikipedia.org/wiki/PyPy)
**PyPy** is an alternate implementation of the Python programming language written in **Python**. Specifically, its interpreter is written in ***RPython*** (a subset of Python).  
In contrast, the standard reference implementation of Python is written in C (known as [**CPython**](https://en.wikipedia.org/wiki/CPython)). The implementation of the interpreter in *high level* Python, over a *low-level* implementation in C, enables quick experimentation of new language features.  
This is shown to have benefits in areas of execution speed, memory usage, sandboxing etc., in certain use cases. The [self-hosting](https://en.wikipedia.org/wiki/Self-hosting) nature of PyPy is reflected in the project's logo, which depicts a snake swallowing its own tail in an ouroboros.  

#### [what](http://doc.pypy.org/en/latest/introduction.html)
Historically, PyPy has been used to mean two things.   
The first is the [RPython translation toolchain](http://rpython.readthedocs.io/en/latest/index.html#index) for generating interpreters for dynamic programming languages.  
And the second is one particular implementation of [Python](http://python.org/) produced with it.  
