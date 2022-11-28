[pprint — Data pretty printer](https://docs.python.org/3/library/pprint.html)  
[pprint --- 数据美化输出](https://docs.python.org/zh-cn/3/library/pprint.html)  

从 help(pprint.pprint) 中的函数原型来看，当信息超过80个字符时将分行显示，还可通过 ident 设置分行缩进。

```Shell
>>> help(pprint.pprint)

Help on function pprint in module pprint:

pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)
    Pretty-print a Python object to a stream [default is sys.stdout].
```

- [Python - Pretty Print Numbers](https://www.tutorialspoint.com/python_text_processing/python_pretty_prints.htm)
- [打印 Python 的一切 —— pprint & beeprint](https://zhuanlan.zhihu.com/p/42504137)

## list

以下示例，通过简单列表推导，过滤列表list公用接口，并分别用 print、pprint 打印符号列表。

```Python
import pprint


list_all = [n for n in dir(list) if not n.startswith('_')]
print(list_all)
pprint.pprint(list_all)
```

print 在一行打印整个列表，而 pprint 则在每一行输出一个列表项：

```
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

['append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']
```

以下示例，分别用 print、pprint 打印 string 模块向外导出的符号列表：

```Python
import pprint
import string


print(string.__all__)
pprint.pprint(string.__all__)
```

```
['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace', 'Formatter', 'Template']

['ascii_letters',
 'ascii_lowercase',
 'ascii_uppercase',
 'capwords',
 'digits',
 'hexdigits',
 'octdigits',
 'printable',
 'punctuation',
 'whitespace',
 'Formatter',
 'Template']
```

以下示例，分别用 print、pprint 打印 sys.path：

```Python
import pprint
import sys


print(sys.path)
pprint.pprint(sys.path)
```

对于长列表，pprint 更方便地逐行查看每个元素：

```
['', '/usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python310.zip', '/usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python3.10', '/usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/site-packages', '/usr/local/Cellar/pygments/2.13.0/libexec/lib/python3.10/site-packages']

['',
 '/usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python310.zip',
 '/usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python3.10',
 '/usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload',
 '/usr/local/lib/python3.10/site-packages',
 '/usr/local/Cellar/pygments/2.13.0/libexec/lib/python3.10/site-packages']
```

## dict

以下示例，分别用 print、pprint 打印字典 dict 对象：

```Python
import pprint


d = {'foo': 1, 'bar': 2, 'foobar': 3}
print(d)
pprint.pprint(d)
```

pprint 打印字典时，会在计算其显示形式前会先根据键来排序。

```
{'foo': 1, 'bar': 2, 'foobar': 3}

{'bar': 2, 'foo': 1, 'foobar': 3}
```

以下示例，分别用 print、pprint 打印Python 实现信息字典对象：

```Python
import pprint
import sys


print(sys.implementation.__dict__)
pprint.pprint(sys.implementation.__dict__)
```

对于长字典，pprint 更方便地逐行查看每个item：

```
{'name': 'cpython', 'cache_tag': 'cpython-310', 'version': sys.version_info(major=3, minor=10, micro=8, releaselevel='final', serial=0), 'hexversion': 50989296, '_multiarch': 'darwin'}

{'_multiarch': 'darwin',
 'cache_tag': 'cpython-310',
 'hexversion': 50989296,
 'name': 'cpython',
 'version': sys.version_info(major=3, minor=10, micro=8, releaselevel='final', serial=0)}
```
