
[Glossary — generator](https://docs.python.org/3/glossary.html#term-generator)
[Built-in Types — Generator Types](https://docs.python.org/3/library/stdtypes.html#generator-types)
[9.9. Generators](https://docs.python.org/3/tutorial/classes.html#generators)

可借鉴参考《ES6 标准入门》第 16 章《Generator 函数的语法》。

## 基本概念

Glossary - **generator**：

A function which returns a [generator iterator](https://docs.python.org/3/glossary.html#term-generator-iterator). It looks like a normal function except that it contains [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the [`next()`](https://docs.python.org/3/library/functions.html#next "next") function.

Usually refers to a generator function, but may refer to a *generator iterator* in some contexts. In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.

**Generator Types**:

Python’s [generator](https://docs.python.org/3/glossary.html#term-generator)s provide a convenient way to implement the iterator protocol. If a container object’s [`__iter__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__iter__ "iterator.__iter__") method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the `__iter__()` and [`__next__()`](https://docs.python.org/3/reference/expressions.html#generator.__next__ "generator.__next__") methods. More information about generators can be found in the documentation for [the yield expression](https://docs.python.org/3/reference/expressions.html#yieldexpr).

**Generators**:

[Generators](https://docs.python.org/3/glossary.html#term-generator) are a simple and powerful tool for creating iterators. They are written like regular functions but use the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) statement whenever they want to **return** data. Each time [`next()`](https://docs.python.org/3/library/functions.html#next "next") is called on it, the generator **resumes** where it left off (it remembers all the data values and which statement was last executed).

---

生成器由两个单独的部分组成：生成器的函数和生成器的迭代器，两位一体通称为**生成器**。

生成器的函数和普通函数一样，也是由 def 语句定义的代码块，只是其中包含 yield 语句。
从语法上，可以把 generator 函数理解成一个状态机，yield 语句定义了不同的内部状态。

> `yield` 这个单词既有“让出”的意思，又有“产出”的意思，真实一语双关！

其次，它还是一个迭代器对象生成函数，调用该函数，函数体并不执行，而是返回生成器迭代器。
返回的迭代器对象可以遍历 generator 函数内部的 yield 语句定义的每一个状态。
针对迭代器调用 next（或执行 for 循环），每次执行到 yield 冻结。

每次调用 next 方法，内部指针就从函数头部或上一次停下来的地方开始执行，直到遇到下一条 yield 语句为止。
换言之，generator 函数是分段执行的，yield 语句是暂停执行的标记，而 next 方法可以恢复执行。

以 `y = yield (expr)` 为例：

1. 调用 next 时返回 expr 的值，yield 冻结。
2. 再次调用 next，yield 唤醒返回 None，即 y=None。
3. yield 表达式返回值，则要外面改调 g.send(v) 注入 y=v。

## 简单生成器演示

先来看一个最简单的生成器，只有一条空 yield，仅实现让出运行权的效果。

```Python
def generator1():
    print('before yield')
    yield
    print('after yield')

g1 = generator1()
# NOP
print(next(g1))
# before yield, yield nothing
print(next(g1))
# after yield, no yield else
```

1. g1 = generator1()：返回生成器迭代器，尚未触发执行
2. next(g1): 触发执行生成器函数，打印 'before yield' 后，运行至 yield，无返回值，冻结暂停
3. next(g1): yield 唤醒，继续运行打印 'after yield' 后结束，没有下一条 yield，抛出 StopIteration 异常

稍作改进，yield 后面加一个值，看看运行效果。

```Shell
def generator2():
    print('before yield')
    yield 2024
    print('after yield')

g2 = generator2()
print(next(g2))
print(next(g2))
```

1. g2 = generator2()：返回生成器迭代器，尚未触发执行
2. next(g2): 触发执行生成器函数，打印 'before yield' 后，运行至 yield，返回 2024 打印，冻结暂停
3. next(g2): yield 唤醒，继续运行打印 'after yield' 后结束，没有下一条 yield，抛出 StopIteration 异常

继续改进，给生成器函数增加一条 return 语句，执行结果同上。

- 这里和 ES6 不一样，return 语句不同于 yield 语句，不接受 next 访问语义。

```Python
def generator3():
    print('before yield')
    yield 2024
    print('after yield')
    return 2025

g3 = generator3()
print(next(g3))
print(next(g3))
```

继续改进，再增加两条 yield 语句：

```Python
def generator4():
    print('yield 1')
    yield 2024
    print('yield 2')
    yield 2025
    print('yield 3')
    yield 2026

g4 = generator4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
```

1. next(g4): 输出两行：yield 1; 2024
2. next(g4): 输出两行：yield 2; 2025
3. next(g4): 输出两行：yield 3; 2026
4. next(g4): 抛出 StopIteration 异常

由于生成器函数返回生成器迭代器，故可以直接对其执行 for 循环：

```Python
for i in g4:
    print(i)
```

正常情况下，有 n 条 yield 语句，就可以调用 n 次 next 迭代取值，再调一次抛出 StopIteration 异常。

## 通用生成器--递归

考虑有一个二层嵌套列表：nested = [[1, 2], [3, 4], [5]]，其每个元素还是列表。换而言之，这是一个列表的列表。

如果要将其展开，下面是一种解决方案：

```Python
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
```

外层 for 循环迭代提供嵌套列表中的所有子列表，内存 for 循环按顺序迭代每个子列表的元素。
之前的实现最后一行为 print(element)，这里改为了 yield element 将其变成了生成器。

传入要展开的嵌套列表，然后对 flatten 返回的生成器迭代器，使用 for 循环迭代即可。

```Python
nested = [[1, 2], [3, 4], [5]]
for e in flatten(nested):
    print(e)
```

但是，上面设计的生成器只能处理两层的嵌套列表，这是使用两个for循环来实现的。如果要处理任意层嵌套的列表，该如何办呢？
对于每层嵌套，都需要一个for循环，但由于不知道有多少层嵌套，你必须修改解决方案，使其更灵活。该求助于递归了。

```Python
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

nested = [[[1], 2], 3, 4, [5, [6, 7]], 8]
for e in flatten(nested):
    print(e)
```

调用flatten时，有两种可能性（处理递归时都如此）：基线条件和递归条件。在基线条件下， 要求这个函数展开单个元素（如一个数）。在这种情况下，for循环将引发TypeError异常（因为你试图迭代一个数），而这个生成器只生成一个元素。

然而，如果要展开的是一个列表（或其他任何可迭代对象），你就需要做些工作：遍历所有的子列表（其中有些可能并不是列表）并对它们调用flatten，然后使用另一个for循环生成展开后的子列表中的所有元素。

然而，这个解决方案存在一个问题。如果nested是字符串或类似于字符串的对象，它就属于序列，因此不会引发TypeError异常，可你并不想对其进行迭代。

> 在函数 flatten 中，不应该对类似于字符串的对象进行迭代，主要原因有两个。首先，你想将类似于字符串的对象视为原子值，而不是应该展开的序列。其次，对这样的对象进行迭代会导致无穷递归，因为字符串的第一个元素是一个长度为1的字符串，而长度为1的字符串的第一个元素是字符串本身！

要处理这种问题，必须在生成器开头进行检查。要检查对象是否类似于字符串，最简单、最 快捷的方式是，尝试将对象与一个字符串拼接起来，并检查这是否会引发TypeError异常。添加 这种检查后的生成器如下：

```Python
def flatten(nested):
    try:
        try: nested + ''
        except TypeError: pass # 非字符串拼接异常，继续迭代
        else: raise TypeError  # 类字符串对象，不迭代

        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

nested = ['foo', ['bar', ['baz']]]
for e in flatten(nested):
    print(e)
```

## 通用生成器--带循环

以下 repeater 是个无限循环，初始传入 value=3，每次调用 next 返回 value=3。

```Python
def repeater(value):
    while True:
        yield value

r=repeater(3)
print(next(r))
print(next(r))
print(next(r))
```

1. r=repeater(3)：value=3，返回生成器迭代器，尚未触发执行
2. next(r): 触发执行生成器函数，运行至 yield，返回 3 后冻结
3. next(r): yield 返回 None，继续循环至 yield，返回 3 后冻结
4. next(r): 同上

可参考 [itertools — Functions creating iterators for efficient looping](https://docs.python.org/3.12/library/itertools.html#itertools.takewhile) 中 takewhile、filterfalse 和 dropwhile 的等效生成器实现。

```Python
# 过滤出符合谓词逻辑 predicate 的元素，一旦遇到第一个不符合条件的即终止。
def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break

# 过滤出所有不符合谓词逻辑 predicate 的元素。
def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x

# 过滤掉符合谓词逻辑 predicate 的元素，一旦遇到第一个不符合条件的予以保留（至末尾）。
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
```

## 通用生成器--外部通信

在生成器开始运行后，可使用生成器和外部之间的通信渠道向它提供值。这个通信渠道包含如下两个端点：

- 外部世界：外部世界可访问生成器的方法 send，这个方法类似于 next，但接受一个参数（要发送的“消息”，可以是任何对象）。
- 生成器：在挂起的生成器内部，yield 可能用作表达式而不是语句。换而言之，当生成器重新运行时，yield 返回一个值——通过 send 从外部世界发送的值。

请注意，仅当生成器被挂起（即遇到第一个 yield）后，使用 send（而不是 next）才有意义。 要在此之前向生成器提供信息，可使用生成器的函数的参数。

> 注意：如果一定要在生成器刚启动时对其调用方法 send，可向它传递参数 None。

```Python
def generator5():
    i = 0
    while True:
        reset = yield i
        if reset:
            i = -1
        i += 1

g5 = generator5()
print(next(g5))
print(next(g5))
print(g5.send(True))
print(next(g5))
print(next(g5))
```

1. g5=generator5()：返回生成器迭代器，尚未触发执行
2. next(g5): 触发执行生成器函数，运行至 yield，返回 0 后冻结
3. next(g5): yield 返回 None，i 自增为1，继续循环至 yield，返回 1 后冻结
4. g5.send(True): yield 返回 True，i 复位为 -1 并自增为 0，继续循环至 yield，返回 0 后冻结
5. next(g5): yield 返回 None，i 自增为1，继续循环至 yield，返回 1 后冻结
6. next(g5): yield 返回 None，i 自增为2，继续循环至 yield，返回 2 后冻结

```Python
def repeater(value):
    while True:
        print('before yield')
        yret = yield value
        print('after yield', yret)
        if yret:
            value = yret # update with send param

r=repeater(3)
print(next(r))
print(next(r))
print(r.send('24'))
print(next(r))
print(next(r))
```

1. r=repeater(3)：返回生成器迭代器，尚未触发执行
2. next(r): 触发执行生成器函数，运行至 yield，返回 value=3 后冻结
3. next(r): yield 返回 None，继续循环至 yield，返回 value=3 后冻结
4. r.send('24'): yield 返回 24 并更新 value=24，继续循环至 yield，返回 value=24 后冻结
5. next(r): yield 返回 None，继续循环至 yield，返回 value=24 后冻结
6. next(r): 同上

下面综合演示 yield 语句和表达式混合使用：

```Python
def generator6(x):
    y = 2 * (yield (x+1))
    z = yield (y//3)
    yield (x+y+z)

g6 = generator6(5)
print(next(g6))
print(next(g6))
```

1. g6=generator6(5)：x=5，返回生成器迭代器，尚未触发执行
2. next(g6): 触发执行生成器函数，运行至 yield，返回 x+1=6 后冻结
3. next(g6): yield 表达式返回 None，与整数 2 相乘，报异常 TypeError：

    - TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

修改测试代码，第一次调用 next(g6) 后，可以调用 send 向内注入 yield 表达式值：

```Python
g6 = generator6(5)
print(next(g6))
print(g6.send(12))
print(next(g6))
```

1. g6=generator6(5)：x=5，返回生成器迭代器，尚未触发执行
2. next(g6): 触发执行生成器函数，运行至 yield，返回 x+1=6 后冻结
3. g6.send(12)：第1个 yield 表达式返回 12，y=2*12=24，返回 y//3=8
4. next(g6): 第2个 yield 表达式返回 None，z=None，第三个 yield 语句报异常 TypeError:

- TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

再次修改测试部分，把 send 后的 next 改为再次 send 传值：

```Python
g6 = generator6(5)
print(next(g6))
print(g6.send(12))
print(g6.send(13))
```

1. g6=generator6(5)：x=5，返回生成器迭代器，尚未触发执行
2. next(g6): 触发执行生成器函数，运行至 yield，返回 x+1=6 后冻结
3. g6.send(12)：第1个 yield 表达式返回 12，y=2*12=24，返回 y//3=8
4. g6.send(13)：第2个 yield 表达式返回 13，z=13，yield 语句 x+y+z=5+24+13=42，返回 42

## 圆括号构造简单生成器

在 Python 2.4 中，引入了一个类似于列表推导的概念：生成器推导（也叫生成器表达式）。
其工作原理与列表推导相同，但不是创建一个列表（即不立即执行循环），而是返回一个生成器，让你能够逐步执行计算。

```Shell
>>> g = ((i + 2) ** 2 for i in range(2, 27))
>>> next(g)
16
```

如你所见，不同于列表推导，这里使用的是圆括号。在像这样的简单情形下，还不如使用列表推导；但如果要包装可迭代对象（可能生成大量的值），使用列表推导将立即实例化一个列表，从而丧失迭代的优势。

另一个好处是，直接在一对既有的圆括号内（如在函数调用中）使用生成器推导时，无需再添加一对圆括号。换而言之，可编写下面这样非常漂亮的代码：

> sum(i ** 2 for i in range(10))

string.py 中 string.capwords 函数的早期实现即基于生成器迭代器（现已改为 map 实现）：

```Python
# Capitalize the words in a string, e.g. " aBc  dEf " -> "Abc Def".
def capwords(s, sep=None):
    return (sep or ' ').join(x.capitalize() for x in s.split(sep))
```

以下构建生成器，过滤生成 1-10 内的偶数，even 承接返回迭代器：

```Shell
>>> even=(n for n in range(1,11) if n%2==0)
>>> type(even)
<class 'generator'>
```

[syntax - Python equivalent of c++ find_if - Stack Overflow](https://stackoverflow.com/questions/51410881/python-equivalent-of-c-find-if)

找出序列中第一个被 5 整除的数：

```Shell
>>> lst=[1,2,10,3,5,3,4]
>>> next(n for n in lst if n%5==0)
10
```

A slight modification will give you the index rather than the value:

```Shell
>>> next(idx for idx,n in enumerate(lst) if n%5==0)
2
```

## 基于生成器创建斐波那契数列

假如只想找出第一个大于1000的斐波那契数，而不关注前向序列，如果用列表实现，非常耗费内存。
在迭代器专题中，我们演示了基于迭代器实现了斐波那契数列。

```Python
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__ (self):
        return self

fibs = Fibs()
for fib in fibs:
    if fib > 1000:
        print(fib)
        break
```

这一节，我们基于生成器（迭代器）来更简洁地实现。

```Python
def fibonacci():
    a,b = 0,1
    while True:
        a,b = b,a+b
        yield b

for fib in fibonacci():
    if fib > 1000:
        print(fib)
        break
```
