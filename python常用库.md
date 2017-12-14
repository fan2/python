
> [哪些Python库让你拍案叫绝，有相见恨晚之感？](https://www.wukong.com/question/6488161616905896205/)  

# raspbian
raspbian 的 pip 安装包的目录（Location）为 `/usr/lib/python2.7/dist-packages`，  
raspbian 的 pip3 安装包的目录（Location）为 `/usr/lib/python3/dist-package`。  

在 raspbian 中输入 `pip list` 或 `pip3 list` 可以看到 raspbian 默认已经安装了79个常用 python 模块（包括 pip3 自身），包括： 

- Python IDE for beginners：[thonny](http://thonny.org)  
- Packaging：[pip](https://pip.pypa.io/)，[setuptools](https://github.com/pypa/setuptools)、wheel  
- GPIO 相关：RPi.GPIO、automationhat、blinkt、[gpiozero](https://github.com/RPi-Distro/python-gpiozero)、[pyserial](https://github.com/pyserial/pyserial)  
- HAT 相关：ExplorerHAT、fourletterphat、[picamera](http://picamera.readthedocs.io/)  
- Sensor 相关：RTIMULib、[sense-emu](http://sense-emu.readthedocs.io/)、[sense-hat](https://github.com/RPi-Distro/python-sense-hat)  
- [pimoroni](http://www.pimoroni.com)：mote、microdotphat、motephat、phatbeat、[pianohat](http://shop.pimoroni.com)、piglow、rainbowhat、scrollphat、scrollphathd、skywriter、sn3218、touchphat  
- 加解密、认证模块：cryptography、[pycrypto](http://www.pycrypto.org/)、[oauthlib](https://github.com/idan/oauthlib)、[pyOpenSSL](https://pyopenssl.readthedocs.io/)  
- 文档转换模块：[docutils](http://www.xuebuyuan.com/1029378.html)，参考 [Parsing reStructuredText into HTML](https://stackoverflow.com/questions/6654519/parsing-restructuredtext-into-html)；[pandocfilters](http://github.com/jgm/pandocfilters)  
- Markups：[pyasn1](http://sourceforge.net/projects/pyasn1/)、[PyYAML](http://pyyaml.org/wiki/PyYAML)、[Markups](https://github.com/retext-project/pymarkups)、[Markdown](https://pythonhosted.org/Markdown/)、Pygments（语法高亮）  
- Client Request：[requests](http://python-requests.org)、[requests-oauthlib](https://github.com/requests/requests-oauthlib)、[urllib3](https://urllib3.readthedocs.io/)  
- 轻量级 Web 框架：[Flask](https://pypi.python.org/pypi/Flask) - [pocoo](http://flask.pocoo.org/) - [github](http://github.com/pallets/flask/)，依赖模板引擎 [Jinja2](http://jinja.pocoo.org/) 和 WSGI 工具集 [Werkzeug](http://werkzeug.pocoo.org/)，参考 [pythondoc](http://www.pythondoc.com/flask/)，[jinkan-docs](http://docs.jinkan.org/docs/flask/) 和 [The Flask Mega-Tutorial](http://www.pythondoc.com/flask-mega-tutorial/index.html)。  
- 通用处理库：[IDNA](https://github.com/kjd/idna)，图像处理库 [Pillow](http://python-pillow.org)，JSON处理库 [simplejson](http://github.com/simplejson/simplejson)、[PyJWT](http://github.com/jpadilla/pyjwt)，文本处理 [textile](http://github.com/textile/python-textile)  
- 其他 bindings：python-apt(Python bindings for APT)

输入 `pip show pkg`（`pip3 show pkg`）可查看具体 pkg 的信息。

# python package help

> [python 查询函数用法?](https://www.zhihu.com/question/29433964)  
> [python如何查看某一个包中的某一个函数的使用方法？](https://www.zhihu.com/question/28509228)  
> [查看python的模块和函数帮助文档方法](http://blog.csdn.net/u013810296/article/details/55509284)  

1. 导入 roman 包（模块）：`import roman`  
2. 列举包中所有的函数：`dir(roman)`  
3. 查看包帮助说明文档（Manual Page）：`help(roman)`，输入 <kbd>q</kbd> 退回 Python Shell。 

```Shell
pi@raspberrypi:~ $ python3
Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import roman
>>> dir(roman)
['InvalidRomanNumeralError', 'NotIntegerError', 'OutOfRangeError', 'RomanError', '__author__', '__builtins__', '__cached__', '__copyright__', '__date__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'fromRoman', 're', 'romanNumeralMap', 'romanNumeralPattern', 'toRoman']
>>> help(roman)

Help on module roman:

NAME
    roman - Convert to and from Roman numerals

CLASSES
    builtins.Exception(builtins.BaseException)

FUNCTIONS
    fromRoman(s)
        convert Roman numeral to integer
    
    toRoman(n)
        convert integer to Roman numeral

```

也可通过 `help(包名.类名.函数名)` 的格式直接查看模块内某各类函数的帮助说明。

例如输入 `help(roman.fromRoman)` / `help(roman.toRoman)` 可分别查看 fromRoman 和 toRoman 这两个函数的说明。

```Shell

>>> help(roman.fromRoman)

Help on function fromRoman in module roman:

fromRoman(s)
    convert Roman numeral to integer

>>> help(roman.toRoman)

Help on function toRoman in module roman:

toRoman(n)
    convert integer to Roman numeral
```

## __doc__

如果嫌 Manual Page 翻页麻烦，可直接调用 print 打印该模块及函数的简单说明（`__doc__`）：

```
>>> print(roman.__doc__)
Convert to and from Roman numerals

>>> print(roman.fromRoman.__doc__)
convert Roman numeral to integer

>>> print(roman.toRoman.__doc__)
convert integer to Roman numeral`
```

> python中每个module，每个class，每个def都是留有写doc的地方的，可以用 `对象名称.__doc__` 查看。

## 函数调用

类似 C++ 命名空间及 Java 包库函数的逐层引用，可使用 `包名.类名.函数名` 的格式调用 python 库的具体函数。

```Shell
>>> roman.toRoman(3)
'III'
```

# Utilities

## [roman](http://pypi.python.org/pypi/roman)
```Shell
pi@raspberrypi:~ $ pip3 show roman
Name: roman
Version: 2.0.0
Summary: Integer to Roman numerals converter
Home-page: http://pypi.python.org/pypi/roman
Author: Mark Pilgrim
Author-email: f8dy@diveintopython.org
License: Python 2.1.1
Location: /usr/lib/python3/dist-packages
Requires: 
```

## [numpy](http://www.numpy.org)

```Shell
pi@raspberrypi:~ $ pip3 show numpy
Name: numpy
Version: 1.12.1
Summary: NumPy: array processing for numbers, strings, records, and objects.
Home-page: http://www.numpy.org
Author: NumPy Developers
Author-email: numpy-discussion@scipy.org
License: BSD
Location: /usr/lib/python3/dist-packages
Requires: 
```

numpy(**Num**erical **Py**thon extensions)是一个第三方的Python包，用于科学计算。这个库的前身是1995年就开始开发的一个用于数组运算的库。经过了长时间的发展，基本上成了绝大部分Python科学计算的基础包，当然也包括所有提供Python接口的深度学习框架。

## [matplotlib](http://matplotlib.org/)
[绘图: matplotlib核心剖析](http://www.cnblogs.com/vamei/archive/2013/01/30/2879700.html)  
[python中的matplotlib用法](http://blog.csdn.net/xiaodongxiexie/article/details/53123371)  
[python使用matplotlib绘图 -- barChart](http://www.cnblogs.com/qianlifeng/archive/2012/02/13/2350086.html)  
[matplotlib 绘图可视化知识点整理](http://python.jobbole.com/85106/)  
[给深度学习入门者的Python快速教程 - numpy和Matplotlib篇](https://zhuanlan.zhihu.com/p/24309547)  
