[Python模块和包](https://blog.csdn.net/u011655519/article/details/39908279)

[The Python Language Reference](https://docs.python.org/3/reference/index.html) - [The import system](https://docs.python.org/3/reference/import.html#importsystem)  
[The Python Tutorial](https://docs.python.org/3.6/tutorial/) - [Modules](https://docs.python.org/3.6/tutorial/modules.html)  

Python的程序由包（[package](https://docs.python.org/3/glossary.html#term-package)）、模块（[module](https://docs.python.org/3/glossary.html#term-module)）和函数组成。包是由一系列模块组成的集合。模块是处理某一类问题的函数和类的集合。

- ***package***: A Python [module](https://docs.python.org/3/glossary.html#term-module) which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an `__path__` attribute.

- ***module***: An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of [importing](https://docs.python.org/3/glossary.html#term-importing).

- ***function***: A series of statements which returns some value to a caller. It can also be passed zero or more [arguments](https://docs.python.org/3/glossary.html#term-argument) which may be used in the execution of the body. See also [parameter](https://docs.python.org/3/glossary.html#term-parameter), [method](https://docs.python.org/3/glossary.html#term-method), and the [Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function) section.

## import

Python code in one [module](https://docs.python.org/3/glossary.html#term-module) **gains access** to the code in another module by the process of [importing](https://docs.python.org/3/glossary.html#term-importing) it. The [import](https://docs.python.org/3/reference/simple_stmts.html#import) statement is the most common way of invoking the import machinery, but it is not the only way. Functions such as [importlib.import_module()](https://docs.python.org/3/library/importlib.html#importlib.import_module) and built-in [`__import__()`](https://docs.python.org/3/library/functions.html#__import__) can also be used to invoke the import machinery.

The [import](https://docs.python.org/3/reference/simple_stmts.html#import) statement combines two operations; it **searches** for the named module, then it **binds** the results of that search to a name in the local scope.

### Search Path

The first place checked during import search is [sys.modules](https://docs.python.org/3/library/sys.html#sys.modules). 

- ***sys.path***: A list of strings that specifies the search path for modules. Initialized from the environment variable [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH), plus an installation-dependent default.  
- ***sys.modules***: This is a dictionary that maps module names to modules which have already been loaded. This can be manipulated to force reloading of modules and other tricks. However, replacing the dictionary will not necessarily work as expected and deleting essential items from the dictionary may cause Python to fail.  

When the named module is not found in [sys.modules](https://docs.python.org/3/library/sys.html#sys.modules), Python next searches [sys.meta_path](https://docs.python.org/3/library/sys.html#sys.meta_path), which contains a list of meta path finder objects. These finders are queried in order to see if they know how to handle the named module.

- ***sys.meta_path***: A list of [meta path finder](https://docs.python.org/3/glossary.html#term-meta-path-finder) objects that have their [find_spec()](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec) methods called to see if one of the objects can find the module to be imported. 

### [The import statement](https://docs.python.org/3/reference/simple_stmts.html#import)  

> If the requested module is retrieved successfully, it will be made **available** in the local namespace.

Examples:

```shell
import foo                 # foo imported and bound locally
import foo.bar.baz         # foo.bar.baz imported, foo bound locally
import foo.bar.baz as fbb  # foo.bar.baz imported and bound as fbb
from foo.bar import baz    # foo.bar.baz imported and bound as baz
from foo import attr       # foo imported and foo.attr bound as attr
```

> import 类似 C(++) 中的 include，Objective-C 中的 import；  
> `from module import class(.method)` 类似 C++ 中命名空间的导入引用（using）。  

If the list of identifiers is replaced by a star ('`*`'), all public names defined in the module are bound in the local namespace for the scope where the import statement occurs.

The wild card form of import — `from module import *` — is only allowed at the **module** level. Attempting to use it in class or function definitions will raise a SyntaxError.

## [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__)

'`__main__`' is the name of the scope in which top-level code executes. A module’s `__name__` is set equal to '`__main__`' when read from standard input, a script, or from an interactive prompt.

A module can discover whether or not it is running in the main scope by checking its own `__name__`, which allows a common idiom for conditionally executing code in a module when it is run as a script or with `python -m` but not when it is imported:

```python
if __name__ == "__main__":
    # execute only if run as a script
    main()
```

For a package, the same effect can be achieved by including a `__main__.py` module, the contents of which will be executed when the module is run with `-m`.

```shell
⇒  python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):

-m mod : run library module as a script (terminates option list)

```

[Special considerations for __main__](https://docs.python.org/3/reference/import.html#special-considerations-for-main)  
