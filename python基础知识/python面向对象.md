[TOC]

## 类——对现实世界的抽象

对象由属性和方法组成。属性不过是属于对象的变量，而方法是存储在属性中的函数。
相比于其他函数，（关联的）方法有一个不同之处，那就是它总是将其所属的对象作为第一个参数，而这个参数通常被命名为self。

面向对象编程是最有效的软件编写方法之一。在面向对象编程中，你编写表示现实世界中的事物和情景的类，并基于这些类来创建对象。
编写类时，你定义一大类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。

类：kind; class; category
类型：type; form; genre; mold
特征：characteristic; feature

实例化：instantiation
实例属性：instance attribute
实例模型：case model

type: n.类型，种类；具有某种特征的人，典型（typical）；
mold: n.模具；铸模；模制品；类型，个性，风格；框架；v.浇铸，塑造；用模子制作；


类是具有相同特征的事物的分类抽象和概括统称，例如“人类”、“鸟类”。

对象（object）是一类事物的具体实例（instance；living example），例如“张三”、“李四”是个活生生的个人，他们是“人类”的一份子。

根据类来创建对象被称为实例化。

## 面向过程的程序设计

函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

## 面向对象编程的基本概念

在面向对象编程中，术语对象大致意味着一系列数据（属性）以及一套访问和操作这些数据的方法。

使用对象而非全局变量和函数。

在有些语言（如 scheme 和 Lisp） 中，几乎所有的任务都是以这种方式使用函数来完成的。
在 Python 中，通常不会如此倚重函数，而是创建自定义对象。

Python 提供了一些有助于进行这种函数式编程的函数：map、filter和reduce。

### 封装

属性、方法

组合、复用

### 继承

生物遗传

编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用 继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类， 而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

### 多态

术语多态（polymorphism）源自希腊语，意思是“有多种形态”。这大致意味着即便你不知道变量指向的是哪种对象，也能够对其执行操作，且操作的行为将随对象所属的类型（类）而异。

多态可对不同类型的对象执行相同的操作，是面向对象编程最有趣的特性。

## Python面向对象

### 构造函数

`__init__`

self

### 继承扩展

创建子类时，父类必须包含在当前文件中，且位于子类前面。定义子类时，必须在括号内指定父类的名称。

多重继承

如果只想定制某种操作的行为，就没有理由去重新实现其他所有方法。这就是程序 员的懒惰（也是常识）。

那么该如何做呢？“咒语”就是继承。在能够继承的情况下为何去重新实现呢？在标准库中， 模块collections提供了抽象和具体的基类，但你也可以继承内置类型。因此，如果要实现一种 行为类似于内置列表的序列类型，可直接继承list。

```Shell
>>> [n for n in dir(builtins) if not n.startswith('_') and n.startswith('is')]
['isinstance', 'issubclass']
>>> [n for n in dir(builtins) if not n.startswith('_') and n.find('attr')!=-1]
['delattr', 'getattr', 'hasattr', 'setattr']
>>> [n for n in dir(builtins) if not n.startswith('_') and n.lower().find('method') != -1]
['classmethod', 'staticmethod']
```

### super

```Shell
Help on class super in module builtins:

class super(object)
 |  super() -> same as super(__class__, <first argument>)
 |  super(type) -> unbound super object
 |  super(type, obj) -> bound super object; requires isinstance(obj, type)
 |  super(type, type2) -> bound super object; requires issubclass(type2, type)
 |  Typical use to call a cooperative superclass method:
 |  class C(B):
 |      def meth(self, arg):
 |          super().meth(arg)
 |  This works for class methods too:
 |  class C(B):
 |      @classmethod
 |      def cmeth(cls, arg):
 |          super().cmeth(arg)
```

### classmethod

```Shell
class classmethod(object)
 |  classmethod(function) -> method
 |
 |  Convert a function to be a class method.
 |
 |  A class method receives the class as implicit first argument,
 |  just like an instance method receives the instance.
 |  To declare a class method, use this idiom:
 |
 |    class C:
 |        @classmethod
 |        def f(cls, arg1, arg2, argN):
 |            ...
 |
 |  It can be called either on the class (e.g. C.f()) or on an instance
 |  (e.g. C().f()).  The instance is ignored except for its class.
 |  If a class method is called for a derived class, the derived class
 |  object is passed as the implied first argument.
 |
 |  Class methods are different than C++ or Java static methods.
 |  If you want those, see the staticmethod builtin.
```

### staticmethod

```Shell
class staticmethod(object)
 |  staticmethod(function) -> method
 |
 |  Convert a function to be a static method.
 |
 |  A static method does not receive an implicit first argument.
 |  To declare a static method, use this idiom:
 |
 |       class C:
 |           @staticmethod
 |           def f(arg1, arg2, argN):
 |               ...
 |
 |  It can be called either on the class (e.g. C.f()) or on an instance
 |  (e.g. C().f()). Both the class and the instance are ignored, and
 |  neither is passed implicitly as the first argument to the method.
 |
 |  Static methods in Python are similar to those found in Java or C++.
 |  For a more advanced concept, see the classmethod builtin.
```