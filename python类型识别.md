[The Python Standard Library](https://docs.python.org/3/library/index.html)

## type

type 为内建模块（builtins）中定义的基本类型。

```shell
>>> help(type)

Help on class type in module builtins:

class type(object)
 |  type(object_or_name, bases, dict)
 |  type(object) -> the object's type
 |  type(name, bases, dict) -> a new type
```

执行 `type(object)`  可查看变量的类型：

```shell
>>> i=2018
>>> print(type(i))
<class 'int'>

>>> str_1 = str()
>>> print(type(str_1))
<class 'str'>
```

## id

执行 `help(builtins)` 可以查看到内置函数 `id()`：

```shell
>>> help(builtins)

Help on built-in module builtins:

    id(obj, /)
        Return the identity of an object.
```

`id(obj)` 用于获取类或对象的类型 ID。

```shell
# 也可执行 print(id.__doc__)

>>> help(id)

Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)
```

> CPython

以下测试打印类 str 和实例 str1 和 str2 的类型 ID：

```shell
>>> str1=str()
>>> str2='str2'
>>> id(str)
4363629888
>>> id(str1)
4364618416
>>> id(str2)
4391268056
```

## isinstance

```shell
    isinstance(obj, class_or_tuple, /)
        Return whether an object is an instance of a class or of a subclass thereof.

```

## class method

### `__base__`

执行 `obj.__base__()` 或 `obj.__bases__()` 可以查看 obj 的基类。

```shell
# str 的基类是 object
>>> print(str.__base__)
<class 'object'>

# bool 的基类是 int
>>> print(bool.__base__)
<class 'int'>
>>> print(bool.__bases__)
(<class 'int'>,)

# int 的基类是 object
>>> print(int.__base__)
<class 'object'>
```

### `__subclasses__`

某些类别提供了 `__subclasscheck__()` 方法，用于检测是否是其他类的子类。

```shell
 |  __subclasscheck__(...)
 |      __subclasscheck__() -> bool
 |      check if a class is a subclass
```

`__subclasses__()` 方法则用于列举子类。

```shell
 |  __subclasses__(...)
 |      __subclasses__() -> list of immediate subclasses
```

执行 `int.__subclasses__()` 可列举查看 int 的子类：

```shell
>>> print(int.__subclasses__())
[<class 'bool'>, <enum 'IntEnum'>, <enum 'IntFlag'>, <class 'sre_constants._NamedIntConstant'>]

```

**特例**：查看 object 所有的子类，相当于列举所有可用的类：

```shell
>>> print(object.__subclasses__())
```

```shell
    issubclass(cls, class_or_tuple, /)
        Return whether 'cls' is a derived from another class or is the same class.
```

## demos

[How to find out if a Python object is a string?](https://stackoverflow.com/questions/1303243/how-to-find-out-if-a-python-object-is-a-string)

```shell
>>> str1=str()
>>> str2='str2'

>>> type(str1)
<class 'str'>
>>> type(str2)
<class 'str'>

>>> type(str1) is str
True
>>> type(str2) is str
True

>>> isinstance(str1,str)
True

>>> str(str2)==str2
True
```
